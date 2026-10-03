# -*- coding: utf-8 -*-
# Executed inside build_site.py's namespace (see the exec() call at the end of build_site.py).
import datetime, textwrap
from site_copy import *          # copy blocks + prices (T, PCT, NMIN, END, PHONE_TXT, UPDATED ...)

TODAY = datetime.date.today().isoformat()
END_ISO = f"{OFFER['end']}T23:59:59+05:30"
P_BUNK, P_SINGLE, P_BULK = '/bunker-cot-double-decker-bed/', '/steel-single-cot/', '/bulk-quote/'
TAGOFF = f'<span class="tag" data-offer-only>{OFFER["off_pct"]}% OFF · Anniversary offer</span>' if ACTIVE else ''
OFFER_LABEL = 'Offer' if ACTIVE else 'Prices'
def slug_id(t): return re.sub(r'[^a-z0-9]+', '-', re.sub(r'<[^>]+>', '', t).lower()).strip('-')

# ------------------------------------------------------------------ CSS additions
EXTRA_CSS = r'''
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* countdown */
.ob-cd{display:inline-flex;align-items:center;gap:4px;font-variant-numeric:tabular-nums}
.ob-cd b{background:rgba(0,0,0,.28);border-radius:4px;padding:1px 5px}
.cd{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:14px 0}
.cd>div{background:rgba(0,0,0,.35);border:1px solid rgba(240,182,64,.5);border-radius:10px;padding:8px 4px;text-align:center}
.cd b{display:block;font:800 clamp(1.4rem,6vw,1.9rem)/1 'Montserrat','Inter',sans-serif;color:#FFE29A;font-variant-numeric:tabular-nums}
.cd span{display:block;margin-top:3px;font:600 .62rem/1 'Inter',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#F1DFC4}
.cd-mini{display:flex;align-items:center;flex-wrap:wrap;gap:6px 8px;font-size:.84rem;font-weight:600;color:var(--gold-deep)}
.cd-mini .ob-cd b{background:#3A0C07;color:#FFE29A}
/* offer pop-up */
body.pop-open{overflow:hidden}
.pop{position:fixed;inset:0;z-index:200;display:flex;align-items:flex-end;justify-content:center}
.pop[hidden]{display:none}
.pop-backdrop{position:absolute;inset:0;background:rgba(20,6,3,.68);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
.pop-card{position:relative;width:100%;max-height:92vh;max-height:92dvh;overflow:auto;background:linear-gradient(160deg,#4A0F09,#2B0A05);color:#FFF3DC;border-radius:20px 20px 0 0;border:1px solid rgba(240,182,64,.45);box-shadow:0 -20px 60px rgba(0,0,0,.5);animation:popIn .5s cubic-bezier(.2,.8,.2,1);outline:none}
@keyframes popIn{from{transform:translateY(46px);opacity:0}}
.pop-x{position:absolute;right:10px;top:10px;z-index:3;width:42px;height:42px;border-radius:50%;border:0;background:rgba(43,10,5,.8);color:#FFE29A;font-size:1.6rem;line-height:1;cursor:pointer}
.pop-media{aspect-ratio:16/8;overflow:hidden;background:#2B0A05}
.pop-media img{width:100%;height:100%;object-fit:cover}
.pop-body{padding:16px 18px 22px}
.pop-tag{display:inline-block;background:#FFE066;color:#3A0C07;font:800 .7rem/1 'Inter',sans-serif;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:5px 12px}
.pop-h{margin:10px 0 4px;font:900 clamp(1.7rem,7vw,2.5rem)/1.05 'Playfair Display',Georgia,serif;color:#FFF3DC}
.pop-h em{font-style:normal;color:#F0B640}
.pop-sub{font-size:.9rem;color:#F1DFC4}
.pop-prices{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:12px 0 0}
.pop-price{background:linear-gradient(160deg,#FFF8E6,#F7E2B0);color:#3A0C07;border-radius:12px;padding:9px 12px}
.pop-price small{display:block;font:700 .66rem/1.2 'Inter',sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#7A2A12}
.pop-price b{display:inline-block;margin-top:2px;font:800 1.45rem/1.1 'Montserrat','Inter',sans-serif;color:#8E1616}
.pop-price s{font-size:.8rem;color:#6E5C49;margin-left:5px}
.pop-limited{display:flex;align-items:center;gap:8px;margin:12px 0 0;font-weight:700;font-size:.86rem;color:#FFE29A}
.pop-limited .pulse{flex:none;width:9px;height:9px;border-radius:50%;background:#FFE066;animation:annPulse 1.6s infinite}
.pop-lbl{margin:10px 0 0;font:700 .7rem/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#F6D9A8}
.pop-cta{display:flex;flex-direction:column;gap:8px}
.pop-cta .btn{width:100%;justify-content:center}
.pop-link{display:block;text-align:center;color:#FFE29A;font-weight:600;font-size:.86rem;margin-top:2px}
.pop-no{display:block;margin:6px auto 0;background:none;border:0;color:#D8C3A0;font:500 .8rem 'Inter',sans-serif;cursor:pointer;text-decoration:underline;padding:8px}
@media(min-width:720px){.pop{align-items:center;padding:24px}.pop-card{max-width:860px;border-radius:20px;display:grid;grid-template-columns:.85fr 1.15fr;max-height:90vh}.pop-media{aspect-ratio:auto;height:100%}.pop-body{padding:26px 26px 22px}.pop-cta{flex-direction:row}.pop-cta .btn{width:auto;flex:1}}
@media(prefers-reduced-motion:reduce){.pop-card{animation:none}.pop-limited .pulse{animation:none}}
/* product page layout */
.pgrid{display:grid;grid-template-columns:minmax(0,1fr);gap:30px;padding:10px 0 20px}.pgrid>*{min-width:0}
@media(min-width:1040px){.pgrid{grid-template-columns:minmax(0,1fr) 330px;gap:52px}}
.pmain.prose{max-width:none;padding-top:14px}
.pmain h2{scroll-margin-top:100px}
.pmain .psec+.psec{margin-top:6px}
.pside{align-self:start}
@media(min-width:1040px){.pside{position:sticky;top:96px}}
.pcard{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:18px;margin-bottom:16px}
.pcard .pc-ctas{margin-top:12px}
.pcard .pc-ctas .btn{width:100%;justify-content:center}
.toc{list-style:none;margin:8px 0 0;padding:0;display:grid;gap:2px;font-size:.86rem}
.toc a{display:block;padding:6px 0;text-decoration:none;color:var(--muted);border-bottom:1px solid var(--line)}
.toc a:hover{color:var(--ink)}
.trust-list{list-style:none;margin:16px 0 0;padding:0;display:grid;grid-template-columns:1fr 1fr;gap:6px 14px;font-size:.84rem;color:var(--muted)}
.trust-list li::before{content:"✓";color:#3E6B3A;font-weight:800;margin-right:6px}
.psec .quick{margin-top:0}
.ann-eyebrow{margin-bottom:2px}
h1.ann-title .ann-eyebrow{font-size:.7rem}
/* footer + header refinements */
.foot-grid{display:grid;gap:30px;padding-bottom:30px}
@media(min-width:760px){.foot-grid{grid-template-columns:1.5fr 1fr 1fr 1fr 1fr}}
.foot-brand address{font-style:normal;margin-top:14px;font-size:.88rem;line-height:1.75;color:var(--muted)}
.foot-brand address a{color:var(--muted);text-decoration:none}.foot-brand address a:hover{color:var(--ink);text-decoration:underline}
.foot-cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px}
.foot-cta .btn{padding:10px 16px;font-size:.86rem}
.foot-bottom a{color:var(--muted)}
/* documents / sitemap / contact */
.doc .page-head{padding-bottom:0}
.doc .prose{max-width:780px;padding-top:18px}
.doc .prose h2{margin-top:30px}
.doc .prose ul,.doc .prose ol{margin:0 0 16px}
.steps-list{padding-left:1.2em}.steps-list li{margin:8px 0}
.sm-grid{display:grid;gap:30px;padding:10px 0 60px}
@media(min-width:760px){.sm-grid{grid-template-columns:1fr 1fr}}
.sm-grid h2{font-size:1.15rem;margin:0 0 10px;font-family:'Montserrat',sans-serif}
.sm-grid ul{list-style:none;margin:0;padding:0;display:grid;gap:10px}
.sm-grid li a{font-weight:600;color:var(--ink)}
.sm-grid li span{display:block;font-size:.84rem;color:var(--muted)}
.contact-cards{display:grid;gap:14px;padding:14px 0 30px}
@media(min-width:760px){.contact-cards{grid-template-columns:repeat(3,1fr)}}
.contact-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:20px}
.contact-card h2{font-size:1rem;margin-bottom:6px;font-family:'Montserrat',sans-serif}
.contact-card p,.contact-card a{font-size:.94rem}
.contact-card .btn{margin-top:12px}
/* ui-polish v1 */
.nav{box-shadow:0 6px 24px -14px rgba(58,12,7,.45);border-bottom:2px solid transparent;border-image:linear-gradient(90deg,transparent,var(--gold-hi),var(--gold-deep),var(--gold-hi),transparent) 1}
.nav-links a{position:relative;padding:6px 0;font-weight:600;letter-spacing:.01em}
.nav-links a::after{content:"";position:absolute;left:0;right:0;bottom:0;height:2px;border-radius:2px;background:linear-gradient(90deg,var(--gold-hi),var(--gold-deep));transform:scaleX(0);transform-origin:left;transition:transform .25s ease}
.nav-links a:hover::after,.nav-links a[aria-current]::after{transform:scaleX(1)}
.nav .btn-gold{position:relative;overflow:hidden;box-shadow:0 6px 16px -6px rgba(158,94,24,.7)}
.nav .btn-gold::before{content:"";position:absolute;top:0;left:-70%;width:45%;height:100%;background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-20deg);animation:uiSheen 4.5s ease-in-out infinite}
.offer-bar{background-image:linear-gradient(90deg,#3A0C07,#7A1A0E 45%,#3A0C07);background-size:200% 100%;animation:uiBar 9s linear infinite}
.ob-cd [data-s],.cd [data-s]{animation:uiBlink 1s ease-in-out infinite}
.cd{animation:uiGlow 2s ease-in-out infinite}
.pop-price .save{display:inline-block;margin-left:6px;background:#FFE066;color:#3A0C07;font:800 .64rem/1 'Inter',sans-serif;letter-spacing:.06em;text-transform:uppercase;padding:3px 7px;border-radius:999px;vertical-align:middle}
@keyframes uiBlink{0%,100%{opacity:1}50%{opacity:.35}}
@keyframes uiGlow{0%,100%{box-shadow:0 0 0 0 rgba(255,224,102,0)}50%{box-shadow:0 0 18px 2px rgba(255,224,102,.35)}}
@keyframes uiSheen{0%,60%{left:-70%}100%{left:130%}}
@keyframes uiBar{0%{background-position:0 0}100%{background-position:-200% 0}}
@media(prefers-reduced-motion:reduce){.nav .btn-gold::before,.offer-bar,.ob-cd [data-s],.cd [data-s],.cd{animation:none}.nav-links a::after{transition:none}}
/* ui-polish v2 */
.nav{background:#F6F2EA;-webkit-backdrop-filter:none;backdrop-filter:none}
.ship-note{display:block;margin-top:6px;font-size:.78rem;font-weight:600;color:var(--muted)}
.pcard .ship-note{margin:4px 0 0}
.pop-fine{margin:10px 0 0;font:600 .74rem/1.3 'Inter',sans-serif;color:#F1DFC4}
'''

# ------------------------------------------------------------------ JS: countdown + pop-up (replaces the old END block)
COUNTDOWN_JS = r''' var END=new Date('__END_ISO__').getTime(),expired=false,cds=document.querySelectorAll('[data-cd]'),pop=document.getElementById('offerPop'),lastF=null;
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
  if(!seen)setTimeout(openPop,8000)}
 if(Date.now()>END){expire()}else{setCd(END-Date.now());setInterval(function(){var ms=END-Date.now();if(ms<=0){expire();return}setCd(ms)},1000)}
'''
_a = JS.index(" var END="); _b = JS.index(" document.querySelectorAll('[data-year]')")
JS = JS[:_a] + COUNTDOWN_JS.replace('__END_ISO__', END_ISO) + JS[_b:]
CSS = CSS + EXTRA_CSS

# ------------------------------------------------------------------ header / banner / footer / pop-up
NAV_ITEMS = [(P_BUNK, 'Bunker Cots'), (P_SINGLE, 'Single Cots'), ('/#pricing', OFFER_LABEL), (P_BULK, 'Bulk Quote'),
             ('/blog/', 'Guides'), ('/about/', 'About'), ('/contact/', 'Contact')]
CD_INLINE = '<span class="ob-cd" data-cd>Ends in <b data-d>07</b>d <b data-h>00</b>h <b data-m>00</b>m <b data-s>00</b>s</span>'

def banner():
    if not ACTIVE: return ''
    return (f'<a class="offer-bar" data-offer-bar href="/#pricing" aria-label="5th Anniversary Offer, up to {OFFER["off_pct"]}% off. Bunker cot {B} rupees, single cot {S} rupees. Limited pieces left. Order now">'
            f'<span class="ob-tag">5th Anniversary Offer</span>'
            f'<span>Bunker cot <b class="blink">₹{B}</b> <s>₹{BR}</s></span>'
            f'<span>Single cot <b class="blink">₹{S}</b> <s>₹{SR}</s></span>'
            f'{CD_INLINE}</a>')

def _active(h, path): return path == h or (h == '/blog/' and path.startswith('/blog/'))

def nav(active=''):
    li = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if _active(h, active) else ""}>{t}</a></li>' for h, t in NAV_ITEMS)
    return f'''<a class="skip" href="#main">Skip to content</a>
{banner()}
<header class="nav">
 <div class="nav-inner">
  <a href="/" class="brand"><img src="/images/bunkworks-logo.png" alt="Bunkworks logo — steel bunker cots, double decker beds and single cots for hostels, Kerala" width="{LOGO_W}" height="{LOGO_H}"></a>
  <nav aria-label="Main"><ul class="nav-links">{li}</ul></nav>
  <div class="nav-right">
   <a class="nav-wa" href="{wa('Hi Bunkworks, I have a question about your beds.')}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
   <a href="{P_BULK}" class="btn btn-gold">Get a Quote {ARROW}</a>
   <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mpanel"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  </div>
 </div>
 <div class="mobile-panel" id="mpanel"><nav aria-label="Mobile"><ul>{li}<li><a class="btn btn-gold" href="{P_BULK}">Get a Bulk Quote</a></li></ul></nav></div>
</header>'''

def footer():
    guides = ''.join(f'<li><a href="/blog/{p["slug"]}/" lang="{p["lang"]}">{short(p)}</a></li>' for p in POSTS[:6])
    return f'''<footer>
 <div class="wrap">
  <div class="foot-grid">
   <div class="foot-brand"><a href="/"><img src="/images/bunkworks-logo.png" alt="Bunkworks logo — steel bunker cots, double decker beds and single cots for hostels, Kerala" width="{LOGO_W}" height="{LOGO_H}" loading="lazy"></a>
    <address><strong>Bunkworks</strong> — steel hostel furniture manufacturer<br>Kerala, India<br><a href="tel:+919072431550">{PHONE_TXT}</a> (call / WhatsApp)<br><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="{GBP}" target="_blank" rel="noopener">Bunkworks Warehouse on Google</a></address>
    <div class="foot-cta"><a class="btn btn-wa" href="{wa('Hi Bunkworks, I have a question about your beds.')}" target="_blank" rel="noopener">WhatsApp</a><a class="btn btn-gold" href="{P_BULK}">Bulk quote {ARROW}</a></div></div>
   <nav class="foot-col" aria-label="Products"><h2>Products</h2><ul><li><a href="{P_BUNK}">Bunker cot / double decker bed</a></li><li><a href="{P_SINGLE}">Steel single cot</a></li><li><a href="/#mattress">Foam mattress</a></li><li><a href="/#collections">Swadesh &amp; Perunthachan</a></li><li><a href="/#pricing">{'5th Anniversary Offer' if ACTIVE else 'Prices'}</a></li></ul></nav>
   <nav class="foot-col" aria-label="Guides"><h2>Guides</h2><ul>{guides}<li><a href="/blog/">All guides &amp; blog</a></li></ul></nav>
   <nav class="foot-col" aria-label="Company"><h2>Company</h2><ul><li><a href="/about/">About Bunkworks</a></li><li><a href="/contact/">Contact</a></li><li><a href="{P_BULK}">Bulk order quote</a></li><li><a href="/#projects">Hostel projects</a></li><li><a href="/sitemap/">Sitemap</a></li></ul></nav>
   <nav class="foot-col" aria-label="Legal"><h2>Legal</h2><ul><li><a href="/privacy-policy/">Privacy policy</a></li><li><a href="/terms/">Terms of sale &amp; use</a></li><li><a href="/shipping-delivery/">Shipping &amp; delivery</a></li></ul></nav>
  </div>
  <div class="foot-bottom"><span>© <span data-year>2026</span> Bunkworks. {TAGLINE}. Made in Kerala, India.</span><span><a href="/sitemap/">Sitemap</a> · <a href="/sitemap.xml">sitemap.xml</a> · <a href="/llms.txt">llms.txt</a></span></div>
 </div>
</footer>'''

def popup():
    if not ACTIVE: return ''
    wg = wa("Hi Bunkworks, I want to book from the 5th Anniversary Offer (limited pieces). Product: , Quantity: , Delivery city: ")
    return f'''<div class="pop" id="offerPop" role="dialog" aria-modal="true" aria-labelledby="pop-h" hidden data-offer-only>
 <div class="pop-backdrop" data-close></div>
 <div class="pop-card" tabindex="-1">
  <button class="pop-x" data-close aria-label="Close offer">×</button>
  <div class="pop-media">{img('anniversary-bunk-bed-terracotta-room', 'Bunkworks steel bunker cot (double decker bed) in a hostel room — 5th anniversary offer', '(min-width:720px) 380px, 100vw')}</div>
  <div class="pop-body">
   <span class="pop-tag">5th Anniversary Offer</span>
   <h2 class="pop-h" id="pop-h">Up to <em>{OFFER["off_pct"]}% OFF</em> steel bunker cots &amp; single cots</h2>
   <p class="pop-sub">Factory-direct hostel furniture from Kerala.</p>
   <div class="pop-prices"><div class="pop-price"><small>Bunker cot</small><b class="blink">₹{B}</b><s>₹{BR}</s><em class="save">Save ₹{OFFER["bunk_reg"]-OFFER["bunk"]}</em></div><div class="pop-price"><small>Single cot</small><b class="blink">₹{S}</b><s>₹{SR}</s><em class="save">Save ₹{OFFER["single_reg"]-OFFER["single"]}</em></div></div>
   <p class="pop-limited"><span class="pulse" aria-hidden="true"></span>Limited pieces left — order before the timer ends</p>
   <p class="pop-lbl">Offer ends in</p>
   <div class="cd" data-cd role="timer" aria-label="Time left in the offer"><div><b data-d>07</b><span>Days</span></div><div><b data-h>00</b><span>Hours</span></div><div><b data-m>00</b><span>Minutes</span></div><div><b data-s>00</b><span>Seconds</span></div></div>
   <div class="pop-cta"><a class="btn btn-foil" href="{wg}" target="_blank" rel="noopener">Order now on WhatsApp {ARROW}</a><a class="btn btn-ghost" href="{P_BULK}">Bulk quote (50+)</a></div>
   <button class="pop-no" data-close>No thanks, I'll browse</button>
  </div>
 </div>
</div>'''

def page(path, title, desc, body, lang='en', og_image='/og-image.jpg', og_type='website', ld=(), extra_head='', keywords='', robots='index, follow', popup_on=True):
    ldj = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    kw = f'<meta name="keywords" content="{H.escape(keywords)}">' if keywords else ''
    fonts = FONTS + ('' if 'Great+Vibes' in extra_head else HERO_FONTS)
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
{kw}
<meta name="author" content="Bunkworks">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE}{path}">
{extra_head}
<meta name="theme-color" content="#F6F2EA">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Bunkworks">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:image:alt" content="{H.escape(title)}">
<meta property="og:locale" content="{ {'en':'en_IN','ml':'ml_IN','hi':'hi_IN'}[lang] }">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{H.escape(title)}">
<meta name="twitter:description" content="{H.escape(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="sitemap" type="application/xml" href="/sitemap.xml">
{fonts}
<link rel="stylesheet" href="/assets/site.css">
{ldj}
</head>
<body>
{nav(path)}
<main id="main">
{body}
</main>
{footer()}
{popup() if popup_on else ''}
<script src="/assets/site.js" defer></script>
</body>
</html>'''

ORG.update({"areaServed": "IN", "contactPoint": [{"@type": "ContactPoint", "telephone": "+91-9072431550", "email": EMAIL, "contactType": "sales",
            "areaServed": "IN", "availableLanguage": ["English", "Malayalam", "Hindi"]}],
            "knowsAbout": ["bunker cots", "double decker beds", "bunk beds", "single cots", "hostel furniture", "galvanised steel furniture"]})

# ------------------------------------------------------------------ shared blocks
def quote_form(default_product='Bunker cots / double decker beds', heading_units='Number of pieces'):
    opts = ['Bunker cots / double decker beds', 'Steel single cots', 'Bunker cots and single cots', '3 inch foam mattress', 'Swadesh series', 'Perunthachan series']
    o = ''.join(f'<option{" selected" if x == default_product else ""}>{H.escape(x)}</option>' for x in opts)
    return f'''<form class="form" id="quoteForm" action="mailto:{EMAIL}" method="post" enctype="text/plain">
   <div><label for="q-name">Name</label><input id="q-name" name="Name" autocomplete="name" required></div>
   <div><label for="q-org">Hostel / organisation</label><input id="q-org" name="Organisation" autocomplete="organization" required></div>
   <div><label for="q-city">Delivery city</label><input id="q-city" name="City" autocomplete="address-level2" required></div>
   <div><label for="q-units">{heading_units}</label><input id="q-units" name="Units" inputmode="numeric" required></div>
   <div class="full"><label for="q-type">Product</label><select id="q-type" name="Product">{o}</select></div>
   <div class="full"><label for="q-contact">Phone or email</label><input id="q-contact" name="Contact" autocomplete="tel" required></div>
   <div class="full"><label for="q-msg">Anything else</label><textarea id="q-msg" name="Message" placeholder="Custom sizes, opening date, stairs or lift, mattresses needed"></textarea></div>
   <div class="full pc-ctas"><button type="submit" class="btn btn-gold">Send on WhatsApp {ARROW}</button><button type="button" id="emailBtn" class="btn btn-line-light">Send by email</button></div>
  </form>'''

def bulk_band(product_label, default_product, heading_id='bulk-h'):
    return f'''<section class="section enquiry" id="bulk-quote" aria-labelledby="{heading_id}">
 <div class="wrap enq-grid">
  <div><span class="eyebrow">Bulk quote — {NMIN}+ pieces</span><h2 id="{heading_id}">Get a bulk quote for {H.escape(product_label)}</h2>
   <p>Factory-direct pricing, custom sizes and delivery planned for your opening date. Tell us the quantity and your city — we reply with a written quote.</p>
   <p><a class="btn btn-foil" href="{WA_BULK}" target="_blank" rel="noopener">Bulk quote on WhatsApp {ARROW}</a></p>
   <p>Or call <a href="tel:+919072431550" style="color:#fff">{PHONE_TXT}</a> · email <a href="{MAIL_BULK}" style="color:#fff">{EMAIL}</a></p></div>
  {quote_form(default_product)}
 </div>
</section>'''

def crumbs_html(items):
    lis = ''.join((f'<li><a href="{u}">{H.escape(n)}</a></li>' if i < len(items) - 1 else f'<li aria-current="page">{H.escape(n)}</li>') for i, (n, u) in enumerate(items))
    return f'<nav class="crumbs" aria-label="Breadcrumb"><ol>{lis}</ol></nav>'

def bc_ld(items):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u} for i, (n, u) in enumerate(items)]}

def webpage_ld(path, name, desc, kind='WebPage', about=None):
    d = {"@context": "https://schema.org", "@type": kind, "@id": SITE + path + "#webpage", "url": SITE + path, "name": name, "description": desc,
         "inLanguage": "en-IN", "isPartOf": {"@id": SITE + "/#website"}, "publisher": {"@id": SITE + "/#org"}, "dateModified": TODAY}
    if about: d["about"] = about
    return d

# ------------------------------------------------------------------ product pages
def _kp(name, value, unit=None):
    d = {"@type": "PropertyValue", "name": name, "value": value}
    if unit: d["unitText"] = unit
    return d

PRODUCTS = {
 P_BUNK.strip('/'): dict(
   name='Bunkworks Steel Bunker Cot (Double Decker Bed)', short='Bunker cot / double decker bed', sku='BW-BUNK',
   h1='Steel Bunker Cot / Double Decker Bed for Hostels, PGs & Institutions',
   title=lambda: (f'Bunker Cot / Double Decker Bed Price ₹{B} | Bunkworks' if ACTIVE else f'Bunker Cot / Double Decker Bed Price ₹{PB} | Bunkworks'),
   desc=lambda: (f'Steel bunker cot (double decker bed) for hostels & PGs: galvanised, 1.40 m, 100 kg per deck, 12mm plywood decks. ₹{B} offer (MRP ₹{BR}). Bulk quote {NMIN}+.' if ACTIVE else
                 f'Steel bunker cot (double decker bed) for hostels & PGs: galvanised, 1.40 m high, 100 kg per deck, 12mm plywood decks. ₹{PB} per piece. Bulk quote {NMIN}+ pieces.'),
   intro='A galvanised steel bunker cot (double decker bed) with two 12mm plywood decks, guard rail and ladder handle. Epoxy coated, 1.40 m high, 200 kg total weight bearing (100 kg per deck) — made in Kerala for hostels, PGs and dormitories.',
   quick=lambda: (f'<strong>A bunker cot — also called a double decker bed or bunk bed — is a two-deck bed on one frame.</strong> The Bunkworks steel bunker cot is made in Kerala from galvanised steel with an epoxy coating. It is 1.40 m (140 cm) high, has two 183 × 76 cm (6 × 2.5 ft) decks on 12mm plywood bases and a 200 kg total weight-bearing capacity (100 kg per deck). '
                  + swap(f'Price: ₹{B} per piece in the 5th Anniversary Offer (MRP ₹{BR}, {PCT}% off) until {END} or while stock lasts', f'Price: ₹{PB} per piece') + f', without mattress. Orders above {NMIN} pieces get a bulk quote.'),
   imgs=[('anniversary-bunk-bed-terracotta-room', 'Bunkworks galvanised steel bunker cot with 12mm plywood decks, guard rail and ladder handle in a hostel room'),
         ('bunk-bed-studio-cutout', 'Steel bunker cot studio view — hostel double decker bed with plywood decks, bolted joints and protected feet'),
         ('anniversary-bunk-bed-warm-lit-room', 'Heavy-duty steel double decker bed for hostels and PGs — 1.40 m high, 200 kg total (100 kg per deck), epoxy coated'),
         ('bolted-steel-corner-joint-plywood', 'Bolted galvanised steel corner joint of the bunker cot frame under the 12mm plywood deck — rust-resistant hostel furniture')],
   facts=[('Also called', 'Double decker bed, double decker cot, bunk bed'), ('Height', '1.40 m (140 cm)'), ('Deck size', '183 × 76 cm (6 × 2.5 ft) × 2'), ('Deck base', '12mm plywood'),
          ('Frame', 'Galvanised anti-rust steel'), ('Coating', 'Epoxy (not powder coating)'), ('Weight bearing', '200 kg total (100 kg per deck)'), ('Assembly', 'Bolt-together, flat-packed'),
          ('Mattress', 'Not included'), ('Made in', 'Kerala, India')],
   sections=BUNK_SECTIONS, price_block=bunk_price_fn, faqs=bunk_faqs, price=OFFER['bunk'], reg=OFFER['bunk_reg'], after=OFFER['bunk_after'], P=B, PR=BR, PA=PB,
   guides=['cheapest-bunk-bed-price-india', 'bunk-bed-bunker-cot-price-guide', 'galvanised-steel-vs-painted-steel-beds', 'bunk-bed-size-guide', 'bunk-beds-for-adults', 'hostel-setup-cost-india'],
   kw='bunker cot, double decker bed, double decker cot, bunk bed for hostel, bunker cot price, double decker bed price in kerala, steel bunk bed',
   props=[_kp('Height', '1.40', 'm'), _kp('Total weight bearing capacity', '200', 'kg'), _kp('Weight bearing capacity per deck', '100', 'kg'), _kp('Deck size', '183 x 76', 'cm'), _kp('Deck base thickness', '12', 'mm'),
          _kp('Frame material', 'Galvanised steel'), _kp('Coating', 'Epoxy (not powder coated)'), _kp('Number of decks', '2')],
   other=(P_SINGLE, 'Steel single cot'), order_label='steel bunker cots'),
 P_SINGLE.strip('/'): dict(
   name='Bunkworks Steel Single Cot (Hostel Single Bed)', short='Steel single cot', sku='BW-SINGLE',
   h1='Steel Single Cot for Hostels, PGs & Institutions — Galvanised, 12mm Plywood Base',
   title=lambda: (f'Steel Single Cot Price ₹{S} | Hostel Bed | Bunkworks' if ACTIVE else f'Steel Single Cot Price ₹{PS} | Hostel Bed | Bunkworks'),
   desc=lambda: (f'Steel single cot for hostels & PGs: 6×2.5 ft, 40 cm high, galvanised, 12mm plywood base, 100 kg. ₹{S} offer (MRP ₹{SR}). Bulk quote {NMIN}+.' if ACTIVE else
                 f'Steel single cot for hostels & PGs: 6×2.5 ft, 40 cm high, galvanised, 12mm plywood base, 100 kg. ₹{PS} per piece. Bulk quote {NMIN}+ pieces.'),
   intro='A 6 × 2.5 ft galvanised steel single cot, 40 cm high, with a solid 12mm plywood base and an epoxy coating, rated for up to 100 kg. Bolt-together and made in Kerala for hostels, PGs, dormitories and institutions.',
   quick=lambda: (f'<strong>A single cot — also called a single bed, iron cot or steel cot — is a one-person bed on a metal frame.</strong> The Bunkworks steel single cot is galvanised steel with an epoxy coating, 6 × 2.5 ft (183 × 76 cm), 40 cm high, with a 12mm plywood base and up to 100 kg load capacity. '
                  + swap(f'Price: ₹{S} per piece in the 5th Anniversary Offer (MRP ₹{SR}, {PCT}% off) until {END} or while stock lasts', f'Price: ₹{PS} per piece') + f', without mattress. Orders above {NMIN} pieces get a bulk quote.'),
   imgs=[('single-cot-terracotta-dressed-bed', 'Bunkworks steel single cot with mattress, pillows and bedding — grey epoxy-coated frame with arched head rail'),
         ('anniversary-single-cot-wood-top', 'Steel single cot for hostels with wooden plywood top, grey galvanised steel frame, head rail and anti-skid feet'),
         ('bolted-steel-corner-joint-plywood', 'Bolted galvanised steel corner joint under the 12mm plywood base of the steel single cot — 100 kg rated hostel single bed'),
         ('steel-bed-frames-factory-kerala', 'Stack of galvanised steel single cot and bunker cot frames with plywood bases at the Bunkworks factory, Kerala')],
   facts=[('Also called', 'Single bed, iron cot, steel cot'), ('Size (L × W)', '6 × 2.5 ft (183 × 76 cm)'), ('Height', '40 cm'), ('Base', '12mm plywood'),
          ('Frame', 'Galvanised anti-rust steel'), ('Coating', 'Epoxy (not powder coating)'), ('Load', 'Up to 100 kg'), ('Feet', 'Anti-skid leg bushes'),
          ('Mattress', 'Not included'), ('Made in', 'Kerala, India')],
   sections=SINGLE_SECTIONS, price_block=single_price_fn, faqs=single_faqs, price=OFFER['single'], reg=OFFER['single_reg'], after=OFFER['single_after'], P=S, PR=SR, PA=PS,
   guides=['iron-cot-vs-steel-cot-price', 'steel-single-cot-for-hostel', 'galvanised-steel-vs-painted-steel-beds', 'hostel-beds-wholesale-factory-price', 'bunk-bed-size-guide', 'hostel-setup-cost-india'],
   kw='single cot, steel single cot, single cot price, iron cot price, steel cot price, single bed for hostel, hostel single bed wholesale',
   props=[_kp('Length', '183', 'cm'), _kp('Width', '76', 'cm'), _kp('Height', '40', 'cm'), _kp('Load capacity', '100', 'kg'), _kp('Base thickness', '12', 'mm'),
          _kp('Frame material', 'Galvanised steel'), _kp('Coating', 'Epoxy (not powder coated)')],
   other=(P_BUNK, 'Steel bunker cot (double decker bed)'), order_label='steel single cots'),
}

def product_page(slug):
    d = PRODUCTS[slug]; path = f'/{slug}/'
    by = {p['slug']: p for p in POSTS}
    main = img(d['imgs'][0][0], d['imgs'][0][1], '(min-width:900px) 55vw, 100vw', eager=True)
    thumbs = ''.join(f'<figure>{img(k, a, "(min-width:900px) 18vw, 33vw")}</figure>' for k, a in d['imgs'][1:])
    facts = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in d['facts'])
    price = swap(f'<span class="blink">₹{d["P"]}</span><s>₹{d["PR"]}</s>', f'₹{d["PA"]}')
    per = f'per piece, without mattress' + swap(' — 5th Anniversary Offer, limited pieces', '')
    order = wa(f"Hi Bunkworks, I want to order {d['order_label']} at ₹{d['P'] if ACTIVE else d['PA']}. Quantity: , Delivery city: ")
    secs, toc = '', ''
    for h2, html_ in d['sections']:
        if html_ is None: html_ = d['price_block']()
        sid = slug_id(h2)
        secs += f'<section class="psec" id="{sid}"><h2>{H.escape(h2)}</h2>{html_}</section>\n'
        toc += f'<li><a href="#{sid}">{H.escape(h2)}</a></li>'
    faqs = d['faqs']()
    tag = f'<span class="tag" data-offer-only>5th Anniversary Offer · {PCT}% OFF</span>' if ACTIVE else ''
    body = f'''
<div class="wrap">
 {crumbs_html([('Home', '/'), ('Products', '/#products'), (d['short'], path)])}
 <div class="prod-grid">
  <div class="gallery"><div class="main">{main}</div><div class="thumbs">{thumbs}</div></div>
  <div class="prod-info">
   {tag}
   <h1 style="margin-top:12px">{H.escape(d['h1'])}</h1>
   <p style="margin-top:12px;color:var(--muted)">{d['intro']}</p>
   <p class="big-price">{price}</p><p class="per">{per}</p>
   {('<div class="cd-mini" data-offer-only>Offer ends in ' + CD_INLINE.replace('Ends in ', '') + '</div>') if ACTIVE else ''}
   <dl class="keyfacts">{facts}</dl>
   <div class="pc-ctas"><a class="btn btn-gold" href="{order}" target="_blank" rel="noopener">Order on WhatsApp {ARROW}</a><a class="btn btn-line" href="#bulk-quote">Bulk quote ({NMIN}+ pcs)</a></div>
   <ul class="trust-list"><li>Made in Kerala</li><li>Galvanised + epoxy coated</li><li>Bolt-together, flat-packed</li><li>Bulk quote for {NMIN}+ pieces</li></ul>
  </div>
 </div>
 <div class="pgrid">
  <article class="pmain prose">
   <div class="psec"><div class="quick"><p class="quick-label">Quick answer</p><p>{d['quick']()}</p></div></div>
   {secs}
  </article>
  <aside class="pside" aria-label="Order and page contents">
   <div class="pcard"><p class="big-price" style="margin-top:0">{price}</p><p class="per">{per}</p>
    {('<div class="cd-mini" data-offer-only>Ends in ' + CD_INLINE.replace('Ends in ', '') + '</div>') if ACTIVE else ''}
    <div class="pc-ctas"><a class="btn btn-gold" href="{order}" target="_blank" rel="noopener">Order on WhatsApp</a><a class="btn btn-line" href="#bulk-quote">Get bulk quote</a></div></div>
   <div class="pcard"><strong>On this page</strong><ul class="toc">{toc}<li><a href="#bulk-quote">Bulk quote</a></li><li><a href="#pfaq">FAQ</a></li></ul></div>
  </aside>
 </div>
</div>
{bulk_band(d['order_label'], 'Bunker cots / double decker beds' if d['sku'] == 'BW-BUNK' else 'Steel single cots')}
<div class="wrap">
 <section class="article-faq" aria-labelledby="pfaq"><h2 id="pfaq">Frequently asked questions about the {H.escape(d['short'].lower())}</h2><div class="faq">{faq_html(faqs)}</div></section>
 <section class="section" style="padding-top:20px" aria-labelledby="pg"><h2 id="pg" style="font-size:1.4rem;margin-bottom:20px">Buying guides</h2><div class="grid-3">{''.join(post_card(by[g]) for g in d['guides'][:6])}</div></section>
 <p class="fine" style="padding-bottom:50px">Also see: <a href="{d['other'][0]}">{d['other'][1]}</a> · <a href="{P_BULK}">bulk order quote</a> · <a href="/blog/">all guides</a></p>
</div>'''
    offer = {"@type": "Offer", "@id": SITE + path + "#offer", "url": SITE + path, "priceCurrency": "INR", "price": str(d['price'] if ACTIVE else d['after']),
             "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition", "seller": {"@id": SITE + "/#org"}}
    if ACTIVE:
        offer["priceValidUntil"] = OFFER['end']
        offer["priceSpecification"] = [{"@type": "UnitPriceSpecification", "price": str(d['price']), "priceCurrency": "INR"},
                                       {"@type": "UnitPriceSpecification", "priceType": "https://schema.org/StrikethroughPrice", "price": str(d['reg']), "priceCurrency": "INR"}]
    prod = {"@context": "https://schema.org", "@type": "Product", "@id": SITE + path + "#product", "name": d['name'], "sku": d['sku'], "description": d['intro'],
            "image": [f"{SITE}/images/{k}.jpg" for k, _ in d['imgs']], "brand": {"@type": "Brand", "name": "Bunkworks"}, "manufacturer": {"@id": SITE + "/#org"},
            "category": "Hostel furniture", "material": "Galvanised steel, plywood", "additionalProperty": d['props'], "offers": offer, "url": SITE + path}
    crumbs = [('Home', '/'), ('Products', '/#products'), (d['short'], path)]
    ttl = d['title'](); dsc = d['desc']()
    return page(path, ttl, dsc, body, og_image=f"/images/{d['imgs'][0][0]}.jpg", ld=[ORG, webpage_ld(path, ttl, dsc, 'ItemPage', {"@id": SITE + path + "#product"}), prod, bc_ld(crumbs), faq_ld(faqs)], keywords=d['kw'])

# ------------------------------------------------------------------ document / company pages
def doc_page(path, title, desc, h1, inner, crumbs, kind='WebPage', extra_ld=(), popup_on=False, band=None, faqs=None, robots='index, follow'):
    body = f'''<div class="wrap doc">{crumbs_html(crumbs)}<header class="page-head"><h1>{H.escape(h1)}</h1></header><div class="prose">{inner}</div>
{('<section class="article-faq" aria-labelledby="dfaq" style="padding-bottom:40px"><h2 id="dfaq">Frequently asked questions</h2><div class="faq">' + faq_html(faqs) + '</div></section>') if faqs else ''}</div>{band or ''}'''
    ld = [ORG, webpage_ld(path, title, desc, kind), bc_ld(crumbs)] + list(extra_ld) + ([faq_ld(faqs)] if faqs else [])
    return page(path, title, desc, body, ld=ld, popup_on=popup_on, robots=robots)

def bulk_page():
    steps, plan = bulk_body()
    inner = f'''<p class="lede">Furnishing a hostel, PG, dormitory or institution? Bunkworks supplies steel <a href="{P_BUNK}">bunker cots (double decker beds)</a> and <a href="{P_SINGLE}">single cots</a> factory-direct from Kerala. Orders of more than {NMIN} pieces get a separate bulk quote — with pricing, delivery and timing confirmed in writing.</p>
<div class="quick"><p class="quick-label">Quick answer</p><p>To get a bulk quote for hostel beds, send Bunkworks the number of bunker cots and single cots, any custom size, your delivery city and opening date via the form below, WhatsApp ({PHONE_TXT}) or email ({EMAIL}). Orders above {NMIN} pieces receive a written bulk quote.</p></div>
<h2>How a bulk order works</h2>{steps}
<h2>How many beds does your hostel need?</h2><p>One bunker cot sleeps two and takes the floor space of one bed, so the two products cover most layouts:</p>{plan}
<h2>What to include in your request</h2><ul><li>Number of bunker cots and single cots (or the number of residents)</li><li>Any custom size</li><li>Delivery city and whether the site has stairs or a lift</li><li>Your opening date</li><li>Whether you also need mattresses</li></ul>
<h2>Why buy factory-direct</h2><p>You skip dealer margin, receive identical batches and deal directly with the people who make the bed. Read our guide to <a href="/blog/hostel-beds-wholesale-factory-price/">buying hostel beds wholesale</a>, or see what a <a href="/blog/hostel-setup-cost-india/">20-bed hostel costs to set up</a>.</p>'''
    crumbs = [('Home', '/'), ('Bulk order quote', P_BULK)]
    ttl = f'Bulk Order Quote for Hostel Beds ({NMIN}+ Pieces) | Bunkworks'
    dsc = f'Factory-direct bulk quote for steel bunker cots and single cots for hostels, PGs and institutions — {NMIN}+ pieces, custom sizes, planned delivery.'
    return doc_page(P_BULK, ttl, dsc, f'Bulk Order Quote — Hostel Bunker Cots & Single Cots ({NMIN}+ Pieces)', inner, crumbs, faqs=BULK_FAQS, popup_on=True,
                    band=bulk_band('your hostel or institution', 'Bunker cots and single cots', 'bulk-h'))

def about_page():
    crumbs = [('Home', '/'), ('About', '/about/')]
    ttl = 'About Bunkworks | Steel Hostel Furniture Manufacturer, Kerala'
    dsc = 'Bunkworks builds galvanised steel bunker cots (double decker beds) and single cots for hostels, PGs and institutions in Kerala. Factory-direct, bulk, custom.'
    return doc_page('/about/', ttl, dsc, 'About Bunkworks — Steel Hostel Furniture Made in Kerala', ABOUT_HTML, crumbs, kind='AboutPage', popup_on=True)

def contact_page():
    crumbs = [('Home', '/'), ('Contact', '/contact/')]
    ttl = 'Contact Bunkworks | WhatsApp, Phone & Email for Quotes'
    dsc = f'Contact Bunkworks, Kerala steel hostel furniture maker: WhatsApp or call {PHONE_TXT}, email {EMAIL}, or use the quote form.'
    cards = f'''<div class="contact-cards">
 <div class="contact-card"><h2>WhatsApp &amp; phone</h2><p><a href="tel:+919072431550"><strong>{PHONE_TXT}</strong></a></p><p>Fastest way to get a quote.</p><a class="btn btn-wa" href="{wa('Hi Bunkworks, I have a question about your beds.')}" target="_blank" rel="noopener">Chat on WhatsApp</a></div>
 <div class="contact-card"><h2>Email</h2><p><a href="mailto:{EMAIL}"><strong>{EMAIL}</strong></a></p><p>For quotes, drawings and documents.</p><a class="btn btn-line" href="mailto:{EMAIL}">Send an email</a></div>
 <div class="contact-card"><h2>Find us</h2><p><strong>Bunkworks Warehouse</strong><br>Kerala, India</p><p>Workshop and warehouse.</p><a class="btn btn-line" href="{GBP}" target="_blank" rel="noopener">Open on Google</a></div></div>'''
    inner = f'<p class="lede">Questions about bunker cots, single cots, bulk orders or delivery? Reach Bunkworks by WhatsApp, phone or email, or use the quote form below.</p>{cards}<h2>Useful links</h2><ul><li><a href="{P_BULK}">Bulk order quote ({NMIN}+ pieces)</a></li><li><a href="{P_BUNK}">Steel bunker cot / double decker bed</a></li><li><a href="{P_SINGLE}">Steel single cot</a></li><li><a href="/shipping-delivery/">Shipping &amp; delivery</a></li></ul>'
    cp = {"@context": "https://schema.org", "@type": "ContactPage", "url": SITE + "/contact/", "name": ttl, "mainEntity": {"@id": SITE + "/#org"}}
    return doc_page('/contact/', ttl, dsc, 'Contact Bunkworks — Quotes, Bulk Orders & Delivery', inner, crumbs, kind='ContactPage', extra_ld=[cp], popup_on=True,
                    band=bulk_band('your order', 'Bunker cots and single cots', 'contact-h'))

def sitemap_page():
    crumbs = [('Home', '/'), ('Sitemap', '/sitemap/')]
    ttl = 'Sitemap | Bunkworks — All Pages, Guides & Policies'
    dsc = 'Every page on the Bunkworks website: products, bulk quote, buying guides in English, Malayalam and Hindi, company information and policies.'
    def li(u, t, d=''): return f'<li><a href="{u}">{H.escape(t)}</a>{f"<span>{H.escape(d)}</span>" if d else ""}</li>'
    prods = li('/', 'Home — 5th Anniversary Offer' if ACTIVE else 'Home', 'Steel bunker cots and single cots for hostels, factory direct from Kerala.') + li(P_BUNK, 'Steel bunker cot / double decker bed', 'Galvanised, 1.40 m, 200 kg total (100 kg per deck), 12mm plywood decks.') + li(P_SINGLE, 'Steel single cot', '6 × 2.5 ft, 40 cm high, 12mm plywood base, 100 kg.') + li(P_BULK, 'Bulk order quote', f'{NMIN}+ pieces — WhatsApp, email or form.')
    comp = li('/about/', 'About Bunkworks', 'Who we are and how we build.') + li('/contact/', 'Contact', 'WhatsApp, phone, email and Google listing.') + li('/blog/', 'Guides & blog', 'Costs, prices and buying advice.')
    legal = li('/privacy-policy/', 'Privacy policy') + li('/terms/', 'Terms of sale & use') + li('/shipping-delivery/', 'Shipping & delivery')
    tech = li('/sitemap.xml', 'sitemap.xml', 'For search engines.') + li('/robots.txt', 'robots.txt') + li('/llms.txt', 'llms.txt', 'Summary for AI assistants and LLMs.') + li('/llms-full.txt', 'llms-full.txt', 'Full product, price and FAQ facts for LLMs.')
    def guides(lang): return ''.join(li(f'/blog/{p["slug"]}/', p['title'], p['excerpt']) for p in POSTS if p['lang'] == lang)
    inner = (f'<div class="sm-grid"><div><h2>Products &amp; quotes</h2><ul>{prods}</ul><h2 style="margin-top:26px">Company</h2><ul>{comp}</ul><h2 style="margin-top:26px">Legal</h2><ul>{legal}</ul><h2 style="margin-top:26px">Technical files</h2><ul>{tech}</ul></div>'
             f'<div><h2>Guides in English</h2><ul>{guides("en")}</ul><h2 style="margin-top:26px" lang="ml">മലയാളം ഗൈഡുകൾ</h2><ul>{guides("ml")}</ul><h2 style="margin-top:26px" lang="hi">हिंदी गाइड</h2><ul>{guides("hi")}</ul></div></div>')
    body = f'<div class="wrap doc">{crumbs_html(crumbs)}<header class="page-head"><h1>Sitemap — All Bunkworks Pages</h1><p>Every page on the site, with a one-line brief of each guide.</p></header>{inner}</div>'
    return page('/sitemap/', ttl, dsc, body, ld=[ORG, webpage_ld('/sitemap/', ttl, dsc, 'CollectionPage'), bc_ld(crumbs)], popup_on=False)

def legal_page(path, ttl, dsc, h1, html_, short_name):
    return doc_page(path, ttl, dsc, h1, html_, [('Home', '/'), (short_name, path)], popup_on=False)

# ------------------------------------------------------------------ pages registry
pages = {'/index.html': home(), '/blog/index.html': blog_index(), '/404.html': not_found(),
         f'{P_BUNK}index.html': product_page(P_BUNK.strip('/')), f'{P_SINGLE}index.html': product_page(P_SINGLE.strip('/')),
         f'{P_BULK}index.html': bulk_page(), '/about/index.html': about_page(), '/contact/index.html': contact_page(), '/sitemap/index.html': sitemap_page(),
         '/privacy-policy/index.html': legal_page('/privacy-policy/', 'Privacy Policy | Bunkworks', 'How Bunkworks collects, uses and protects personal information when you visit the website or request a quote.', 'Privacy Policy', privacy_html(), 'Privacy policy'),
         '/terms/index.html': legal_page('/terms/', 'Terms of Sale & Use | Bunkworks', 'Terms for using the Bunkworks website and buying steel bunker cots and single cots: prices, offers, orders, delivery, use and liability.', 'Terms of Sale & Use', terms_html(), 'Terms'),
         '/shipping-delivery/index.html': legal_page('/shipping-delivery/', 'Shipping & Delivery | Bunkworks', 'How Bunkworks delivers steel bunker cots and single cots from Kerala: flat-packed transport, quotes, delivery planning and checking on arrival.', 'Shipping & Delivery', shipping_html(), 'Shipping & delivery')}
for p in POSTS: pages[f"/blog/{p['slug']}/index.html"] = post_page(p)
for k, v in pages.items(): w(k, v)
w('/assets/site.css', CSS); w('/assets/site.js', JS)

# ------------------------------------------------------------------ sitemap.xml
PAGE_IMGS = {}
for path, html_ in pages.items():
    if path == '/404.html': continue
    PAGE_IMGS['/' if path == '/index.html' else path.replace('index.html', '')] = sorted(set(re.findall(r'<img src="(/images/[\w-]+\.(?:jpg|png))"', html_)))
by_url = {f"/blog/{p['slug']}/": p for p in POSTS}
def alts(p):
    if not p or not p['group']: return ''
    return ''.join(f'<xhtml:link rel="alternate" hreflang="{q["lang"]}" href="{SITE}/blog/{q["slug"]}/"/>' for q in POSTS if q['group'] == p['group'])
PRIO = {'/': ('1.0', 'daily'), P_BUNK: ('0.95', 'weekly'), P_SINGLE: ('0.95', 'weekly'), P_BULK: ('0.9', 'monthly'), '/blog/': ('0.8', 'weekly'), '/about/': ('0.5', 'monthly'), '/contact/': ('0.6', 'monthly'),
        '/sitemap/': ('0.3', 'monthly'), '/privacy-policy/': ('0.2', 'yearly'), '/terms/': ('0.2', 'yearly'), '/shipping-delivery/': ('0.3', 'yearly')}
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml" xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n'
for u, ims in PAGE_IMGS.items():
    pr, cf = PRIO.get(u, ('0.7', 'monthly'))
    sm += f'  <url><loc>{SITE}{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority>{alts(by_url.get(u))}' + ''.join(f'<image:image><image:loc>{SITE}{im}</image:loc></image:image>' for im in ims) + '</url>\n'
w('/sitemap.xml', sm + '</urlset>\n')

# ------------------------------------------------------------------ robots.txt
BOTS = ['Googlebot', 'Bingbot', 'OAI-SearchBot', 'ChatGPT-User', 'Claude-SearchBot', 'Claude-User', 'PerplexityBot', 'GPTBot', 'ClaudeBot', 'Google-Extended', 'Applebot', 'Applebot-Extended', 'CCBot']
w('/robots.txt', '# Bunkworks — search engines and AI search / answer engines are welcome.\n# LLM-readable summaries: /llms.txt and /llms-full.txt\n\n' + ''.join(f'User-agent: {b}\nAllow: /\n\n' for b in BOTS) + f'User-agent: *\nAllow: /\nDisallow: /404.html\n\nSitemap: {SITE}/sitemap.xml\n')

# ------------------------------------------------------------------ llms.txt + llms-full.txt
def _now(a, b): return a if ACTIVE else b
offer_line_b = _now(f"₹{B} per piece in the 5th Anniversary Offer (MRP ₹{BR}, {PCT}% off) until {END} or while stock lasts", f"₹{PB} per piece")
offer_line_s = _now(f"₹{S} per piece in the 5th Anniversary Offer (MRP ₹{SR}, {PCT}% off) until {END} or while stock lasts", f"₹{PS} per piece")
def guide_lines(lang): return ''.join(f"- [{p['title']}]({SITE}/blog/{p['slug']}/): {p['excerpt']}\n" for p in POSTS if p['lang'] == lang)
LLMS = f'''# Bunkworks
> Bunkworks is a steel furniture manufacturer in Kerala, India. It makes galvanised steel bunker cots (also called double decker beds or bunk beds) and single cots for hostels, PGs, dormitories and institutions, and sells factory-direct, by the piece or in bulk (more than {NMIN} pieces get a bulk quote).

Key facts (prices per piece, without mattress):
- Steel bunker cot / double decker bed: 1.40 m high, two 183 x 76 cm (6 x 2.5 ft) decks on 12mm plywood, galvanised steel frame with epoxy coating (not powder coating), 200 kg total weight bearing (100 kg per deck), bolt-together. Price: {offer_line_b}.
- Steel single cot: 6 x 2.5 ft (183 x 76 cm), 40 cm high, 12mm plywood base, galvanised steel frame with epoxy coating, up to 100 kg. Price: {offer_line_s}.
- Bulk quote (more than {NMIN} pieces): WhatsApp {PHONE_TXT} or {EMAIL}.

## Products
- [Steel bunker cot / double decker bed]({SITE}{P_BUNK}): specifications, price, FAQ and bulk quote
- [Steel single cot]({SITE}{P_SINGLE}): specifications, price, FAQ and bulk quote
- [Bulk order quote]({SITE}{P_BULK}): how bulk orders work for hostels and institutions

## Guides (English)
{guide_lines('en')}
## Guides (Malayalam)
{guide_lines('ml')}
## Guides (Hindi)
{guide_lines('hi')}
## Company and policies
- [About Bunkworks]({SITE}/about/)
- [Contact]({SITE}/contact/)
- [Shipping and delivery]({SITE}/shipping-delivery/)
- [Privacy policy]({SITE}/privacy-policy/)
- [Terms of sale and use]({SITE}/terms/)
- [HTML sitemap]({SITE}/sitemap/)

## Optional
- [llms-full.txt]({SITE}/llms-full.txt): full specifications, prices and FAQs in one file
- [sitemap.xml]({SITE}/sitemap.xml)
'''
w('/llms.txt', LLMS)

OFFER_TXT = (f'5th Anniversary Offer: up to {PCT}% off — bunker cot ₹{B} (MRP ₹{BR}) and single cot ₹{S} (MRP ₹{SR}), per piece without mattress, limited pieces, valid until {END} (23:59 IST) or while stock lasts. After the offer, prices are ₹{PB} (bunker cot) and ₹{PS} (single cot).' if ACTIVE else f'Bunker cot ₹{PB} and single cot ₹{PS}, per piece without mattress. Bulk quote for more than {NMIN} pieces.')
def faq_md(fq): return ''.join(f'### {q}\n{a}\n\n' for q, a in fq)
LLMS_FULL = f'''# Bunkworks — full reference for AI assistants
Last updated: {TODAY}. Website: {SITE}/ . Contact: WhatsApp / phone {PHONE_TXT}, email {EMAIL}. Location: Kerala, India (workshop and warehouse; "Bunkworks Warehouse" on Google).

## Who Bunkworks is
Bunkworks is a steel furniture manufacturer in Kerala, India. It designs and builds bunker cots (double decker beds) and single cots for hostels, PGs, dormitories and institutions and sells factory-direct. Tagline: "Furniture for spaces that work". Bunkworks is celebrating its 5th anniversary.

## Terminology
"Bunker cot", "double decker bed", "double decker cot" and "bunk bed" mean the same product: two sleeping decks on one frame. "Single cot", "single bed", "iron cot" and "steel cot" mean a one-person bed on a metal frame.

## Product 1 — Steel bunker cot / double decker bed  ({SITE}{P_BUNK})
- Height: 1.40 m (140 cm). Two decks, each 183 x 76 cm (6 x 2.5 ft), on 12mm plywood bases.
- Frame: galvanised anti-rust steel; epoxy coating (not powder coating). Weight bearing: 200 kg total (100 kg per deck).
- Top guard rail and ladder handle; bolt-together; legs and platforms supplied separately (flat-packed). Mattress not included. Made in Kerala.
- Price: {offer_line_b}. Custom sizes on request.
{faq_md(bunk_faqs())}
## Product 2 — Steel single cot  ({SITE}{P_SINGLE})
- Size: 6 x 2.5 ft (183 x 76 cm); height 40 cm; 12mm plywood base; galvanised steel frame with epoxy coating (not powder coating); load up to 100 kg; anti-skid leg bushes; bolt-together, one-person assembly. Mattress not included. Made in Kerala.
- Price: {offer_line_s}. Custom sizes on request.
{faq_md(single_faqs())}
## Why galvanised steel
Paint cannot be applied inside a hollow steel tube, so painted mild-steel frames can rust from the inside. Galvanised steel is zinc-coated inside and out, and the zinc keeps protecting the steel at scratches. Bunkworks frames are galvanised and epoxy coated.

## Bulk orders
Orders of more than {NMIN} pieces get a separate written bulk quote. Send quantities, custom sizes, delivery city and opening date via {SITE}{P_BULK}, WhatsApp {PHONE_TXT} or {EMAIL}. Capacity planning: one bunker cot sleeps two, so a 20-bed hostel needs 10 bunker cots or 20 single cots.
{faq_md(BULK_FAQS)}
## Prices
{OFFER_TXT}

## Guides
### English
{guide_lines('en')}### Malayalam
{guide_lines('ml')}### Hindi
{guide_lines('hi')}
## Policies
Shipping and delivery: {SITE}/shipping-delivery/ . Privacy: {SITE}/privacy-policy/ . Terms: {SITE}/terms/ .
'''
w('/llms-full.txt', LLMS_FULL)

# ------------------------------------------------------------------ manifest, redirects, headers, htaccess
w('/site.webmanifest', json.dumps({"name": "Bunkworks — Furniture for spaces that work", "short_name": "Bunkworks", "start_url": "/", "display": "browser", "background_color": "#F6F2EA", "theme_color": "#15120F",
   "icons": [{"src": "/images/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/images/icon-512.png", "sizes": "512x512", "type": "image/png"}, {"src": "/images/icon-maskable-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, indent=1))
ALIASES = {P_BUNK: ['/bunk-beds/', '/bunk-bed/', '/bunk-beds', '/bunker-cot/', '/bunker-cots/', '/double-decker-bed/', '/double-decker-beds/', '/double-decker-cot/', '/double-decker-cots/', '/double-decker/', '/bunker-cot-price/', '/bunk-bed-price/', '/double-decker-bed-price/'],
           P_SINGLE: ['/single-cots/', '/single-cot/', '/single-bed/', '/single-beds/', '/iron-cot/', '/steel-cot/', '/steel-cots/', '/cot-price/', '/single-cot-price/'],
           P_BULK: ['/bulk/', '/bulk-order/', '/bulk-orders/', '/bulk-order-quote/', '/wholesale/', '/quote/', '/get-a-quote/', '/enquiry/'],
           '/blog/': ['/blogs/', '/articles/', '/guides/', '/news/'], '/about/': ['/about-us/', '/aboutus/', '/company/'], '/contact/': ['/contact-us/', '/contactus/'],
           '/privacy-policy/': ['/privacy/', '/privacy-policy.html'], '/terms/': ['/terms-and-conditions/', '/terms-conditions/', '/terms-of-service/', '/tos/'],
           '/shipping-delivery/': ['/shipping/', '/delivery/', '/shipping-policy/'], '/sitemap/': ['/sitemap.html', '/site-map/'], '/': ['/index.html', '/home/']}
red = ['# Bunkworks redirects (Netlify _redirects). Domain canonical: https://www.bunkworks.com', '',
       '# 1. Force HTTPS and the www host', 'http://bunkworks.com/*      https://www.bunkworks.com/:splat  301!', 'http://www.bunkworks.com/*  https://www.bunkworks.com/:splat  301!', 'https://bunkworks.com/*     https://www.bunkworks.com/:splat  301!', '',
       '# 2. Alternate and old URLs -> canonical pages (301)']
for dest, olds in ALIASES.items():
    for o in olds: red.append(f'{o.ljust(34)} {dest}  301')
red += ['', '# Old blog paths without trailing slash are handled automatically by Netlify "pretty URLs".']
w('/_redirects', '\n'.join(red) + '\n')
w('/_headers', '''/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: SAMEORIGIN
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
/images/*
  Cache-Control: public, max-age=2592000
/assets/*
  Cache-Control: public, max-age=86400
/favicon*
  Cache-Control: public, max-age=604800
/robots.txt
  Cache-Control: public, max-age=3600
/sitemap.xml
  Cache-Control: public, max-age=3600
/llms.txt
  Content-Type: text/plain; charset=utf-8
/llms-full.txt
  Content-Type: text/plain; charset=utf-8
''')
ht = ['# Bunkworks — Apache / cPanel hosting alternative to Netlify _redirects and _headers', 'RewriteEngine On', '',
      '# Force HTTPS + www', 'RewriteCond %{HTTPS} off [OR]', 'RewriteCond %{HTTP_HOST} !^www\\.bunkworks\\.com$ [NC]', 'RewriteRule ^(.*)$ https://www.bunkworks.com/$1 [L,R=301]', '', '# Alternate URLs -> canonical pages']
for dest, olds in ALIASES.items():
    for o in olds:
        if o == '/': ht.append('RewriteRule ^index\\.html$ / [R=301,L]'); continue
        ht.append(f'RewriteRule ^{re.escape(o.strip("/"))}/?$ {dest} [R=301,L]')
ht += ['', 'ErrorDocument 404 /404.html', 'DirectoryIndex index.html', '',
       '<IfModule mod_headers.c>', '  Header set X-Content-Type-Options "nosniff"', '  Header set X-Frame-Options "SAMEORIGIN"', '  Header set Referrer-Policy "strict-origin-when-cross-origin"',
       '  Header set Strict-Transport-Security "max-age=31536000; includeSubDomains"', '</IfModule>',
       '<IfModule mod_expires.c>', '  ExpiresActive On', '  ExpiresByType image/jpeg "access plus 30 days"', '  ExpiresByType image/webp "access plus 30 days"', '  ExpiresByType image/png "access plus 30 days"', '  ExpiresByType text/css "access plus 1 day"', '  ExpiresByType application/javascript "access plus 1 day"', '</IfModule>',
       '<IfModule mod_deflate.c>', '  AddOutputFilterByType DEFLATE text/html text/css application/javascript application/json application/xml text/plain image/svg+xml', '</IfModule>']
w('/.htaccess', '\n'.join(ht) + '\n')

# ------------------------------------------------------------------ alt-text manifest + blog brief
ALT_LOG['bunkworks-logo'] = 'Bunkworks logo — steel bunker cots, double decker beds and single cots for hostels, Kerala'
rows = ['| File | Alt text |', '|---|---|']
for k, a in sorted(ALT_LOG.items()):
    f = f'/images/{k}.png' if k == 'bunkworks-logo' else f'/images/{k}.jpg (+ .webp' + (', -sm' if 'sm' in META.get(k, {}) else '') + ')'
    rows.append(f'| {f} | {a} |')
rows += ['| /images/bunkworks-logo-square.png | Bunkworks logo — Furniture for spaces that work (Google Business Profile, social) |', '| /og-image.jpg | Bunkworks 5th Anniversary Offer — steel bunker cot and single cot prices (social share image) |',
         '| /favicon.ico, /favicon-16.png, /favicon-32.png, /favicon-48.png, /apple-touch-icon.png, /images/icon-*.png | Bunkworks icon (browser tab / home screen) |']
w('/IMAGE-ALT-TEXT.md', '# Image alt text\n\nEvery image on the site and the alt text it uses.\n\n' + '\n'.join(rows) + '\n')
brief = ['# Blog brief', '', 'Every guide: URL, language, target search phrases and a one-line brief.', '', '| Title | URL | Language | Target keywords | Brief |', '|---|---|---|---|---|']
for p in POSTS: brief.append(f"| {p['title']} | {SITE}/blog/{p['slug']}/ | {p['lang']} | {p['keywords']} | {p['excerpt']} |")
w('/BLOG-BRIEF.md', '\n'.join(brief) + '\n')

# ------------------------------------------------------------------ single-file preview (hash-routed)
def main_of(s): return re.search(r'<main id="main">(.*)</main>', s, re.S).group(1)
views = []
for path, s in pages.items():
    if path == '/404.html': continue
    route = 'home' if path == '/index.html' else path.replace('/index.html', '').strip('/')
    lang = re.search(r'<html lang="(\w+)"', s).group(1)
    views.append((route, lang, s))
secs = ''
for route, lang, s in views:
    t = re.search(r'<title>(.*?)</title>', s).group(1)
    secs += f'<div class="view" data-route="{route}" data-title="{t}" lang="{lang}"{" hidden" if route != "home" else ""}>{main_of(s)}</div>\n'
home_html = pages['/index.html']
shell = home_html.replace(main_of(home_html), secs)
shell = shell.replace('<link rel="stylesheet" href="/assets/site.css">', '<style>' + CSS + '\n.view[lang=ml]{font-family:"Noto Sans Malayalam","Inter",sans-serif;line-height:1.8}.view[lang=hi]{font-family:"Noto Sans Devanagari","Inter",sans-serif;line-height:1.75}</style>')
router = r'''
(function(){var vs=document.querySelectorAll('.view');
function route(){var h=location.hash||'#/',r='home',anchor=null;
 if(h.indexOf('#/?')===0){anchor=h.slice(3)}else if(h.indexOf('#/')===0){r=h.slice(2).replace(/\/$/,'')||'home'}else{anchor=h.slice(1)}
 var cur;if(!(anchor&&h.indexOf('#/?')!==0)){vs.forEach(function(v){var on=v.dataset.route===r;v.hidden=!on;if(on)cur=v});if(!cur){vs[0].hidden=false;cur=vs[0]}document.title=cur.dataset.title.replace(/&amp;/g,'&')}
 requestAnimationFrame(function(){if(anchor){var t=document.getElementById(anchor);if(t)t.scrollIntoView()}else window.scrollTo(0,0)})}
window.addEventListener('hashchange',route);route();})();'''
shell = shell.replace('<script src="/assets/site.js" defer></script>', '<script>' + JS + router + '</script>')
def _href(m):
    u = m.group(1)
    if u.startswith('/#'): return f'href="#/?{u[2:]}"'
    if u.startswith('/images/') or u.startswith('//'): return m.group(0)
    if u in ('/sitemap.xml', '/robots.txt', '/llms.txt', '/llms-full.txt', '/favicon.ico'): return 'href="#/sitemap/"'
    return 'href="#' + (u if u == '/' else u) + '"' if u == '/' else 'href="#' + u + '"'
shell = re.sub(r'href="(/[^"#]*|/#[^"]*)"', _href, shell)
shell = re.sub(r'<source [^>]*>', '', shell).replace('<picture>', '').replace('</picture>', '')
shell = re.sub(r' srcset="[^"]*" sizes="[^"]*"', '', shell)
shell = re.sub(r'<link rel="(icon|apple-touch-icon|manifest|sitemap)"[^>]*>', '', shell)
def pick(m):
    k = m.group(1)
    return f'data-k="{k}-sm.jpg"' if k.startswith('blog-') and os.path.exists(f'{OUT}/images/{k}-sm.jpg') else f'data-k="{k}.jpg"'
shell = re.sub(r'src="/images/([\w-]+)\.jpg"', pick, shell)
shell = shell.replace('src="/images/bunkworks-logo.png"', 'data-k="bunkworks-logo.png"')
keys = sorted(set(re.findall(r'data-k="([^"]+)"', shell)))
imgmap = '{' + ','.join(f'"{k}":"' + ('data:image/png;base64,' if k.endswith('.png') else 'data:image/jpeg;base64,') + base64.b64encode(open(f"{OUT}/images/{k}", "rb").read()).decode() + '"' for k in keys) + '}'
loader = '<script>(function(){var M=' + imgmap + ';document.querySelectorAll("img[data-k]").forEach(function(i){i.src=M[i.dataset.k]})})();</script>'
shell = shell.replace('</body>', loader + '</body>')
PREVIEW = os.environ.get('BW_PREVIEW', '/mnt/user-data/outputs/bunkworks-site.html')
os.makedirs(os.path.dirname(PREVIEW), exist_ok=True)
open(PREVIEW, 'w', encoding='utf-8').write(shell)
print('pages:', len(pages), 'preview bytes:', os.path.getsize(PREVIEW))
