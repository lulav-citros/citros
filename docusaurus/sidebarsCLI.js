module.exports = {
  gettingStartedSidebar: [

    {
      type: 'doc',
      label: 'Introduction',
      id: 'general/overview',
    },
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        {
          type: 'doc',
          id: 'general/quickstart',
          label: 'Quick Start',
        },
        {
          type: 'doc',
          id: 'general/install',
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
          id: 'commands/init',
          label: 'Init',
        },
        {
          type: 'doc',
          id: 'commands/launch',
          label: 'Launch',
        },
        {
          type: 'category',
          label: 'Data',
          link: {
            type: 'doc',
            id: 'commands/data',
          },
          items: [
            {
              type: 'doc',
              id: 'commands/data/list',
              label: 'List',
            },
            {
              type: 'doc',
              id: 'commands/data/tree',
              label: 'Tree',
            },
            {
              type: 'category',
              label: 'DB',
              link: {
                type: 'doc',
                id: 'commands/data/db',
              },
              items: ["commands/data/db/clean",
                "commands/data/db/create",
                "commands/data/db/init",
                "commands/data/db/logs",
                "commands/data/db/status",
                "commands/data/db/stop",]
            },
          ]
        },
        {
          type: 'category',
          label: 'Service',
          link: {
            type: 'doc',
            id: 'commands/service',
          },
          items: [
            "commands/service/status",
            "commands/service/start",
            "commands/service/stop",
          ]
        },
        {
          type: 'category',
          label: 'Parameter',
          link: {
            type: 'doc',
            id: 'commands/parameter',
          },
          items: [
            {

              type: 'category',
              label: 'Setup',
              link: {
                type: 'doc',
                id: 'commands/parameter/setup',
              },
              items: ["commands/parameter/setup/list",
                "commands/parameter/setup/new",]
            },
          ]
        },

        {
          type: 'category',
          label: 'Report',
          link: {
            type: 'doc',
            id: 'commands/report',
          },
          items: [
            "commands/report/generate",
            "commands/report/list",
            "commands/report/validate",
          ]
        },

        {
          type: 'category',
          label: 'Simulation',
          link: {
            type: 'doc',
            id: 'commands/simulation',
          },
          items: [
            "commands/simulation/list",
            "commands/simulation/run",
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
          id: 'guides/config_params',
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
          id: 'advanced_guides/install_advanced',
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
          id: 'advanced_guides/install_advanced',
        },

      ],
    }
    // {
    //   type: 'category',
    //   label: 'Data Analysis',

    // },
  ],
};
