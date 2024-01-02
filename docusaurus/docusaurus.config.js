// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require("prism-react-renderer/themes/vsLight");
const darkCodeTheme = require("prism-react-renderer/themes/vsDark");
const math = require("remark-math");
const katex = require("rehype-katex");

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: "CITROS",
  tagline: "The starting point for your next robotic project", 
  favicon: "img/favicon.ico",

  // Set the production url of your site here
  url: 'https://docs.citros.io',
//   url: "http://localhost:3000",
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: "/",

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: "citros", // Usually your GitHub org/user name.
  projectName: "citros", // Usually your repo name.

  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",

  // Matkdown
  markdown: {
    mermaid: true,
  },
  themes: ["@docusaurus/theme-mermaid"],

  // Even if you don't use internalization, you can use this field to set useful
  // metadata like html lang. For example, if your site is Chinese, you may want
  // to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: "en",
    locales: ["en"],
  },

  presets: [
    [
      "classic",
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: "docs",
          sidebarPath: require.resolve("./sidebarsCLI.js"),
          remarkPlugins: [math],
          rehypePlugins: [katex],
        },
        // blog: {
        //   showReadingTime: true,
        //   remarkPlugins: [math],
        //   rehypePlugins: [katex],
        //   // Please change this to your repo.
        //   // Remove this to remove the "edit this page" links.
        //   //editUrl:
        //   //  'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        // },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      }),
    ],
  ],

  plugins: [
    [
      "@docusaurus/plugin-content-docs",
      {
        id: "docs_data_analysis",
        path: "docs_data_analysis",
        routeBasePath: "docs_data_analysis",
        sidebarPath: require.resolve("./sidebarsDataAnalysis.js"),
        remarkPlugins: [math],
        rehypePlugins: [katex],
        // includeCurrentVersion: false,
      },
    ],
    [
      "@docusaurus/plugin-content-docs",
      {
        id: "docs_tutorials",
        path: "docs_tutorials",
        routeBasePath: "docs_tutorials",
        sidebarPath: require.resolve("./sidebarsTutorials.js"),
        remarkPlugins: [math],
        rehypePlugins: [katex],
        // includeCurrentVersion: false,
      },
    ],
  ],

  stylesheets: [
    {
      //   href: "katex/katex.min.css",
      //   type: "text/css",
      href: "https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css",
      type: "text/css",
      // integrity:
      //   'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      // crossorigin: 'anonymous',
    },
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: "dark",
        disableSwitch: true,
        respectPrefersColorScheme: false,
      },

      // Replace with your project's social card
      image: "img/citros-link.png",

      navbar: {
        logo: {
          alt: "CITROS Logo",
          src: "img/citros.png",
          href: "https://docs.citros.io",
        },
        items: [
          {
            type: "docSidebar",
            sidebarId: "gettingStartedSidebar",
            label: "Docs",
            position: "left",
            activeBaseRegex: `/docs/`,
          },
          // {
          //   to: "/docs_cli", // ./docs-api/Intro.md
          //   label: "CLI",
          //   position: "left",
          //   activeBaseRegex: `/docs_cli/`,
          // },
          {
            to: "/docs_data_analysis", // ./docs-api/Intro.md
            label: "Data analysis",
            position: "left",
            activeBaseRegex: `/docs_data_analysis/`,
          },
          {
            to: "/docs_tutorials", // ./docs-api/Intro.md
            label: "Tutorials",
            position: "left",
            activeBaseRegex: `/docs_tutorials/`,
          },
          // { to: "/blog", label: "Blog", position: "left" },
          // {
          //   type: "docsVersionDropdown",
          //   position: "right",
          //   docsPluginId: "docs_cli",
          //   // dropdownItemsAfter: [{to: '/versions', label: 'All versions'}],
          //   // dropdownActiveClassDisabled: true,
          // },
          {
            type: "docsVersionDropdown",
            position: "right",
            docsPluginId: "docs_data_analysis",
            // dropdownItemsAfter: [{to: '/versions', label: 'All versions'}],
            dropdownActiveClassDisabled: false,
          },
        ],
      },
      footer: {
        style: "dark",
        links: [
          {
            title: "Visit",
            items: [
              // {
              //   label: "Blog",
              //   to: "/blog",
              // },
              {
                label: "Twitter",
                to: "https://twitter.com/lulavspace",
              },
              {
                label: "Linkdin",
                to: "https://www.linkedin.com/company/lulav-space/",
              },
              // {
              //   label: "Website",
              //   to: "https://www.lulav.space",
              // },
            ],
          },
          {
            title: "More to Learn",
            items: [
              // {
              //   label: 'ChangeLog',
              //   to: '/docs_data_analysis',
              // },
              {
                label: "CITROS Garden in GitHub",
                to: "https://github.com/citros-garden",
              },
            ],
          },
          {
            title: "Legal",
            items: [
              {
                label: "Terms and Conditions",
                to: "https://www.lulav.space",
              },
              {
                label: "Privacy Policy",
                to: "https://www.lulav.space",
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} Lulav Space.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
        additionalLanguages: ["python"],
      },
    }),
};

module.exports = config;
