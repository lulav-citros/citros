import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
  {
    path: '/doc/__docusaurus/debug',
    component: ComponentCreator('/doc/__docusaurus/debug', 'c62'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/config',
    component: ComponentCreator('/doc/__docusaurus/debug/config', 'f7e'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/content',
    component: ComponentCreator('/doc/__docusaurus/debug/content', '504'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/globalData',
    component: ComponentCreator('/doc/__docusaurus/debug/globalData', 'f10'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/metadata',
    component: ComponentCreator('/doc/__docusaurus/debug/metadata', '336'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/registry',
    component: ComponentCreator('/doc/__docusaurus/debug/registry', '970'),
    exact: true
  },
  {
    path: '/doc/__docusaurus/debug/routes',
    component: ComponentCreator('/doc/__docusaurus/debug/routes', '038'),
    exact: true
  },
  {
    path: '/doc/docs',
    component: ComponentCreator('/doc/docs', 'd3e'),
    routes: [
      {
        path: '/doc/docs/',
        component: ComponentCreator('/doc/docs/', '4f3'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/citros_structure',
        component: ComponentCreator('/doc/docs/citros_structure', 'a42'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/cli_commands',
        component: ComponentCreator('/doc/docs/cli_commands', 'eea'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/cli_install',
        component: ComponentCreator('/doc/docs/cli_install', 'bae'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/cli_quickstart',
        component: ComponentCreator('/doc/docs/cli_quickstart', '61e'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/config_params',
        component: ComponentCreator('/doc/docs/config_params', 'b62'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      },
      {
        path: '/doc/docs/not_in_use/cli_install_advenced',
        component: ComponentCreator('/doc/docs/not_in_use/cli_install_advenced', 'ed0'),
        exact: true
      },
      {
        path: '/doc/docs/user_templates',
        component: ComponentCreator('/doc/docs/user_templates', '193'),
        exact: true,
        sidebar: "gettingStartedSidebar"
      }
    ]
  },
  {
    path: '/doc/',
    component: ComponentCreator('/doc/', 'fcd'),
    exact: true
  },
  {
    path: '*',
    component: ComponentCreator('*'),
  },
];
