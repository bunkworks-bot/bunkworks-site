# Bunkworks website — Netlify deploy
1. Netlify > Add new site > Deploy manually > drag the **deploy** folder (its contents, with _redirects, _headers and index.html at the top level).
2. Domains: set www.bunkworks.com as PRIMARY, add bunkworks.com as an alias (the _redirects file forces https + www).
3. Google Search Console: verify the domain (DNS TXT record) and submit https://www.bunkworks.com/sitemap.xml

## Offer timer (already set)
- Ends 5 Oct 2026, 23:59 IST (one week from 28 Sep 2026). Fixed date, not a per-visitor reset.
- When it ends, visitors' pages switch automatically to Rs 6,500 (bunker cot) and Rs 3,500 (single cot) and the offer bar, pop-up and hero prices disappear.
- The search-result title/description are static: after 5 Oct, ask for a rebuild so the description drops the discount wording (the homepage title stays the same).
- To change dates/prices: edit OFFER at the top of source/content2.py (end, bunk, bunk_reg, bunk_after, single, single_reg, single_after) and rebuild.

## Load rating
Bunker cot: 200 kg total = 100 kg per deck. Single cot: 100 kg. Applied on every page, schema, llms files and the A3 spec sheets.

## Before / after go-live
- Have the Privacy, Terms and Shipping pages reviewed by a lawyer.
- Keep the struck-through MRPs (9,999 / 5,500) real and defensible, and keep "limited pieces left" true.
