(function(){var ur=function(a){OBR.i.gk&&(a.state.HK.forEach(b=>b.setAttribute("loading","eager")),tr(a))},wr=function(a){const b=a.state.nt;b&&b.addEventListener("click",()=>vr(a),{once:!0})},vr=function(a){const b=a.state.Cx,c=a.state.Te,d=a.state.da;d&&d.C.Hz.fire();a.state.fw=!0;clearInterval(b);c.classList.add("ob-read-next-out");c.addEventListener("animationend",()=>c.remove())},zr=function(a){const b=a.state.j,c=a.state.settings,d=a.state.uJ,e=a.state.vq,f=c.yK;a.state.Te.classList.add("ob-read-next-visible");
setTimeout(()=>OBR.sc.ah(b.H()),0);OBR.za.nc(b,e);1<d&&(xr(a),OBR._jsc.fi("visibilitychange",()=>a.state.paused=document.hidden),a.state.Cx=setInterval(()=>{!a.state.paused&&a.next()},f));if(b.pp()){const g={onClose:()=>{a.state.paused=!1},onPlay:()=>{a.state.paused=!0}};OBR.controller.Kh(b,k=>{OBR._jsc.Qi(k.currentWidget,k.beforeLoadTime,g)})}c.O&&yr(a)},Ar=function(a){const b=a.state.ka;b.style.visibility="hidden";b.style.opacity="0";a.state.settings.O||(b.style.transform="translate(-100%)");
a.state.paused=!0},Br=function(a){const b=a.state.ka;b.style.visibility="visible";b.style.opacity="1";b.style.transform="";a.state.paused=!1},xr=function(a){a.As();window.addEventListener("resize",a.dL)},yr=function(a){var b=a.state.settings.xK;let c=0;b&&(b=OBR._jsc.ci(b),Array.from(b).forEach(d=>{(new OBR.IntersectionObserver({callback:e=>{0!==e.intersectionRatio?(c++,Ar(a)):0!==c&&(c--,c||Br(a))},element:d,threshold:0,intersectPercentage:-1,unobserve:!1})).observe()}))},tr=function(a){a=a.state.j.A();
Array.from(a.querySelectorAll(".ob-rec-rtb-image")).map(b=>{if(b=b.style.backgroundImage)return b.substring(5,b.length-2)}).forEach(b=>{b&&((new Image).src=b)})},Cr=class{B(a){if(!this.state){this.state=this.wm(a);if(a=!this.state.fw){var b;if(b=((a=this.state.settings.wK)?2===a.split(":").length:!1)&&a.split(":"))if(a=OBR._jsc.Tc("rn")){{const [e,f]=b,[g,k]=a.split(",");b=Date.now();if(Math.abs(b-g)/36E5<f&&k>=e)a=!1;else{var [c,d]=a.split(",");Math.abs(b-c)/36E5>f?OBR._jsc.Sc("rn",`${b},1`):OBR._jsc.Sc("rn",
`${c},${parseInt(d)+1}`);a=!0}}}else OBR._jsc.Sc("rn",`${Date.now()},1`),a=!0;else a=!0}if(a){ur(this);this.pm();a=this.state.settings;b=this.state.Te;const e=this.Gm();a.O?(e.right&&(b.style.right="0px"),e.bottom&&(b.style.bottom="0px")):(e.top&&(b.style.top=`${e.top}px`),e.bottom&&(b.style.bottom=`${e.bottom}px`),e.left&&(b.style.left=`${e.left}px`),e.right&&(b.style.right=`${e.right}px`));wr(this);this.$d();this.dL=OBR.Ye(this.As.bind(this),500);this.play()}}}wm(a){const b=this.sm(a),c=a.A(),
d=c.querySelector(".ob-read-next-layout");b.O&&(d.classList.add("ob-mobile-read-next"),b.isRTL&&d.classList.add("ob-mobile-read-next-RTL"));const e=Array.from(c.querySelectorAll(".ob-dynamic-rec-container")),f=Array.from(c.querySelectorAll(".ob-rec-image")),g=e.length,k=e[0],l=0===g||!b.Ax,n=new OBR.dataBI(a,h=>h.gg);k&&k.classList.add("ob-active-card");return{j:a,ka:c,settings:b,Te:d,vq:e,HK:f,Es:k,Fs:0,uJ:g,nt:void 0,fw:l,Cx:void 0,da:n,paused:!1}}sm(a){const b=1E3*parseInt(a.l("readNextDelayBeforeShow",
10),10),c=1E3*parseInt(a.l("readNextIntervalBetweenRecs",6),10),d=a.l("frequencyCapping",null),e=a.l("readNextText","Read Next Story"),f="mobile"===a.o("readerPlatform",""),g="RTL"===a.l("dynamicWidgetDirection","LTR"),[k,l]=a.l("readNextOffset","15,15").split(",").map(m=>+m),n={x:k,y:l},h=a.l("readNextHideSelector","");return{vK:b,yK:c,zK:n,Ax:e,wK:d,AK:a.l("readNextPosition","bottom-right"),O:f,isRTL:g,xK:h}}$d(){OBR.za.$b(this.state.j,{uh:!0})}pm(){const a=this.state.vq,b=this.state.Te;var c=this.state.settings;
const d=c.isRTL,e=c.Ax;c=c.O;const f=OBR._jsc.V("span");f.innerHTML='<button class="ob-read-next-close-container" title="close" type="button">\n          <img class="ob-read-next-close" src="https://widgets.outbrain.com/images/widgetIcons/icon-x.svg" alt=""/>\n        </button>';d&&c&&f.querySelector(".ob-read-next-close-container").classList.add("ob-read-next-close-container-RTL");b.insertBefore(f.firstChild,b.firstChild);this.state.nt=b.firstChild;a.forEach(g=>{const k=OBR._jsc.V("span");k.innerHTML=
`${e}&nbsp;
        <img class="ob-read-next-chevron" src="https://widgets.outbrain.com/images/widgetIcons/icon-chevron.svg" alt=""/>`;k.classList="ob-unit ob-rec-button";g.querySelector(".ob-sub-units").appendChild(k)})}Gm(){const a=this.state.settings,b=this.state.Te,c=a.AK,d=a.zK,e=b.getAttribute("style");b.style.display="block";b.style.visibility="hidden";b.getBoundingClientRect();b.setAttribute("style",e);if(a.O)return{bottom:d.y,right:d.x};switch(c){case "top-right":return this.position="right",{top:d.y,
right:d.x};case "bottom-left":return this.position="left",{bottom:30+d.y,left:d.x};case "bottom-right":return this.position="right",{bottom:30+d.y,right:d.x}}this.position="left";return{top:d.y,left:d.x}}play(){setTimeout(()=>zr(this),this.state.settings.vK)}As(){const a=this.state.settings,b=this.state.Te;("right"===this.position?b.offsetLeft:window.innerWidth-b.offsetLeft-b.offsetWidth)<window.innerWidth/2&&!a.O?Ar(this):Br(this)}next(){var a=this.state.vq;const b=this.state.Es,c=(this.state.Fs+
1)%a.length;a=a[c];a.classList.add("ob-active-card");b.classList.add("ob-active-exit");b.addEventListener("animationend",()=>{b.classList.remove("ob-active-card");b.classList.remove("ob-active-exit")},{once:!0});this.state.Es=a;this.state.Fs=c}};OBR.zx=OBR.zx||new Cr;OBR.s.U(OBR.s.v.gg);}).call(window);