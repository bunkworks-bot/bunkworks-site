from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
SITE = "https://www.bunkworks.com"

checks = []
index = (DEPLOY / "index.html").read_text(encoding="utf-8")
robots = (DEPLOY / "robots.txt").read_text(encoding="utf-8")
sitemap = (DEPLOY / "sitemap.xml").read_text(encoding="utf-8")
kerala_sitemap = DEPLOY / "sitemap-kerala.xml"

ann_start = index.find('<section class="ann"')
ann_end = index.find('</section>', ann_start) if ann_start >= 0 else -1
summary_pos = index.find('id="answer-summary"')

checks += [
    ("answer summary present", summary_pos >= 0),
    ("answer summary below hero", ann_end >= 0 and summary_pos > ann_end),
    ("anniversary bunker price", "₹5,999" in index),
    ("anniversary single price", "₹3,299" in index),
    ("regular bunker price", "₹6,499" in index),
    ("regular single price", "₹3,499" in index),
    ("offer ends October 15", "October 15, 2026" in index or "15 October 2026" in index),
    ("no stale MRP", "MRP" not in index and "₹10,999" not in index and "₹5,500" not in index),
    ("homepage title", "<title>Bunkworks | Hostel Beds & Bunk Beds Manufacturer in Kerala</title>" in index or "<title>Bunkworks | Hostel Beds &amp; Bunk Beds Manufacturer in Kerala</title>" in index),
    ("homepage description", "Bunkworks manufactures steel hostel beds" in index),
    ("no meta keywords", not re.search(r'<meta\s+name=["\']keywords["\']', index, re.I)),
    ("canonical homepage", '<link rel="canonical" href="https://www.bunkworks.com/">' in index),
    ("local business schema", '"@id": "https://www.bunkworks.com/#localbusiness"' in index),
    ("business phone", "+91 90724 31550" in index or "+91-9072431550" in index),
    ("robots sitemap", "Sitemap: https://www.bunkworks.com/sitemap.xml" in robots),
    ("Kerala sitemap reference", "Sitemap: https://www.bunkworks.com/sitemap-kerala.xml" in robots),
    ("main sitemap exists", "<urlset" in sitemap and "www.bunkworks.com" in sitemap),
    ("Kerala sitemap exists", kerala_sitemap.exists()),
    ("llms.txt exists", (DEPLOY / "llms.txt").exists()),
    ("llms-full.txt exists", (DEPLOY / "llms-full.txt").exists()),
    ("redirects file exists", (DEPLOY / "_redirects").exists()),
    ("security headers file exists", (DEPLOY / "_headers").exists()),
]

# Validate the LocalBusiness address from its structured-data fields rather than
# requiring one exact concatenated address string. Locality may be represented by
# the neighbourhood/locality or the city name while the street, state and PIN
# provide the stronger location checks.
def extract_localbusiness_jsonld(html):
    for raw in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.I | re.S):
        try:
            data = json.loads(raw.strip())
        except json.JSONDecodeError:
            continue
        nodes = data if isinstance(data, list) else data.get("@graph", [data]) if isinstance(data, dict) else []
        if isinstance(nodes, dict):
            nodes = [nodes]
        for node in nodes:
            if isinstance(node, dict) and node.get("@id") == f"{SITE}/#localbusiness":
                return node
    return None

localbusiness = extract_localbusiness_jsonld(index)
address = localbusiness.get("address", {}) if localbusiness else {}
locality = str(address.get("addressLocality", "")).strip()
locality_ok = bool(locality) and any(term in locality.lower() for term in ("kochi", "chakkarapparambu", "vennela"))
checks.extend([
    ("localbusiness structured data parsed", localbusiness is not None),
    ("verified street address", address.get("streetAddress") == "First Floor, SRA-53, Shanthinagar Rd"),
    ("verified locality", locality_ok),
    ("verified region", address.get("addressRegion") == "Kerala"),
    ("verified postal code", address.get("postalCode") == "682028"),
    ("verified country", address.get("addressCountry") == "IN"),
])

# New content architecture must be present in the final build.
for slug in ("hostel-furniture", "bulk-hostel-furniture"):
    p = DEPLOY / slug / "index.html"
    checks.append((f"new page exists: {slug}", p.exists()))
    if p.exists():
        html = p.read_text(encoding="utf-8")
        checks.append((f"canonical: {slug}", f'<link rel="canonical" href="{SITE}/{slug}/">' in html))
        checks.append((f"collection schema: {slug}", '"@type": "CollectionPage"' in html))
        checks.append((f"kerala coverage: {slug}", "Thiruvananthapuram" in html and "Kasaragod" in html and "Kochi, Ernakulam" in html))
        checks.append((f"bulk quote link: {slug}", "/bulk-quote/" in html))

# Every production HTML page must have basic indexable metadata.
html_files = list(DEPLOY.rglob("*.html"))
checks.append(("production HTML exists", bool(html_files)))
for path in html_files:
    html = path.read_text(encoding="utf-8")
    checks.append((f"metadata: {path.relative_to(DEPLOY)}", bool(re.search(r"<title>[^<]+</title>", html, re.I) and re.search(r'<meta\s+name=["\']description["\'][^>]*>', html, re.I))))
    checks.append((f"no keywords: {path.relative_to(DEPLOY)}", not re.search(r'<meta\s+name=["\']keywords["\']', html, re.I)))

checks.append(("hostel furniture in sitemap", "https://www.bunkworks.com/hostel-furniture/" in sitemap or not (DEPLOY / "hostel-furniture" / "index.html").exists()))
checks.append(("bulk hostel furniture in sitemap", "https://www.bunkworks.com/bulk-hostel-furniture/" in sitemap or not (DEPLOY / "bulk-hostel-furniture" / "index.html").exists()))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(("PASS" if ok else "FAIL") + ": " + name)
if failed:
    raise SystemExit("SEO validation failed: " + ", ".join(failed))
print(f"SEO validation passed: {len(checks)} checks.")
