from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
SITE = "https://www.bunkworks.com"

checks = []

index = (DEPLOY / "index.html").read_text(encoding="utf-8")
robots = (DEPLOY / "robots.txt").read_text(encoding="utf-8")
sitemap = (DEPLOY / "sitemap.xml").read_text(encoding="utf-8")
kerala_sitemap = DEPLOY / "sitemap-kerala.xml"

# Finalizer runs immediately before this validator, so these checks describe
# the actual production files that Netlify is about to publish.
checks.append(("homepage title", "<title>Bunkworks | Hostel Beds & Bunk Beds Manufacturer in Kerala</title>" in index or "<title>Bunkworks | Hostel Beds &amp; Bunk Beds Manufacturer in Kerala</title>" in index))
checks.append(("homepage description", "Bunkworks manufactures steel hostel beds" in index))
checks.append(("no meta keywords", not re.search(r'<meta\s+name=["\']keywords["\']', index, re.I)))
checks.append(("canonical homepage", '<link rel="canonical" href="https://www.bunkworks.com/">' in index))
checks.append(("local business schema", '"@id": "https://www.bunkworks.com/#localbusiness"' in index))
checks.append(("verified address", "682028" in index and "Chakkarapparambu, Vennala" in index))
checks.append(("business phone", "+91 90724 31550" in index or "+91-9072431550" in index))
checks.append(("robots sitemap", "Sitemap: https://www.bunkworks.com/sitemap.xml" in robots))
checks.append(("Kerala sitemap reference", "Sitemap: https://www.bunkworks.com/sitemap-kerala.xml" in robots))
checks.append(("main sitemap exists", "<urlset" in sitemap and "www.bunkworks.com" in sitemap))
checks.append(("Kerala sitemap exists", kerala_sitemap.exists()))
checks.append(("llms.txt exists", (DEPLOY / "llms.txt").exists()))
checks.append(("llms-full.txt exists", (DEPLOY / "llms-full.txt").exists()))
checks.append(("redirects file exists", (DEPLOY / "_redirects").exists()))
checks.append(("security headers file exists", (DEPLOY / "_headers").exists()))

# Every production HTML page must have the basic indexable metadata pattern.
html_files = list(DEPLOY.rglob("*.html"))
checks.append(("production HTML exists", bool(html_files)))
for path in html_files:
    html = path.read_text(encoding="utf-8")
    checks.append((f"metadata: {path.relative_to(DEPLOY)}", bool(re.search(r"<title>[^<]+</title>", html, re.I) and re.search(r'<meta\s+name=["\']description["\'][^>]*>', html, re.I)))
    checks.append((f"no keywords: {path.relative_to(DEPLOY)}", not re.search(r'<meta\s+name=["\']keywords["\']', html, re.I)))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(("PASS" if ok else "FAIL") + ": " + name)

if failed:
    raise SystemExit("SEO validation failed: " + ", ".join(failed))

print(f"SEO validation passed: {len(checks)} checks.")
