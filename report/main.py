import os
import json
import sys
import nbformat
from PyPDF2 import PdfReader, PdfWriter
from nbconvert import HTMLExporter, PDFExporter
from nbconvert.preprocessors import ExecutePreprocessor
from traitlets.config import Config
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from weasyprint import HTML


def process_settings(settings_path):
    with open(settings_path, 'r') as settings_file:
        settings_data = json.load(settings_file)
        print(settings_data)
    return settings_data


def execute_notebooks(notebook_paths, output_folder):
    config = Config()
    config.ExecutePreprocessor.kernel_name = 'python3'

    for notebook_path in notebook_paths:
        with open(notebook_path, 'r', encoding='utf-8') as nb_file:
            try:
                nb_node = nbformat.read(nb_file, as_version=4)
            except nbformat.reader.NotJSONError:
                print(f"The file {notebook_path} is not valid JSON.")
                continue
            except nbformat.validator.ValidationError as e:
                print(f"The file {notebook_path} is not a valid notebook; validation error: {e}")
                continue

        execute_preprocessor = ExecutePreprocessor(config=config)
        execute_preprocessor.preprocess(nb_node, {'metadata': {'path': output_folder}})

        with open(notebook_path, 'wt', encoding='utf-8') as nb_file:
            nbformat.write(nb_node, nb_file)


def render_notebooks_to_pdf(notebook_paths, output_folder, css_file_path = 'data/reports/teplates/default_style.css'):
    html_exporter = HTMLExporter()

    for notebook_path in notebook_paths:
        output_pdf_path = os.path.join(output_folder, os.path.basename(notebook_path).replace('.ipynb', '.pdf'))
        with open(notebook_path) as nb_file:
            nb_node = nbformat.read(nb_file, as_version=4)

        (body, _) = html_exporter.from_notebook_node(nb_node)
        if css_file_path:
            with open(css_file_path, 'r') as css_file:
                css_content = css_file.read()
            body = '<style>\n' + css_content + '\n</style>\n' + body
            
        HTML(string=body).write_pdf(output_pdf_path)


def sign_pdf_with_key(pdf_path, private_key_path, output_folder):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    reader = PdfReader(pdf_path)
    content = b"".join([page.extract_text().encode('utf-8') for page in reader.pages])
    
    signature = private_key.sign(
        content,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    
    output_pdf_path = os.path.join(output_folder, os.path.basename(pdf_path))
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    writer.add_metadata({"/CitrosSign": signature})
    
    with open(output_pdf_path, 'wb') as output_file:
        writer.write(output_file)


def generate_signature(content, private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )

    signature = private_key.sign(
        content,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    
    return signature

def verify_pdf_signature(pdf_path, public_key_path):
    with open(public_key_path, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    reader = PdfReader(pdf_path)
    content = b"".join([page.extract_text().encode('utf-8') for page in reader.pages])
    signature = reader.metadata.get("/CitrosSign", None)
    
    if signature is None:
        return False

    try:
        public_key.verify(
            signature,
            content,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception as e:
        print(f"Verification failed: {e}")
        return False


def main(argv=None):
    if argv is None:
        argv = sys.argv

    if len(argv) < 3:
        print("Usage: python main.py [-e] [-r] [-s] [-c] <notebook_path1.ipynb> <notebook_path2.ipynb> ... <settings.json> [<style.css>] <output_folder>/")
        sys.exit(1)


    execute_flag = '-e' in sys.argv
    render_flag = '-r' in sys.argv
    sign_flag = '-s' in sys.argv
    check_flag = '-c' in sys.argv

    notebook_paths = [arg for arg in sys.argv if arg.endswith('.ipynb')]
    key_path = next((arg for arg in sys.argv if arg.endswith('.pem')), None)
    settings_path = next((arg for arg in sys.argv if arg.endswith('.json')), None)
    style_path = next((arg for arg in sys.argv if arg.endswith('.css')), None)
    output_folder = next((arg for arg in sys.argv if arg.endswith('/') or arg == sys.argv[-1]), None)

    if not check_flag and (not notebook_paths or not output_folder):
        print("Error: Missing notebook paths or output folder.")
        sys.exit(1)

    if (sign_flag or check_flag) and not key_path:
        print("Error: Missing key for signing/checking.")
        sys.exit(1)

    if settings_path is None:
        print("Error: Missing settings file.")
        sys.exit(1)

    if execute_flag:
        execute_notebooks(notebook_paths, output_folder)

    if render_flag:
        if style_path:
            render_notebooks_to_pdf(notebook_paths, output_folder, style_path)
        else:
            render_notebooks_to_pdf(notebook_paths, output_folder)

    if sign_flag:
        if not render_flag:
            print("Error: Signing requires notebooks to be rendered to PDF first.")
            sys.exit(1)
        pdf_paths = [os.path.join(output_folder, os.path.basename(notebook_path).replace('.ipynb', '.pdf')) for notebook_path in notebook_paths]
        for pdf_path in pdf_paths:
            sign_pdf_with_key(pdf_path, key_path, output_folder)

    elif check_flag:
        pdf_paths_to_check = [arg for arg in sys.argv if arg.endswith('.pdf')]
        for pdf_path in pdf_paths_to_check:
            if verify_pdf_signature(pdf_path, key_path):
                print(f"The contents of {pdf_path} are intact.")
            else:
                print(f"Warning: The contents of {pdf_path} may have been altered.")

    print("Operation completed.")


if __name__ == "__main__":
    main()
