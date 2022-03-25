System.register(["./chunk-vendor.js","./chunk-frameworks.js","./chunk-input-demux.js","./chunk-ref-selector.js"],function(){"use strict";var m,D,y,i,b,S,A,q,L,x,I;return{setters:[function(u){m=u.a,D=u.r,y=u.o,i=u.t,b=u.c},function(u){S=u.r,A=u.aD,q=u.aC,L=u.p,x=u.g,I=u.e},function(){},function(){}],execute:function(){var u=Object.defineProperty,v=(e,t)=>u(e,"name",{value:t,configurable:!0});m("click",".js-codespaces-update-skus-url",e=>{const t=e.currentTarget;if(!t)return;const o=t.getAttribute("data-refname");if(document.querySelector("form.js-prefetch-codespace-location")&&o){const n=document.querySelector("[data-codespace-skus-url]"),r=n?n.getAttribute("data-codespace-skus-url"):"";if(r){const a=new URL(r,window.location.origin);a.searchParams.set("ref_name",o),n&&n.setAttribute("data-codespace-skus-url",a.toString()),n&&n.setAttribute("data-branch-has-changed","true")}}}),m("remote-input-error","#js-codespaces-repository-select",()=>{const e=document.querySelector("#js-codespaces-unable-load-repositories-warning");e.hidden=!1}),D(".js-new-codespace-form",async function(e,t){const o=e.closest("[data-replace-remote-form-target]"),s=o.querySelector(".js-new-codespace-submit-button");s instanceof HTMLInputElement&&(s.disabled=!0),e.classList.remove("is-error"),e.classList.add("is-loading");try{const n=await t.html();o.replaceWith(n.html)}catch{e.classList.remove("is-loading"),e.classList.add("is-error")}});let M=null;function _(e){M=e,e!==null&&document.querySelector(".js-codespace-loading-steps").setAttribute("data-current-state",M)}v(_,"advanceLoadingState"),y(".js-codespace-loading-steps",{constructor:HTMLElement,add:e=>{const t=e.getAttribute("data-current-state");t&&_(t)}}),y(".js-codespace-advance-state",{constructor:HTMLElement,add:e=>{const t=e.getAttribute("data-state");t&&_(t)}});let B=null;function H(e){D(".js-fetch-cascade-token",async function(t,o){try{B=(await o.json()).json.token}catch{}}),S(e)}v(H,"fetchCascadeToken");function $(e,t,o){if(document.querySelector(e)){const n=Date.now(),a=setInterval(v(()=>{const C=Date.now()-n;if(B||C>=o){clearInterval(a),t(B||void 0);return}},"checkToken"),50)}}v($,"waitForCascadeTokenWithTimeout"),y(".js-auto-submit-form",{constructor:HTMLFormElement,initialize:S}),y(".js-workbench-form-container",{constructor:HTMLElement,add:e=>{const t=e.querySelector(".js-cascade-token");U(e,t)}});function U(e,t){if(t.value!==""){const o=e.querySelector("form");S(o)}else{const o=document.querySelector(".js-fetch-cascade-token");H(o),$(".js-workbench-form-container",R,1e4)}}v(U,"resolveCascadeToken");function R(e){const t=document.querySelector(".js-workbench-form-container form");t&&e?(V(t,e),W(t,e),S(t)):_("failed")}v(R,"insertCodespaceTokenIntoShowAuthForm");function V(e,t){const o=e.querySelector(".js-cascade-token");o&&o.setAttribute("value",t)}v(V,"insertCodespaceTokenIntoCascadeField");function W(e,t){const o=e.querySelector(".js-partner-info");if(o){let s=o.getAttribute("value");s&&(s=s.replace("%CASCADE_TOKEN_PLACEHOLDER%",t),o.setAttribute("value",s))}}v(W,"insertCodespaceTokenIntoPartnerInfo");var X=Object.defineProperty,ee=Object.getOwnPropertyDescriptor,te=(e,t)=>X(e,"name",{value:t,configurable:!0}),d=(e,t,o,s)=>{for(var n=s>1?void 0:s?ee(t,o):t,r=e.length-1,a;r>=0;r--)(a=e[r])&&(n=(s?a(t,o,n):a(n))||n);return s&&n&&X(t,o,n),n};let c=class extends HTMLElement{async connectedCallback(){const e=this.formForLocations();if(e){const t=await A(e,!this.vscsLocationList);this.updatePickableLocations(t)}}formForLocations(){return this.advancedOptionsForm||this.createCodespaceForm}toggleLoadingVscode(){const e=this.loadingVscode.hidden,t=this.children;for(let o=0;o<t.length;o++)t[o].hidden=e;this.loadingVscode.hidden=!e}machineTypeSelected(e){const o=e.currentTarget.getAttribute("data-sku-name");this.skuNameInput&&o&&(this.skuNameInput.value=o),this.advancedOptionsForm&&this.advancedOptionsForm.requestSubmit()}pollForVscode(e){this.toggleLoadingVscode();const t=e.currentTarget.getAttribute("data-src");t&&this.vscodePoller.setAttribute("src",t)}async updatePickableLocations(e){const t=this.formForLocations();if(!e&&t){const n=t.getAttribute("data-codespace-locations-url");if(!n)return;e=await q(n)}const o=e.current,s=e.available;this.hideUnavailableLocations(s),this.preventSubmissionOfUnavailableLocation(s,o)}hideUnavailableLocations(e){if(!!this.vscsLocationList)if(this.advancedOptionsForm){const t=this.vscsLocationList.querySelectorAll(".select-menu-item");for(const o of t){const s=o.querySelector("input");if(s&&e.includes(s.getAttribute("data-location"))){o.removeAttribute("hidden");continue}s&&(s.removeAttribute("checked"),s.setAttribute("aria-checked","false")),o.setAttribute("hidden","hidden")}}else{const t=this.vscsLocationList.querySelectorAll(".SelectMenu-item");for(const o of t)e.includes(o.getAttribute("data-location"))?o.removeAttribute("hidden"):o.setAttribute("hidden","hidden")}}preventSubmissionOfUnavailableLocation(e,t){if(this.createCodespaceForm){const o=this.createCodespaceForm.querySelector('[name="codespace[location]"]');o&&!e.includes(o.value)&&(o.value=t,this.vscsLocationSummary&&(this.vscsLocationSummary.textContent=this.vscsLocationSummary.getAttribute("data-blank-title")))}if(this.advancedOptionsForm){const o=this.advancedOptionsForm.querySelector('[name="location"]');o&&!e.includes(o.value)&&(o.value=t),!this.advancedOptionsForm.querySelector('[name="selected_location"]:checked')&&this.autoSelectLocation&&this.autoSelectLocation.hidden&&(this.selectedLocation&&this.selectedLocation.setAttribute("hidden","hidden"),this.needsSelectedLocation&&this.needsSelectedLocation.removeAttribute("hidden"))}}vscsTargetUrlUpdated(e){const t=e.currentTarget;this.vscsTargetUrl.value=t.value}};te(c,"NewCodespaceElement"),d([i],c.prototype,"form",2),d([i],c.prototype,"createCodespaceForm",2),d([i],c.prototype,"createCodespaceWithSkuSelectForm",2),d([i],c.prototype,"vscsTargetUrl",2),d([i],c.prototype,"vscsLocationList",2),d([i],c.prototype,"vscsLocationSummary",2),d([i],c.prototype,"loadingVscode",2),d([i],c.prototype,"vscodePoller",2),d([i],c.prototype,"advancedOptionsForm",2),d([i],c.prototype,"locationResubmitParam",2),d([i],c.prototype,"skuNameInput",2),d([i],c.prototype,"selectedLocation",2),d([i],c.prototype,"autoSelectLocation",2),d([i],c.prototype,"needsSelectedLocation",2),c=d([b],c);var oe=Object.defineProperty,k=(e,t)=>oe(e,"name",{value:t,configurable:!0});m("submit",".js-toggle-hidden-codespace-form",function(e){const t=e.currentTarget;g(t)}),m("click",".js-create-codespace-with-sku-button",async function(e){const t=e.currentTarget,o=t.closest("[data-target*='new-codespace.createCodespaceForm']")||t.closest("[data-target*='new-codespace.createCodespaceWithSkuSelectForm']");await A(o),o.classList.contains("js-open-in-vscode-form")?(g(o),F(o)):(o.submit(),T())});function g(e){const t=e.querySelectorAll(".js-toggle-hidden");for(const s of t)s.hidden=!s.hidden;const o=e.querySelectorAll(".js-toggle-disabled");for(const s of o)s.getAttribute("aria-disabled")?s.removeAttribute("aria-disabled"):s.setAttribute("aria-disabled","true")}k(g,"toggleFormSubmissionInFlight");function N(e){return e.closest("[data-replace-remote-form-target]")}k(N,"getFormTarget");async function T(){const e=document.querySelector(".js-codespaces-details-container");e&&(e.open=!1);const t=document.querySelector("new-codespace");if(t&&!t.getAttribute("data-no-submit-on-create"))try{const o=await fetch("/codespaces/new");if(o&&o.ok){const s=L(document,await o.text());t.replaceWith(s)}}catch{}}k(T,"createFormSubmitted"),m("submit",".js-create-codespaces-form-command",function(e){const t=e.currentTarget;t.classList.contains("js-open-in-vscode-form")||(T(),g(t))}),m("submit","form.js-codespaces-delete-form",async function(e){e.preventDefault();const t=e.currentTarget;try{const o=await fetch(t.action,{method:t.method,body:new FormData(t),headers:{Accept:"text/fragment+html","X-Requested-With":"XMLHttpRequest"}});if(o.ok){const s=L(document,await o.text());N(t).replaceWith(s)}else if(o.status===401)t.submit();else throw new Error(`Unexpected response: ${o.statusText}`)}finally{g(t)}}),m("submit","form.js-open-in-vscode-form",async function(e){e.preventDefault();const t=e.currentTarget;await F(t)});async function z(e,t){const o=document.querySelector(`#${e}`),s=await x({content:o.content.cloneNode(!0),dialogClass:"project-dialog"});return t&&t.setAttribute("aria-expanded","true"),s.addEventListener("dialog:remove",function(){t&&g(t)},{once:!0}),s}k(z,"openDialog");async function F(e){const t=await fetch(e.action,{method:e.method,body:new FormData(e),headers:{Accept:"application/json","X-Requested-With":"XMLHttpRequest"}});if(t.ok){const o=await t.json();o.codespace_url?(window.location.href=o.codespace_url,g(e),T(),G()):(e.closest("get-repo")||e.closest("new-codespace")?(e.setAttribute("data-src",o.loading_url),e.dispatchEvent(new CustomEvent("pollvscode"))):e.closest("prefetch-pane")&&(e.setAttribute("data-src",o.loading_url),e.dispatchEvent(new CustomEvent("prpollvscode"))),g(e))}else t.status===422&&await z("concurrency-error",e)}k(F,"createCodespaceIntoVscode");async function G(){const e=document.querySelector(".js-codespaces-completable"),t=e&&e.getAttribute("data-src");if(!t)return;const o=await fetch(t,{method:"GET",headers:{Accept:"text/fragment+html","X-Requested-With":"XMLHttpRequest"}});if(o.ok){const s=L(document,await o.text());e.replaceWith(s)}else throw new Error(`Unexpected response: ${o.statusText}`)}k(G,"renderAllDone");var K=Object.defineProperty,se=Object.getOwnPropertyDescriptor,ne=(e,t)=>K(e,"name",{value:t,configurable:!0}),O=(e,t,o,s)=>{for(var n=s>1?void 0:s?se(t,o):t,r=e.length-1,a;r>=0;r--)(a=e[r])&&(n=(s?a(t,o,n):a(n))||n);return s&&n&&K(t,o,n),n};let w=class extends HTMLElement{constructor(){super(...arguments);this.abortPoll=null}connectedCallback(){this.abortPoll=new AbortController,this.loadingIndicator.hidden||this.startPoll()}disconnectedCallback(){var e;(e=this.abortPoll)==null||e.abort()}async exportBranch(e){e.preventDefault(),this.form.hidden=!0,this.loadingIndicator.hidden=!1,(await fetch(this.form.action,{method:this.form.method,body:new FormData(this.form),headers:{Accept:"text/fragment+html","X-Requested-With":"XMLHttpRequest"}})).ok?this.startPoll():(this.form.hidden=!1,this.loadingIndicator.hidden=!0)}async startPoll(){const e=this.getAttribute("data-exported-codespace-url")||"",t=await this.poll(e);if(t)if(t.ok)this.loadingIndicator.hidden=!0,this.viewBranchLink.hidden=!1;else{const o=this.getAttribute("data-export-error-redirect-url")||"";window.location.href=o}}async poll(e,t=1e3){var o,s;if((o=this.abortPoll)==null?void 0:o.signal.aborted)return;const n=await fetch(e,{signal:(s=this.abortPoll)==null?void 0:s.signal});return n.status===202?(await new Promise(r=>setTimeout(r,t)),this.poll(e,t*1.5)):n}};ne(w,"ExportBranchElement"),O([i],w.prototype,"form",2),O([i],w.prototype,"loadingIndicator",2),O([i],w.prototype,"viewBranchLink",2),w=O([b],w);var Q=Object.defineProperty,ie=Object.getOwnPropertyDescriptor,re=(e,t)=>Q(e,"name",{value:t,configurable:!0}),f=(e,t,o,s)=>{for(var n=s>1?void 0:s?ie(t,o):t,r=e.length-1,a;r>=0;r--)(a=e[r])&&(n=(s?a(t,o,n):a(n))||n);return s&&n&&Q(t,o,n),n};let p=class extends HTMLElement{reset(e){for(e.preventDefault(),this.dropdownDetails.hidden=!1,this.modalDetails.hidden=!0,this.exportDetails.hidden=!0,this.skuForm.hidden=!1;this.resultMessage.firstChild;)this.resultMessage.removeChild(this.resultMessage.firstChild);this.resultMessage.hidden=!0,this.errorMessage.hidden=!0}showSettingsModal(){this.dropdownDetails.hidden=!0,this.modalDetails.open=!0,this.modalDetails.hidden=!1,this.dynamicSkus&&this.dynamicSkus.setAttribute("src",this.dynamicSkus.getAttribute("data-src"))}showExportModal(){this.dropdownDetails.hidden=!0,this.exportDetails.open=!0,this.exportDetails.hidden=!1,this.insertBranchExportComponent()}async insertBranchExportComponent(){const e=this.querySelector("[data-branch-export-url]");if(!e)return;const t=e.getAttribute("data-branch-export-url");if(!t)return;const o=await I(document,t);!o||(e.innerHTML="",e.appendChild(o))}};re(p,"OptionsPopoverElement"),f([i],p.prototype,"dropdownDetails",2),f([i],p.prototype,"modalDetails",2),f([i],p.prototype,"settingsModal",2),f([i],p.prototype,"skuForm",2),f([i],p.prototype,"resultMessage",2),f([i],p.prototype,"errorMessage",2),f([i],p.prototype,"exportDetails",2),f([i],p.prototype,"dynamicSkus",2),p=f([b],p);var Y=Object.defineProperty,ae=Object.getOwnPropertyDescriptor,ce=(e,t)=>Y(e,"name",{value:t,configurable:!0}),h=(e,t,o,s)=>{for(var n=s>1?void 0:s?ae(t,o):t,r=e.length-1,a;r>=0;r--)(a=e[r])&&(n=(s?a(t,o,n):a(n))||n);return s&&n&&Y(t,o,n),n};let l=class extends HTMLElement{constructor(){super(...arguments);this.prefetching=!1,this.remainingRetries=3}async connectedCallback(){this.openSkuButton&&this.skipSkuButton?(await this.prefetchLocationAndSkus(),this.hideSpinner(),this.hidden=!1):this.showOpenSkuButton()}async prefetchLocationAndSkus(){const e=this.getAttribute("data-branch-has-changed")==="true";if(this.prefetching&&!e)return;const t=document.querySelector("form.js-prefetch-codespace-location")||document.querySelector("form.js-open-in-vscode-form");if(t){this.prefetching=!0;const o=await A(t);if(o&&(this.currentLocation=o.current),!this.skuSelect)return;const s=this.getAttribute("data-codespace-skus-url");if(this.currentLocation&&s){const n=await fetch(`${s}&location=${this.currentLocation}`,{headers:{"X-Requested-With":"XMLHttpRequest",Accept:"text/html_fragment"}});if(n.ok){this.setAttribute("data-branch-has-changed","false");const r=L(document,await n.text()),C=Array.from(r.querySelectorAll("input[name='codespace[sku_name]']")).filter(j=>!j.disabled),E=C.find(j=>j.checked);E&&this.defaultSkuPreview?(this.defaultSkuPreview.innerHTML=E.getAttribute("data-preview")||"",this.showSkipSkuButton()):C.length===1?(E||C[0].select(),this.showSkipSkuButton()):this.disableDropDownButton(),this.skuSelect.replaceWith(r),this.skuSelect.hidden=!1,this.skuError&&(this.skuError.hidden=!0)}else this.showOpenSkuButton(),this.remainingRetries-=1,this.remainingRetries>0&&(this.prefetching=!1),this.skuSelect.hidden=!0,this.skuError&&(this.skuError.hidden=!1)}}}showOpenSkuButton(){var e;this.shownButton===void 0&&this.openSkuButton&&(this.shownButton=this.openSkuButton,this.shownButton.hidden=!1,(e=this.skipSkuButton)==null||e.remove())}hideSpinner(){const e=document.querySelector("[data-target='codespacesCreateButtonSpinner']");e&&(e.hidden=!0)}disableDropDownButton(){this.dropdownButton&&(this.useAdvancedCreation(),this.dropdownButton.style.pointerEvents="none",this.dropdownButton.classList.add("color-fg-muted"))}showSkipSkuButton(){var e,t;if(this.shownButton===void 0&&this.skipSkuButton){this.shownButton=this.skipSkuButton,this.shownButton.hidden=!1;const o=(e=this.openSkuButton)==null?void 0:e.parentElement;o&&o instanceof HTMLDetailsElement&&(o.hidden=!0),(t=this.openSkuButton)==null||t.remove()}}toggleLoadingVscode(){if(this.loadingVscode){const e=this.loadingVscode.hidden,t=this.children;for(let o=0;o<t.length;o++)t[o].hidden=e;this.loadingVscode.hidden=!e}}pollForVscode(e){if(this.vscodePoller){this.toggleLoadingVscode();const t=e.currentTarget.getAttribute("data-src");t&&this.vscodePoller.setAttribute("src",t)}}useBasicCreation(){this.advancedOptionsLink&&(this.openSkuButton&&(this.openSkuButton.hidden=!1),this.skipSkuButton&&(this.skipSkuButton.hidden=!1),this.advancedOptionsLink&&(this.advancedOptionsLink.hidden=!0)),this.basicOptionsCheck&&this.basicOptionsCheck.classList.remove("v-hidden"),this.advancedOptionsCheck&&this.advancedOptionsCheck.classList.add("v-hidden"),this.selectionDetails.open=!1}useAdvancedCreation(){this.advancedOptionsLink&&(this.openSkuButton&&(this.openSkuButton.hidden=!0),this.skipSkuButton&&(this.skipSkuButton.hidden=!0),this.advancedOptionsLink.hidden=!1),this.basicOptionsCheck&&this.basicOptionsCheck.classList.add("v-hidden"),this.advancedOptionsCheck&&this.advancedOptionsCheck.classList.remove("v-hidden"),this.selectionDetails.open=!1}};ce(l,"PrefetchPaneElement"),h([i],l.prototype,"skuSelect",2),h([i],l.prototype,"skuError",2),h([i],l.prototype,"selectionDetails",2),h([i],l.prototype,"loadingVscode",2),h([i],l.prototype,"vscodePoller",2),h([i],l.prototype,"openSkuButton",2),h([i],l.prototype,"skipSkuButton",2),h([i],l.prototype,"defaultSkuPreview",2),h([i],l.prototype,"dropdownButton",2),h([i],l.prototype,"advancedOptionsLink",2),h([i],l.prototype,"basicOptionsCheck",2),h([i],l.prototype,"advancedOptionsCheck",2),l=h([b],l);var Z=Object.defineProperty,de=Object.getOwnPropertyDescriptor,le=(e,t)=>Z(e,"name",{value:t,configurable:!0}),J=(e,t,o,s)=>{for(var n=s>1?void 0:s?de(t,o):t,r=e.length-1,a;r>=0;r--)(a=e[r])&&(n=(s?a(t,o,n):a(n))||n);return s&&n&&Z(t,o,n),n};let P=class extends HTMLElement{async connectedCallback(){this.closeDetailsPopover();const e=this.getAttribute("data-codespace-url");e&&(window.location.href=e)}closeDetailsPopover(){const e=document.querySelector(".js-codespaces-details-container");e&&(e.open=!1)}};le(P,"VscodeForwarderElement"),J([i],P.prototype,"vscodeLink",2),P=J([b],P)}}});
//# sourceMappingURL=codespaces-736c7ece.js.map
