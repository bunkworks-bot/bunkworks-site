from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"

for path in DEPLOY.rglob("*.html"):
    html = path.read_text(encoding="utf-8")
    updated = html.replace("40% off the MRP of ₹5,500", "special 5th Anniversary Offer price")
    if updated != html:
        path.write_text(updated, encoding="utf-8")

print("Pricing copy finalization complete.")
