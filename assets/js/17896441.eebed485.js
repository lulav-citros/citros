"use strict";(self.webpackChunkcitros_doc=self.webpackChunkcitros_doc||[]).push([[7918],{34630:(e,t,n)=>{n.d(t,{Z:()=>i});var c=n(67294),o=n(86010),l=n(10195),s=n(95999),a=n(30345),r=n(37666);const u={copyButtonCopied:"copyButtonCopied__QnY",copyButtonIcons:"copyButtonIcons_FhaS",copyButtonIcon:"copyButtonIcon_phi_",copyButtonSuccessIcon:"copyButtonSuccessIcon_FfTR"};function i(e){let{code:t,className:n}=e;const[i,m]=(0,c.useState)(!1),p=(0,c.useRef)(void 0),d=(0,c.useCallback)((()=>{const e=t.split("\n").map((e=>e.startsWith(">>> ")?e.substring(4):e.startsWith("$ ")?e.substring(2):e)).join("\n");(0,l.Z)(e),m(!0),p.current=window.setTimeout((()=>{m(!1)}),1e3)}),[t]);return(0,c.useEffect)((()=>()=>window.clearTimeout(p.current)),[]),c.createElement("button",{type:"button","aria-label":i?(0,s.I)({id:"theme.CodeBlock.copied",message:"Copied",description:"The copied button label on code blocks"}):(0,s.I)({id:"theme.CodeBlock.copyButtonAriaLabel",message:"Copy code to clipboard",description:"The ARIA label for copy code blocks button"}),title:(0,s.I)({id:"theme.CodeBlock.copy",message:"Copy",description:"The copy button label on code blocks"}),className:(0,o.Z)("clean-btn",n,u.copyButton,i&&u.copyButtonCopied),onClick:d},c.createElement("span",{className:u.copyButtonIcons,"aria-hidden":"true"},c.createElement(a.Z,{className:u.copyButtonIcon}),c.createElement(r.Z,{className:u.copyButtonSuccessIcon})))}},47456:(e,t,n)=>{n.d(t,{Z:()=>a});var c=n(87462),o=n(67294),l=n(86010);const s={codeLine:"codeLine_iPqp",codeLineNumber:"codeLineNumber_F4P7",codeLineContent:"codeLineContent_pOih",unselectablePrefix:"unselectablePrefix_Y3F4"};function a(e){let{line:t,classNames:n,showLineNumbers:a,getLineProps:r,getTokenProps:u}=e;1===t.length&&"\n"===t[0].content&&(t[0].content="");const[i,m]=g(">");let p=!1,d=0,b=[...t];function g(e){let n=!1,c=0;return t.length>0&&t[0].content.startsWith(e)?(n=!0,c=0):t.length>1&&""==t[0].content&&t[1].content.startsWith(e)&&(n=!0,c=1),[n,c]}i?b=function(e){let n=[...t],c=-1,o=0+e,l=0,s=0;for(;o<t.length&&o<3+e;){for(l=0,s=0;l<t[o].content.length&&l<3+e-o&&">"==t[o].content[l];)s++,l++;s>0&&(n[o]={...t[o],content:t[o].content.substring(s)},c=o),o++}c>=0&&(n[c].content.length>0&&" "==n[c].content[0]?n[c]={...n[c],content:n[c].content.substring(1)}:n.length>c&&n[c+1].content.length>0&&" "==n[c+1].content[0]&&(n[c+1]={...n[c+1],content:n[c+1].content.substring(1)}));return n}(m):([p,d]=g("$"),p&&(b=function(e){let n=[...t],c=0+e;n[c]={...t[c],content:t[c].content.substring(1)},n[c].content.length>0&&" "==n[c].content[0]?n[c]={...n[c],content:n[c].content.substring(1)}:n.length>c&&n[c+1].content.length>0&&" "==n[c+1].content[0]&&(n[c+1]={...n[c+1],content:n[c+1].content.substring(1)});return n}(d)));const h=r({modifiedLine:b,className:(0,l.Z)(n,a&&s.codeLine)}),E=b.map(((e,t)=>o.createElement("span",(0,c.Z)({key:t},u({token:e,key:t})))));return o.createElement("span",h,a?o.createElement(o.Fragment,null,i?o.createElement(o.Fragment,null,o.createElement("span",{className:s.unselectablePrefix},">>> ")):o.createElement(o.Fragment,null,p?o.createElement(o.Fragment,null,o.createElement("span",{className:s.unselectablePrefix},"$ ")):o.createElement(o.Fragment,null)),o.createElement("span",{className:s.codeLineNumber}),o.createElement("span",{className:s.codeLineContent},E)):o.createElement(o.Fragment,null,i?o.createElement(o.Fragment,null,o.createElement("span",{className:s.unselectablePrefix},">>> ")):o.createElement(o.Fragment,null,p?o.createElement(o.Fragment,null,o.createElement("span",{className:s.unselectablePrefix},"$ ")):o.createElement(o.Fragment,null)),E),o.createElement("br",null))}}}]);