from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
SITE = "https://www.bunkworks.com"

ADDRESS = {
    "@type": "PostalAddress",
    "streetAddress": "First Floor, SRA-53, Shanthinagar Rd",
    "addressLocality": "Chakkarapparambu, Vennela",
    "addressRegion": "Kerala",
    "postalCode": "682028",
    "addressCountry": "IN",
}

LOCAL_ENTITY = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "@id": f"{SITE}/#localbusiness",
    "name": "Bunkworks",
    "description": "Bunkworks is a furniture manufacturer in Kochi, Kerala, specialising in steel hostel beds, bunker cots, double-decker beds and steel single cots for hostels, PGs, dormitories and institutions.",
    "url": f"{SITE}/",
    "logo": f"{SITE}/images/bunkworks-logo.png",
    "image": f"{SITE}/og-image.jpg",
    "telephone": "+91 90724 31550",
    "address": ADDRESS,
    "areaServed": [
        {"@type": "City", "name": "Kochi"},
        {"@type": "AdministrativeArea", "name": "Ernakulam"},
        {"@type": "State", "name": "Kerala"},
        {"@type": "Country", "name": "India"},
    ],
    "knowsAbout": [
        "hostel beds",
        "bunk beds",
        "bunker cots",
        "double-decker beds",
        "steel single cots",
        "hostel furniture",
        "institutional furniture",
        "bulk hostel furniture supply",
    ],
}

TITLE = "Bunkworks | Hostel Beds & Bunk Beds Manufacturer in Kerala"
DESCRIPTION = "Bunkworks manufactures steel hostel beds, bunk beds, bunker cots and single cots in Kerala. Factory-direct for hostels, PGs and institutions. Bulk orders welcome."

ANSWER_SUMMARY_STYLE = """
.answer-summary{padding:42px 0 28px;background:var(--cream)}
.answer-summary-inner{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:28px 24px}
.answer-summary-copy{max-width:760px}
.answer-summary-copy h2{font-size:clamp(1.5rem,3vw,2.15rem)}
.answer-summary-copy p{margin-top:10px;color:var(--muted);max-width:70ch}
.answer-summary-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));margin-top:24px;border-top:1px solid var(--line);border-left:1px solid var(--line)}
.answer-summary-grid div{padding:14px 15px;border-right:1px solid var(--line);border-bottom:1px solid var(--line);display:grid;gap:3px}
.answer-summary-grid strong{font-size:.78rem;text-transform:uppercase;letter-spacing:.08em;color:var(--gold-deep)}
.answer-summary-grid span{font-size:.9rem;color:var(--muted)}
.answer-address{margin-top:18px;font-size:.84rem;color:var(--muted)}
.price-regular{display:inline-block;font:600 .78rem/1.2 'Inter',sans-serif;color:var(--muted);margin-left:8px;vertical-align:middle}
@media(min-width:760px){.answer-summary-inner{padding:34px}.answer-summary-grid{grid-template-columns:repeat(4,minmax(0,1fr))}}
@media(max-width:560px){.answer-summary-inner{padding:22px 18px}.price-regular{display:block;margin:6px 0 0}}
"""

def strip_keywords(html: str) -> str:
    return re.sub(r"\s*<meta\s+name=[\"']keywords[\"'][^>]*>", "", html, flags=re.I)


def replace_first(pattern: str, replacement: str, text: str, flags=re.I | re.S):
    return re.sub(pattern, replacement, text, count=1, flags=flags)


def homepage_metadata(html: str) -> str:
    html = replace_first(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
    html = replace_first(
        r"<meta\s+name=[\"']description[\"'][^>]*>",
        f'<meta name="description" content="{DESCRIPTION}">',
        html,
    )
    html = replace_first(r'(<meta\s+property=[\"\']og:title[\"\'][^>]*content=[\"\'])[^\"\']*([\"\'])', lambda m: m.group(1) + TITLE + m.group(2), html)
    html = replace_first(r'(<meta\s+property=[\"\']og:description[\"\'][^>]*content=[\"\'])[^\"\']*([\"\'])', lambda m: m.group(1) + DESCRIPTION + m.group(2), html)
    html = replace_first(r'(<meta\s+name=[\"\']twitter:title[\"\'][^>]*content=[\"\'])[^\"\']*([\"\'])', lambda m: m.group(1) + TITLE + m.group(2), html)
    html = replace_first(r'(<meta\s+name=[\"\']twitter:description[\"\'][^>]*content=[\"\'])[^\"\']*([\"\'])', lambda m: m.group(1) + DESCRIPTION + m.group(2), html)
    style = f'<style id="answer-summary-style">{ANSWER_SUMMARY_STYLE}</style>'
    if 'id="answer-summary-style"' not in html:
        html = html.replace("</head>", style + "</head>", 1)
    return html


def inject_local_schema(html: str) -> str:
    marker = '"@id": "https://www.bunkworks.com/#localbusiness"'
    if marker in html:
        return html
    block = '<script type="application/ld+json">\n' + json.dumps(LOCAL_ENTITY, ensure_ascii=False, indent=2) + '\n</script>\n'
    if "</head>" in html:
        return html.replace("</head>", block + "</head>", 1)
    return html


def inject_answer_summary(html: str) -> str:
    if 'id="answer-summary"' in html:
        return html
    section = '''
<section id="answer-summary" class="section answer-summary" aria-labelledby="answer-summary-title">
  <div class="wrap">
    <div class="answer-summary-inner">
      <div class="answer-summary-copy">
        <span class="eyebrow">At a glance</span>
        <h2 id="answer-summary-title">Hostel furniture from Kochi, Kerala</h2>
        <p>Bunkworks manufactures steel hostel beds, bunk beds, bunker cots, double-decker beds and steel single cots for hostels, PGs, dormitories and institutions.</p>
      </div>
      <div class="answer-summary-grid" aria-label="Bunkworks key facts">
        <div><strong>Based in</strong><span>Kochi, Ernakulam, Kerala</span></div>
        <div><strong>Delivery</strong><span>Enquiries across all 14 Kerala districts</span></div>
        <div><strong>Orders</strong><span>Single units, bulk and custom-size enquiries</span></div>
        <div><strong>Call / WhatsApp</strong><span>+91 90724 31550</span></div>
      </div>
      <p class="answer-address"><strong>Business address:</strong> First Floor, SRA-53, Shanthinagar Rd, Chakkarapparambu, Vennala, Kochi, Ernakulam, Kerala 682028, India.</p>
    </div>
  </div>
</section>
'''
    pattern = r'(<section class="ann"[^>]*>.*?</section>)'
    if re.search(pattern, html, flags=re.I | re.S):
        return re.sub(pattern, lambda m: m.group(1) + section, html, count=1, flags=re.I | re.S)
    return html.replace("<main", "<main", 1)



SHIP_NOTE = '<p class="ship-note">Shipping charges apply. This product is non-returnable.</p>'
POLICY_RETURN = {"@type": "MerchantReturnPolicy", "applicableCountry": "IN", "returnPolicyCategory": "https://schema.org/MerchantReturnNotPermitted"}
POLICY_SHIP = {"@type": "OfferShippingDetails", "shippingLabel": "Shipping charges apply", "shippingDestination": {"@type": "DefinedRegion", "addressCountry": "IN"}}


def commerce_policies(html: str, path: Path) -> str:
    """Shipping charges apply + non-returnable: structured data and visible notes (idempotent)."""
    def fix_ld(m):
        raw = m.group(2)
        if '"Product"' not in raw:
            return m.group(0)
        try:
            d = json.loads(raw)
        except ValueError:
            return m.group(0)
        if not isinstance(d, dict) or d.get("@type") != "Product":
            return m.group(0)
        offers = d.get("offers")
        for o in (offers if isinstance(offers, list) else [offers]):
            if isinstance(o, dict):
                o.setdefault("shippingDetails", POLICY_SHIP)
                o.setdefault("hasMerchantReturnPolicy", POLICY_RETURN)
        return m.group(1) + json.dumps(d, ensure_ascii=False) + m.group(3)
    html = re.sub(r'(<script type="application/ld\+json">)(.*?)(</script>)', fix_ld, html, flags=re.S)
    rel = path.relative_to(DEPLOY).as_posix()
    if rel in ("bunker-cot-double-decker-bed/index.html", "steel-single-cot/index.html"):
        html = re.sub(r'(<p class="per">(?:(?!</p>).)*</p>)(?!<p class="ship-note">)', lambda m: m.group(1) + SHIP_NOTE, html, flags=re.S)
        html = re.sub(r'(?:<p class="ship-note">[^<]*</p>){2,}', SHIP_NOTE, html)
    if rel == "index.html":
        def card(m):
            c = m.group(0)
            if "card-price" not in c or "ship-note" in c:
                return c
            return c.replace('</div><a class="circle-link"', '<span class="ship-note">Shipping charges apply · Non-returnable</span></div><a class="circle-link"', 1)
        html = re.sub(r'<article class="card".*?</article>', card, html, flags=re.S)
    if 'id="offerPop"' in html and 'class="pop-fine"' not in html:
        html = html.replace('<p class="pop-limited">', '<p class="pop-fine">Shipping charges apply · Non-returnable product</p><p class="pop-limited">', 1)
    if rel == "shipping-delivery/index.html" and "non-returnable" not in html.lower():
        html = html.replace("<h2>Questions?</h2>", '<p><strong>Shipping charges apply</strong> to all orders and are stated in your quote. <strong>Products are non-returnable</strong> once delivered, so please check the packages on arrival and report any visible damage or missing parts immediately.</p><h2>Questions?</h2>', 1)
    if rel == "terms/index.html" and "non-returnable" not in html.lower():
        html = html.replace("See our <a href=\"/shipping-delivery/\">shipping and delivery</a> page.</p>", "See our <a href=\"/shipping-delivery/\">shipping and delivery</a> page.</p><p>Shipping charges apply to all orders. Products are non-returnable once delivered, other than as required by applicable consumer-protection law; please report visible damage or missing parts on delivery.</p>", 1)
    return html

def process_html(path: Path):
    html = path.read_text(encoding="utf-8")
    original = html
    html = strip_keywords(html)
    html = commerce_policies(html, path)
    if path == DEPLOY / "index.html":
        html = homepage_metadata(html)
        html = inject_local_schema(html)
        html = inject_answer_summary(html)
    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def write_robots():
    p = DEPLOY / "robots.txt"
    text = p.read_text(encoding="utf-8") if p.exists() else "User-agent: *\nAllow: /\n"
    line = "Sitemap: https://www.bunkworks.com/sitemap-kerala.xml"
    if line not in text:
        if not text.endswith("\n"):
            text += "\n"
        text += line + "\n"
        p.write_text(text, encoding="utf-8")


def main():
    if not DEPLOY.exists():
        raise SystemExit("deploy/ directory not found")
    changed = 0
    for path in DEPLOY.rglob("*.html"):
        if process_html(path):
            changed += 1
    write_robots()
    print(f"SEO finalization complete: {changed} HTML files updated.")


if __name__ == "__main__":
    main()
