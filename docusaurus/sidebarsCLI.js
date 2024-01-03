module.exports = {
  gettingStartedSidebar: [

    {
      type: 'doc',
      label: 'Introduction',
      id: 'cli/cli_overview',
    },
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        {
          type: 'doc',
          id: 'cli/cli_quickstart',
          label: 'Quick Start',
        },
        {
          type: 'doc',
          id: 'cli/cli_install',
          label: 'Installation',
        },
      ],

    },


    {



      type: 'category',
      label: 'Commands',
      items: [
        {
          type: 'doc',
          id: 'cli/commands/init',
          label: 'Init',
        },
        {
          type: 'doc',
          id: 'cli/commands/launch',
          label: 'Launch',
        },
        {
          type: 'category',
          label: 'Data',
          link: {
            type: 'doc',
            id: 'cli/commands/data',
          },
          items: [
            {
              type: 'doc',
              id: 'cli/commands/data/list',
              label: 'List',
            },
            {
              type: 'doc',
              id: 'cli/commands/data/tree',
              label: 'Tree',
            },
            {
              type: 'category',
              label: 'DB',
              link: {
                type: 'doc',
                id: 'cli/commands/data/db',
              },
              items: ["cli/commands/data/db/clean",
                "cli/commands/data/db/create",
                "cli/commands/data/db/init",
                "cli/commands/data/db/logs",
                "cli/commands/data/db/status",
                "cli/commands/data/db/stop",]
            },
          ]
        },
        {
          type: 'category',
          label: 'Service',
          link: {
            type: 'doc',
            id: 'cli/commands/service',
          },
          items: [
            "cli/commands/service/status",
            "cli/commands/service/start",
            "cli/commands/service/stop",
          ]
        },
        {
          type: 'category',
          label: 'Parameter',
          link: {
            type: 'doc',
            id: 'cli/commands/parameter',
          },
          items: [
            {

              type: 'category',
              label: 'Setup',
              link: {
                type: 'doc',
                id: 'cli/commands/parameter/setup',
              },
              items: ["cli/commands/parameter/setup/list",
                "cli/commands/parameter/setup/new",]
            },
          ]
        },

        {
          type: 'category',
          label: 'Report',
          link: {
            type: 'doc',
            id: 'cli/commands/report',
          },
          items: [
            "cli/commands/report/generate",
            "cli/commands/report/list",
            "cli/commands/report/validate",
          ]
        },

        {
          type: 'category',
          label: 'Simulation',
          link: {
            type: 'doc',
            id: 'cli/commands/simulation',
          },
          items: [
            "cli/commands/simulation/list",
            "cli/commands/simulation/run",
          ]
        },
      ]



    },

    {
      type: 'category',
      label: 'Guides',
      items: [
        {
          type: 'doc',
          label: 'Adding Functions to Parameter Setup',
          id: 'cli/config_params',
        },
        {
          type: 'doc',
          id: 'guides/getting_started',
          label: 'Installation',
        },
        {
          type: 'doc',
          id: 'guides/dockerfile_overview',
          label: 'Installation',
        },
      ],

    },

    {
      type: 'category',
      label: 'Advanced Guides',
      items: [
        {
          type: 'doc',
          label: 'CITROS Overview',
          id: 'advanced_guides/citros_overview',
        },
        {
          type: 'doc',
          label: '.CITROS File Structure',
          id: 'advanced_guides/citros_structure',
        },
        {
          type: 'doc',
          label: 'Advanced Installation',
          id: 'advanced_guides/cli_install_advanced',
        },
      ],

    },

    {
      type: 'category',
      label: 'Data Analysis',
      items: [
        {
          type: 'doc',
          label: 'TBD',
          id: 'advanced_guides/cli_install_advanced',
        },

      ],
    }
    // {
    //   type: 'category',
    //   label: 'Data Analysis',

    // },
  ],
};
