from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
BUILD = ROOT / "source" / "build_site.py"

OLD_GBP = "https://share.google/gJ9QIqYunFs6Jm2MU"
NEW_GBP = "https://share.google/lSNdgoG97YMX7hqwc"

ADDRESS_OLD = '{"@type": "PostalAddress", "addressRegion": "Kerala", "addressCountry": "IN"}'
ADDRESS_NEW = '{"@type": "PostalAddress", "streetAddress": "First Floor, SRA-53, Shanthinagar Rd", "addressLocality": "Chakkarapparambu, Vennala", "addressRegion": "Kerala", "postalCode": "682028", "addressCountry": "IN"}'

for path in DEPLOY.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    original = text
    text = text.replace(OLD_GBP, NEW_GBP)
    text = text.replace(ADDRESS_OLD, ADDRESS_NEW)
    if text != original:
        path.write_text(text, encoding="utf-8")

# Keep the source generator aligned so future generated pages retain the verified entity.
if BUILD.exists():
    text = BUILD.read_text(encoding="utf-8")
    original = text
    text = text.replace("GBP = 'https://share.google/gJ9QIqYunFs6Jm2MU'", "GBP = 'https://share.google/lSNdgoG97YMX7hqwc'")
    if text != original:
        BUILD.write_text(text, encoding="utf-8")

# Update the repository-level LLM reference file if it exists.
for path in [ROOT / "llms.txt", ROOT / "llms-full.txt", DEPLOY / "llms.txt", DEPLOY / "llms-full.txt"]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        original = text
        text = text.replace(OLD_GBP, NEW_GBP)
        if "First Floor, SRA-53, Shanthinagar Rd" not in text and "Bunkworks Warehouse" in text:
            text = text.replace("Bunkworks Warehouse", "Bunkworks Warehouse\nFirst Floor, SRA-53, Shanthinagar Rd, Chakkarapparambu, Vennala, Kochi, Ernakulam, Kerala 682028, India", 1)
        if text != original:
            path.write_text(text, encoding="utf-8")
