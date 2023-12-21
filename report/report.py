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
    """
    This function executes jupiter notebooks provided
    Args:
        notebook_paths (str): path to folder with notebooks 
        output_folder (str): path where executed notebooks should be
        
    """
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


def render_notebooks_to_pdf(notebook_paths, output_folder, css_file_path='data/reports/templates/default_style.css'):
    """
    This function renders executed notebooks to PDF file.

    Args:
        notebook_paths (str): path to folder with notebooks
        output_folder (str): path where notebooks should be rendered
        css_file_path (str, optional): path to css file, defaults to 'data/reports/templates/default_style.css'.
    """
    html_exporter = HTMLExporter()
    
    with open('data/reports/teplates/default_template.html', 'r') as template_file:
        html_template = template_file.read()

    for notebook_path in notebook_paths:
        output_pdf_path = os.path.join(output_folder, os.path.basename(notebook_path).replace('.ipynb', '.pdf'))
        with open(notebook_path) as nb_file:
            nb_node = nbformat.read(nb_file, as_version=4)

        (body, _) = html_exporter.from_notebook_node(nb_node)

        if css_file_path:
            with open(css_file_path, 'r') as css_file:
                css_content = css_file.read()
            body = '<style>\n' + css_content + '\n</style>\n' + body

        final_html = html_template.replace('{{ notebook_content }}', body)

        HTML(string=final_html).write_pdf(output_pdf_path)


def sign_pdf_with_key(pdf_path, private_key_path, output_folder):
    """
    Signs PDF with private key

    Args:
        pdf_path (str): path to PDF file that needs to be signed
        private_key_path (str): path to private key
        output_folder (str): path to folder where signed pdf should be saved
    """
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
    """
    Checks if signed PDF was altered or not using public key
    
    Args:
        pdf_path (str): path to PDF files for check
        public_key_path (str): path to public key

    Returns:
        bool: Result of check
    """
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
