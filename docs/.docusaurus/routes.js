import React from 'react';
import ComponentCreator from '@docusaurus/ComponentCreator';

export default [
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
