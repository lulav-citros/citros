"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[27918],{78945:(e,t,n)=>{n.r(t),n.d(t,{default:()=>ie});var a=n(67294),l=n(1944),o=n(902);const c=a.createContext(null);function s(e){let{children:t,content:n}=e;const l=function(e){return(0,a.useMemo)((()=>({metadata:e.metadata,frontMatter:e.frontMatter,assets:e.assets,contentTitle:e.contentTitle,toc:e.toc})),[e])}(n);return a.createElement(c.Provider,{value:l},t)}function r(){const e=(0,a.useContext)(c);if(null===e)throw new o.i6("DocProvider");return e}function i(){const{metadata:e,frontMatter:t,assets:n}=r();return a.createElement(l.d,{title:e.title,description:e.description,keywords:t.keywords,image:n.image??t.image})}var d=n(86010),m=n(87524),u=n(87462),p=n(95999),b=n(32244);function h(e){const{previous:t,next:n}=e;return a.createElement("nav",{className:"pagination-nav docusaurus-mt-lg","aria-label":(0,p.I)({id:"theme.docs.paginator.navAriaLabel",message:"Docs pages",description:"The ARIA label for the docs pagination"})},t&&a.createElement(b.Z,(0,u.Z)({},t,{subLabel:a.createElement(p.Z,{id:"theme.docs.paginator.previous",description:"The label used to navigate to the previous doc"},"Previous")})),n&&a.createElement(b.Z,(0,u.Z)({},n,{subLabel:a.createElement(p.Z,{id:"theme.docs.paginator.next",description:"The label used to navigate to the next doc"},"Next"),isNext:!0})))}function v(){const{metadata:e}=r();return a.createElement(h,{previous:e.previous,next:e.next})}var f=n(52263),E=n(39960),g=n(80143),L=n(35281),C=n(60373),N=n(74477);const k={unreleased:function(e){let{siteTitle:t,versionMetadata:n}=e;return a.createElement(p.Z,{id:"theme.docs.versions.unreleasedVersionLabel",description:"The label used to tell the user that he's browsing an unreleased doc version",values:{siteTitle:t,versionLabel:a.createElement("b",null,n.label)}},"This is unreleased documentation for {siteTitle} {versionLabel} version.")},unmaintained:function(e){let{siteTitle:t,versionMetadata:n}=e;return a.createElement(p.Z,{id:"theme.docs.versions.unmaintainedVersionLabel",description:"The label used to tell the user that he's browsing an unmaintained doc version",values:{siteTitle:t,versionLabel:a.createElement("b",null,n.label)}},"This is documentation for {siteTitle} {versionLabel}, which is no longer actively maintained.")}};function _(e){const t=k[e.versionMetadata.banner];return a.createElement(t,e)}function Z(e){let{versionLabel:t,to:n,onClick:l}=e;return a.createElement(p.Z,{id:"theme.docs.versions.latestVersionSuggestionLabel",description:"The label used to tell the user to check the latest version",values:{versionLabel:t,latestVersionLink:a.createElement("b",null,a.createElement(E.Z,{to:n,onClick:l},a.createElement(p.Z,{id:"theme.docs.versions.latestVersionLinkLabel",description:"The label used for the latest version suggestion link label"},"latest version")))}},"For up-to-date documentation, see the {latestVersionLink} ({versionLabel}).")}function y(e){let{className:t,versionMetadata:n}=e;const{siteConfig:{title:l}}=(0,f.Z)(),{pluginId:o}=(0,g.gA)({failfast:!0}),{savePreferredVersionName:c}=(0,C.J)(o),{latestDocSuggestion:s,latestVersionSuggestion:r}=(0,g.Jo)(o),i=s??(m=r).docs.find((e=>e.id===m.mainDocId));var m;return a.createElement("div",{className:(0,d.Z)(t,L.k.docs.docVersionBanner,"alert alert--warning margin-bottom--md"),role:"alert"},a.createElement("div",null,a.createElement(_,{siteTitle:l,versionMetadata:n})),a.createElement("div",{className:"margin-top--md"},a.createElement(Z,{versionLabel:r.label,to:i.path,onClick:()=>c(r.name)})))}function x(e){let{className:t}=e;const n=(0,N.E)();return n.banner?a.createElement(y,{className:t,versionMetadata:n}):null}function T(e){let{className:t}=e;const n=(0,N.E)();return n.badge?a.createElement("span",{className:(0,d.Z)(t,L.k.docs.docVersionBadge,"badge badge--secondary")},a.createElement(p.Z,{id:"theme.docs.versionBadge.label",values:{versionLabel:n.label}},"Version: {versionLabel}")):null}function B(e){let{lastUpdatedAt:t,formattedLastUpdatedAt:n}=e;return a.createElement(p.Z,{id:"theme.lastUpdated.atDate",description:"The words used to describe on which date a page has been last updated",values:{date:a.createElement("b",null,a.createElement("time",{dateTime:new Date(1e3*t).toISOString()},n))}}," on {date}")}function I(e){let{lastUpdatedBy:t}=e;return a.createElement(p.Z,{id:"theme.lastUpdated.byUser",description:"The words used to describe by who the page has been last updated",values:{user:a.createElement("b",null,t)}}," by {user}")}function H(e){let{lastUpdatedAt:t,formattedLastUpdatedAt:n,lastUpdatedBy:l}=e;return a.createElement("span",{className:L.k.common.lastUpdated},a.createElement(p.Z,{id:"theme.lastUpdated.lastUpdatedAtBy",description:"The sentence used to display when a page has been last updated, and by who",values:{atDate:t&&n?a.createElement(B,{lastUpdatedAt:t,formattedLastUpdatedAt:n}):"",byUser:l?a.createElement(I,{lastUpdatedBy:l}):""}},"Last updated{atDate}{byUser}"),!1)}var U=n(84881),w=n(86233);const A={lastUpdated:"lastUpdated_vwxv"};function M(e){return a.createElement("div",{className:(0,d.Z)(L.k.docs.docFooterTagsRow,"row margin-bottom--sm")},a.createElement("div",{className:"col"},a.createElement(w.Z,e)))}function P(e){let{editUrl:t,lastUpdatedAt:n,lastUpdatedBy:l,formattedLastUpdatedAt:o}=e;return a.createElement("div",{className:(0,d.Z)(L.k.docs.docFooterEditMetaRow,"row")},a.createElement("div",{className:"col"},t&&a.createElement(U.Z,{editUrl:t})),a.createElement("div",{className:(0,d.Z)("col",A.lastUpdated)},(n||l)&&a.createElement(H,{lastUpdatedAt:n,formattedLastUpdatedAt:o,lastUpdatedBy:l})))}function F(){const{metadata:e}=r(),{editUrl:t,lastUpdatedAt:n,formattedLastUpdatedAt:l,lastUpdatedBy:o,tags:c}=e,s=c.length>0,i=!!(t||n||o);return s||i?a.createElement("footer",{className:(0,d.Z)(L.k.docs.docFooter,"docusaurus-mt-lg")},s&&a.createElement(M,{tags:c}),i&&a.createElement(P,{editUrl:t,lastUpdatedAt:n,lastUpdatedBy:o,formattedLastUpdatedAt:l})):null}var S=n(86043),O=n(93743);const V={tocCollapsibleButton:"tocCollapsibleButton_TO0P",tocCollapsibleButtonExpanded:"tocCollapsibleButtonExpanded_MG3E"};function R(e){let{collapsed:t,...n}=e;return a.createElement("button",(0,u.Z)({type:"button"},n,{className:(0,d.Z)("clean-btn",V.tocCollapsibleButton,!t&&V.tocCollapsibleButtonExpanded,n.className)}),a.createElement(p.Z,{id:"theme.TOCCollapsible.toggleButtonLabel",description:"The label used by the button on the collapsible TOC component"},"On this page"))}const D={tocCollapsible:"tocCollapsible_ETCw",tocCollapsibleContent:"tocCollapsibleContent_vkbj",tocCollapsibleExpanded:"tocCollapsibleExpanded_sAul"};function $(e){let{toc:t,className:n,minHeadingLevel:l,maxHeadingLevel:o}=e;const{collapsed:c,toggleCollapsed:s}=(0,S.u)({initialState:!0});return a.createElement("div",{className:(0,d.Z)(D.tocCollapsible,!c&&D.tocCollapsibleExpanded,n)},a.createElement(R,{collapsed:c,onClick:s}),a.createElement(S.z,{lazy:!0,className:D.tocCollapsibleContent,collapsed:c},a.createElement(O.Z,{toc:t,minHeadingLevel:l,maxHeadingLevel:o})))}const q={tocMobile:"tocMobile_ITEo"};function z(){const{toc:e,frontMatter:t}=r();return a.createElement($,{toc:e,minHeadingLevel:t.toc_min_heading_level,maxHeadingLevel:t.toc_max_heading_level,className:(0,d.Z)(L.k.docs.docTocMobile,q.tocMobile)})}var j=n(39407);function W(){const{toc:e,frontMatter:t}=r();return a.createElement(j.Z,{toc:e,minHeadingLevel:t.toc_min_heading_level,maxHeadingLevel:t.toc_max_heading_level,className:L.k.docs.docTocDesktop})}var Y=n(92503),G=n(33101);function J(e){let{children:t}=e;const n=function(){const{metadata:e,frontMatter:t,contentTitle:n}=r();return t.hide_title||void 0!==n?null:e.title}();return a.createElement("div",{className:(0,d.Z)(L.k.docs.docMarkdown,"markdown")},n&&a.createElement("header",null,a.createElement(Y.Z,{as:"h1"},n)),a.createElement(G.Z,null,t))}var Q=n(53438),K=n(48596),X=n(44996);function ee(e){return a.createElement("svg",(0,u.Z)({viewBox:"0 0 24 24"},e),a.createElement("path",{d:"M10 19v-5h4v5c0 .55.45 1 1 1h3c.55 0 1-.45 1-1v-7h1.7c.46 0 .68-.57.33-.87L12.67 3.6c-.38-.34-.96-.34-1.34 0l-8.36 7.53c-.34.3-.13.87.33.87H5v7c0 .55.45 1 1 1h3c.55 0 1-.45 1-1z",fill:"currentColor"}))}const te={breadcrumbHomeIcon:"breadcrumbHomeIcon_YNFT"};function ne(){const e=(0,X.Z)("/");return a.createElement("li",{className:"breadcrumbs__item"},a.createElement(E.Z,{"aria-label":(0,p.I)({id:"theme.docs.breadcrumbs.home",message:"Home page",description:"The ARIA label for the home page in the breadcrumbs"}),className:"breadcrumbs__link",href:e},a.createElement(ee,{className:te.breadcrumbHomeIcon})))}const ae={breadcrumbsContainer:"breadcrumbsContainer_Z_bl"};function le(e){let{children:t,href:n,isLast:l}=e;const o="breadcrumbs__link";return l?a.createElement("span",{className:o,itemProp:"name"},t):n?a.createElement(E.Z,{className:o,href:n,itemProp:"item"},a.createElement("span",{itemProp:"name"},t)):a.createElement("span",{className:o},t)}function oe(e){let{children:t,active:n,index:l,addMicrodata:o}=e;return a.createElement("li",(0,u.Z)({},o&&{itemScope:!0,itemProp:"itemListElement",itemType:"https://schema.org/ListItem"},{className:(0,d.Z)("breadcrumbs__item",{"breadcrumbs__item--active":n})}),t,a.createElement("meta",{itemProp:"position",content:String(l+1)}))}function ce(){const e=(0,Q.s1)(),t=(0,K.Ns)();return e?a.createElement("nav",{className:(0,d.Z)(L.k.docs.docBreadcrumbs,ae.breadcrumbsContainer),"aria-label":(0,p.I)({id:"theme.docs.breadcrumbs.navAriaLabel",message:"Breadcrumbs",description:"The ARIA label for the breadcrumbs"})},a.createElement("ul",{className:"breadcrumbs",itemScope:!0,itemType:"https://schema.org/BreadcrumbList"},t&&a.createElement(ne,null),e.map(((t,n)=>{const l=n===e.length-1;return a.createElement(oe,{key:n,active:l,index:n,addMicrodata:!!t.href},a.createElement(le,{href:t.href,isLast:l},t.label))})))):null}const se={docItemContainer:"docItemContainer_Djhp",docItemCol:"docItemCol_VOVn"};function re(e){let{children:t}=e;const n=function(){const{frontMatter:e,toc:t}=r(),n=(0,m.i)(),l=e.hide_table_of_contents,o=!l&&t.length>0;return{hidden:l,mobile:o?a.createElement(z,null):void 0,desktop:!o||"desktop"!==n&&"ssr"!==n?void 0:a.createElement(W,null)}}();return a.createElement("div",{className:"row"},a.createElement("div",{className:(0,d.Z)("col",!n.hidden&&se.docItemCol)},a.createElement(x,null),a.createElement("div",{className:se.docItemContainer},a.createElement("article",null,a.createElement(ce,null),a.createElement(T,null),n.mobile,a.createElement(J,null,t),a.createElement(F,null)),a.createElement(v,null))),n.desktop&&a.createElement("div",{className:"col col--3"},n.desktop))}function ie(e){const t=`docs-doc-id-${e.content.metadata.unversionedId}`,n=e.content;return a.createElement(s,{content:e.content},a.createElement(l.FG,{className:t},a.createElement(i,null),a.createElement(re,null,a.createElement(n,null))))}},39407:(e,t,n)=>{n.d(t,{Z:()=>d});var a=n(87462),l=n(67294),o=n(86010),c=n(93743);const s={tableOfContents:"tableOfContents_bqdL",docItemContainer:"docItemContainer_F8PC"},r="table-of-contents__link toc-highlight",i="table-of-contents__link--active";function d(e){let{className:t,...n}=e;return l.createElement("div",{className:(0,o.Z)(s.tableOfContents,"thin-scrollbar",t)},l.createElement(c.Z,(0,a.Z)({},n,{linkClassName:r,linkActiveClassName:i})))}},93743:(e,t,n)=>{n.d(t,{Z:()=>b});var a=n(87462),l=n(67294),o=n(86668);function c(e){const t=e.map((e=>({...e,parentIndex:-1,children:[]}))),n=Array(7).fill(-1);t.forEach(((e,t)=>{const a=n.slice(2,e.level);e.parentIndex=Math.max(...a),n[e.level]=t}));const a=[];return t.forEach((e=>{const{parentIndex:n,...l}=e;n>=0?t[n].children.push(l):a.push(l)})),a}function s(e){let{toc:t,minHeadingLevel:n,maxHeadingLevel:a}=e;return t.flatMap((e=>{const t=s({toc:e.children,minHeadingLevel:n,maxHeadingLevel:a});return function(e){return e.level>=n&&e.level<=a}(e)?[{...e,children:t}]:t}))}function r(e){const t=e.getBoundingClientRect();return t.top===t.bottom?r(e.parentNode):t}function i(e,t){let{anchorTopOffset:n}=t;const a=e.find((e=>r(e).top>=n));if(a){return function(e){return e.top>0&&e.bottom<window.innerHeight/2}(r(a))?a:e[e.indexOf(a)-1]??null}return e[e.length-1]??null}function d(){const e=(0,l.useRef)(0),{navbar:{hideOnScroll:t}}=(0,o.L)();return(0,l.useEffect)((()=>{e.current=t?0:document.querySelector(".navbar").clientHeight}),[t]),e}function m(e){const t=(0,l.useRef)(void 0),n=d();(0,l.useEffect)((()=>{if(!e)return()=>{};const{linkClassName:a,linkActiveClassName:l,minHeadingLevel:o,maxHeadingLevel:c}=e;function s(){const e=function(e){return Array.from(document.getElementsByClassName(e))}(a),s=function(e){let{minHeadingLevel:t,maxHeadingLevel:n}=e;const a=[];for(let l=t;l<=n;l+=1)a.push(`h${l}.anchor`);return Array.from(document.querySelectorAll(a.join()))}({minHeadingLevel:o,maxHeadingLevel:c}),r=i(s,{anchorTopOffset:n.current}),d=e.find((e=>r&&r.id===function(e){return decodeURIComponent(e.href.substring(e.href.indexOf("#")+1))}(e)));e.forEach((e=>{!function(e,n){n?(t.current&&t.current!==e&&t.current.classList.remove(l),e.classList.add(l),t.current=e):e.classList.remove(l)}(e,e===d)}))}return document.addEventListener("scroll",s),document.addEventListener("resize",s),s(),()=>{document.removeEventListener("scroll",s),document.removeEventListener("resize",s)}}),[e,n])}function u(e){let{toc:t,className:n,linkClassName:a,isChild:o}=e;return t.length?l.createElement("ul",{className:o?void 0:n},t.map((e=>l.createElement("li",{key:e.id},l.createElement("a",{href:`#${e.id}`,className:a??void 0,dangerouslySetInnerHTML:{__html:e.value}}),l.createElement(u,{isChild:!0,toc:e.children,className:n,linkClassName:a}))))):null}const p=l.memo(u);function b(e){let{toc:t,className:n="table-of-contents table-of-contents__left-border",linkClassName:r="table-of-contents__link",linkActiveClassName:i,minHeadingLevel:d,maxHeadingLevel:u,...b}=e;const h=(0,o.L)(),v=d??h.tableOfContents.minHeadingLevel,f=u??h.tableOfContents.maxHeadingLevel,E=function(e){let{toc:t,minHeadingLevel:n,maxHeadingLevel:a}=e;return(0,l.useMemo)((()=>s({toc:c(t),minHeadingLevel:n,maxHeadingLevel:a})),[t,n,a])}({toc:t,minHeadingLevel:v,maxHeadingLevel:f});return m((0,l.useMemo)((()=>{if(r&&i)return{linkClassName:r,linkActiveClassName:i,minHeadingLevel:v,maxHeadingLevel:f}}),[r,i,v,f])),l.createElement(p,(0,a.Z)({toc:E,className:n,linkClassName:r},b))}},74477:(e,t,n)=>{n.d(t,{E:()=>s,q:()=>c});var a=n(67294),l=n(902);const o=a.createContext(null);function c(e){let{children:t,version:n}=e;return a.createElement(o.Provider,{value:n},t)}function s(){const e=(0,a.useContext)(o);if(null===e)throw new l.i6("DocsVersionProvider");return e}},34630:(e,t,n)=>{n.d(t,{Z:()=>d});var a=n(67294),l=n(86010),o=n(10195),c=n(95999),s=n(30345),r=n(37666);const i={copyButtonCopied:"copyButtonCopied__QnY",copyButtonIcons:"copyButtonIcons_FhaS",copyButtonIcon:"copyButtonIcon_phi_",copyButtonSuccessIcon:"copyButtonSuccessIcon_FfTR"};function d(e){let{code:t,className:n}=e;const[d,m]=(0,a.useState)(!1),u=(0,a.useRef)(void 0),p=(0,a.useCallback)((()=>{const e=t.split("\n").map((e=>e.startsWith(">>> ")?e.substring(4):e.startsWith("$ ")?e.substring(2):e)).join("\n");(0,o.Z)(e),m(!0),u.current=window.setTimeout((()=>{m(!1)}),1e3)}),[t]);return(0,a.useEffect)((()=>()=>window.clearTimeout(u.current)),[]),a.createElement("button",{type:"button","aria-label":d?(0,c.I)({id:"theme.CodeBlock.copied",message:"Copied",description:"The copied button label on code blocks"}):(0,c.I)({id:"theme.CodeBlock.copyButtonAriaLabel",message:"Copy code to clipboard",description:"The ARIA label for copy code blocks button"}),title:(0,c.I)({id:"theme.CodeBlock.copy",message:"Copy",description:"The copy button label on code blocks"}),className:(0,l.Z)("clean-btn",n,i.copyButton,d&&i.copyButtonCopied),onClick:p},a.createElement("span",{className:i.copyButtonIcons,"aria-hidden":"true"},a.createElement(s.Z,{className:i.copyButtonIcon}),a.createElement(r.Z,{className:i.copyButtonSuccessIcon})))}},47456:(e,t,n)=>{n.d(t,{Z:()=>s});var a=n(87462),l=n(67294),o=n(86010);const c={codeLine:"codeLine_iPqp",codeLineNumber:"codeLineNumber_F4P7",codeLineContent:"codeLineContent_pOih",unselectablePrefix:"unselectablePrefix_Y3F4"};function s(e){let{line:t,classNames:n,showLineNumbers:s,getLineProps:r,getTokenProps:i}=e;1===t.length&&"\n"===t[0].content&&(t[0].content="");const[d,m]=h(">");let u=!1,p=0,b=[...t];function h(e){let n=!1,a=0;return t.length>0&&t[0].content.startsWith(e)?(n=!0,a=0):t.length>1&&""==t[0].content&&t[1].content.startsWith(e)&&(n=!0,a=1),[n,a]}d?b=function(e){let n=[...t],a=-1,l=0+e,o=0,c=0;for(;l<t.length&&l<3+e;){for(o=0,c=0;o<t[l].content.length&&o<3+e-l&&">"==t[l].content[o];)c++,o++;c>0&&(n[l]={...t[l],content:t[l].content.substring(c)},a=l),l++}a>=0&&(n[a].content.length>0&&" "==n[a].content[0]?n[a]={...n[a],content:n[a].content.substring(1)}:n.length>a&&n[a+1].content.length>0&&" "==n[a+1].content[0]&&(n[a+1]={...n[a+1],content:n[a+1].content.substring(1)}));return n}(m):([u,p]=h("$"),u&&(b=function(e){let n=[...t],a=0+e;n[a]={...t[a],content:t[a].content.substring(1)},n[a].content.length>0&&" "==n[a].content[0]?n[a]={...n[a],content:n[a].content.substring(1)}:n.length>a&&n[a+1].content.length>0&&" "==n[a+1].content[0]&&(n[a+1]={...n[a+1],content:n[a+1].content.substring(1)});return n}(p)));const v=r({modifiedLine:b,className:(0,o.Z)(n,s&&c.codeLine)}),f=b.map(((e,t)=>l.createElement("span",(0,a.Z)({key:t},i({token:e,key:t})))));return l.createElement("span",v,s?l.createElement(l.Fragment,null,d?l.createElement(l.Fragment,null,l.createElement("span",{className:c.unselectablePrefix},">>> ")):l.createElement(l.Fragment,null,u?l.createElement(l.Fragment,null,l.createElement("span",{className:c.unselectablePrefix},"$ ")):l.createElement(l.Fragment,null)),l.createElement("span",{className:c.codeLineNumber}),l.createElement("span",{className:c.codeLineContent},f)):l.createElement(l.Fragment,null,d?l.createElement(l.Fragment,null,l.createElement("span",{className:c.unselectablePrefix},">>> ")):l.createElement(l.Fragment,null,u?l.createElement(l.Fragment,null,l.createElement("span",{className:c.unselectablePrefix},"$ ")):l.createElement(l.Fragment,null)),f),l.createElement("br",null))}}}]);