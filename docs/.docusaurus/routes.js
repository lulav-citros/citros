import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/docs/__docusaurus/debug',
    component: ComponentCreator('/docs/__docusaurus/debug', '4cc'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/config',
    component: ComponentCreator('/docs/__docusaurus/debug/config', '788'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/content',
    component: ComponentCreator('/docs/__docusaurus/debug/content', '949'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/globalData',
    component: ComponentCreator('/docs/__docusaurus/debug/globalData', '511'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/metadata',
    component: ComponentCreator('/docs/__docusaurus/debug/metadata', '92d'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/registry',
    component: ComponentCreator('/docs/__docusaurus/debug/registry', '9fe'),
    exact: true
  },
  {
    path: '/docs/__docusaurus/debug/routes',
    component: ComponentCreator('/docs/__docusaurus/debug/routes', '934'),
    exact: true
  },
  {
    path: '/docs/docs_data_analysis/next',
    component: ComponentCreator('/docs/docs_data_analysis/next', 'bc8'),
    routes: [
      {
        path: '/docs/docs_data_analysis/next/',
        component: ComponentCreator('/docs/docs_data_analysis/next/', '5c9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/', '062'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/batch_content', 'acd'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/batch_overview',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/batch_overview', '384'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/getting_started', '268'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/plot_data',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/plot_data', 'c03'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/query_data',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/query_data', 'a5b'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/repository_overview',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/repository_overview', 'a04'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/data_access/users_overview',
        component: ComponentCreator('/docs/docs_data_analysis/next/data_access/users_overview', '623'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/data_access/citros_db',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/data_access/citros_db', 'e82'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/data_access/citros_dict',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/data_access/citros_dict', 'ba9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/data_access/references',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/data_access/references', '20e'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/error_analysis/citros_data',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/error_analysis/citros_data', '994'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/error_analysis/citros_data_array',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/error_analysis/citros_data_array', 'a26'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/error_analysis/citros_stat',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/error_analysis/citros_stat', '918'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/documentation/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/next/documentation/validation/', 'a40'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/error_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/next/error_analysis/', '5b5'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/error_analysis/correlation',
        component: ComponentCreator('/docs/docs_data_analysis/next/error_analysis/correlation', 'e20'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/error_analysis/getting_started_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/next/error_analysis/getting_started_query_data', 'f47'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/error_analysis/regression',
        component: ComponentCreator('/docs/docs_data_analysis/next/error_analysis/regression', 'a85'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/error_analysis/statistics',
        component: ComponentCreator('/docs/docs_data_analysis/next/error_analysis/statistics', 'a41'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_batch_content', '0c6'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_batches',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_batches', '26d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_plotting',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_plotting', '797'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_query_data', '82b'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_repositories',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_repositories', '086'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_users',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/data_access/snippets_users', '555'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/snippets_error_analysis',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/snippets_error_analysis', '9cd'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/snippets_doc/snippets_validation',
        component: ComponentCreator('/docs/docs_data_analysis/next/snippets_doc/snippets_validation', '4f9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/', '272'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/getting_started', '37d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/mean_value_test',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/mean_value_test', '4c9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/norm_test',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/norm_test', '202'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/set_multiple_tests',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/set_multiple_tests', '593'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/standard_deviation_boundary_test',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/standard_deviation_boundary_test', 'f08'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/standard_deviation_test',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/standard_deviation_test', 'df9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/next/validation/testing_each_simulation',
        component: ComponentCreator('/docs/docs_data_analysis/next/validation/testing_each_simulation', '1cb'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      }
    ]
  },
  {
    path: '/docs/docs_data_analysis/v0.5.0',
    component: ComponentCreator('/docs/docs_data_analysis/v0.5.0', '627'),
    routes: [
      {
        path: '/docs/docs_data_analysis/v0.5.0/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/', 'b81'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/', '3a3'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/batch_content', '2a9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/batch_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/batch_overview', 'c6d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/getting_started', '075'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/plot_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/plot_data', '366'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/query_data', 'f4e'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/repository_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/repository_overview', '5ad'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/data_access/users_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/data_access/users_overview', '14d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/data_access/citros_db',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/data_access/citros_db', '00f'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/data_access/citros_dict',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/data_access/citros_dict', 'cbf'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_data', '550'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_data_array',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_data_array', '0ec'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_stat',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/error_analysis/citros_stat', 'a0d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/documentation/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/documentation/validation/', '324'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/error_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/error_analysis/', 'b53'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/error_analysis/correlation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/error_analysis/correlation', 'ca0'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/error_analysis/getting_started_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/error_analysis/getting_started_query_data', '4d1'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/error_analysis/regression',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/error_analysis/regression', '000'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/error_analysis/statistics',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/error_analysis/statistics', '91c'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/', 'b85'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/getting_started', 'cd0'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/mean_value_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/mean_value_test', '449'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/norm_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/norm_test', '870'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/set_multiple_tests',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/set_multiple_tests', '278'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/standard_deviation_boundary_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/standard_deviation_boundary_test', '7bc'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.5.0/validation/testing_each_simulation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.5.0/validation/testing_each_simulation', 'a56'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      }
    ]
  },
  {
    path: '/docs/docs_data_analysis/v0.7.17',
    component: ComponentCreator('/docs/docs_data_analysis/v0.7.17', '4e7'),
    routes: [
      {
        path: '/docs/docs_data_analysis/v0.7.17/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/', 'b3f'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/', 'af8'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/batch_content', '140'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/batch_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/batch_overview', '214'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/getting_started', '9db'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/plot_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/plot_data', '0ae'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/query_data', '99d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/repository_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/repository_overview', '26c'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/data_access/users_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/data_access/users_overview', '266'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/data_access/citros_db',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/data_access/citros_db', 'f78'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/data_access/citros_dict',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/data_access/citros_dict', '9b3'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/data_access/references',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/data_access/references', '599'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_data', '550'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_data_array',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_data_array', '1ed'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_stat',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/error_analysis/citros_stat', '092'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/documentation/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/documentation/validation/', 'dfd'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/error_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/error_analysis/', 'e26'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/error_analysis/correlation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/error_analysis/correlation', 'dba'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/error_analysis/getting_started_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/error_analysis/getting_started_query_data', 'f69'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/error_analysis/regression',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/error_analysis/regression', 'c32'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/error_analysis/statistics',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/error_analysis/statistics', 'f7a'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/', 'ff3'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/getting_started', '7d6'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/mean_value_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/mean_value_test', 'edb'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/norm_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/norm_test', '757'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/set_multiple_tests',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/set_multiple_tests', '4cf'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/standard_deviation_boundary_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/standard_deviation_boundary_test', 'b44'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/standard_deviation_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/standard_deviation_test', 'af8'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.7.17/validation/testing_each_simulation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.7.17/validation/testing_each_simulation', '929'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      }
    ]
  },
  {
    path: '/docs/docs_data_analysis/v0.8.0',
    component: ComponentCreator('/docs/docs_data_analysis/v0.8.0', '15d'),
    routes: [
      {
        path: '/docs/docs_data_analysis/v0.8.0/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/', '52c'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/', '2e7'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/batch_content', '98d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/batch_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/batch_overview', 'ae9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/getting_started', '596'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/plot_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/plot_data', '9f0'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/query_data', 'e20'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/repository_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/repository_overview', 'ebc'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/data_access/users_overview',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/data_access/users_overview', '359'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/data_access/citros_db',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/data_access/citros_db', 'f7a'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/data_access/citros_dict',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/data_access/citros_dict', 'dda'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/data_access/references',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/data_access/references', 'df6'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_data', 'da2'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_data_array',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_data_array', '0ef'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_stat',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/error_analysis/citros_stat', 'fc9'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/documentation/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/documentation/validation/', 'fe2'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/error_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/error_analysis/', 'b95'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/error_analysis/correlation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/error_analysis/correlation', '053'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/error_analysis/getting_started_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/error_analysis/getting_started_query_data', '842'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/error_analysis/regression',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/error_analysis/regression', '08a'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/error_analysis/statistics',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/error_analysis/statistics', '753'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_batch_content', 'c91'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_batches',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_batches', 'b31'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_plotting',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_plotting', 'aba'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_query_data', '437'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_repositories',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_repositories', '562'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_users',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/data_access/snippets_users', '5af'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/snippets_error_analysis',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/snippets_error_analysis', '939'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/snippets_doc/snippets_validation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/snippets_doc/snippets_validation', '822'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/', '32d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/getting_started', '180'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/mean_value_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/mean_value_test', '612'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/norm_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/norm_test', 'f15'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/set_multiple_tests',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/set_multiple_tests', '938'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/standard_deviation_boundary_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/standard_deviation_boundary_test', '533'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/standard_deviation_test',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/standard_deviation_test', 'f83'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/v0.8.0/validation/testing_each_simulation',
        component: ComponentCreator('/docs/docs_data_analysis/v0.8.0/validation/testing_each_simulation', 'a47'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      }
    ]
  },
  {
    path: '/docs/docs',
    component: ComponentCreator('/docs/docs', 'dff'),
    routes: [
      {
        path: '/docs/docs/',
        component: ComponentCreator('/docs/docs/', '7c4'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/citros_structure',
        component: ComponentCreator('/docs/docs/citros_structure', '060'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/cli_commands',
        component: ComponentCreator('/docs/docs/cli_commands', '65f'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/cli_install',
        component: ComponentCreator('/docs/docs/cli_install', '225'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/cli_quickstart',
        component: ComponentCreator('/docs/docs/cli_quickstart', '424'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/config_params',
        component: ComponentCreator('/docs/docs/config_params', '371'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/docs/docs/not_in_use/cli_install_advenced',
        component: ComponentCreator('/docs/docs/not_in_use/cli_install_advenced', 'a4c'),
        exact: true
      },
      {
        path: '/docs/docs/user_templates',
        component: ComponentCreator('/docs/docs/user_templates', '9a2'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      }
    ]
  },
  {
    path: '/docs/docs_data_analysis',
    component: ComponentCreator('/docs/docs_data_analysis', '083'),
    routes: [
      {
        path: '/docs/docs_data_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/', '4df'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/', 'c65'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/batch_content', 'fd6'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/batch_overview',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/batch_overview', '88d'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/getting_started', '55f'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/plot_data',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/plot_data', '723'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/query_data',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/query_data', 'fba'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/repository_overview',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/repository_overview', 'ec7'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/data_access/users_overview',
        component: ComponentCreator('/docs/docs_data_analysis/data_access/users_overview', '151'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/data_access/citros_db',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/data_access/citros_db', '4a0'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/data_access/citros_dict',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/data_access/citros_dict', 'cf2'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/data_access/references',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/data_access/references', '326'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/error_analysis/citros_data',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/error_analysis/citros_data', '3f1'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/error_analysis/citros_data_array',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/error_analysis/citros_data_array', '456'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/error_analysis/citros_stat',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/error_analysis/citros_stat', '8ff'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/documentation/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/documentation/validation/', 'fb8'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/error_analysis/',
        component: ComponentCreator('/docs/docs_data_analysis/error_analysis/', '775'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/error_analysis/correlation',
        component: ComponentCreator('/docs/docs_data_analysis/error_analysis/correlation', '5c6'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/error_analysis/getting_started_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/error_analysis/getting_started_query_data', '2cd'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/error_analysis/regression',
        component: ComponentCreator('/docs/docs_data_analysis/error_analysis/regression', 'a06'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/error_analysis/statistics',
        component: ComponentCreator('/docs/docs_data_analysis/error_analysis/statistics', '332'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_batch_content',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_batch_content', '30b'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_batches',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_batches', 'ea5'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_plotting',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_plotting', '682'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_query_data',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_query_data', '271'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_repositories',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_repositories', 'e75'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/data_access/snippets_users',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/data_access/snippets_users', '956'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/snippets_error_analysis',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/snippets_error_analysis', '603'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/snippets_doc/snippets_validation',
        component: ComponentCreator('/docs/docs_data_analysis/snippets_doc/snippets_validation', '7f0'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/',
        component: ComponentCreator('/docs/docs_data_analysis/validation/', '3aa'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/getting_started',
        component: ComponentCreator('/docs/docs_data_analysis/validation/getting_started', '7ea'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/mean_value_test',
        component: ComponentCreator('/docs/docs_data_analysis/validation/mean_value_test', 'e3f'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/norm_test',
        component: ComponentCreator('/docs/docs_data_analysis/validation/norm_test', 'cbc'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/set_multiple_tests',
        component: ComponentCreator('/docs/docs_data_analysis/validation/set_multiple_tests', '069'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/standard_deviation_boundary_test',
        component: ComponentCreator('/docs/docs_data_analysis/validation/standard_deviation_boundary_test', 'f90'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/standard_deviation_test',
        component: ComponentCreator('/docs/docs_data_analysis/validation/standard_deviation_test', '49e'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      },
      {
        path: '/docs/docs_data_analysis/validation/testing_each_simulation',
        component: ComponentCreator('/docs/docs_data_analysis/validation/testing_each_simulation', 'c9a'),
        exact: true,
        sidebar: "dataAnalysisSidebar"
      }
    ]
  },
  {
    path: '/docs/docs_tutorials',
    component: ComponentCreator('/docs/docs_tutorials', '0d1'),
    routes: [
      {
        path: '/docs/docs_tutorials/',
        component: ComponentCreator('/docs/docs_tutorials/', 'a44'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/dockerfile_overview/',
        component: ComponentCreator('/docs/docs_tutorials/dockerfile_overview/', '810'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/drone/',
        component: ComponentCreator('/docs/docs_tutorials/drone/', '8e1'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/gal_orbits/',
        component: ComponentCreator('/docs/docs_tutorials/gal_orbits/', 'dce'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/getting_started/',
        component: ComponentCreator('/docs/docs_tutorials/getting_started/', '4f6'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/mass_spring_damper/',
        component: ComponentCreator('/docs/docs_tutorials/mass_spring_damper/', '247'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/pendulum/',
        component: ComponentCreator('/docs/docs_tutorials/pendulum/', '7e3'),
        exact: true,
        sidebar: "tutorialSidebar"
      },
      {
        path: '/docs/docs_tutorials/soft_landing/',
        component: ComponentCreator('/docs/docs_tutorials/soft_landing/', '5ec'),
        exact: true,
        sidebar: "tutorialSidebar"
      }
    ]
  },
  {
    path: '/docs/',
    component: ComponentCreator('/docs/', '606'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
