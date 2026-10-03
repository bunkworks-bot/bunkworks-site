from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
SITE = "https://www.bunkworks.com"

PAGE = '''<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hostel Furniture Manufacturer in Kerala | Bunkworks</title>
<meta name="description" content="Bunkworks manufactures steel hostel furniture in Kerala, including bunker cots, double-decker beds and single cots for hostels, PGs, dormitories and institutions.">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://www.bunkworks.com/hostel-furniture/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Bunkworks">
<meta property="og:title" content="Hostel Furniture Manufacturer in Kerala | Bunkworks">
<meta property="og:description" content="Steel hostel furniture from Bunkworks: bunker cots, double-decker beds and single cots for hostels, PGs, dormitories and institutions.">
<meta property="og:url" content="https://www.bunkworks.com/hostel-furniture/">
<meta property="og:image" content="https://www.bunkworks.com/images/anniversary-bunk-bed-terracotta-room.jpg">
<link rel="stylesheet" href="/assets/site.css">
<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@graph":[
    {"@type":"WebPage","@id":"https://www.bunkworks.com/hostel-furniture/#webpage","url":"https://www.bunkworks.com/hostel-furniture/","name":"Hostel Furniture Manufacturer in Kerala | Bunkworks","inLanguage":"en-IN","about":{"@id":"https://www.bunkworks.com/#localbusiness"}},
    {"@type":"CollectionPage","@id":"https://www.bunkworks.com/hostel-furniture/#collection","url":"https://www.bunkworks.com/hostel-furniture/","name":"Bunkworks Hostel Furniture","isPartOf":{"@id":"https://www.bunkworks.com/hostel-furniture/#webpage"},"mainEntity":{"@type":"ItemList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Bunker Cot / Double-Decker Bed","url":"https://www.bunkworks.com/bunker-cot-double-decker-bed/"},
      {"@type":"ListItem","position":2,"name":"Steel Single Cot","url":"https://www.bunkworks.com/steel-single-cot/"},
      {"@type":"ListItem","position":3,"name":"Hostel Beds in Kerala","url":"https://www.bunkworks.com/hostel-beds-kerala/"}
    ]}},
    {"@type":"BreadcrumbList","@id":"https://www.bunkworks.com/hostel-furniture/#breadcrumb","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":"https://www.bunkworks.com/"},
      {"@type":"ListItem","position":2,"name":"Hostel Furniture","item":"https://www.bunkworks.com/hostel-furniture/"}
    ]}
  ]
}
</script>
</head>
<body>
<header class="nav"><div class="nav-inner">
<a href="/" class="brand"><img src="/images/bunkworks-logo.png" alt="Bunkworks — steel hostel furniture manufacturer in Kerala" width="720" height="181"></a>
<nav aria-label="Main"><ul class="nav-links"><li><a href="/hostel-furniture/" aria-current="page">Hostel Furniture</a></li><li><a href="/bunker-cot-double-decker-bed/">Bunker Cots</a></li><li><a href="/steel-single-cot/">Single Cots</a></li><li><a href="/hostel-beds-kerala/">Kerala Hostel Beds</a></li><li><a href="/bulk-quote/">Bulk Quote</a></li><li><a href="/blog/">Guides</a></li><li><a href="/about/">About</a></li><li><a href="/contact/">Contact</a></li></ul></nav>
</div></header>
<main id="main">
<div class="wrap">
<nav aria-label="Breadcrumb"><a href="/">Home</a> / Hostel Furniture</nav>
<h1>Hostel Furniture Manufacturer in Kerala</h1>
<p><strong>Bunkworks is a furniture manufacturer based in Kochi, Kerala.</strong> The company supplies steel hostel furniture for student hostels, working-professional PGs, dormitories, staff accommodation and institutional projects.</p>
<h2>Hostel furniture from Bunkworks</h2>
<p>The current product range focuses on high-use steel sleeping furniture. Product specifications, pricing and availability are listed on the individual product pages.</p>
<section aria-labelledby="products"><h2 id="products">Hostel bed products</h2>
<h3><a href="/bunker-cot-double-decker-bed/">Bunker Cot / Double-Decker Bed</a></h3>
<p>A two-level steel bed designed for space-efficient hostel and dormitory accommodation. See dimensions, materials, load information, current offer and FAQs on the product page.</p>
<h3><a href="/steel-single-cot/">Steel Single Cot</a></h3>
<p>A steel single bed for hostel rooms, PGs and institutional accommodation. See specifications, current offer and FAQs on the product page.</p>
<h3><a href="/hostel-beds-kerala/">Hostel Beds in Kerala</a></h3>
<p>Our Kerala-focused category page explains the product range, bulk supply process and service-area considerations for hostel projects.</p>
</section>
<section aria-labelledby="bulk"><h2 id="bulk">Bulk hostel furniture supply</h2><p>For project enquiries, send the quantity, preferred mix of bunker cots and single cots, required dimensions, delivery city and target date.</p><p><a href="/bulk-quote/">Request a bulk quotation →</a></p></section>
<section aria-labelledby="location"><h2 id="location">Based in Kochi, serving Kerala and beyond</h2><p>Bunkworks is based at First Floor, SRA-53, Shanthinagar Rd, Chakkarapparambu, Vennala, Kochi, Ernakulam, Kerala 682028, India. Delivery availability, freight and lead time are confirmed for the project destination and quantity.</p></section>
</div>
</main>
<footer><div class="wrap"><p><strong>Bunkworks</strong> — Furniture for spaces that work. Kerala, India.</p><p><a href="/hostel-furniture/">Hostel Furniture</a> · <a href="/hostel-beds-kerala/">Hostel Beds Kerala</a> · <a href="/bulk-quote/">Bulk Quote</a> · <a href="/contact/">Contact</a></p></div></footer>
</body>
</html>
'''


def ensure_category_page():
    out = DEPLOY / "hostel-furniture" / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(PAGE, encoding="utf-8")


def add_nav_links(path: Path):
    html = path.read_text(encoding="utf-8")
    if "/hostel-furniture/" in html or path == DEPLOY / "hostel-furniture" / "index.html":
        return
    original = html
    # Add a single contextual category link to the primary navigation where the existing list is present.
    html = html.replace('<li><a href="/bunker-cot-double-decker-bed/">Bunker Cots</a></li>', '<li><a href="/hostel-furniture/">Hostel Furniture</a></li><li><a href="/bunker-cot-double-decker-bed/">Bunker Cots</a></li>', 1)
    if html != original:
        path.write_text(html, encoding="utf-8")


def ensure_sitemap():
    p = DEPLOY / "sitemap.xml"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    url = f"{SITE}/hostel-furniture/"
    if url in text:
        return
    loc = f"  <url><loc>{url}</loc></url>\n"
    text = text.replace("</urlset>", loc + "</urlset>", 1)
    p.write_text(text, encoding="utf-8")


def main():
    ensure_category_page()
    for path in DEPLOY.rglob("*.html"):
        add_nav_links(path)
    ensure_sitemap()
    print("Structure finalization complete: hostel-furniture category and contextual navigation enabled.")


if __name__ == "__main__":
    main()
