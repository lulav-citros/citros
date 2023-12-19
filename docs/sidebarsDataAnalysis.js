/**
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */


module.exports = {
  dataAnalysisSidebar: [
    {
      type: 'doc',
      id: "index",
    },
    {
      type: 'category',
      label: 'Snippets',
      items: [
        {
          type: 'category',
          label: 'Data Access',
          items: ["snippets_doc/data_access/snippets_repositories", 
                  "snippets_doc/data_access/snippets_batches",
                  "snippets_doc/data_access/snippets_users",
                  "snippets_doc/data_access/snippets_batch_content",
                  "snippets_doc/data_access/snippets_query_data", 
                  "snippets_doc/data_access/snippets_plotting"],
        },
        "snippets_doc/snippets_error_analysis", 
        "snippets_doc/snippets_validation"
      ]
    },
    {
      type: 'category',
      label: 'Data Access',
      items: [
        {
          type: 'doc',
          id: "data_access/index",
        },
        {
          type: 'category',
          label: 'Examples',
          items: ["data_access/getting_started", "data_access/repository_overview", "data_access/batch_overview",
                  "data_access/users_overview", "data_access/batch_content", "data_access/query_data",
                  "data_access/plot_data"],
        },
        {
          type: 'category',
          label: 'Documentation',
          items: ['documentation/data_access/citros_db', 'documentation/data_access/citros_dict', 
                  'documentation/data_access/references']
        },
      ]
    },
    {
      type: 'category',
      label: 'Error Analysis',
      items: [
        {
          type: 'doc',
          id: "error_analysis/index",
        },
        {
          type: 'category',
          label: 'Examples',
          items: ['error_analysis/getting_started_query_data', 'error_analysis/statistics', 
                  'error_analysis/correlation', 'error_analysis/regression', ],
        },
        {
          type: 'category',
          label: 'Documentation',
          items: ['documentation/error_analysis/citros_data', 'documentation/error_analysis/citros_data_array', 
                  'documentation/error_analysis/citros_stat'],
        },
      ],
    },
    {
      type: 'category',
      label: 'Validation',
      items: [
        {
          type: 'doc',
          id: "validation/index",
        },
        {
          type: 'category',
          label: 'Examples',
          items: ['validation/getting_started', 'validation/standard_deviation_boundary_test', 'validation/mean_value_test',
                  'validation/standard_deviation_test', 'validation/norm_test', 'validation/testing_each_simulation', 
                  'validation/set_multiple_tests'],
        },
        {
          type: 'category',
          label: 'Documentation',
          items: ['documentation/validation/validation'],
        },
      ],
    },
  ],
};