
(function(){
 var END=new Date('2026-10-15T23:59:59+05:30').getTime(),expired=false,cds=document.querySelectorAll('[data-cd]'),pop=document.getElementById('offerPop'),lastF=null;
 function pad(n){return n<10?'0'+n:''+n}
 function setCd(ms){var s=Math.max(0,Math.floor(ms/1000)),d=Math.floor(s/86400),h=Math.floor(s%86400/3600),m=Math.floor(s%3600/60),c=s%60;
  cds.forEach(function(el){var q=function(k){return el.querySelector('[data-'+k+']')};if(q('d')){q('d').textContent=pad(d);q('h').textContent=pad(h);q('m').textContent=pad(m);q('s').textContent=pad(c)}})}
 function openPop(){if(!pop||expired)return;lastF=document.activeElement;pop.hidden=false;document.body.classList.add('pop-open');var c=pop.querySelector('.pop-card');if(c)c.focus();try{sessionStorage.setItem('bwPop','1')}catch(e){}}
 function closePop(){if(!pop||pop.hidden)return;pop.hidden=true;document.body.classList.remove('pop-open');if(lastF&&lastF.focus)try{lastF.focus()}catch(e){}}
 function expire(){if(expired)return;expired=true;
  document.querySelectorAll('[data-after]').forEach(function(e){e.innerHTML=e.getAttribute('data-after')});
  document.querySelectorAll('[data-offer-bar],[data-offer-only]').forEach(function(e){e.hidden=true});closePop()}
 if(pop){pop.querySelectorAll('[data-close]').forEach(function(b){b.addEventListener('click',closePop)});
  pop.querySelectorAll('a.btn,a.pop-link').forEach(function(a){a.addEventListener('click',closePop)});
  document.addEventListener('keydown',function(e){if(pop.hidden)return;if(e.key==='Escape'){closePop();return}
   if(e.key==='Tab'){var f=pop.querySelectorAll('a[href],button:not([disabled])');if(!f.length)return;var a=f[0],z=f[f.length-1];
    if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}});
  var seen=false;try{seen=sessionStorage.getItem('bwPop')==='1'}catch(e){}
  if(!seen)setTimeout(openPop,2200)}
 if(Date.now()>END){expire()}else{setCd(END-Date.now());setInterval(function(){var ms=END-Date.now();if(ms<=0){expire();return}setCd(ms)},1000)}
 document.querySelectorAll('[data-year]').forEach(function(e){e.textContent=new Date().getFullYear()});
 var b=document.getElementById('burger'),p=document.getElementById('mpanel');
 if(b&&p){b.addEventListener('click',function(){var o=p.classList.toggle('open');b.setAttribute('aria-expanded',o?'true':'false')});
  p.querySelectorAll('a').forEach(function(a){a.addEventListener('click',function(){p.classList.remove('open');b.setAttribute('aria-expanded','false')})});}
 var root=document.getElementById('heroCarousel');
 if(root){var s=root.querySelectorAll('.ann-slide'),d=root.querySelectorAll('.ann-dots button'),i=0,t;
  var reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function show(n){s[i].classList.remove('active');d[i].setAttribute('aria-selected','false');i=(n+s.length)%s.length;s[i].classList.add('active');d[i].setAttribute('aria-selected','true')}
  function go(){clearInterval(t);if(!reduce)t=setInterval(function(){show(i+1)},6000)}
  root.querySelector('.next').addEventListener('click',function(){show(i+1);go()});
  root.querySelector('.prev').addEventListener('click',function(){show(i-1);go()});
  d.forEach(function(x,k){x.addEventListener('click',function(){show(k);go()})});go();}
 var f=document.getElementById('quoteForm');
 if(f){var msg=function(){var t='Hi Bunkworks, quote request:\n';new FormData(f).forEach(function(v,k){if(v)t+=k+': '+v+'\n'});return t};
  f.addEventListener('submit',function(e){e.preventDefault();if(!f.reportValidity())return;window.open('https://wa.me/919072431550?text='+encodeURIComponent(msg()),'_blank','noopener')});
  var eb=document.getElementById('emailBtn');if(eb)eb.addEventListener('click',function(){if(!f.reportValidity())return;location.href='mailto:bunkworksindia@gmail.com?subject='+encodeURIComponent('Quote request')+'&body='+encodeURIComponent(msg())});}
 var chips=document.querySelectorAll('.chips button');
 chips.forEach(function(c){c.addEventListener('click',function(){var l=c.dataset.lang;
  chips.forEach(function(o){o.setAttribute('aria-pressed',o===c?'true':'false')});
  document.querySelectorAll('.post-list .post-card').forEach(function(card){card.hidden=!(l==='all'||card.dataset.lang===l)})})});
})();
