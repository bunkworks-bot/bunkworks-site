from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"

checks = []

index = (DEPLOY / "index.html").read_text(encoding="utf-8")
robots = (DEPLOY / "robots.txt").read_text(encoding="utf-8")
sitemap = (DEPLOY / "sitemap.xml").read_text(encoding="utf-8")
kerala_sitemap = DEPLOY / "sitemap-kerala.xml"

checks.append(("homepage title", "Bunkworks | Hostel Beds &amp; Bunk Beds Manufacturer in Kerala" in index))
checks.append(("homepage description", "Bunkworks manufactures steel hostel beds" in index))
checks.append(("no meta keywords", not re.search(r'<meta\s+name=["\']keywords["\']', index, re.I)))
checks.append(("local business schema", '"@id": "https://www.bunkworks.com/#localbusiness"' in index))
checks.append(("verified address", "682028" in index and "Chakkarapparambu, Vennala" in index))
checks.append(("robots sitemap", "Sitemap: https://www.bunkworks.com/sitemap.xml" in robots))
checks.append(("Kerala sitemap reference", "Sitemap: https://www.bunkworks.com/sitemap-kerala.xml" in robots))
checks.append(("main sitemap exists", "<urlset" in sitemap and "www.bunkworks.com" in sitemap))
checks.append(("Kerala sitemap exists", kerala_sitemap.exists()))
checks.append(("llms.txt exists", (DEPLOY / "llms.txt").exists()))
checks.append(("llms-full.txt exists", (DEPLOY / "llms-full.txt").exists()))

failed = [name for name, ok in checks if not ok]
for name, ok in checks:
    print(("PASS" if ok else "FAIL") + ": " + name)

if failed:
    raise SystemExit("SEO validation failed: " + ", ".join(failed))

print(f"SEO validation passed: {len(checks)} checks.")
