# -*- coding: utf-8 -*-
import os, json, re, base64, html as H
from content import UI, DATE, inr
from content2 import POSTS, OFFER, ACTIVE, offer_box, swap, quick, B, BR, S, SR, PB, PS, WA_BULK, MAIL_BULK, EMAIL as _EMAIL
import content2

OUT = os.environ.get('BW_OUT','/home/claude/site')
SITE = 'https://www.bunkworks.com'
META = json.load(open('/home/claude/img_meta.json'))
LOGO_W, LOGO_H = META['logo']
PHONE = '9072431550'
WA = 'https://wa.me/919072431550'
EMAIL = 'bunkworksindia@gmail.com'
GBP = 'https://share.google/lSNdgoG97YMX7hqwc'
from urllib.parse import quote as _q
def wa(msg): return WA + '?text=' + _q(msg)
TAGLINE = 'Furniture for spaces that work'
ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
DIAG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg>'

def img(key, alt, sizes='100vw', cls='', eager=False):
    m = META[key]; w, h = m['lg']
    srcset = f' srcset="/images/{key}-sm.jpg {m["sm"][0]}w, /images/{key}.jpg {w}w" sizes="{sizes}"' if 'sm' in m else ''
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    c = f' class="{cls}"' if cls else ''
    ALT_LOG.setdefault(key, alt)
    wsrc = f'/images/{key}-sm.webp {m["sm"][0]}w, /images/{key}.webp {w}w' if 'sm' in m else f'/images/{key}.webp'
    wsz = f' sizes="{sizes}"' if 'sm' in m else ''
    return f'<picture><source type="image/webp" srcset="{wsrc}"{wsz}><img src="/images/{key}.jpg"{srcset} alt="{H.escape(alt)}" width="{w}" height="{h}"{load} decoding="async"{c}></picture>'
ALT_LOG = {}

CSS = r'''
:root{--ink:#121212;--muted:#58524A;--cream:#F6F2EA;--card:#FCFAF5;--line:#E6DDCB;--gold-hi:#E9A83B;--gold:#C07A22;--gold-deep:#8A5418;--btn-a:#9E5E18;--btn-b:#774511;--dark:#15120F;--dark-2:#221D17;--radius:14px;--maxw:1220px;
box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
*,*::before,*::after{box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(84px + env(safe-area-inset-top,0px));background:var(--cream)}
body{margin:0;background:var(--cream);color:var(--ink);font-family:'Inter','Noto Sans Malayalam','Noto Sans Devanagari',system-ui,-apple-system,'Segoe UI',Roboto,sans-serif;line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}
html[lang=ml] body{font-family:'Noto Sans Malayalam','Inter',system-ui,sans-serif;line-height:1.8}
html[lang=hi] body{font-family:'Noto Sans Devanagari','Inter',system-ui,sans-serif;line-height:1.75}
img{max-width:100%;height:auto;display:block}
picture{display:contents}
.price-card>*,.prod-grid>*,.grid-3>*{min-width:0}
a{color:inherit}
h1,h2,h3,h4{margin:0;font-family:'Montserrat','Noto Sans Malayalam','Noto Sans Devanagari',system-ui,sans-serif;font-weight:800;line-height:1.12;letter-spacing:-.015em}
html[lang=ml] h1,html[lang=ml] h2,html[lang=ml] h3,html[lang=hi] h1,html[lang=hi] h2,html[lang=hi] h3{line-height:1.35;letter-spacing:0}
p{margin:0}
button{font-family:inherit}
:focus-visible{outline:2.5px solid var(--gold);outline-offset:3px;border-radius:4px}
.sr-only{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip{position:absolute;left:-999px;top:8px;background:var(--ink);color:#fff;padding:8px 14px;border-radius:6px;z-index:100}
.skip:focus{left:12px}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 20px}
@media(min-width:900px){.wrap{padding:0 40px}}
.eyebrow{display:block;font-size:.74rem;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);margin-bottom:10px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:12px 22px;border-radius:8px;font-weight:600;font-size:.94rem;text-decoration:none;border:1.5px solid transparent;cursor:pointer;transition:filter .15s,background .15s,color .15s,border-color .15s;white-space:nowrap;min-height:44px}
.btn svg{width:15px;height:15px}
.btn-gold{background:linear-gradient(135deg,var(--btn-a),var(--btn-b));color:#fff}
.btn-gold:hover{filter:brightness(1.12)}
.btn-line{border-color:var(--gold-deep);color:var(--gold-deep);background:transparent}
.btn-line:hover{background:var(--gold-deep);color:#fff}
.btn-line-light{border-color:rgba(255,255,255,.55);color:#fff}
.btn-line-light:hover{background:rgba(255,255,255,.12);border-color:#fff}
.btn-wa{border-color:#2F7D4B;color:#2F7D4B}
.btn-wa:hover{background:#2F7D4B;color:#fff}
.gold-rule{display:block;width:44px;height:3px;border-radius:2px;background:linear-gradient(90deg,var(--gold-hi),var(--gold-deep));margin:14px 0 0}

/* nav */
.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:60;background:rgba(246,242,234,.94);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.nav-inner{max-width:var(--maxw);margin:0 auto;padding:10px 20px;display:flex;align-items:center;justify-content:space-between;gap:14px}
@media(min-width:900px){.nav-inner{padding:12px 40px}}
.brand img{height:40px;width:auto}
@media(min-width:900px){.brand img{height:48px}}
.nav-links{display:none;gap:20px;list-style:none;margin:0;padding:0}
@media(min-width:1140px){.nav-links{display:flex}}
.nav-links a{text-decoration:none;color:var(--muted);font-size:.9rem;font-weight:500;white-space:nowrap}
.nav-links a:hover,.nav-links a[aria-current]{color:var(--ink)}
.nav-right{display:flex;align-items:center;gap:10px}
.nav-wa{display:none;align-items:center;gap:6px;font-size:.9rem;font-weight:500;color:var(--muted);text-decoration:none}
.nav-wa svg{width:18px;height:18px;color:#2F7D4B}
@media(min-width:760px){.nav-wa{display:inline-flex}}
.nav .btn{padding:10px 16px}
@media(max-width:420px){.nav .btn-gold{display:none}}
.burger{display:inline-flex;align-items:center;justify-content:center;width:44px;height:44px;background:none;border:1.5px solid var(--line);border-radius:8px;cursor:pointer;color:var(--ink)}
.burger svg{width:20px;height:20px}
@media(min-width:1140px){.burger{display:none}}
.mobile-panel{display:none;border-top:1px solid var(--line);background:var(--card)}
.mobile-panel.open{display:block}
.mobile-panel ul{list-style:none;margin:0;padding:10px 20px 18px;display:grid}
.mobile-panel a{display:block;padding:11px 0;text-decoration:none;font-weight:600;border-bottom:1px solid var(--line)}
.mobile-panel .btn{margin-top:14px;width:100%}
@media(min-width:1140px){.mobile-panel{display:none!important}}

/* hero */
@media(max-width:600px){.hero-trust{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.trust-item{border:0;margin:0;padding:0;flex-direction:column;align-items:flex-start;gap:6px}}

/* sections */
.section{padding:72px 0}
.section-head{display:flex;flex-wrap:wrap;justify-content:space-between;align-items:flex-end;gap:18px 40px;margin-bottom:36px}
.section-head h2{font-size:clamp(1.55rem,3.4vw,2.35rem);max-width:20ch}
.section-head p{max-width:40ch;color:var(--muted);font-size:.95rem}
.link-arrow{display:inline-flex;align-items:center;gap:6px;margin-top:10px;font-weight:600;font-size:.9rem;color:var(--gold-deep);text-decoration:none}
.link-arrow svg{width:14px;height:14px}
.link-arrow:hover{text-decoration:underline}

.grid-3{display:grid;gap:20px}
@media(min-width:680px){.grid-3{grid-template-columns:repeat(2,1fr)}}
@media(min-width:980px){.grid-3{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:flex;flex-direction:column}
.card .thumb{aspect-ratio:4/3;overflow:hidden;background:#EFE7D8}
.card .thumb img{width:100%;height:100%;object-fit:cover;transition:transform .5s ease}
.card:hover .thumb img{transform:scale(1.03)}
.card-body{padding:18px 20px 22px;display:flex;justify-content:space-between;gap:14px;align-items:flex-start;flex:1}
.card-body h3{font-size:1.1rem}
.card-body p{margin-top:6px;font-size:.88rem;color:var(--muted)}
.circle-link{flex:none;width:40px;height:40px;border-radius:50%;border:1.5px solid var(--line);display:flex;align-items:center;justify-content:center;color:var(--ink);text-decoration:none;transition:.15s}
.circle-link:hover{background:var(--ink);border-color:var(--ink);color:#fff}
.circle-link svg{width:15px;height:15px}
.cot-art{width:100%;height:100%}

/* engineered */
.engineered{background:linear-gradient(180deg,var(--cream),#EFE8DA)}
.eng-grid{display:grid;gap:36px;align-items:center}
@media(min-width:900px){.eng-grid{grid-template-columns:1fr 1fr;gap:56px}}
.eng-grid h2{font-size:clamp(1.55rem,3.4vw,2.35rem)}
.eng-grid .lead{margin-top:14px;color:var(--muted);max-width:44ch}
.features{margin-top:30px;display:grid;grid-template-columns:repeat(2,1fr);gap:0}
@media(min-width:560px){.features{grid-template-columns:repeat(4,1fr)}}
.feature{padding:14px 12px;text-align:center;border-left:1px solid var(--line)}
.feature:first-child,.features .feature:nth-child(3){border-left:0}
@media(min-width:560px){.features .feature:nth-child(3){border-left:1px solid var(--line)}}
.feature svg{width:34px;height:34px;margin:0 auto;color:var(--ink)}
.feature span{display:block;margin-top:10px;font-size:.8rem;font-weight:600;line-height:1.3}
.joint{position:relative;border-radius:var(--radius);overflow:hidden;background:var(--dark);aspect-ratio:308/181}
.joint img{width:100%;height:100%;object-fit:cover}
.joint-note{position:absolute;right:14px;top:14px;background:rgba(252,250,245,.94);border-radius:8px;padding:8px 12px;font-size:.78rem;font-weight:600;line-height:1.4;border-left:3px solid var(--gold)}

/* projects band */
.projects{position:relative;color:#fff;overflow:hidden;background:var(--dark)}
.projects-bg{position:absolute;inset:0}
.projects-bg img{width:100%;height:100%;object-fit:cover;opacity:.55}
.projects-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(95deg,rgba(21,18,15,.97) 0%,rgba(21,18,15,.88) 48%,rgba(21,18,15,.5) 100%)}
.projects-inner{position:relative;padding:72px 0}
.projects .eyebrow{color:var(--gold-hi)}
.projects h2{font-size:clamp(1.55rem,3.4vw,2.35rem);max-width:16ch}
.projects p{margin-top:14px;max-width:44ch;color:#DCD5C8}
.projects .btn{margin-top:24px}
.pf{margin-top:36px;display:flex;flex-wrap:wrap;gap:18px 32px}
.pf div{display:flex;align-items:center;gap:10px;max-width:190px}
.pf svg{flex:none;width:26px;height:26px;color:var(--gold-hi)}
.pf span{font-size:.84rem;font-weight:600;line-height:1.3;color:#EFE9DD}

/* collections */
.coll-grid{display:grid;gap:20px}
@media(min-width:820px){.coll-grid{grid-template-columns:1fr 1fr}}
.coll{border-radius:var(--radius);padding:36px 30px;color:#fff;position:relative;overflow:hidden}
.coll.sw{background:var(--ink)}
.coll.pe{background:linear-gradient(140deg,#8A5418,#5C370E)}
.coll .eyebrow{color:var(--gold-hi)}
.coll.pe .eyebrow{color:#F6D29A}
.coll h3{font-size:1.45rem}
.coll p{margin-top:12px;max-width:40ch;color:#E6DFD2;font-size:.95rem}
.coll .btn{margin-top:22px}
.coll svg.glyph{width:42px;height:42px;margin-bottom:18px;color:var(--gold-hi)}
.coll.pe svg.glyph{color:#F6D29A}

/* blog cards */
.post-card .thumb{aspect-ratio:16/9;position:relative}
.lang-chip{position:absolute;left:12px;top:12px;background:rgba(18,18,18,.82);color:#fff;font-size:.72rem;font-weight:600;padding:4px 10px;border-radius:999px}
.post-card .card-body{flex-direction:column;gap:0}
.post-card h3{font-size:1.04rem;line-height:1.3}
.post-card h3 a{text-decoration:none}
.post-card h3 a::after{content:"";position:absolute;inset:0}
.post-card{position:relative}
.post-meta{margin-top:12px;font-size:.78rem;color:var(--muted)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:26px}
.chips button{border:1.5px solid var(--line);background:var(--card);border-radius:999px;padding:8px 16px;font-size:.86rem;font-weight:600;cursor:pointer;color:var(--ink);min-height:40px}
.chips button[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:#fff}

/* faq */
.faq{max-width:820px}
.faq details{border-bottom:1px solid var(--line);padding:4px 0}
.faq summary{cursor:pointer;list-style:none;padding:16px 36px 16px 0;font-weight:700;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:4px;top:12px;font-size:1.4rem;font-weight:400;color:var(--gold-deep)}
.faq details[open] summary::after{content:"–"}
.faq details p{padding:0 0 18px;color:var(--muted);max-width:68ch}

/* google strip */
.gstrip{display:grid;background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
@media(min-width:760px){.gstrip{grid-template-columns:1.2fr 1fr}}
.gstrip-copy{padding:26px;display:flex;flex-wrap:wrap;align-items:center;gap:14px 22px}
.gstrip-copy svg.g{width:34px;height:34px;flex:none}
.gstrip-copy strong{display:block;font-size:1.05rem}
.gstrip-copy span.sub{font-size:.86rem;color:var(--muted)}
.gstrip-img{aspect-ratio:21/9}
.gstrip-img img{width:100%;height:100%;object-fit:cover}

/* about + enquiry */
.about p{max-width:66ch;color:var(--muted)}
.about p+p{margin-top:14px}
.enquiry{background:var(--dark);color:#fff}
.enq-grid{display:grid;gap:34px}
@media(min-width:900px){.enq-grid{grid-template-columns:.85fr 1.15fr;gap:56px}}
.enquiry h2{font-size:clamp(1.55rem,3.4vw,2.35rem);max-width:14ch}
.enquiry .eyebrow{color:var(--gold-hi)}
.enquiry p{margin-top:14px;color:#CFC8BA;max-width:40ch}
.form{display:grid;grid-template-columns:1fr 1fr;gap:14px;background:var(--dark-2);padding:22px;border-radius:var(--radius);border:1px solid #3A3128}
.form .full{grid-column:1/-1}
.form label{display:block;font-size:.8rem;font-weight:600;margin-bottom:6px;color:#DCD5C8}
.form input,.form textarea,.form select{width:100%;padding:11px 12px;border-radius:8px;border:1px solid #4A4035;background:#F6F2EA;color:var(--ink);font:inherit;font-size:.94rem;min-height:44px}
.form textarea{min-height:90px;resize:vertical}
@media(max-width:560px){.form{grid-template-columns:1fr}}

/* footer */
footer{border-top:1px solid var(--line);padding:56px 0 26px;background:var(--cream)}
.foot-grid{display:grid;gap:32px;padding-bottom:34px}
@media(min-width:760px){.foot-grid{grid-template-columns:1.4fr 1fr 1fr 1.2fr}}
.foot-brand img{height:56px;width:auto}
.foot-brand p{margin-top:14px;font-size:.88rem;color:var(--muted);max-width:30ch}
.foot-col h2{font-size:.86rem;font-weight:700;margin-bottom:12px;font-family:'Inter',sans-serif;letter-spacing:0}
.foot-col ul{list-style:none;margin:0;padding:0;display:grid;gap:8px}
.foot-col a{text-decoration:none;color:var(--muted);font-size:.9rem}
.foot-col a:hover{color:var(--ink);text-decoration:underline}
.foot-touch{display:grid;gap:10px;max-width:240px}
.foot-bottom{border-top:1px solid var(--line);padding-top:20px;display:flex;flex-wrap:wrap;justify-content:space-between;gap:10px;font-size:.8rem;color:var(--muted)}

/* article */
.crumbs{font-size:.82rem;color:var(--muted);padding-top:26px}
.crumbs ol{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.crumbs li+li::before{content:"/";margin-right:6px;color:var(--line)}
.crumbs a{text-decoration:none}
.crumbs a:hover{text-decoration:underline}
.article-head{max-width:820px;padding:18px 0 26px}
.article-head h1{font-size:clamp(1.7rem,4.4vw,2.7rem)}
.article-meta{margin-top:14px;display:flex;flex-wrap:wrap;gap:8px 16px;font-size:.84rem;color:var(--muted);align-items:center}
.article-meta .pill{background:var(--ink);color:#fff;border-radius:999px;padding:3px 10px;font-weight:600;font-size:.74rem}
.langs{margin-top:14px;font-size:.86rem;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.langs a{border:1.5px solid var(--line);border-radius:999px;padding:4px 12px;text-decoration:none;font-weight:600;background:var(--card)}
.langs a[aria-current]{background:var(--ink);color:#fff;border-color:var(--ink)}
.article-hero{border-radius:var(--radius);overflow:hidden;max-width:1000px;aspect-ratio:16/9}
.article-hero img{width:100%;height:100%;object-fit:cover}
.prose{max-width:720px;padding:34px 0 10px;font-size:1.04rem}
.prose .lede{font-size:1.15rem;color:var(--ink)}
.prose h2{font-size:clamp(1.25rem,2.6vw,1.6rem);margin:38px 0 12px}
.prose p{margin:0 0 14px;color:#2E2A24}
.prose ul{padding-left:1.2em;margin:0 0 16px}
.prose li{margin:6px 0}
.prose a{color:var(--gold-deep);font-weight:600}
.prose .note{font-size:.88rem;color:var(--muted);font-style:italic}
.table-wrap{overflow-x:auto;margin:10px 0 14px;border:1px solid var(--line);border-radius:10px;background:var(--card)}
.cost-table,.spec-table{width:100%;border-collapse:collapse;font-size:.92rem;min-width:420px}
.cost-table th,.cost-table td,.spec-table th,.spec-table td{padding:10px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top}
.cost-table thead th{background:#EFE7D8;font-weight:700}
.cost-table td:nth-child(n+2),.cost-table tfoot td{text-align:right;white-space:nowrap}
.cost-table tfoot th,.cost-table tfoot td{font-weight:800;background:#F3ECDF;border-bottom:0}
.spec-table th{width:40%;font-weight:600;color:var(--muted)}
.cta-box{max-width:720px;margin:26px 0;background:var(--ink);color:#fff;border-radius:var(--radius);padding:24px;display:flex;flex-wrap:wrap;gap:16px 24px;align-items:center;justify-content:space-between}
.cta-box p{max-width:42ch;color:#EDE7DB}
.article-faq{max-width:720px;padding:10px 0 20px}
.article-faq h2{font-size:clamp(1.25rem,2.6vw,1.6rem);margin-bottom:6px}
.page-head{padding:44px 0 10px}
.page-head h1{font-size:clamp(1.8rem,4.6vw,2.8rem);max-width:20ch}
.page-head p{margin-top:12px;color:var(--muted);max-width:56ch}
.nf{padding:100px 0;text-align:center}
.nf h1{font-size:clamp(2rem,6vw,3.2rem)}
.nf p{margin:14px auto 26px;color:var(--muted);max-width:40ch}
.offer-bar{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:6px 16px;padding:9px 16px;text-decoration:none;color:#fff;font-size:.88rem;font-weight:600;text-align:center;background:linear-gradient(90deg,#8E1616,#C62828 35%,#E4572E 70%,#F08A1C)}
.offer-bar:hover{filter:brightness(1.06)}
.offer-bar s{opacity:.8;font-weight:500}
.ob-tag{background:#FFE066;color:#3A0A0A;border-radius:999px;padding:2px 10px;font-size:.72rem;letter-spacing:.08em;text-transform:uppercase}
.ob-cta{text-decoration:underline;text-underline-offset:3px}
.blink{display:inline-block;border-radius:6px;padding:0 .22em;animation:bwBlink 1s ease-in-out 0s 9 forwards}
@keyframes bwBlink{0%,100%{background:#FFE066;color:#2A0A00;box-shadow:0 0 0 3px rgba(255,224,102,.45)}50%{background:transparent;color:inherit;box-shadow:none}}
@media(min-width:760px){.promo-inner{grid-template-columns:1fr 1.2fr;gap:24px}.promo-cta{grid-column:1/-1}}
@media(min-width:1200px){.promo-inner{grid-template-columns:1.1fr 1.3fr auto;gap:28px}.promo-cta{grid-column:auto}}
@media(max-width:420px){.promo-deals{grid-template-columns:1fr}}
.big-price .blink{padding:0 .15em}
@media(prefers-reduced-motion:reduce){.blink{animation:none;background:#FFE066;color:#2A0A00}}

.quick{background:var(--card);border:1px solid var(--line);border-left:4px solid var(--gold);border-radius:10px;padding:16px 18px;margin:0 0 22px}
.quick-label{font-size:.74rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--gold-deep);margin:0 0 6px!important}
.quick p{margin:0}
.offer-box{background:linear-gradient(135deg,#1a1510,#2b2118);color:#F3E9D6;border-radius:var(--radius);padding:20px 22px;margin:18px 0 26px}
.offer-box .offer-h{font-weight:700;color:var(--gold-hi);margin:0 0 10px}
.offer-box ul{list-style:none;padding:0;margin:0 0 10px}
.offer-box li{display:flex;flex-wrap:wrap;justify-content:space-between;gap:4px 16px;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.12)}
.offer-box .price strong{font-size:1.25rem;color:#fff} .offer-box s{opacity:.6;margin-left:6px}
.offer-box small{opacity:.75}
.offer-box .offer-bulk{margin:8px 0 4px;color:#F3E9D6} .offer-box .offer-bulk a{color:var(--gold-hi)}
.offer-box .offer-note{font-size:.8rem;opacity:.75;margin:0}
.prose .offer-box p{color:#F3E9D6}
.cost-table tr.ours td{font-weight:700;background:#F7EEDD}
.price-grid{display:grid;gap:20px}
@media(min-width:760px){.price-grid{grid-template-columns:1fr 1fr}}
.price-card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;display:grid}
.price-card .pc-img{aspect-ratio:4/3;background:#EFE7D8;overflow:hidden} .price-card .pc-img img{width:100%;height:100%;object-fit:cover}
.price-card .pc-body{padding:22px}
.tag{display:inline-block;background:var(--ink);color:var(--gold-hi);font-size:.72rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:4px 10px}
.price-card h3{font-size:1.15rem;margin:10px 0 4px}
.price-card .aka{font-size:.84rem;color:var(--muted)}
.big-price{margin:14px 0 4px;font:800 2.1rem/1 'Montserrat',sans-serif;color:var(--ink)}
.price-regular{display:inline-block;font:600 .78rem/1.2 'Inter',sans-serif;color:var(--muted);margin-left:8px;vertical-align:middle}
.big-price s{font:600 1rem 'Inter',sans-serif;color:var(--muted);margin-left:8px}
.per{font-size:.82rem;color:var(--muted)}
.price-card ul{margin:12px 0 16px;padding-left:1.1em;font-size:.88rem;color:var(--muted)}
.pc-ctas{display:flex;flex-wrap:wrap;gap:10px}
.fine{margin-top:18px;font-size:.84rem;color:var(--muted);max-width:80ch}
.card-price{display:block;margin-top:8px;font-weight:700;color:var(--gold-deep)}
.card-price s{color:var(--muted);font-weight:500;margin-left:6px}
.prod-grid{display:grid;gap:30px;padding:10px 0 40px}
@media(min-width:900px){.prod-grid{grid-template-columns:1.1fr .9fr;gap:48px}}
.gallery{display:grid;gap:10px}
.gallery .main{border-radius:var(--radius);overflow:hidden;aspect-ratio:5/4;background:#EFE7D8}
.gallery .main img{width:100%;height:100%;object-fit:cover}
.gallery .thumbs{display:grid;grid-template-columns:repeat(auto-fit,minmax(0,1fr));gap:10px}
.gallery .thumbs figure{margin:0;border-radius:10px;overflow:hidden;aspect-ratio:4/3;background:#EFE7D8}
.gallery .thumbs img{width:100%;height:100%;object-fit:cover}
.prod-info h1{font-size:clamp(1.6rem,4vw,2.4rem)}
.keyfacts{margin:18px 0;display:grid;grid-template-columns:auto 1fr;gap:6px 16px;font-size:.92rem}
.keyfacts dt{font-weight:700} .keyfacts dd{margin:0;color:var(--muted)}

/* ===== 5th anniversary hero ===== */
.ann{position:relative;overflow:hidden;color:#FFF3DC;background:radial-gradient(900px 560px at 8% 16%,rgba(214,86,30,.45),transparent 62%),linear-gradient(115deg,#3A0C07 0%,#5C150D 48%,#2B0A05 100%)}
.ann::before{content:"";position:absolute;inset:8px;border:1px solid rgba(240,182,64,.32);border-radius:14px;pointer-events:none;z-index:5}
.ann-media{position:relative;aspect-ratio:3/2;background:#2B0A05;overflow:hidden}
.ann-media::after{content:"";position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,rgba(43,10,5,0) 58%,rgba(43,10,5,.9) 100%)}
.ann-slide{position:absolute;inset:0;opacity:0;transition:opacity .9s ease}
.ann-slide.active{opacity:1}
.ann-slide img{width:100%;height:100%;object-fit:cover}
.ann-seal{position:absolute;right:16px;top:16px;width:84px;height:84px;z-index:4;filter:drop-shadow(0 6px 14px rgba(0,0,0,.45))}
.ann-seal .ring{transform-origin:60px 60px;animation:annSpin 32s linear infinite}
@keyframes annSpin{to{transform:rotate(360deg)}}
.ann-ctrl{position:absolute;right:16px;bottom:16px;z-index:4;display:flex;align-items:center;gap:8px}
.ann-dots{display:flex;gap:4px;background:rgba(43,10,5,.74);border-radius:999px;padding:4px}
.ann-dots button{border:0;background:transparent;color:#F6D9A8;font:600 .72rem/1 'Inter',sans-serif;padding:7px 9px;border-radius:999px;cursor:pointer;min-width:34px;min-height:30px}
.ann-dots button[aria-selected=true]{background:#F0B640;color:#3A0C07}
.ann-arrow{width:40px;height:40px;border-radius:50%;border:0;background:rgba(43,10,5,.74);color:#FFE29A;display:flex;align-items:center;justify-content:center;cursor:pointer}
.ann-arrow svg{width:16px;height:16px}
.ann-copy{position:relative;z-index:2;padding:22px 2px 46px}
.ann-eyebrow{display:flex;align-items:center;gap:10px;font:700 .72rem/1.3 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#F6D9A8}
.ann-eyebrow::before{content:"";flex:none;width:26px;height:1px;background:#F0B640}
.ann-title{margin:8px 0 0;font-weight:400;line-height:1;letter-spacing:0}
.ann-script{display:block;font-family:'Great Vibes',cursive;font-size:clamp(2.7rem,11vw,4.2rem);line-height:1.08;padding:0 .3em .1em 0;background:linear-gradient(100deg,#FFF0C2,#F0B640 55%,#E89A2B);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;color:#F0B640}
.ann-big{display:block;font-family:'Playfair Display',Georgia,serif;font-weight:900;font-size:clamp(2.1rem,9.4vw,4.3rem);letter-spacing:.012em;text-transform:uppercase;line-height:1.03;color:#FFF3DC;text-shadow:0 3px 0 rgba(0,0,0,.28)}
.ann-offer{display:flex;align-items:center;gap:14px;margin-top:8px;font-family:'Playfair Display',Georgia,serif;font-style:italic;font-weight:700;font-size:clamp(1rem,4vw,1.6rem);letter-spacing:.42em;text-transform:uppercase;color:#F0B640}
.ann-offer::before,.ann-offer::after{content:"";height:1px;width:clamp(26px,9vw,64px);background:linear-gradient(90deg,transparent,#F0B640)}
.ann-offer::after{background:linear-gradient(270deg,transparent,#F0B640)}
.ann-badge-wrap{display:inline-block;margin-top:18px;filter:drop-shadow(0 8px 14px rgba(0,0,0,.45))}
.ann-badge{position:relative;overflow:hidden;display:inline-flex;align-items:baseline;gap:.55rem;padding:9px 30px 11px;color:#3A0C07;background:linear-gradient(135deg,#FFE9A8,#F0B640 50%,#C98A1B);clip-path:polygon(0 0,100% 0,calc(100% - 14px) 50%,100% 100%,0 100%,14px 50%)}
.ann-badge .bt{font:800 .8rem/1 'Inter',sans-serif;letter-spacing:.16em}
.ann-badge .bp{font:800 clamp(2.4rem,9vw,3.5rem)/1 'Montserrat','Inter',sans-serif;letter-spacing:-.02em}
.ann-badge .bo{font:800 1.15rem/1 'Inter',sans-serif;letter-spacing:.14em}
.ann-badge::after{content:"";position:absolute;top:0;bottom:0;width:56px;left:-90px;background:linear-gradient(100deg,transparent,rgba(255,255,255,.75),transparent);transform:skewX(-20deg);animation:annSheen 4.6s ease-in-out 1.2s infinite}
@keyframes annSheen{0%{left:-90px}45%,100%{left:120%}}
.ann-sub{margin-top:16px;max-width:46ch;font-size:1rem;color:#F1DFC4}
.ann-deals{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:20px}
.ann-deal{display:grid;grid-template-columns:1fr auto;align-items:center;gap:2px 8px;text-decoration:none;color:#3A0C07;background:linear-gradient(160deg,#FFF8E6,#F7E2B0);border:1px solid rgba(255,214,120,.85);border-radius:14px;padding:13px 15px 14px;box-shadow:0 12px 30px -14px rgba(0,0,0,.75);transition:transform .15s ease}
.ann-deal:hover{transform:translateY(-2px)}
.ann-deal .dn{font:700 .7rem/1.25 'Inter',sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#7A2A12}
.ann-deal .dn small{display:block;margin-top:2px;font-weight:500;letter-spacing:0;text-transform:none;color:#7B6A58;font-size:.72rem}
.ann-deal .dp{justify-self:start;align-self:start;margin-top:4px;font:800 clamp(1.5rem,6.2vw,2.2rem)/1.05 'Montserrat','Inter',sans-serif;color:#8E1616}
.ann-deal .dw{font-size:.82rem;color:#6E5C49}
.ann-deal .dw s{margin-right:4px;font-weight:600}
.ann-deal .dn,.ann-deal .dp{grid-column:1/-1}.ann-deal .do{justify-self:end;margin-top:0;background:#8E1616;color:#fff;font:800 .68rem/1 'Inter',sans-serif;letter-spacing:.06em;border-radius:999px;padding:5px 10px}
.ann-limited{display:inline-flex;align-items:center;gap:9px;margin:18px 0 0;background:rgba(142,22,22,.88);border:1px solid rgba(255,214,120,.55);color:#FFF3DC;border-radius:999px;padding:8px 16px;font-weight:700;font-size:.88rem;line-height:1.3}
.ann-limited .pulse{flex:none;width:9px;height:9px;border-radius:50%;background:#FFE066;box-shadow:0 0 0 0 rgba(255,224,102,.7);animation:annPulse 1.6s infinite}
@keyframes annPulse{70%{box-shadow:0 0 0 10px rgba(255,224,102,0)}100%{box-shadow:0 0 0 0 rgba(255,224,102,0)}}
.ann-ctas{margin-top:18px;display:flex;flex-wrap:wrap;gap:12px}
.btn-foil{background:linear-gradient(135deg,#FFE9A8,#F0B640 55%,#C98A1B);color:#3A0C07;font-weight:800;padding:14px 26px;font-size:1rem;box-shadow:0 12px 26px -12px rgba(240,182,64,.85)}
.btn-foil:hover{filter:brightness(1.07)}
.btn-ghost{border-color:rgba(255,243,220,.6);color:#FFF3DC}
.btn-ghost:hover{background:rgba(255,243,220,.12);border-color:#FFF3DC}
.ann-fine{margin-top:14px;font-size:.8rem;color:#DCC7A4}
.ann-fine a{color:#FFE29A;font-weight:600}
.spark{position:absolute;z-index:1;background:#FFE29A;clip-path:polygon(50% 0,60% 40%,100% 50%,60% 60%,50% 100%,40% 60%,0 50%,40% 40%);opacity:0;animation:annTwinkle 3.6s ease-in-out infinite;pointer-events:none}
.spark.s1{right:6%;top:26%;width:16px;height:16px}.spark.s2,.spark.s4{display:none}.spark.s3{right:10%;top:58%;width:9px;height:9px;animation-delay:1.6s}.spark.s5{right:4%;bottom:6%;width:14px;height:14px;animation-delay:.4s}
@keyframes annTwinkle{0%,100%{opacity:0;transform:scale(.6)}50%{opacity:.95;transform:scale(1)}}
@media(max-width:339px){.ann-deals{grid-template-columns:1fr}}
@media(max-width:560px){.offer-bar{font-size:.8rem;gap:4px 12px;padding:8px 12px}.offer-bar .ob-cta{display:none}}
@media(min-width:700px) and (max-width:1199px){
 .ann-media{aspect-ratio:16/9}.ann-seal{width:112px;height:112px;right:28px;top:24px}.ann-ctrl{right:28px;bottom:22px}
 .ann-copy{padding:28px 0 54px;max-width:700px}
 .ann-big{font-size:clamp(3rem,7vw,4.3rem)}
}
@media(min-width:1200px){
 .ann{min-height:clamp(560px,78vh,760px);display:flex;align-items:center}
 .ann-media{position:absolute;right:0;top:0;bottom:0;width:min(62%,1100px);aspect-ratio:auto;-webkit-mask-image:linear-gradient(90deg,transparent 0,#000 16%);mask-image:linear-gradient(90deg,transparent 0,#000 16%)}
 .ann-media::after{display:none}
 .ann-seal{width:120px;height:120px;right:38px;top:34px}
 .ann-ctrl{right:38px;bottom:30px}
 .ann-grid{position:relative;z-index:2;width:100%}
 .ann-copy{padding:36px 0 40px;width:min(540px,44vw)}
 .ann-script{font-size:clamp(2.6rem,3.8vw,3.8rem)}
 .ann-big{font-size:clamp(2.4rem,3.7vw,3.6rem)}
 .ann-offer{margin-top:4px;font-size:clamp(1rem,1.3vw,1.3rem)}
 .ann-badge-wrap{margin-top:12px}.ann-badge{padding:6px 26px 8px}.ann-badge .bp{font-size:clamp(2.2rem,3vw,2.9rem)}
 .ann-sub{margin-top:12px;font-size:.95rem}.ann-deals{margin-top:14px;gap:10px}.ann-deal{padding:10px 14px 11px}.ann-limited{margin-top:14px;padding:7px 14px;font-size:.84rem}.ann-ctas{margin-top:14px}.btn-foil{padding:12px 24px}.ann-fine{margin-top:10px}
 .ann-slide img{object-position:60% 50%!important}
 .ann-deal .dp{font-size:clamp(1.7rem,2.1vw,2.1rem)}
 .spark.s1{left:72%;right:auto;top:34%}.spark.s3{left:-3%;right:auto;top:57%}.spark.s5{left:62%;right:auto;top:8%;bottom:auto}
}
@media(prefers-reduced-motion:reduce){.ann-badge::after,.spark,.ann-limited .pulse,.ann-seal .ring{animation:none}.spark{opacity:.55}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}.ann-slide,.card .thumb img{transition:none}}
'''

JS = r'''
(function(){
 var END=new Date('__OFFER_END__T23:59:59+05:30');
 if(Date.now()>END.getTime()){document.querySelectorAll('[data-after]').forEach(function(e){e.innerHTML=e.getAttribute('data-after')});document.querySelectorAll('[data-offer-bar],[data-offer-only]').forEach(function(e){e.hidden=true})}
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
'''

if OFFER['end']:
    JS = JS.replace('__OFFER_END__', OFFER['end'])
else:
    _a = JS.index(" var END="); _b = JS.index(" document.querySelectorAll('[data-year]')"); JS = JS[:_a] + JS[_b:]
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Montserrat:wght@700;800&family=Noto+Sans+Devanagari:wght@400;600;700&family=Noto+Sans+Malayalam:wght@400;600;700&display=swap" rel="stylesheet">')

WA_ICON = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 20Zm4.4-5.9c-.2-.1-1.4-.7-1.6-.8-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1-.7-.3-1.5-.8-2.1-1.5-.5-.6-1-1.3-1.2-1.5-.1-.2 0-.4.1-.5l.4-.5c.1-.1.1-.3.1-.4 0-.1-.5-1.2-.7-1.6-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.4.1-.6.3-.7.7-1 1.5-.9 2.4.2 1.2.9 2.4 2 3.6 1.3 1.5 2.7 2.3 4.3 2.7.5.1.9.1 1.3 0 .5-.1 1.4-.6 1.6-1.1.2-.5.2-.9.1-1.1-.1-.1-.2-.2-.4-.3Z"/></svg>'

NAV_ITEMS = [('/#products', 'Products'), ('/bunker-cot-double-decker-bed/', 'Bunk Beds'), ('/steel-single-cot/', 'Single Cots'), ('/#pricing', 'Offer'),
             ('/#collections', 'Collections'), ('/#projects', 'Projects'), ('/blog/', 'Blog'), ('/#about', 'About')]

def banner():
    if not ACTIVE: return ''
    return (f'<a class="offer-bar" data-offer-bar href="/#pricing" aria-label="5th Anniversary Offer. Bunk bed ₹{B}. Single cot ₹{S}. Offer ends {OFFER["end_label"]["en"]}.">'
            f'<span class="ob-tag">5th Anniversary Offer</span>'
            f'<span>Bunk bed <b class="blink">₹{B}</b></span>'
            f'<span>Single cot <b class="blink">₹{S}</b></span>'
            f'<span class="ob-cta">Ends {OFFER["end_label"]["en"]} — book now →</span></a>')

HERO_FONTS = '<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital,wght@0,800;0,900;1,700&display=swap" rel="stylesheet">'

def ann_hero():
    slides = [('anniversary-bunk-bed-terracotta-room', 'Bunkworks galvanised steel bunk bed (bunker cot, double decker bed) with 12mm plywood decks and guard rail in a hostel room', 'center 50%'),
              ('anniversary-single-cot-wood-top', 'Steel single cot for hostels and PGs with wooden plywood top and grey galvanised steel frame — steel single cot for hostels', 'center 50%'),
              ('anniversary-bunk-bed-warm-lit-room', 'Heavy-duty steel double decker bed for hostels with ladder handle, epoxy coating and 200 kg total (100 kg per deck) weight bearing — factory direct from Kerala', 'center 50%'),
              ('single-cot-terracotta-dressed-bed', 'Bunkworks steel single cot with mattress, pillows and bedding — grey epoxy-coated galvanised frame with arched head rail for hostels and PGs', 'center 55%')]
    sl = ''.join(f'<div class="ann-slide{" active" if i == 0 else ""}">{img(k, a, "(min-width:1200px) 62vw, 100vw", eager=(i == 0)).replace("<img ", f"<img style=\"object-position:{pos}\" ")}</div>' for i, (k, a, pos) in enumerate(slides))
    dots = ''.join(f'<button role="tab" aria-selected="{"true" if i == 0 else "false"}" aria-label="Show photo {i+1}">0{i+1}</button>' for i in range(len(slides)))
    seal = """<svg class="ann-seal" viewBox="0 0 120 120" aria-hidden="true" focusable="false"><defs><linearGradient id="sg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE9A8"/><stop offset=".55" stop-color="#F0B640"/><stop offset="1" stop-color="#B9771C"/></linearGradient><path id="sc" d="M60,60 m-45,0 a45,45 0 1,1 90,0 a45,45 0 1,1 -90,0"/></defs><circle cx="60" cy="60" r="58" fill="url(#sg)"/><circle cx="60" cy="60" r="53" fill="#4A0F09"/><circle cx="60" cy="60" r="50" fill="none" stroke="#FFE9A8" stroke-width=".8" stroke-dasharray="1.5 3"/><g class="ring"><text font-size="8.6" font-weight="700" letter-spacing="1.4" fill="#FFE9A8" font-family="Inter,sans-serif"><textPath href="#sc" textLength="278" lengthAdjust="spacing">BUNKWORKS • ANNIVERSARY OFFER • </textPath></text></g><text x="60" y="73" text-anchor="middle" font-family="Playfair Display,Georgia,serif" font-weight="900" font-size="44" fill="url(#sg)">5</text><text x="60" y="90" text-anchor="middle" font-family="Inter,sans-serif" font-weight="800" font-size="9" letter-spacing="3" fill="#FFE9A8">YEARS</text></svg>"""
    ctrl = f'<div class="ann-ctrl"><button class="ann-arrow prev" aria-label="Previous photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 18l-6-6 6-6"/></svg></button><div class="ann-dots" role="tablist" aria-label="Hero photos">{dots}</div><button class="ann-arrow next" aria-label="Next photo"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18l6-6-6-6"/></svg></button></div>'
    media = f'<div class="ann-media" id="heroCarousel">{sl}{seal}{ctrl}</div>'
    sparks = '<i class="spark s1"></i><i class="spark s2"></i><i class="spark s3"></i><i class="spark s4"></i><i class="spark s5"></i>'
    if not ACTIVE:
        return f'''<section class="ann" aria-labelledby="ann-h">{media}<div class="wrap ann-grid"><div class="ann-copy">{sparks}<span class="ann-eyebrow">Hostel &amp; institutional furniture</span>
 <h1 class="ann-title" id="ann-h"><span class="ann-big">Built for spaces that work.</span></h1>
 <p class="ann-sub">Galvanised steel bunk beds, double decker cots and single cots for hostels, PGs and institutions — factory direct from Kerala.</p>
 <div class="ann-ctas"><a class="btn btn-foil" href="#products">Explore products {ARROW}</a><a class="btn btn-ghost" href="#enquire">Get a quote</a></div></div></div></section>'''
    pct = OFFER['off_pct']
    wb = wa(f"Hi Bunkworks, I want to book steel bunk beds at ₹{B} (5th Anniversary Offer). Quantity: , Delivery city: ")
    ws = wa(f"Hi Bunkworks, I want to book steel single cots at ₹{S} (5th Anniversary Offer). Quantity: , Delivery city: ")
    wg = wa(f"Hi Bunkworks, I want to book from the 5th Anniversary Offer (limited pieces). Product: , Quantity: , Delivery city: ")
    return f'''<section class="ann" aria-labelledby="ann-h">
{media}
<div class="wrap ann-grid"><div class="ann-copy">{sparks}
 <h1 class="ann-title" id="ann-h"><span class="ann-eyebrow">Bunkworks — steel bunker cots, double decker beds &amp; single cots</span><span class="ann-script">Our 5th</span> <span class="ann-big">Anniversary</span> <span class="ann-offer">Offer</span></h1>
 <div class="ann-badge-wrap" data-offer-only><div class="ann-badge"><span class="bt">ANNIVERSARY</span><span class="bp">PRICES</span><span class="bo">UNTIL 15 OCT</span></div></div>
 <p class="ann-sub">Steel bunk beds (double decker cots) and single cots for hostels, PGs and institutions — factory direct from Kerala.</p>
 <div class="ann-deals" data-offer-only>
  <a class="ann-deal" href="{wb}" target="_blank" rel="noopener" aria-label="Book steel bunk bed at {B} rupees on WhatsApp"><span class="dn">Steel bunk bed<small>Bunker cot / double decker</small></span><span class="dp blink">₹{B}</span><span class="dw"><s>₹{BR}</s> regular from 16 Oct</span></a>
  <a class="ann-deal" href="{ws}" target="_blank" rel="noopener" aria-label="Book steel single cot at {S} rupees on WhatsApp"><span class="dn">Steel single cot<small>6 × 2.5 ft hostel bed</small></span><span class="dp blink">₹{S}</span><span class="dw"><s>₹{SR}</s> regular from 16 Oct</span></a>
 </div>
 <p class="ann-limited" data-offer-only><span class="pulse" aria-hidden="true"></span>Limited pieces left — offer ends {OFFER["end_label"]["en"]}, book your order now</p>
 <div class="ann-ctas"><a class="btn btn-foil" href="{wg}" target="_blank" rel="noopener">Book your order now {ARROW}</a><a class="btn btn-ghost" href="#pricing">See all prices</a></div>
 <p class="ann-fine">Prices per piece, without mattress. Buying {OFFER["bulk_min"]}+ pieces? <a href="{WA_BULK}" target="_blank" rel="noopener">Get a bulk quote</a></p>
</div></div>
</section>'''

def nav(active=''):
    li = ''.join(f'<li><a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a></li>' for h, t in NAV_ITEMS)
    return f'''<a class="skip" href="#main">Skip to content</a>
{banner()}
<header class="nav">
 <div class="nav-inner">
  <a href="/" class="brand"><img src="/images/bunkworks-logo.png" alt="Bunkworks logo — steel bunk beds, double decker cots and single cots for hostels, Kerala" width="{LOGO_W}" height="{LOGO_H}"></a>
  <nav aria-label="Main"><ul class="nav-links">{li}</ul></nav>
  <div class="nav-right">
   <a class="nav-wa" href="{wa('Hi Bunkworks, I have a question about your beds.')}" target="_blank" rel="noopener">{WA_ICON}WhatsApp</a>
   <a href="/#enquire" class="btn btn-gold">Get a Quote {ARROW}</a>
   <button class="burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="mpanel"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  </div>
 </div>
 <div class="mobile-panel" id="mpanel"><ul>{li}<li><a class="btn btn-gold" href="/#enquire">Get a Quote</a></li></ul></div>
</header>'''

def footer():
    guides = ''.join(f'<li><a href="/blog/{p["slug"]}/" lang="{p["lang"]}">{short(p)}</a></li>' for p in POSTS[:4])
    return f'''<footer>
 <div class="wrap">
  <div class="foot-grid">
   <div class="foot-brand"><img src="/images/bunkworks-logo.png" alt="Bunkworks logo — steel bunk beds, double decker cots and single cots for hostels, Kerala" width="{LOGO_W}" height="{LOGO_H}" loading="lazy"><p>Hostel and institutional furniture, manufactured in Kerala, India. Factory-direct bunk beds, single beds and cots.</p></div>
   <div class="foot-col"><h2>Quick links</h2><ul><li><a href="/bunker-cot-double-decker-bed/">Steel bunk beds</a></li><li><a href="/steel-single-cot/">Steel single cots</a></li><li><a href="/#pricing">Anniversary offer prices</a></li><li><a href="/#mattress">Foam mattress</a></li><li><a href="/#collections">Collections</a></li></ul></div>
   <div class="foot-col"><h2>Guides</h2><ul>{guides}<li><a href="/blog/">All articles</a></li></ul></div>
   <div class="foot-col"><h2>Get in touch</h2><div class="foot-touch"><a class="btn btn-wa" href="{wa('Hi Bunkworks, I have a question about your beds.')}" target="_blank" rel="noopener">Chat on WhatsApp</a><a class="btn btn-gold" href="/#enquire">Get a Quote {ARROW}</a><a href="tel:+919072431550" style="font-size:.9rem;color:var(--muted)">+91 90724 31550</a><a href="mailto:{EMAIL}" style="font-size:.9rem;color:var(--muted)">{EMAIL}</a><a href="{GBP}" target="_blank" rel="noopener" style="font-size:.9rem;color:var(--muted)">Bunkworks Warehouse on Google</a></div></div>
  </div>
  <div class="foot-bottom"><span>© <span data-year>2026</span> Bunkworks. {TAGLINE}.</span><span><a href="/#about">About</a> &nbsp; <a href="/#process">Our process</a> &nbsp; <a href="/sitemap.xml">Sitemap</a></span></div>
 </div>
</footer>'''

def short(p): return p['short']
ORG = {"@context": "https://schema.org", "@type": "Organization", "@id": SITE + "/#org", "name": "Bunkworks", "url": SITE + "/",
       "logo": SITE + "/images/bunkworks-logo-square.png", "image": SITE + "/og-image.jpg", "email": EMAIL, "slogan": TAGLINE,
       "description": "Manufacturer of galvanised steel bunk beds, single beds and cots for hostels, PGs, dormitories and institutions.",
       "address": {"@type": "PostalAddress", "streetAddress": "First Floor, SRA-53, Shanthinagar Rd", "addressLocality": "Chakkarapparambu, Vennela", "addressRegion": "Kerala", "postalCode": "682028", "addressCountry": "IN"}, "telephone": "+91-9072431550", "sameAs": [GBP]}

def page(path, title, desc, body, lang='en', og_image='/og-image.jpg', og_type='website', ld=(), extra_head='', keywords='', robots='index, follow'):
    ldj = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    kw = f'<meta name="keywords" content="{H.escape(keywords)}">' if keywords else ''
    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{H.escape(title)}</title>
<meta name="description" content="{H.escape(desc)}">
{kw}
<meta name="robots" content="{robots}">
<link rel="canonical" href="{SITE}{path}">
{extra_head}
<meta name="theme-color" content="#F6F2EA">
<meta name="google-site-verification" content="PASTE-YOUR-SEARCH-CONSOLE-CODE">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="Bunkworks">
<meta property="og:title" content="{H.escape(title)}">
<meta property="og:description" content="{H.escape(desc)}">
<meta property="og:url" content="{SITE}{path}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:locale" content="{ {'en':'en_IN','ml':'ml_IN','hi':'hi_IN'}[lang] }">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{H.escape(title)}">
<meta name="twitter:description" content="{H.escape(desc)}">
<meta name="twitter:image" content="{SITE}{og_image}">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png"><link rel="icon" type="image/png" sizes="16x16" href="/favicon-16.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
{FONTS}
<link rel="stylesheet" href="/assets/site.css">
{ldj}
</head>
<body>
{nav(path if path == '/blog/' else '')}
<main id="main">
{body}
</main>
{footer()}
<script src="/assets/site.js" defer></script>
</body>
</html>'''

def post_card(p, sizes='(min-width:980px) 33vw, (min-width:680px) 50vw, 100vw'):
    u = UI[p['lang']]
    return f'''<article class="card post-card" data-lang="{p['lang']}" lang="{p['lang']}">
 <div class="thumb">{img(p['thumb'], p['alt'], sizes)}<span class="lang-chip">{u['chip']}</span></div>
 <div class="card-body"><h3><a href="/blog/{p['slug']}/">{H.escape(p['title'])}</a></h3><p>{H.escape(p['excerpt'])}</p><span class="post-meta">{u['date']} &nbsp;|&nbsp; {p['read']} {u['min']}</span></div>
</article>'''

HOME_FAQ = [
 ('What is the price of a bunk bed (bunker cot / double decker bed) at Bunkworks?', (f'₹{B} per piece in the 5th Anniversary Offer (regular price ₹{BR}, {OFFER["off_pct"]}% off) while stock lasts. ' if ACTIVE else f'₹{PB} per piece. ') + f'Orders of more than {OFFER["bulk_min"]} pieces get a bulk quote. Prices are per piece, without mattress.'),
 ('What is the price of a steel single cot?', (f'₹{S} per piece in the 5th Anniversary Offer (regular price ₹{SR}, {OFFER["off_pct"]}% off) while stock lasts. ' if ACTIVE else f'₹{PS} per piece. ') + 'It is 6 × 2.5 ft with a galvanised steel frame, a 12mm plywood base and a load capacity of up to 100 kg.'),
 ('Is a bunker cot the same as a double decker bed?', 'Yes. Bunker cot, double decker bed, double decker cot and bunk bed all describe two sleeping decks stacked on one frame.'),
 ('Do you sell hostel beds wholesale, direct from the factory?', f'Yes. Bunkworks manufactures in its own workshop in Kerala and supplies hostels, PGs and institutions directly. Orders above {OFFER["bulk_min"]} pieces get a separate bulk quote.'),
 ('Is the mattress included in the price?', 'No. Prices are for the steel frame with its plywood base. Mention mattresses in your enquiry if you need them.'),
 ('Can I order custom sizes?', 'Yes. Tell us the size, quantity and delivery city in the quote form and we will confirm what is possible.'),
]

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs): return ''.join(f'<details><summary>{H.escape(q)}</summary><p>{H.escape(a)}</p></details>' for q, a in faqs)

COT_SVG = '''<svg class="cot-art" viewBox="0 0 400 300" role="img" aria-label="Folding steel cot with X-shaped legs — cots and folding beds for hostels, PGs and guest rooms"><rect width="400" height="300" fill="#EFE7D8"/><rect y="238" width="400" height="62" fill="#E4D9C4"/>
<path d="M58 132 L292 104 L346 126 L112 156 Z" fill="#1d1d1d"/><path d="M58 132 L112 156 L112 166 L58 142 Z" fill="#0f0f0f"/><path d="M112 156 L346 126 L346 136 L112 166 Z" fill="#2a2a2a"/>
<g stroke="#121212" stroke-width="7" stroke-linecap="round"><path d="M92 150 L150 246"/><path d="M150 158 L94 244"/><path d="M296 124 L346 226"/><path d="M340 132 L292 232"/></g>
<g stroke="#8A5418" stroke-width="3"><path d="M121 199 L320 176"/></g><ellipse cx="200" cy="262" rx="150" ry="9" fill="#d6c8ad"/></svg>'''

def home():
    cards_sizes = '(min-width:980px) 33vw, (min-width:680px) 50vw, 100vw'
    posts = ''.join(post_card(p) for p in POSTS)
    body = f'''
{ann_hero()}

<section class="section" id="pricing" aria-labelledby="pricing-h" style="padding-bottom:20px">
 <div class="wrap">
  <div class="section-head"><div><span class="eyebrow">{'5th Anniversary Offer' if ACTIVE else 'Factory prices'}</span><h2 id="pricing-h">{('Up to ' + str(OFFER['off_pct']) + '% off, only in our 5th year.') if ACTIVE else 'Factory-direct prices.'}</h2></div>
   <p>{swap('Limited pieces are available at these prices — book your order before the stock is gone.', 'Per piece, without mattress, direct from our Kerala workshop.')}</p></div>
  <div class="price-grid">
   <article class="price-card"><div class="pc-img">{img('bunk-bed-studio-cutout', 'Steel bunk bed (bunker cot, double decker bed) for hostels — galvanised frame, 12mm plywood decks, guard rail and ladder handle, price and specifications', '(min-width:760px) 45vw, 100vw')}</div>
    <div class="pc-body">{TAGOFF}<h3>Steel bunk bed</h3><p class="aka">Bunker cot / double decker bed / double decker cot, 1.40 m high</p>
     <p class="big-price">{swap(f'<span class="blink">₹{B}</span> <small class="price-regular">regular ₹{PB} from 16 Oct</small>', f'₹{PB}')}</p><p class="per">per piece, without mattress</p>
     <ul><li>Galvanised anti-rust steel frame</li><li>12mm plywood decks, epoxy coated</li><li>1.40 m high, 200 kg total (100 kg per deck)</li></ul>
     <div class="pc-ctas"><a class="btn btn-gold" href="{wa(f'Hi Bunkworks, I want to book steel bunk beds at ₹{B if ACTIVE else BR}. Quantity: , Delivery city: ')}" target="_blank" rel="noopener">Book now on WhatsApp</a><a class="btn btn-line" href="/bunker-cot-double-decker-bed/">Details</a></div></div></article>
   <article class="price-card"><div class="pc-img">{img('anniversary-single-cot-wood-top', 'Steel single cot for hostels and PGs — wooden plywood top, grey galvanised steel frame and anti-skid feet, price and specifications', '(min-width:760px) 45vw, 100vw')}</div>
    <div class="pc-body">{TAGOFF}<h3>Steel single cot</h3><p class="aka">Single bed / hostel cot, 6 × 2.5 ft, 40 cm high</p>
     <p class="big-price">{swap(f'<span class="blink">₹{S}</span> <small class="price-regular">regular ₹{PS} from 16 Oct</small>', f'₹{PS}')}</p><p class="per">per piece, without mattress</p>
     <ul><li>Galvanised anti-rust steel frame</li><li>12mm plywood base, up to 100 kg</li><li>Epoxy coated, anti-skid feet</li></ul>
     <div class="pc-ctas"><a class="btn btn-gold" href="{wa(f'Hi Bunkworks, I want to book steel single cots at ₹{S if ACTIVE else SR}. Quantity: , Delivery city: ')}" target="_blank" rel="noopener">Book now on WhatsApp</a><a class="btn btn-line" href="/steel-single-cot/">Details</a></div></div></article>
  </div>
  <p class="fine"><strong>Buying more than {OFFER["bulk_min"]} pieces?</strong> <a href="{WA_BULK}" target="_blank" rel="noopener">Get a bulk quote on WhatsApp (+91 90724 31550)</a> or email <a href="{MAIL_BULK}">{EMAIL}</a>.</p>
 </div>
</section>

<section class="section" id="products" aria-labelledby="products-h">
 <div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Our products</span><h2 id="products-h">Built for the spaces that need more.</h2></div>
   <div><p>Durable, practical, space-efficient sleeping for hostels, PGs, institutions and modern living spaces.</p><a class="link-arrow" href="#enquire">Ask for the full catalogue {ARROW}</a></div></div>
  <div class="grid-3">
   <article class="card" id="bunk-beds"><div class="thumb">{img('anniversary-bunk-bed-warm-lit-room', 'Galvanised steel bunk bed (double decker cot, bunker cot) with 12mm plywood decks, ladder handle and guard rail for hostels and PGs', cards_sizes)}</div>
    <div class="card-body"><div><h3><a href="/bunker-cot-double-decker-bed/" style="text-decoration:none">Bunk Beds</a></h3><p>Bunker cots and double decker beds that double the sleepers per room in hostels, PGs and dormitories.</p><span class="card-price">{swap(f'₹{B} <small class="price-regular">regular ₹{PB} from 16 Oct</small>', f'₹{PB}')}</span></div><a class="circle-link" href="/bunker-cot-double-decker-bed/" aria-label="Steel bunk bed details and price">{DIAG}</a></div></article>
   <article class="card" id="single-beds"><div class="thumb">{img('single-cot-terracotta-dressed-bed', 'Bunkworks steel single cot with mattress and bedding — grey galvanised steel hostel single bed with plywood base', cards_sizes)}</div>
    <div class="card-body"><div><h3><a href="/steel-single-cot/" style="text-decoration:none">Single Cots</a></h3><p>Strong, practical single cots — 6 × 2.5 ft, 40 cm high, 12mm plywood base, up to 100 kg.</p><span class="card-price">{swap(f'₹{S} <small class="price-regular">regular ₹{PS} from 16 Oct</small>', f'₹{PS}')}</span></div><a class="circle-link" href="/steel-single-cot/" aria-label="Steel single cot details and price">{DIAG}</a></div></article>
   <article class="card" id="mattress"><div class="thumb"><picture><source type="image/webp" srcset="/images/foam-mattress-3-inch-sm.webp 720w, /images/foam-mattress-3-inch.webp 1500w" sizes="(min-width:980px) 33vw, (min-width:680px) 50vw, 100vw"><img src="/images/foam-mattress-3-inch.jpg" srcset="/images/foam-mattress-3-inch-sm.jpg 720w, /images/foam-mattress-3-inch.jpg 1500w" sizes="(min-width:980px) 33vw, (min-width:680px) 50vw, 100vw" alt="Bunkworks 3 inch high density foam mattress with red, grey and black printed cover and black piped edges" width="1500" height="1125" loading="lazy" decoding="async"></picture></div>
    <div class="card-body"><div><h3>3-inch High Density Foam Mattress</h3><p>Supportive 3-inch (7.5 cm) high density foam mattress with a printed cover and piped edges.</p><span class="card-price">₹1,485</span></div><a class="circle-link" href="#enquire" aria-label="Enquire about the 3 inch high density foam mattress"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M7 17 17 7M9 7h8v8"/></svg></a></div></article>
  </div>
 </div>
</section>

<section class="section engineered" id="process" aria-labelledby="eng-h">
 <div class="wrap eng-grid">
  <div><span class="eyebrow">Built to last</span><h2 id="eng-h">Engineered for everyday use.</h2>
   <p class="lead">Galvanised steel frames, 12mm plywood bases and bolted joints — made to handle real-world use in hostels, PGs and institutions, monsoon after monsoon.</p>
   <div class="features">
    <div class="feature"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M4 12 20 6l8 4-16 6Z"/><path d="M4 12v8l8 4 16-6v-8"/><path d="M12 16v8"/></svg><span>Galvanised anti-rust steel</span></div>
    <div class="feature"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="m4 11 12-5 12 5-12 5Z"/><path d="m4 16 12 5 12-5M4 21l12 5 12-5"/></svg><span>12mm thick plywood base</span></div>
    <div class="feature"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" aria-hidden="true"><path d="M16 3 6 7v8c0 7 4.5 11.5 10 14 5.5-2.5 10-7 10-14V7Z"/></svg><span>Bunk 200 kg total · Single 100 kg</span></div>
    <div class="feature"><svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 9a5 5 0 1 0-6 5l-8 8v4h4l8-8a5 5 0 0 0 5-6l-3 3-3-1-1-3Z"/></svg><span>Bolted, easy to assemble</span></div>
   </div>
  </div>
  <figure class="joint" style="margin:0">{img('bolted-steel-corner-joint-plywood', 'Bolted galvanised steel corner joint of a Bunkworks bunk bed and single cot with 12mm plywood base — rust-resistant hostel furniture', '(min-width:900px) 50vw, 100vw')}
   <figcaption class="joint-note">12mm plywood base<br>Galvanised steel frame</figcaption></figure>
 </div>
</section>

<section class="projects" id="projects" aria-labelledby="proj-h">
 <div class="projects-bg">{img('steel-bed-frames-factory-kerala', 'Stacks of galvanised steel bunk bed and single cot frames with plywood bases ready for a wholesale hostel furniture order, Kerala factory', '100vw')}</div>
 <div class="wrap projects-inner">
  <span class="eyebrow">For hostels, PGs &amp; institutions</span>
  <h2 id="proj-h">Furnishing an entire hostel?</h2>
  <p>From a single PG room to a 200+ bed hostel, Bunkworks supplies coordinated, factory-priced furniture for the whole project.</p>
  <a href="#enquire" class="btn btn-gold">Get a Project Quote {ARROW}</a>
  <div class="pf">
   <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="10" width="18" height="8" rx="1.5"/><path d="M7 10V7a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v3M3 18v2M21 18v2"/></svg><span>Custom configurations</span></div>
   <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" aria-hidden="true"><rect x="1" y="7" width="13" height="9" rx="1"/><path d="M14 10h4l3 3v3h-7Z"/><circle cx="6" cy="18" r="1.7"/><circle cx="17" cy="18" r="1.7"/></svg><span>Wholesale supply, timely delivery</span></div>
   <div><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1 7 17M17 7l2.1-2.1"/></svg><span>Support for institutional projects</span></div>
  </div>
 </div>
</section>

<section class="section" id="collections" aria-labelledby="coll-h">
 <div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Collections</span><h2 id="coll-h">Swadesh and Perunthachan</h2></div><p>Two named lines, built to the same Bunkworks standard.</p></div>
  <div class="coll-grid">
   <div class="coll sw"><svg class="glyph" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="6" y="8" width="30" height="8" rx="1"/><path d="M6 16v18M36 16v18" stroke-dasharray="3 3"/><path d="M2 34h40"/></svg>
    <span class="eyebrow">Swadesh series</span><h3>Rooted in India. Made for every space.</h3>
    <p>Foldable, wall-mounted hostel furniture that folds flat when the room needs space — for PG rooms and shared dorms where every square foot works twice.</p>
    <a href="#enquire" class="btn btn-line-light">Enquire about Swadesh</a></div>
   <div class="coll pe"><svg class="glyph" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M24 4 44 16v18L24 44 4 34V16Z"/><path d="M24 4v40M4 16l40 18M44 16 4 34"/></svg>
    <span class="eyebrow">Perunthachan series</span><h3>Named for the master builder.</h3>
    <p>Perunthachan is Kerala's legendary master carpenter. This line carries heavier-gauge frames and joinery-grade finishing for institutions that want furniture to outlast the building.</p>
    <a href="#enquire" class="btn btn-line-light">Enquire about Perunthachan</a></div>
  </div>
 </div>
</section>

<section class="section" id="guides" aria-labelledby="blog-h" style="padding-top:0">
 <div class="wrap">
  <div class="section-head"><div><span class="eyebrow">Guides</span><h2 id="blog-h">Planning a hostel? Start here.</h2></div>
   <div><p>Prices, sizes, costs and buying advice in English, മലയാളം and हिंदी.</p><a class="link-arrow" href="/blog/">All articles {ARROW}</a></div></div>
  <div class="grid-3">{posts}</div>
 </div>
</section>

<section class="section" id="faq" aria-labelledby="faq-h" style="padding-top:0">
 <div class="wrap">
  <span class="eyebrow">Questions</span><h2 id="faq-h" style="font-size:clamp(1.55rem,3.4vw,2.35rem);margin-bottom:18px">Frequently asked questions</h2>
  <div class="faq">{faq_html(HOME_FAQ)}</div>
 </div>
</section>

<section class="section" id="about" aria-labelledby="about-h" style="padding-top:0">
 <div class="wrap">
  <div class="gstrip">
   <div class="gstrip-copy"><svg class="g" viewBox="0 0 48 48" aria-hidden="true"><path fill="#4285F4" d="M45.1 24.5c0-1.6-.1-3.1-.4-4.6H24v9.1h11.9c-.5 2.8-2.1 5.1-4.4 6.7v5.5h7.1c4.2-3.9 6.5-9.6 6.5-16.7Z"/><path fill="#34A853" d="M24 46c6 0 11-2 14.6-5.3l-7.1-5.5c-2 1.3-4.5 2.1-7.5 2.1-5.8 0-10.7-3.9-12.4-9.1H4.3v5.7C7.9 41.1 15.3 46 24 46Z"/><path fill="#FBBC05" d="M11.6 28.2c-.4-1.3-.7-2.7-.7-4.2s.3-2.9.7-4.2v-5.7H4.3C2.8 17 2 20.4 2 24s.8 7 2.3 9.9Z"/><path fill="#EA4335" d="M24 10.7c3.3 0 6.2 1.1 8.5 3.3l6.3-6.3C34.9 4.2 30 2 24 2 15.3 2 7.9 6.9 4.3 14.1l7.3 5.7c1.7-5.2 6.6-9.1 12.4-9.1Z"/></svg>
    <div><strong id="about-h">Bunkworks Warehouse</strong><span class="sub">Workshop and warehouse in Kerala, India</span></div>
    <a class="link-arrow" style="margin-top:0" href="{GBP}" target="_blank" rel="noopener">Find us on Google {DIAG}</a></div>
   <div class="gstrip-img">{img('steel-single-cot-minimal-room', 'Steel single cot with dark grey epoxy-coated frame in a hostel room — Bunkworks hostel single bed', '(min-width:760px) 45vw, 100vw')}</div>
  </div>
  <div class="about" style="margin-top:34px">
   <p>Bunkworks manufactures galvanised steel bunk beds, single beds and cots at its own workshop in Kerala. Every frame is welded, galvanised and fitted with its plywood base in-house before it is stacked for dispatch.</p>
   <p>We work direct-to-business: wholesale quantities, factory pricing, custom configurations and coordinated delivery for projects from a single PG room to a 200+ bed hostel.</p>
  </div>
 </div>
</section>

<section class="section enquiry" id="enquire" aria-labelledby="enq-h">
 <div class="wrap enq-grid">
  <div><span class="eyebrow">Get a quote</span><h2 id="enq-h">Ready to furnish your hostel?</h2>
   <p>Tell us what you need and where. We will reply with a factory-direct quote, lead time and delivery cost.</p>
   <p>WhatsApp or call <a href="tel:+919072431550" style="color:#fff">+91 90724 31550</a>. Email <a href="mailto:{EMAIL}" style="color:#fff">{EMAIL}</a>.</p>
   <p><a class="btn btn-gold" style="margin-top:6px" href="{WA_BULK}" target="_blank" rel="noopener">Bulk quote on WhatsApp {ARROW}</a></p></div>
  <form class="form" id="quoteForm" action="mailto:{EMAIL}" method="post" enctype="text/plain">
   <div><label for="q-name">Name</label><input id="q-name" name="Name" autocomplete="name" required></div>
   <div><label for="q-org">Hostel / organisation</label><input id="q-org" name="Organisation" autocomplete="organization" required></div>
   <div><label for="q-city">Delivery city</label><input id="q-city" name="City" autocomplete="address-level2" required></div>
   <div><label for="q-units">Number of beds</label><input id="q-units" name="Units" inputmode="numeric" required></div>
   <div class="full"><label for="q-type">Product</label><select id="q-type" name="Product"><option>Bunk beds / double decker cots</option><option>Single beds / single cots</option><option>3 inch foam mattress</option><option>Swadesh series</option><option>Perunthachan series</option><option>A mix — I'll explain below</option></select></div>
   <div class="full"><label for="q-contact">Phone or email</label><input id="q-contact" name="Contact" autocomplete="tel" required></div>
   <div class="full"><label for="q-msg">Anything else</label><textarea id="q-msg" name="Message" placeholder="Sizes, opening date, floor and stairs, mattresses needed"></textarea></div>
   <div class="full pc-ctas"><button type="submit" class="btn btn-gold">Send on WhatsApp {ARROW}</button><button type="button" id="emailBtn" class="btn btn-line-light">Send by email</button></div>
  </form>
 </div>
</section>'''
    website = {"@context": "https://schema.org", "@type": "WebSite", "@id": SITE + "/#website", "name": "Bunkworks", "url": SITE + "/", "inLanguage": ["en", "ml", "hi"], "publisher": {"@id": SITE + "/#org"}}
    return page('/', 'Bunkworks | Hostel Beds | Bunker Cots | Double Decker Beds Factory Sale',
                (f'Up to {OFFER["off_pct"]}% OFF, 5th Anniversary Offer: steel bunker cots (double decker beds) ₹{B}, single cots ₹{S}. Factory sale from Kerala. Bulk discounts {OFFER["bulk_min"]}+.' if ACTIVE else
                 f'Factory-sale hostel beds from Kerala: galvanised steel bunker cots (double decker beds) and single cots. Bulk-order discounts for {OFFER["bulk_min"]}+ pieces, custom sizes.'),
                body, ld=[ORG, website, faq_ld(HOME_FAQ)],
                keywords='bunk bed manufacturer, bunker cot, double decker bed, double decker cot, single cot, hostel beds wholesale, steel cot factory Kerala, hostel furniture')

def blog_index():
    cards = ''.join(post_card(p) for p in POSTS)
    body = f'''
<div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li aria-current="page">Blog</li></ol></nav>
 <header class="page-head"><h1>Guides for hostel and PG owners</h1><p>What it costs to start a hostel, what bunk beds and cots really cost, and how to buy furniture wholesale — in English, മലയാളം and हिंदी.</p></header>
 <div class="chips" role="group" aria-label="Filter by language"><button data-lang="all" aria-pressed="true">All</button><button data-lang="en" aria-pressed="false">English</button><button data-lang="ml" aria-pressed="false" lang="ml">മലയാളം</button><button data-lang="hi" aria-pressed="false" lang="hi">हिंदी</button></div>
 <h2 class="sr-only">All articles</h2><div class="grid-3 post-list" style="padding-bottom:72px">{cards}</div>
</div>'''
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"}]}
    blog = {"@context": "https://schema.org", "@type": "Blog", "name": "Bunkworks Guides", "url": SITE + "/blog/",
            "blogPost": [{"@type": "BlogPosting", "headline": p['title'], "url": f"{SITE}/blog/{p['slug']}/", "inLanguage": p['lang']} for p in POSTS]}
    return page('/blog/', 'Hostel Costs & Bunk Bed Price Guides | Bunkworks',
                'Guides for hostel and PG owners: cost of starting a hostel (English, Malayalam, Hindi), bunk bed and single cot prices, and buying hostel beds wholesale.',
                body, ld=[bc, blog])

def post_page(p):
    u = UI[p['lang']]; path = f"/blog/{p['slug']}/"
    siblings = [q for q in POSTS if p['group'] and q['group'] == p['group']]
    hreflang = ''
    langs = ''
    if siblings:
        hreflang = ''.join(f'<link rel="alternate" hreflang="{q["lang"]}" href="{SITE}/blog/{q["slug"]}/">' for q in siblings)
        hreflang += f'<link rel="alternate" hreflang="x-default" href="{SITE}/blog/{siblings[0]["slug"]}/">'
        langs = '<div class="langs"><span>' + u['read'] + ':</span>' + ''.join(
            f'<a href="/blog/{q["slug"]}/" lang="{q["lang"]}"{" aria-current=\"page\"" if q is p else ""}>{UI[q["lang"]]["chip"]}</a>' for q in siblings) + '</div>'
    related = [q for q in POSTS if q is not p and (q['lang'] == p['lang'] or q['lang'] == 'en') and q not in siblings][:3]
    if len(related) < 3: related += [q for q in POSTS if q is not p and q not in related and q not in siblings][:3 - len(related)]
    rel = ''.join(post_card(q) for q in related)
    body = f'''
<div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/blog/">Blog</a></li><li aria-current="page">{H.escape(short(p))}</li></ol></nav>
 <article>
  <header class="article-head">
   <h1>{H.escape(p['title'])}</h1>
   <div class="article-meta"><span class="pill">{u['chip']}</span><span>{ {'en':'Updated','ml':'പുതുക്കിയത്','hi':'अपडेट'}[p['lang']] } <time datetime="{DATE}">{u['date']}</time></span><span>{p['read']} {u['min']}</span><span>{ {'en':'By the Bunkworks team, Kerala','ml':'Bunkworks ടീം, കേരളം','hi':'Bunkworks टीम, केरल'}[p['lang']] }</span></div>
   {langs}
  </header>
  <figure class="article-hero" style="margin:0">{img(p['thumb'], p['alt'], '(min-width:1000px) 1000px, 100vw', eager=True)}</figure>
  <div class="prose">{p['body']}</div>
  <aside class="cta-box" aria-label="Quote"><p>{u['cta']}</p><a class="btn btn-gold" href="/#enquire">{u['cta_btn']} {ARROW}</a></aside>
  <section class="article-faq" aria-labelledby="faq-{p['slug']}"><h2 id="faq-{p['slug']}">{u['faq']}</h2><div class="faq">{faq_html(p['faqs'])}</div></section>
 </article>
 <section class="section" style="padding-top:30px" aria-labelledby="more-{p['slug']}"><h2 id="more-{p['slug']}" style="font-size:1.4rem;margin-bottom:20px">{u['more']}</h2><div class="grid-3">{rel}</div></section>
</div>'''
    art = {"@context": "https://schema.org", "@type": "BlogPosting", "headline": p['title'], "description": p['desc'], "inLanguage": p['lang'],
           "image": [f"{SITE}/images/{p['thumb']}.jpg"], "datePublished": DATE, "dateModified": DATE,
           "author": {"@type": "Organization", "name": "Bunkworks", "url": SITE + "/"}, "publisher": {"@id": SITE + "/#org"},
           "mainEntityOfPage": SITE + path, "keywords": p['keywords']}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
        {"@type": "ListItem", "position": 3, "name": p['title'], "item": SITE + path}]}
    return page(path, p['seo'] + ' | Bunkworks', p['desc'], body, lang=p['lang'], og_image=f"/images/{p['thumb']}.jpg", og_type='article',
                ld=[ORG, art, bc, faq_ld(p['faqs'])], extra_head=hreflang + f'<meta property="article:published_time" content="{DATE}">', keywords=p['keywords'])


PRODUCTS = {
 'bunker-cot-double-decker-bed': dict(name='Steel Bunk Bed (Bunker Cot / Double Decker Bed)', sku='BW-BUNK', price=OFFER['bunk'], reg=OFFER['bunk_after'], P=B, PR=PB,
   seo=lambda: (f'Steel Bunk Bed Price ₹{B} | Double Decker Cot' if ACTIVE else f'Steel Bunk Bed Price ₹{PB} | Double Decker Cot'),
   desc=lambda: (f'Galvanised steel bunk bed / bunker cot / double decker bed, 12mm plywood decks. 5th Anniversary Offer ₹{B}; regular price ₹{BR} from 16 October 2026. Bulk quote 50+ pcs.' if ACTIVE else
                 f'Galvanised steel bunk bed (bunker cot / double decker bed) with 12mm plywood decks for hostels and PGs. ₹{PB} per piece, factory direct. Bulk quote for {OFFER["bulk_min"]}+ pieces.'),
   h1='Steel bunk bed for hostels — bunker cot / double decker bed',
   intro='A galvanised steel bunk bed with two 12mm plywood decks and an epoxy coating, with a 200 kg weight-bearing capacity and a height of 1.40 m. Built in our Kerala workshop for hostels, PGs and dormitories, it sleeps two people in the floor space of one bed.',
   imgs=[('anniversary-bunk-bed-terracotta-room', 'Bunkworks galvanised steel bunk bed (bunker cot, double decker bed) with 12mm plywood decks, guard rail and ladder handle in a hostel room'),
         ('bunk-bed-studio-cutout', 'Steel bunk bed studio view — hostel double decker cot with plywood decks, bolted joints and anti-skid feet'),
         ('anniversary-bunk-bed-warm-lit-room', 'Heavy-duty steel double decker bed for hostels and PGs — 1.40 m high, 200 kg weight bearing, epoxy coated'),
         ('bolted-steel-corner-joint-plywood', 'Bolted galvanised steel corner joint of the bunk bed frame under the 12mm plywood deck — rust-resistant hostel furniture')],
   facts=[('Also called', 'Bunker cot, double decker bed, double decker cot'), ('Frame', 'Galvanised anti-rust steel'), ('Decks', '12mm thick plywood'),
          ('Height', '1.40 m (140 cm)'), ('Finish', 'Epoxy coating (not powder coating)'), ('Weight bearing', '200 kg'), ('Construction', 'Bolted joints; legs and platforms supplied separately for easy transport'),
          ('Includes', 'Frame, two plywood decks, top guard rail, ladder handle'), ('Mattress', 'Not included'), ('Made in', 'Kerala, India')],
   faqs=lambda: [('What is the price of this bunk bed?', (f'₹{B} per piece in the 5th Anniversary Offer price ₹{B} through {OFFER["end_label"]["en"]}; regular price ₹{BR} from 16 October 2026.' if ACTIVE else f'₹{BR} per piece.') + ' The price is for the frame and plywood decks, without mattresses.'),
                 ('Is a bunker cot the same as a double decker bed?', 'Yes — both names describe this product: two sleeping decks on one steel frame.'),
                 (f'Do you offer bulk pricing?', f'Yes. For more than {OFFER["bulk_min"]} pieces, request a bulk quote with your quantity and delivery city.'),
                 ('How much weight can it take?', 'The bunk bed has a 200 kg weight-bearing capacity.'),
                 ('Will it rust?', 'The frame is galvanised steel with an epoxy coating (not powder coating). Zinc protects the tube inside and out — painted tubes cannot be painted on the inside.')],
   guides=['cheapest-bunk-bed-price-india', 'galvanised-steel-vs-painted-steel-beds', 'bunk-beds-for-adults']),
 'steel-single-cot': dict(name='Steel Single Cot (Hostel Single Bed)', sku='BW-SINGLE', price=OFFER['single'], reg=OFFER['single_after'], P=S, PR=PS,
   seo=lambda: (f'Steel Single Cot Price ₹{S} | Hostel Single Bed' if ACTIVE else f'Steel Single Cot Price ₹{PS} | Hostel Single Bed'),
   desc=lambda: (f'Galvanised steel single cot, 6 × 2.5 ft, 12mm plywood base, 100 kg load. 5th Anniversary Offer ₹{S}; regular price ₹{SR} from 16 October 2026. Bulk quote 50+ pcs.' if ACTIVE else
                 f'Galvanised steel single cot, 6 × 2.5 ft, 12mm plywood base, up to 100 kg. ₹{PS} per piece, factory direct from Kerala; bulk quote for {OFFER["bulk_min"]}+ pieces.'),
   h1='Steel single cot for hostels and PGs',
   intro='A 6 × 2.5 ft galvanised steel single cot, 40 cm high, with a 12mm plywood base and an epoxy coating, rated up to 100 kg. Built for hostels, PGs, dormitories, institutions and homes.',
   imgs=[('anniversary-single-cot-wood-top', 'Bunkworks steel single cot for hostels — wooden plywood top, grey galvanised steel frame, head rail and anti-skid feet'),
         ('bolted-steel-corner-joint-plywood', 'Bolted galvanised steel corner joint under the 12mm plywood base of the steel single cot — 100 kg rated hostel single bed'),
         ('steel-bed-frames-factory-kerala', 'Stack of galvanised steel single cot and bunk bed frames with plywood bases at the Bunkworks factory, Kerala')],
   facts=[('Size (L × W)', '6 × 2.5 ft (183 × 76 cm)'), ('Height', '40 cm'), ('Frame', 'Galvanised anti-rust steel'),
          ('Finish', 'Epoxy coating (not powder coating), grey'), ('Base', '12mm thick plywood'), ('Load capacity', 'Up to 100 kg'),
          ('Feet', 'Anti-skid leg bushes'), ('Mattress', 'Not included'), ('Made in', 'Kerala, India')],
   faqs=lambda: [('What is the price of the steel single cot?', (f'₹{S} per piece in the 5th Anniversary Offer price ₹{S} through {OFFER["end_label"]["en"]}; regular price ₹{SR} from 16 October 2026.' if ACTIVE else f'₹{SR} per piece.') + ' The price is without mattress.'),
                 ('What size is the single cot?', '6 × 2.5 ft (183 × 76 cm), 40 cm high. It fits a standard single mattress.'),
                 ('How much weight can it take?', 'Up to 100 kg.'),
                 ('Do you offer bulk pricing?', f'Yes. For more than {OFFER["bulk_min"]} pieces, request a bulk quote.')],
   guides=['iron-cot-vs-steel-cot-price', 'galvanised-steel-vs-painted-steel-beds', 'steel-single-cot-for-hostel']),
}

def product_page(slug):
    d = PRODUCTS[slug]; path = f'/{slug}/'
    main = img(d['imgs'][0][0], d['imgs'][0][1], '(min-width:900px) 55vw, 100vw', eager=True)
    thumbs = ''.join(f'<figure>{img(k, a, "(min-width:900px) 18vw, 33vw")}</figure>' for k, a in d['imgs'][1:])
    facts = ''.join(f'<dt>{k}</dt><dd>{v}</dd>' for k, v in d['facts'])
    by = {p['slug']: p for p in POSTS}
    guides = ''.join(post_card(by[g]) for g in d['guides'])
    price = swap(f'<span class="blink">₹{d["P"]}</span> <small class="price-regular">regular ₹{d["PR"]} from 16 Oct</small>', f'₹{d["PR"]}')
    body = f"""
<div class="wrap">
 <nav class="crumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/#products">Products</a></li><li aria-current="page">{H.escape(d['name'])}</li></ol></nav>
 <div class="prod-grid">
  <div class="gallery"><div class="main">{main}</div><div class="thumbs">{thumbs}</div></div>
  <div class="prod-info">
   <span class="tag" data-offer-only>5th Anniversary Offer</span>
   <h1 style="margin-top:12px">{H.escape(d['h1'])}</h1>
   <p style="margin-top:12px;color:var(--muted)">{d['intro']}</p>
   <p class="big-price">{price}</p><p class="per">per piece, without mattress{swap(f" — 5th Anniversary Offer, limited pieces", "")}</p>
   <dl class="keyfacts">{facts}</dl>
   <div class="pc-ctas"><a class="btn btn-gold" href="{wa(f"Hi Bunkworks, I want to order: {d['name']} at ₹{d['P'] if ACTIVE else d['PR']}. Quantity: , Delivery city: ")}" target="_blank" rel="noopener">Order on WhatsApp {ARROW}</a><a class="btn btn-line" href="{MAIL_BULK}">Email us</a></div>
   <p class="fine"><strong>More than {OFFER['bulk_min']} pieces?</strong> <a href="{WA_BULK}" target="_blank" rel="noopener">Get a bulk quote on WhatsApp</a> or email <a href="{MAIL_BULK}">{EMAIL}</a>. {swap(f"Limited pieces at the anniversary price; regular price ₹{d['PR']} from 16 October 2026.", "")}</p>
  </div>
 </div>
 <section class="article-faq" aria-labelledby="pfaq"><h2 id="pfaq">Frequently asked questions</h2><div class="faq">{faq_html(d['faqs']())}</div></section>
 <section class="section" style="padding-top:30px" aria-labelledby="pg"><h2 id="pg" style="font-size:1.4rem;margin-bottom:20px">Buying guides</h2><div class="grid-3">{guides}</div></section>
</div>"""
    offer = {"@type": "Offer", "url": SITE + path, "priceCurrency": "INR", "price": str(d['price'] if ACTIVE else d['reg']),
             "availability": "https://schema.org/InStock", "itemCondition": "https://schema.org/NewCondition", "seller": {"@id": SITE + "/#org"}}
    if ACTIVE and OFFER['end']:
        offer["priceValidUntil"] = OFFER['end']
    prod = {"@context": "https://schema.org", "@type": "Product", "name": d['name'], "sku": d['sku'], "description": d['intro'],
            "image": [f"{SITE}/images/{k}.jpg" for k, _ in d['imgs']], "brand": {"@type": "Brand", "name": "Bunkworks"}, "category": "Hostel furniture",
            "material": "Galvanised steel, plywood", "offers": offer}
    bc = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}, {"@type": "ListItem", "position": 2, "name": d['name'], "item": SITE + path}]}
    return page(path, d['seo']() + ' | Bunkworks', d['desc'](), body, og_image=f"/images/{d['imgs'][0][0]}.jpg", ld=[ORG, prod, bc, faq_ld(d['faqs']())],
                keywords='bunk bed price, bunker cot price, double decker cot price, steel cot price, single cot price, hostel bed wholesale')

def not_found():
    body = '<div class="wrap nf"><h1>Page not found</h1><p>The page you were looking for has moved or never existed. Try the products or the guides instead.</p><a class="btn btn-gold" href="/">Go to the homepage ' + ARROW + '</a> &nbsp; <a class="btn btn-line" href="/blog/">Read the guides</a></div>'
    return page('/404.html', 'Page not found | Bunkworks', 'This page could not be found.', body, robots='noindex, follow')

def w(path, s):
    full = OUT + path; os.makedirs(os.path.dirname(full), exist_ok=True); open(full, 'w', encoding='utf-8').write(s)

exec(compile(open('/home/claude/site_extra.py', encoding='utf-8').read(), 'site_extra.py', 'exec'), globals())
