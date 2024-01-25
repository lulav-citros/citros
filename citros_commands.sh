######################################
# To extract documentation from docstrings for citros/data/* :
# 1. make this file executable:

# chmod +x citros_data_analysis_doc.sh

# 2. install package for creating documentation:

# pip install git+https://github.com/lulav/pdoc.git@master

# 3. execute this script:

# ./citros_data_analysis_doc.sh

######################################

PYTHONWARNINGS="ignore" pdoc --pdf --force --output-dir=docusaurus/docs/data_analysis/documentation -c show_type_annotations=False -c sort_identifiers=False citros/data/access citros/data/analysis citros/data/validation

# # rm old documentation and index.md
# rm docusaurus/docs/data_analysis/documentation/index.md
# rm -rf docusaurus/docs/data_analysis/documentation/access/*
# rm -rf docusaurus/docs/data_analysis/documentation/analysis/*
# rm -rf docusaurus/docs/data_analysis/documentation/validation/*

# # mv documentation according to modules
# mv docusaurus/docs/data_analysis/documentation/citros_db.md docusaurus/docs/data_analysis/documentation/citros_dict.md docusaurus/docs/data_analysis/documentation/access/

# mv docusaurus/docs/data_analysis/documentation/citros_data.md docusaurus/docs/data_analysis/documentation/citros_data_array.md docusaurus/docs/data_analysis/documentation/citros_stat.md docusaurus/docs/data_analysis/documentation/analysis/

# mv docusaurus/docs/data_analysis/documentation/validation.md docusaurus/docs/data_analysis/documentation/validation/

# # write sidebar label
# sed -i '3isidebar_label: '\''Class CitrosDB'\''' docusaurus/docs/data_analysis/documentation/access/citros_db.md
# sed -i '3isidebar_label: '\''Class CitrosDict'\''' docusaurus/docs/data_analysis/documentation/access/citros_dict.md

# sed -i '3isidebar_label: '\''Class CitrosData'\''' docusaurus/docs/data_analysis/documentation/analysis/citros_data.md
# sed -i '3isidebar_label: '\''Class CitrosDataArray'\''' docusaurus/docs/data_analysis/documentation/analysis/citros_data_array.md
# sed -i '3isidebar_label: '\''Class CitrosStat'\''' docusaurus/docs/data_analysis/documentation/analysis/citros_stat.md

# sed -i '3isidebar_label: '\''Class Validation'\''' docusaurus/docs/data_analysis/documentation/validation/validation.md

# #write title
# sed -i '9i'\#' Class CitrosDB' docusaurus/docs/data_analysis/documentation/access/citros_db.md
# sed -i '9i'\#' Class CitrosDict' docusaurus/docs/data_analysis/documentation/access/citros_dict.md

# sed -i '9i'\#' Class CitrosData' docusaurus/docs/data_analysis/documentation/analysis/citros_data.md
# sed -i '9i'\#' Class CitrosDataArray' docusaurus/docs/data_analysis/documentation/analysis/citros_data_array.md
# sed -i '9i'\#' Class CitrosStat' docusaurus/docs/data_analysis/documentation/analysis/citros_stat.md

# sed -i '9i'\#' Class Validation' docusaurus/docs/data_analysis/documentation/validation/validation.md

cp -r citros/data/doc/cli citros/docusaurus/docs/commands

