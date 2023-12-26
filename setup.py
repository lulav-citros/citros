#!/usr/bin/env python3
# ==============================================
#  ██████╗██╗████████╗██████╗  ██████╗ ███████╗
# ██╔════╝██║╚══██╔══╝██╔══██╗██╔═══██╗██╔════╝
# ██║     ██║   ██║   ██████╔╝██║   ██║███████╗
# ██║     ██║   ██║   ██╔══██╗██║   ██║╚════██║
# ╚██████╗██║   ██║   ██║  ██║╚██████╔╝███████║
#  ╚═════╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝
# ==============================================
from setuptools import setup, find_packages
import citros_meta

try:
    import sys
    from semantic_release import setup_hook

    setup_hook(sys.argv)
except ImportError:
    pass


def read_requirements():
    with open("requirements.txt", "r") as req:
        content = req.read()
        requirements = content.split("\n")

    return requirements


setup(
    name=citros_meta.__title__,
    version=citros_meta.__version__,
    author=citros_meta.__author__,
    author_email=citros_meta.__author_email__,
    packages=find_packages(),
    package_data={"": ["*.json", "*.sh", "*.py", "*.md", ".gitignore", ".citrosignore"]},
    entry_points={
        "console_scripts": [
            "citros = bin.cli:main",
        ],
    },
    url=citros_meta.__url__,
    license=citros_meta.__license__,
    description="A cli entrypoint for the citros system.",
    long_description_content_type="text/markdown",
    long_description=open("pypi.md").read(),
    install_requires=read_requirements(),
    py_modules=["citros", "citros_meta", "data"],
    project_urls={
        "Documentation": "http://citros.io/doc/docs_cli",
        "Source Code": "https://github.com/lulav/citros_cli",
        "Bug Tracker": "https://github.com/lulav/citros_cli/issues",
    },
)
