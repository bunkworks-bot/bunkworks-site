from datetime import date
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DEPLOY = ROOT / "deploy"
CAMPAIGN_END = date(2026, 10, 15)


def replace_price(html: str, old: str, new: str) -> str:
    return html.replace(old, new)


def remove_expired_offer_schema(html: str) -> str:
    html = re.sub(r',\s*"priceValidUntil":\s*"2026-10-15"', '', html)
    html = re.sub(r',\s*"priceSpecification":\s*\[\s*\{"@type":\s*"UnitPriceSpecification",\s*"price":\s*"(?:5999|6499|3300|3299|3499)"[^\]]*\},\s*\{"@type":\s*"UnitPriceSpecification",\s*"priceType":\s*"https://schema.org/StrikethroughPrice"[^\]]*\}\s*\]', '', html)
    return html


def process(path: Path, campaign_active: bool) -> bool:
    html = path.read_text(encoding="utf-8")
    original = html

    if campaign_active:
        # Bunker cot: ₹5,999 through 15 Oct 2026; regular price ₹6,499 from 16 Oct.
        # Single cot: ₹3,299 through 15 Oct 2026; regular price ₹3,499 from 16 Oct.
        html = replace_price(html, "₹3,300", "₹3,299")
        html = replace_price(html, '"price": "3300"', '"price": "3299"')
        html = replace_price(html, '"price": "5999"', '"price": "5999"')
        html = replace_price(html, "2026-10-05", "2026-10-15")
        html = replace_price(html, "5 October 2026", "15 October 2026")
        html = replace_price(html, "until 5 October 2026", "until 15 October 2026")
        html = replace_price(html, "until 5 October 2026 or while stock lasts", "until 15 October 2026 or while stock lasts")
        html = replace_price(html, "Single cot <b class=\"blink\">₹3,300</b>", "Single cot <b class=\"blink\">₹3,299</b>")
    else:
        # After the anniversary campaign, automatically switch all public pricing
        # to the permanent offer price and remove expired offer markup.
        html = replace_price(html, "₹5,999", "₹6,499")
        html = replace_price(html, "₹3,300", "₹3,499")
        html = replace_price(html, "₹3,299", "₹3,499")
        html = replace_price(html, '"price": "5999"', '"price": "6499"')
        html = replace_price(html, '"price": "3300"', '"price": "3499"')
        html = replace_price(html, '"price": "3299"', '"price": "3499"')
        html = re.sub(r"\s*<s>₹(?:9,999|6,499)</s>", "", html)
        html = re.sub(r"\s*<s>₹(?:5,500|3,499)</s>", "", html)
        html = html.replace("5th Anniversary Offer", "Bunkworks Price")
        html = html.replace("the anniversary price of ₹5,999", "")
        html = html.replace("the anniversary price of ₹3,299", "")
        html = html.replace("until 15 October 2026 or while stock lasts", "")
        html = html.replace("until 15 October 2026", "")
        html = remove_expired_offer_schema(html)

    if html != original:
        path.write_text(html, encoding="utf-8")
        return True
    return False


def main():
    if not DEPLOY.exists():
        raise SystemExit("deploy/ directory not found")
    today = date.today()
    campaign_active = today <= CAMPAIGN_END
    changed = 0
    for path in DEPLOY.rglob("*.html"):
        if process(path, campaign_active):
            changed += 1
    print(f"Pricing finalization complete: {changed} HTML files updated; campaign_active={campaign_active}; campaign_end={CAMPAIGN_END.isoformat()}")


if __name__ == "__main__":
    main()
