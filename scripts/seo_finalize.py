from pathlib import Path
import re
import json

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
SITE = "https://www.bunkworks.com"

ADDRESS = {
    "@type": "PostalAddress",
    "streetAddress": "First Floor, SRA-53, Shanthinagar Rd",
    "addressLocality": "Chakkarapparambu, Vennala",
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
DESCRIPTION = "Bunkworks manufactures steel hostel beds, bunk beds, bunker cots and single cots in Kerala. Factory-direct supply for hostels, PGs, dormitories and institutions, with bulk orders and custom sizes."


def strip_keywords(html: str) -> str:
    return re.sub(r"\s*<meta\s+name=[\"']keywords[\"'][^>]*>", "", html, flags=re.I)


def replace_first(pattern: str, replacement: str, text: str, flags=re.I | re.S):
    return re.sub(pattern, replacement, text, count=1, flags=flags)


def replace_meta_content(html: str, attr: str, value: str) -> str:
    pattern = rf'(<meta\s+{attr}\s*=\s*["\'][^"\']+["\'][^>]*content\s*=\s*["\'])[^"\']*(["\'])'
    return re.sub(pattern, lambda m: m.group(1) + value.replace('"', '&quot;') + m.group(2), html, count=1, flags=re.I)


def homepage_metadata(html: str) -> str:
    html = replace_first(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
    html = replace_first(
        r"<meta\s+name=[\"']description[\"'][^>]*>",
        f'<meta name="description" content="{DESCRIPTION}">',
        html,
    )
    # Keep social previews aligned with the canonical page identity.
    html = replace_first(r'(<meta\s+property=["\']og:title["\'][^>]*content=["\'])[^"\']*(["\'])', lambda m: m.group(1) + TITLE + m.group(2), html)
    html = replace_first(r'(<meta\s+property=["\']og:description["\'][^>]*content=["\'])[^"\']*(["\'])', lambda m: m.group(1) + DESCRIPTION + m.group(2), html)
    html = replace_first(r'(<meta\s+name=["\']twitter:title["\'][^>]*content=["\'])[^"\']*(["\'])', lambda m: m.group(1) + TITLE + m.group(2), html)
    html = replace_first(r'(<meta\s+name=["\']twitter:description["\'][^>]*content=["\'])[^"\']*(["\'])', lambda m: m.group(1) + DESCRIPTION + m.group(2), html)
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
'''            html = re.sub(r"(<main[^>]*>)", r"\1" + section, html, count=1, flags=re.I)
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
