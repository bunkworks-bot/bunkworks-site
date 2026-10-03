from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
BUILD = ROOT / "source" / "build_site.py"

NEW_GBP = "https://share.google/lSNdgoG97YMX7hqwc"
ADDRESS_NEW = '{"@type": "PostalAddress", "streetAddress": "First Floor, SRA-53, Shanthinagar Rd", "addressLocality": "Chakkarapparambu, Vennala", "addressRegion": "Kerala", "postalCode": "682028", "addressCountry": "IN"}'

changed = 0
for path in DEPLOY.rglob("*.html"):
    text = path.read_text(encoding="utf-8")
    original = text
    text = re.sub(r"https://share\.google/[^\"']+", NEW_GBP, text)
    text = re.sub(r'"address"\s*:\s*\{\s*"@type"\s*:\s*"PostalAddress"\s*,\s*"addressRegion"\s*:\s*"Kerala"\s*,\s*"addressCountry"\s*:\s*"IN"\s*\}', '"address": ' + ADDRESS_NEW, text)
    if text != original:
        path.write_text(text, encoding="utf-8")
        changed += 1

if BUILD.exists():
    text = BUILD.read_text(encoding="utf-8")
    original = text
    text = re.sub(r"GBP\s*=\s*['\"]https://share\.google/[^'\"]+['\"]", "GBP = '" + NEW_GBP + "'", text)
    if text != original:
        BUILD.write_text(text, encoding="utf-8")
        changed += 1

for path in [ROOT / "llms.txt", ROOT / "llms-full.txt", DEPLOY / "llms.txt", DEPLOY / "llms-full.txt"]:
    if path.exists():
        text = path.read_text(encoding="utf-8")
        original = text
        text = re.sub(r"https://share\.google/\S+", NEW_GBP, text)
        if "First Floor, SRA-53, Shanthinagar Rd" not in text and "Bunkworks Warehouse" in text:
            text = text.replace("Bunkworks Warehouse", "Bunkworks Warehouse\nFirst Floor, SRA-53, Shanthinagar Rd, Chakkarapparambu, Vennala, Kochi, Ernakulam, Kerala 682028, India", 1)
        if text != original:
            path.write_text(text, encoding="utf-8")
            changed += 1

print(f"Changed {changed} files")
