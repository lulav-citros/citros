pip install git+https://github.com/lulav/pdoc.git@master

pdoc --pdf --force --output-dir=doc/citros_data_analysis/documentation -c show_type_annotations=False -c sort_identifiers=False citros/citros_data_analysis

# rm old documentation and index.md
rm doc/citros_data_analysis/documentation/index.md
rm -rf doc/citros_data_analysis/documentation/data_access/*
rm -rf doc/citros_data_analysis/documentation/error_analysis/*
rm -rf doc/citros_data_analysis/documentation/validation/*

# mv documentation according to modules
mv doc/citros_data_analysis/documentation/citros_db.md doc/citros_data_analysis/documentation/citros_dict.md doc/citros_data_analysis/documentation/data_access/

mv doc/citros_data_analysis/documentation/citros_data.md doc/citros_data_analysis/documentation/citros_data_array.md doc/citros_data_analysis/documentation/citros_stat.md doc/citros_data_analysis/documentation/error_analysis/

mv doc/citros_data_analysis/documentation/validation.md doc/citros_data_analysis/documentation/validation/

# write sidebar label
sed -i '3isidebar_label: '\''Class CitrosDB'\''' doc/citros_data_analysis/documentation/data_access/citros_db.md
sed -i '3isidebar_label: '\''Class CitrosDict'\''' doc/citros_data_analysis/documentation/data_access/citros_dict.md

sed -i '3isidebar_label: '\''Class CitrosData'\''' doc/citros_data_analysis/documentation/error_analysis/citros_data.md
sed -i '3isidebar_label: '\''Class CitrosDataArray'\''' doc/citros_data_analysis/documentation/error_analysis/citros_data_array.md
sed -i '3isidebar_label: '\''Class CitrosStat'\''' doc/citros_data_analysis/documentation/error_analysis/citros_stat.md

sed -i '3isidebar_label: '\''Class Validation'\''' doc/citros_data_analysis/documentation/validation/validation.md

#write title
sed -i '9i'\#' Class CitrosDB' doc/citros_data_analysis/documentation/data_access/citros_db.md
sed -i '9i'\#' Class CitrosDict' doc/citros_data_analysis/documentation/data_access/citros_dict.md

sed -i '9i'\#' Class CitrosData' doc/citros_data_analysis/documentation/error_analysis/citros_data.md
sed -i '9i'\#' Class CitrosDataArray' doc/citros_data_analysis/documentation/error_analysis/citros_data_array.md
sed -i '9i'\#' Class CitrosStat' doc/citros_data_analysis/documentation/error_analysis/citros_stat.md

sed -i '9i'\#' Class Validation' doc/citros_data_analysis/documentation/validation/validation.md
