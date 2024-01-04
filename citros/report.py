import os
import sys
import glob
import json
import nbformat
import importlib_resources
from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path
from datetime import datetime
from nbconvert import HTMLExporter, PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert.preprocessors import CellExecutionError
from rich import inspect
from weasyprint import HTML
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization

from .citros import Citros

from .logger import get_logger, shutdown_log


class NoNotebookFoundException(Exception):
    def __init__(self, message="No Notebook found."):
        super().__init__(message)


class Report:
    """

    Raises:
        NoNotebookFoundException: _description_
        NoNotebookFoundException: _description_

    Returns:
        _type_: _description_
    """

    ###################
    ##### private #####
    ###################
    def _init_log(self, log=None, verbose=False, debug=False):
        self.log = log
        self.verbose = verbose
        self.debug = debug
        if self.log is None:
            Path.home().joinpath(".citros/logs").mkdir(parents=True, exist_ok=True)
            log_dir = Path.home().joinpath(".citros/logs")

            self.log = get_logger(
                __name__,
                log_level=os.environ.get("LOGLEVEL", "DEBUG" if self.debug else "INFO"),
                log_file=str(log_dir / "citros.log"),
                verbose=self.verbose,
            )

    def __init__(
        self,
        name: str = None,
        message: str = None,
        citros: Citros = None,
        output=None,
        batch=None,
        notebooks=[],
        sign=False,
        key=None,
        index: int = -1,  # default to take the last version of a runs
        version=None,
        log=None,
        debug=False,
        verbose=False,
    ):
        self._init_log(log, verbose, debug)
        self.log.debug(f"{self.__class__.__name__}.__init__()")
        self.sign_report = sign

        self.citros = citros
        self.batch = batch
        if self.batch is None:
            self.log.error("batch is None")
            return

        self.version = version
        self.index = index

        self.output = output
        self.reports_dir = citros.root_citros / "reports" / name
        if output is not None:
            self.reports_dir = Path(output)  # / "reports" / name

        # get version
        if not version:  # no version specified
            if batch:  # create new report
                self.version = datetime.today().strftime("%Y%m%d%H%M%S")
            else:
                versions = sorted(glob.glob(f"{str(self.reports_dir)}/*"))
                # get version from index
                self.version = versions[self.index].split("/")[-1]

        self.folder = self.reports_dir / self.version

        # event = {
        #     "type": "ERROR",
        #     "message": "Report not found",
        # }
        self.state = {
            "notebooks": notebooks,
            "data": [
                {
                    "simulation": batch["simulation"],
                    "batch": batch["name"],
                    "version": batch.version,
                }
            ],
            "status": "START",
            "events": [],
            "name": name,
            "message": message,
            "progress": 0,
            "started_at": datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
            "finished_at": None,
        }

        Path(self.folder).mkdir(parents=True, exist_ok=True)
        (Path(self.folder) / "output").mkdir(parents=True, exist_ok=True)
        # (Path(self.folder) / "notebooks").mkdir(parents=True, exist_ok=True)

        self._save()

    def __str__(self):
        # print_json(data=self.data)
        return json.dumps(self.state, indent=4)

    def __getitem__(self, key):
        """get element from object

        Args:
            key (str): the element key

        Returns:
            str: the element value
        """
        return self.state[key]

    def get(self, key, default=None):
        """get element from object

        Args:
            key (str): the element key

        Returns:
            str: the element value
        """
        return self.data.state(key, default)

    def __setitem__(self, key, newvalue):
        self.state[key] = newvalue
        self._save()

    def _save(self):
        self.log.debug(
            f"{self.__class__.__name__}._save()",
        )
        self.state["updated_at"]: datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        with open(self.path(), "w") as file:
            json.dump(self.state, file, indent=4, sort_keys=True)

    ###################
    ##### public ######
    ###################
    def path(self):
        """return the full path to the current main file.

        default to ".citros/project.json"

        Returns:
            str: the full path to the current main file.
        """
        return self.folder / "info.json"

    def run(self):
        self.log.debug(f"{self.__class__.__name__}.run()")
        self.start()
        self.proccess(0)
        self.log.debug("Start executing notebooks")
        self.execute(self.state["notebooks"], self.folder / "output")

        notebooks = glob.glob(f"{self.folder / 'output'}/*")

        self.log.debug("Start rendering notebooks")
        self.render(notebooks, self.folder)
        if self.sign_report:
            self.log.debug("Start signing notebooks")
            self.sign()
            self.log.debug("Start validating notebooks")
            self.validate()
        self.end()

        return self.folder

    # report status.
    def start(self):
        self.log.debug(f"{self.__class__.__name__}.start()")
        self.state["status"] = "START"

    def proccess(self, progress):
        self.state["progress"] = progress

    def end(self, status="END"):
        self.log.debug(f"{self.__class__.__name__}.end()")
        self.proccess(100)
        self["status"] = status
        self["finished_at"] = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

    def event(self, event, message):
        self.state["events"].append({"type": event, "message": message})

    ###################
    ##### public ######
    ###################
    def execute(self, notebook_paths, output_folder, timout=600):
        """
        This function executes jupiter notebooks provided
        Args:
            notebook_paths (str): path to folder with notebooks
            output_folder (str): path where executed notebooks should be

        """
        self.log.debug(f"{self.__class__.__name__}.execute_notebooks()")
        # config = Config()
        # config.ExecutePreprocessor.kernel_name = "python3"

        for notebook_path in notebook_paths:
            notebook_name = notebook_path.split("/")[-1]
            try:
                with open(notebook_path, "r", encoding="utf-8") as nb_file:
                    try:
                        nb_node = nbformat.read(nb_file, as_version=4)
                    except nbformat.reader.NotJSONError:
                        self.log.debug(f"The file {notebook_path} is not valid JSON.")
                        continue
                    except nbformat.validator.ValidationError as e:
                        self.log.debug(
                            f"The file {notebook_path} is not a valid notebook; validation error: {e}"
                        )
                        continue
            except FileNotFoundError:
                self.log.error(f"The file {notebook_path} does not exist.")
                raise NoNotebookFoundException

            # import os
            os.environ["REPORT_NANE"] = "CITROS"
            os.environ["REPORT_VERSION"] = "REPORT_VERSION"
            os.environ["BATCH_SIMULATION"] = "BATCH_SIMULATION"
            os.environ["BATCH_NAME"] = "BATCH_NAME"
            os.environ["BATCH_VERSION"] = "BATCH_VERSION"

            os.environ["PG_HOST"] = "localhost"
            os.environ["PG_PORT"] = "5454"
            os.environ["PG_DATABASE"] = "citros"
            os.environ["PG_SCHEMA"] = "citros"
            os.environ["PG_USER"] = "citros"
            os.environ["PG_PASSWORD"] = "password"

            os.environ["CITROS_ROOT"] = self.reports_dir

            execute_preprocessor = ExecutePreprocessor(
                timeout=timout, kernel_name="python3"
            )
            try:
                execute_preprocessor.preprocess(
                    nb_node,
                    {"metadata": {"path": output_folder}},
                )
            except CellExecutionError as e:
                self.log.exception(e)
                # raise
            finally:
                with open(
                    output_folder / notebook_name, "wt", encoding="utf-8"
                ) as nb_file:
                    nbformat.write(nb_node, nb_file)

    def render(self, notebook_paths, output_folder, css_file_path=None):
        """
        This function renders executed notebooks to PDF file.

        Args:
            notebook_paths (str): path to folder with notebooks
            output_folder (str): path where notebooks should be rendered
            css_file_path (str, optional): path to css file, defaults to 'data/reports/templates/default_style.css'.
        """
        self.log.debug(
            f"{self.__class__.__name__}.render_notebooks_to_pdf({notebook_paths})"
        )

        html_exporter = HTMLExporter(theme="light")
        # from jinja2 import DictLoader

        # with open(
        #     importlib_resources.files(f"data.reports").joinpath(
        #         "templates/index.html.j2"
        #     ),
        #     "r",
        # ) as template_file:
        #     html_template = template_file.read()

        # dl = DictLoader({"citros": html_template})

        # html_exporter = HTMLExporter(extra_loaders=[dl], template_file="citros")
        returns = []
        for notebook_path in notebook_paths:
            output_pdf_path = os.path.join(
                output_folder, os.path.basename(notebook_path).replace(".ipynb", ".pdf")
            )
            try:
                with open(notebook_path) as nb_file:
                    nb_node = nbformat.read(nb_file, as_version=4)
            except FileNotFoundError:
                self.log.error(f"The file {notebook_path} does not exist.")
                raise NoNotebookFoundException

            (body, _) = html_exporter.from_notebook_node(nb_node)

            output_html_path = os.path.join(
                output_folder,
                os.path.basename(notebook_path).replace(".ipynb", ".html"),
            )

            with open(output_html_path, "w") as html_file:
                html_file.write(body)
            # print(final_html)

            HTML(string=body).write_pdf(output_pdf_path)

            returns.append(output_pdf_path)
        return returns

    def sign(self, pdf_path, private_key_path, output_folder):
        """
        Signs PDF with private key

        Args:
            pdf_path (str): path to PDF file that needs to be signed
            private_key_path (str): path to private key
            output_folder (str): path to folder where signed pdf should be saved
        """
        # TODO[critical]: implement signing
        raise NotImplementedError
        self.log.debug(f"{self.__class__.__name__}.sign_pdf_with_key()")
        with open(private_key_path, "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(), password=None, backend=default_backend()
            )

        reader = PdfReader(pdf_path)
        content = b"".join(
            [page.extract_text().encode("utf-8") for page in reader.pages]
        )

        signature = private_key.sign(
            content,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256(),
        )

        output_pdf_path = os.path.join(output_folder, os.path.basename(pdf_path))
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        writer.add_metadata({"/CitrosSign": signature})

        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)

    def validate(self, pdf_path, public_key_path):
        """
        Checks if signed PDF was altered or not using public key

        Args:
            pdf_path (str): path to PDF files for check
            public_key_path (str): path to public key

        Returns:
            bool: Result of check
        """
        raise NotImplementedError
        self.log.debug(f"{self.__class__.__name__}.verify()")
        with open(public_key_path, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(), backend=default_backend()
            )

        reader = PdfReader(pdf_path)
        content = b"".join(
            [page.extract_text().encode("utf-8") for page in reader.pages]
        )
        signature = reader.metadata.get("/CitrosSign", None)

        if signature is None:
            return False

        try:
            public_key.verify(
                signature,
                content,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH,
                ),
                hashes.SHA256(),
            )
            return True
        except Exception as e:
            self.log.exception(f"Verification failed: {e}")
            return False
