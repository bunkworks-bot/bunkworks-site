# -*- coding: utf-8 -*-
"""Final content architecture pass for Bunkworks.
Runs after the site generator and before SEO validation.
Creates the Hostel Furniture and Bulk Hostel Furniture hubs, adds Kerala-wide
coverage messaging, strengthens product-page AEO content, and updates the sitemap.
"""
from pathlib import Path
import re
from html import escape

OUT = Path(__file__).resolve().parents[1] / "deploy"
SITE = "https://www.bunkworks.com"

DISTRICTS = [
    "Thiruvananthapuram", "Kollam", "Pathanamthitta", "Alappuzha", "Kottayam",
    "Idukki", "Ernakulam", "Thrissur", "Palakkad", "Malappuram", "Kozhikode",
    "Wayanad", "Kannur", "Kasaragod"
]

COVERAGE = """
<section class="section" id="delivery-across-kerala">
  <div class="wrap">
    <div class="section-head">
      <div><span class="eyebrow">Kerala delivery</span><h2>Hostel furniture delivery across Kerala</h2></div>
      <p>Bunkworks is based in Kochi, Ernakulam and accepts enquiries for hostel beds and furniture deliveries across Kerala. Freight and delivery arrangements vary by quantity and destination and are confirmed with the quotation.</p>
    </div>
    <div class="chips" aria-label="Kerala delivery districts">
      %s
    </div>
  </div>
</section>
""" % "".join(f'<span class="chip">{escape(d)}</span>' for d in DISTRICTS)

HUB = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Hostel Furniture Manufacturer in Kerala | Bunkworks</title>
<meta name="description" content="Bunkworks manufactures hostel beds and institutional furniture from Kochi, Kerala, with delivery enquiries across all 14 Kerala districts and bulk procurement support.">
<link rel="canonical" href="https://www.bunkworks.com/hostel-furniture/">
<meta property="og:title" content="Hostel Furniture Manufacturer in Kerala | Bunkworks"><meta property="og:description" content="Hostel beds, bunker cots and institutional furniture from Bunkworks in Kochi, with Kerala-wide delivery enquiries."><meta property="og:type" content="website"><meta property="og:url" content="https://www.bunkworks.com/hostel-furniture/">
<link rel="stylesheet" href="/assets/site.css">
</head><body>
<header class="nav"><div class="nav-inner"><a class="brand" href="/"><img src="/images/logo.png" alt="Bunkworks" width="180" height="48"></a><div class="nav-right"><a class="btn btn-gold" href="/bulk-quote/">Get a Bulk Quote</a></div></div></header>
<main>
<section class="section"><div class="wrap"><span class="eyebrow">Hostel furniture</span><h1>Hostel Furniture Manufacturer in Kerala</h1><span class="gold-rule"></span><p style="max-width:760px;margin-top:20px;color:var(--muted);font-size:1.05rem">Bunkworks manufactures hostel beds and related institutional furniture from Kochi, Ernakulam. The range is designed for hostels, PG accommodation, student housing, dormitories and other high-use spaces, with bulk-order enquiries and delivery arrangements across Kerala.</p>
<div class="grid-3" style="margin-top:36px">
<article class="card"><div class="card-body"><div><h3>Hostel Beds – Kerala</h3><p>Explore the core hostel-bed range and procurement information.</p></div><a class="circle-link" href="/hostel-beds-kerala/" aria-label="Hostel beds in Kerala">→</a></div></article>
<article class="card"><div class="card-body"><div><h3>Bunker Cot / Double-Decker Bed</h3><p>Steel bunk beds for space-efficient hostel and dormitory layouts.</p></div><a class="circle-link" href="/bunker-cot-double-decker-bed/" aria-label="Bunker cot">→</a></div></article>
<article class="card"><div class="card-body"><div><h3>Steel Single Cot</h3><p>Single hostel cots for rooms, institutions and accommodation projects.</p></div><a class="circle-link" href="/steel-single-cot/" aria-label="Steel single cot">→</a></div></article>
</div></div></section>
%s
<section class="section engineered"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Procurement</span><h2>Planning a hostel or institutional project?</h2></div><p>For larger quantities, share your bed count, destination and required products so Bunkworks can prepare a project-specific quotation.</p></div><a class="btn btn-gold" href="/bulk-hostel-furniture/">Bulk hostel furniture</a> <a class="btn btn-line" href="/bulk-quote/">Request a quote</a></div></section>
</main></body></html>
""" % COVERAGE

BULK = """<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bulk Hostel Furniture Supplier in Kerala | Bunkworks</title>
<meta name="description" content="Bulk hostel furniture procurement from Bunkworks in Kochi: bunker cots, steel single cots and institutional furniture for hostels, PGs, dormitories and accommodation projects across Kerala.">
<link rel="canonical" href="https://www.bunkworks.com/bulk-hostel-furniture/">
<meta property="og:title" content="Bulk Hostel Furniture Supplier in Kerala | Bunkworks"><meta property="og:description" content="Bulk bunker cots, steel single cots and hostel furniture for institutional projects across Kerala."><meta property="og:type" content="website"><meta property="og:url" content="https://www.bunkworks.com/bulk-hostel-furniture/">
<link rel="stylesheet" href="/assets/site.css">
</head><body>
<header class="nav"><div class="nav-inner"><a class="brand" href="/"><img src="/images/logo.png" alt="Bunkworks" width="180" height="48"></a><div class="nav-right"><a class="btn btn-gold" href="/bulk-quote/">Request a Quote</a></div></div></header>
<main><section class="section"><div class="wrap"><span class="eyebrow">Bulk procurement</span><h1>Bulk Hostel Furniture Supply in Kerala</h1><span class="gold-rule"></span><p style="max-width:760px;margin-top:20px;color:var(--muted);font-size:1.05rem">Bunkworks supports bulk enquiries for hostel and institutional furniture from its Kochi, Ernakulam base. Tell us the quantity, product mix, destination and target delivery schedule and we can discuss the appropriate supply arrangement.</p>
<div class="grid-3" style="margin-top:36px"><article class="card"><div class="card-body"><div><h3>Bunker Cots</h3><p>Double-decker steel beds for space-efficient accommodation.</p></div><a class="circle-link" href="/bunker-cot-double-decker-bed/">→</a></div></article><article class="card"><div class="card-body"><div><h3>Steel Single Cots</h3><p>Single beds for hostels and institutional rooms.</p></div><a class="circle-link" href="/steel-single-cot/">→</a></div></article><article class="card"><div class="card-body"><div><h3>Hostel Furniture</h3><p>Start with the wider product and delivery overview.</p></div><a class="circle-link" href="/hostel-furniture/">→</a></div></article></div></div></section>
<section class="section"><div class="wrap"><span class="eyebrow">How to enquire</span><h2>What to include in a bulk request</h2><ul style="max-width:760px;margin-top:18px"><li>Approximate number of beds or furniture units</li><li>Products required and any known dimensions/specifications</li><li>Delivery district and site location</li><li>Preferred delivery window</li><li>Whether you need one product or a mixed furniture order</li></ul><a class="btn btn-gold" style="margin-top:24px" href="/bulk-quote/">Send a bulk enquiry</a></div></section>
%s
<section class="section engineered"><div class="wrap"><h2>Frequently asked questions</h2><div style="display:grid;gap:18px;margin-top:26px;max-width:820px"><details><summary><strong>Can Bunkworks supply large hostel orders?</strong></summary><p style="margin-top:8px">Yes, Bunkworks accepts bulk enquiries. Final quantities, production and delivery arrangements are confirmed through the quotation.</p></details><details><summary><strong>Where does Bunkworks deliver in Kerala?</strong></summary><p style="margin-top:8px">Bunkworks is based in Kochi, Ernakulam and accepts delivery enquiries across all 14 Kerala districts. Freight and delivery arrangements depend on quantity and destination.</p></details><details><summary><strong>What should I send for a quotation?</strong></summary><p style="margin-top:8px">Send the product, approximate quantity, destination and preferred timeline. Adding drawings or specifications is useful when you need a custom requirement.</p></details></div></div></section>
</main></body></html>
""" % COVERAGE

FAQ_PRODUCT = {
    "bunker-cot-double-decker-bed": """
<section class="section engineered" id="product-faq"><div class="wrap"><span class="eyebrow">Buying guide</span><h2>Bunker cot questions</h2><div style="display:grid;gap:18px;margin-top:24px;max-width:820px"><details><summary><strong>What is the current bunker cot price?</strong></summary><p style="margin-top:8px">The Bunkworks anniversary offer is ₹5,999 through October 15, 2026. The regular price is ₹6,499 from October 16, 2026.</p></details><details><summary><strong>Is the bunker cot suitable for hostels?</strong></summary><p style="margin-top:8px">The double-decker format is designed for space-efficient accommodation such as hostels, dormitories and PG rooms. Confirm the room and ceiling dimensions before ordering.</p></details><details><summary><strong>Does Bunkworks deliver bunker cots across Kerala?</strong></summary><p style="margin-top:8px">Bunkworks is based in Kochi, Ernakulam and accepts delivery enquiries across Kerala. Freight and delivery arrangements depend on order quantity and destination.</p></details><details><summary><strong>Can I request a bulk order?</strong></summary><p style="margin-top:8px">Yes. Use the bulk quote page and include your quantity, destination and preferred delivery window.</p></details></div><p style="margin-top:22px"><a class="link-arrow" href="/bulk-hostel-furniture/">View bulk hostel furniture procurement →</a></p></div></section>
""",
    "steel-single-cot": """
<section class="section engineered" id="product-faq"><div class="wrap"><span class="eyebrow">Buying guide</span><h2>Steel single cot questions</h2><div style="display:grid;gap:18px;margin-top:24px;max-width:820px"><details><summary><strong>What is the current single cot price?</strong></summary><p style="margin-top:8px">The Bunkworks anniversary offer is ₹3,299 through October 15, 2026. The regular price is ₹3,499 from October 16, 2026.</p></details><details><summary><strong>Where can the single cot be used?</strong></summary><p style="margin-top:8px">It is positioned for hostel, PG, dormitory and institutional accommodation where a single sleeping berth is required.</p></details><details><summary><strong>Does Bunkworks deliver single cots across Kerala?</strong></summary><p style="margin-top:8px">Bunkworks is based in Kochi, Ernakulam and accepts delivery enquiries across Kerala. Freight and delivery arrangements depend on quantity and destination.</p></details><details><summary><strong>Can I order single cots in bulk?</strong></summary><p style="margin-top:8px">Yes. Use the bulk quote page and include the quantity, destination and preferred delivery window.</p></details></div><p style="margin-top:22px"><a class="link-arrow" href="/bulk-hostel-furniture/">View bulk hostel furniture procurement →</a></p></div></section>
"""
}

def write_page(path, content):
    p = OUT / path / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")

def inject_before_main_end(html, block):
    if block.strip() in html:
        return html
    return html.replace("</main>", block + "\n</main>", 1)

def add_schema(html, schema):
    if 'application/ld+json' in html and schema.get('@type') in html:
        return html
    tag = '<script type="application/ld+json">' + __import__('json').dumps(schema, ensure_ascii=False) + '</script>'
    return html.replace('</head>', tag + '</head>', 1)

write_page("hostel-furniture", HUB)
write_page("bulk-hostel-furniture", BULK)

# Strengthen existing pages without replacing their generated design/content.
for slug, faq in FAQ_PRODUCT.items():
    p = OUT / slug / "index.html"
    if p.exists():
        html = p.read_text(encoding="utf-8")
        html = inject_before_main_end(html, COVERAGE + faq)
        html = html.replace('href="/bulk-quote/"', 'href="/bulk-quote/"')
        p.write_text(html, encoding="utf-8")

# Add coverage + hub links to the main Kerala authority page.
p = OUT / "hostel-beds-kerala" / "index.html"
if p.exists():
    html = p.read_text(encoding="utf-8")
    block = COVERAGE + '''<section class="section"><div class="wrap"><span class="eyebrow">Explore</span><h2>Hostel furniture and bulk procurement</h2><p style="max-width:720px;margin-top:14px;color:var(--muted)">For a wider view of the range, visit the hostel furniture hub or send a bulk procurement enquiry.</p><p style="margin-top:20px"><a class="btn btn-gold" href="/hostel-furniture/">Hostel furniture</a> <a class="btn btn-line" href="/bulk-hostel-furniture/">Bulk procurement</a></p></div></section>'''
    html = inject_before_main_end(html, block)
    p.write_text(html, encoding="utf-8")

# Add a concise coverage block to the homepage if it does not already have one.
p = OUT / "index.html"
if p.exists():
    html = p.read_text(encoding="utf-8")
    home = COVERAGE.replace('<section class="section" id="delivery-across-kerala">', '<section class="section" id="delivery-across-kerala">')
    html = inject_before_main_end(html, home + '''<section class="section"><div class="wrap"><span class="eyebrow">Hostel furniture</span><h2>Explore the Bunkworks range</h2><p style="max-width:700px;margin-top:14px;color:var(--muted)">See the complete hostel furniture category or go directly to bulk procurement for larger projects.</p><p style="margin-top:20px"><a class="btn btn-gold" href="/hostel-furniture/">Hostel furniture</a> <a class="btn btn-line" href="/bulk-hostel-furniture/">Bulk hostel furniture</a></p></div></section>''')
    p.write_text(html, encoding="utf-8")

# Ensure the new URLs are discoverable in the sitemap.
sitemap = OUT / "sitemap.xml"
if sitemap.exists():
    s = sitemap.read_text(encoding="utf-8")
    additions = [
        "https://www.bunkworks.com/hostel-furniture/",
        "https://www.bunkworks.com/bulk-hostel-furniture/",
    ]
    for url in additions:
        if url not in s:
            s = s.replace('</urlset>', f'<url><loc>{url}</loc></url>\n</urlset>')
    sitemap.write_text(s, encoding="utf-8")

# Machine-readable entity/category signals for the two new hubs.
for slug, page_type, name, desc in [
    ("hostel-furniture", "CollectionPage", "Bunkworks Hostel Furniture", "Hostel beds and institutional furniture supplied from Kochi, Kerala."),
    ("bulk-hostel-furniture", "CollectionPage", "Bunkworks Bulk Hostel Furniture", "Bulk hostel furniture procurement from Kochi, Kerala with delivery enquiries across Kerala."),
]:
    p = OUT / slug / "index.html"
    html = p.read_text(encoding="utf-8")
    schema = {"@context":"https://schema.org","@type":page_type,"name":name,"description":desc,"url":f"{SITE}/{slug}/","isPartOf":{"@type":"WebSite","name":"Bunkworks","url":SITE},"about":{"@type":"Thing","name":"Hostel furniture"}}
    html = add_schema(html, schema)
    p.write_text(html, encoding="utf-8")

print("Content authority finalization complete")
print("Added hostel-furniture and bulk-hostel-furniture hubs, Kerala coverage, product FAQs, internal links and sitemap entries.")
