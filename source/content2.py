# -*- coding: utf-8 -*-
import re, html as H, datetime
from urllib.parse import quote as _q
WA_NUM = '919072431550'; EMAIL = 'bunkworksindia@gmail.com'
WA_BULK = f'https://wa.me/{WA_NUM}?text=' + _q("Hi Bunkworks, I'd like a bulk quote for more than 50 pieces. Product: , Quantity: , Delivery city: ")
MAIL_BULK = f'mailto:{EMAIL}?subject=' + _q('Bulk quote request')
from content import POSTS as BASE, UI, inr

# ---------------- OFFER CONFIG (edit and rebuild) ----------------
# 5th Anniversary Offer. `bunk_reg` / `single_reg` are the regular prices shown for comparison.
# The regular prices are the owner-specified post-offer prices: ₹6,499 for the bunker cot and ₹3,499 for the single cot.
# end=None means no end date (offer runs while stock lasts). Set end='YYYY-MM-DD' to auto-hide the offer after that day
# (then also decide what price the site should show afterwards).
import os
# Fixed anniversary offer with a real end date (the countdown timer counts down to 23:59:59 IST on this date).
# bunk_after / single_after = the selling price the site shows once the offer has ended (owner instruction: prices become 6,499 / 3,499 from 16 October 2026).
OFFER = dict(end=os.environ.get('BW_END', '2026-10-15'), bunk=5999, bunk_reg=6499, single=3299, single_reg=3499, bunk_after=6499, single_after=3499, bulk_min=50,
             end_label={'en': '115 October 2026', 'ml': '2026 ഒക്ടോബർ 15', 'hi': '115 अक्टूबर 2026'})
OFFER['off_pct'] = round(100 * (1 - OFFER['bunk'] / OFFER['bunk_reg']))
ACTIVE = True if OFFER['end'] is None else datetime.date.today() <= datetime.date.fromisoformat(OFFER['end'])
BX_ = None
B, BR, S, SR = inr(OFFER['bunk']), inr(OFFER['bunk_reg']), inr(OFFER['single']), inr(OFFER['single_reg'])
PB, PS = inr(OFFER['bunk_after']), inr(OFFER['single_after'])
BX, SX = (B, S) if ACTIVE else (PB, PS)


def swap(now, after, tag='span', cls=''):
    """Offer text now; JS swaps to `after` once the offer date passes. When the offer is off at build time, `after` is rendered."""
    c = f' class="{cls}"' if cls else ''
    if not ACTIVE: return f'<{tag}{c}>{after}</{tag}>'
    return f'<{tag}{c} data-after="{H.escape(after)}">{now}</{tag}>'

BOX = {
 'en': dict(h=f'5th Anniversary Offer — up to {OFFER["off_pct"]}% off, limited pieces', bunk='Steel bunk bed / bunker cot / double decker bed', single='Steel single cot',
            per='per piece', reg='regular', bulk=f'Ordering more than {OFFER["bulk_min"]} pieces? Ask for a bulk quote.', btn='Get bulk quote',
            note=f'Prices per piece, without mattress. Limited pieces at these prices (regular prices ₹{BR} and ₹{SR}; regular prices apply from 16 October 2026).', h_after='Current factory prices'),
 'ml': dict(h=f'വാർഷിക ഓഫർ — {OFFER["off_pct"]}% വരെ കിഴിവ്, പരിമിതമായ എണ്ണം മാത്രം', bunk='സ്റ്റീൽ ബങ്ക് ബെഡ് / ബങ്കർ കോട്ട് / ഡബിൾ ഡെക്കർ കട്ടിൽ', single='സ്റ്റീൽ സിംഗിൾ കട്ടിൽ',
            per='ഒരെണ്ണത്തിന്', reg='സാധാരണ വില', bulk=f'{OFFER["bulk_min"]}-ൽ കൂടുതൽ എണ്ണം വേണോ? ബൾക്ക് ക്വട്ടേഷൻ ചോദിക്കൂ.', btn='ബൾക്ക് ക്വട്ടേഷൻ',
            note=f'വില ഒരെണ്ണത്തിന്, മെത്ത ഇല്ലാതെ. ഈ വിലയിൽ പരിമിതമായ എണ്ണം മാത്രം (regular prices ₹{BR}, ₹{SR}; regular prices apply from 16 October 2026).', h_after='ഇപ്പോഴത്തെ ഫാക്ടറി വില'),
 'hi': dict(h=f'वर्षगांठ ऑफ़र — {OFFER["off_pct"]}% तक की छूट, सीमित पीस', bunk='स्टील बंक बेड / बंकर कॉट / डबल डेकर बेड', single='स्टील सिंगल कॉट',
            per='प्रति पीस', reg='सामान्य कीमत', bulk=f'{OFFER["bulk_min"]} से ज़्यादा पीस चाहिए? बल्क कोटेशन माँगें।', btn='बल्क कोटेशन',
            note=f'कीमत प्रति पीस, बिना गद्दे के। इस कीमत पर सीमित पीस ही उपलब्ध हैं (regular price ₹{BR} और ₹{SR})।', h_after='मौजूदा फ़ैक्टरी कीमत'),
}

def offer_box(lang):
    t = BOX[lang]
    row = lambda name, p, r, a: (f'<li><span>{name}</span>' + swap(f'<strong class="blink">₹{p}</strong> <s>₹{r}</s> <small>{t["per"]}</small>', f'<strong>₹{a}</strong> <small>{t["per"]}</small>', 'span', 'price') + '</li>')
    return (f'<aside class="offer-box" aria-label="Price">' + swap(t['h'], t['h_after'], 'p', 'offer-h') +
            f'<ul>{row(t["bunk"], B, BR, PB)}{row(t["single"], S, SR, PS)}</ul>'
            f'<p class="offer-bulk">{t["bulk"]} <a href="{WA_BULK}" target="_blank" rel="noopener">{t["btn"]} (WhatsApp) →</a> <a href="{MAIL_BULK}">{EMAIL}</a></p>' +
            swap(t['note'], '', 'p', 'offer-note') + '</aside>')

def quick(lang, text):
    lab = {'en': 'Quick answer', 'ml': 'ചുരുക്കത്തിൽ ഉത്തരം', 'hi': 'संक्षिप्त उत्तर'}[lang]
    return f'<div class="quick"><p class="quick-label">{lab}</p><p>{text}</p></div>'

TEN = {'en': (f'At the Bunkworks 5th Anniversary Offer price of ₹{B}, 10 bunk beds (20 sleepers) cost ₹{inr(OFFER["bunk"]*10)} — below the low end of the table above.',
              f'At the Bunkworks price of ₹{PB}, 10 bunk beds (20 sleepers) cost ₹{inr(OFFER["bunk_after"]*10)}.'),
       'ml': (f'Bunkworks വാർഷിക ഓഫർ വിലയായ ₹{B} പ്രകാരം 10 ബങ്ക് ബെഡ്ഡുകൾക്ക് (20 പേർക്ക്) ₹{inr(OFFER["bunk"]*10)} മാത്രം.',
              f'Bunkworks വിലയായ ₹{PB} പ്രകാരം 10 ബങ്ക് ബെഡ്ഡുകൾക്ക് (20 പേർക്ക്) ₹{inr(OFFER["bunk_after"]*10)}.'),
       'hi': (f'Bunkworks की वर्षगांठ ऑफ़र कीमत ₹{B} पर 10 बंक बेड (20 लोगों के लिए) सिर्फ़ ₹{inr(OFFER["bunk"]*10)} में।',
              f'Bunkworks की कीमत ₹{PB} पर 10 बंक बेड (20 लोगों के लिए) ₹{inr(OFFER["bunk_after"]*10)} में।')}

# ---------------- upgrade existing posts ----------------
UPG = {
 'hostel-setup-cost-india': dict(seo='Hostel Setup Cost in India (2026): 20-Bed Budget', short='Cost to start a hostel',
   quick='A 20-bed hostel or PG in India typically needs about ₹3.8–13.8 lakh in setup costs in 2026, excluding the rental deposit and working capital. Furniture and renovation are the largest costs you control, and bunk beds cut the furniture cost per bed.'),
 'hostel-setup-cost-malayalam': dict(seo='ഹോസ്റ്റൽ തുടങ്ങാൻ ചെലവ് എത്ര? 2026 ബജറ്റ്', short='ഹോസ്റ്റൽ ചെലവ് (മലയാളം)',
   quick='20 കിടക്കകളുള്ള ഹോസ്റ്റലോ പിജിയോ തുടങ്ങാൻ 2026-ൽ ഏകദേശം ₹3.8–13.8 ലക്ഷം വേണം (വാടക ഡെപ്പോസിറ്റും പ്രവർത്തന മൂലധനവും ഒഴികെ). ഫർണിച്ചറും നവീകരണവുമാണ് നിയന്ത്രിക്കാവുന്ന ഏറ്റവും വലിയ ചെലവുകൾ.'),
 'hostel-setup-cost-hindi': dict(seo='हॉस्टल शुरू करने का खर्च 2026: पूरा बजट', short='हॉस्टल खर्च (हिंदी)',
   quick='20 बेड वाला हॉस्टल या पीजी शुरू करने में 2026 में लगभग ₹3.8–13.8 लाख का सेटअप खर्च आता है (किराए की डिपॉज़िट और वर्किंग कैपिटल छोड़कर)। फ़र्नीचर और मरम्मत सबसे बड़े खर्च हैं जिन्हें आप नियंत्रित कर सकते हैं।'),
 'bunk-bed-bunker-cot-price-guide': dict(seo='Bunker Cot & Double Decker Bed Price Guide 2026', short='Bunk bed price guide',
   quick=f'Bunk bed, bunker cot and double decker bed are the same product: two sleeping decks on one frame. Steel hostel bunk beds commonly cost ₹7,000–₹15,000 per unit in 2026; the Bunkworks galvanised bunk bed is ' + swap(f'₹{B} on the 5th Anniversary Offer (MRP ₹{BR})', f'₹{PB}') + '.'),
 'steel-single-cot-for-hostel': dict(seo='Steel Single Cot Size & Price for Hostels (2026)', short='Steel single cot guide',
   quick=f'The standard single cot size in India is 6 × 2.5 ft (183 × 76 cm) or 6 × 3 ft (183 × 91 cm). Steel single cots for hostels commonly cost ₹3,500–₹8,000; the Bunkworks steel single cot is ' + swap(f'₹{S} on the 5th Anniversary Offer (regular price ₹{SR})', f'₹{PS}') + '.'),
 'hostel-beds-wholesale-factory-price': dict(seo='Hostel Beds Wholesale: Factory Price & Bulk Deals', short='Buying beds wholesale',
   quick=f'Buying hostel beds direct from the factory removes dealer margin and gets you consistent batches. Per-piece prices fall with volume; at Bunkworks, orders of more than {OFFER["bulk_min"]} pieces get a separate bulk quote.'),
}
for p in BASE:
    u = UPG[p['slug']]; p.update(seo=u['seo'], short=u['short'])
    body = p['body']
    body = re.sub(r'(<p class="lede">.*?</p>)', lambda m: quick(p['lang'], u['quick']) + m.group(1), body, count=1, flags=re.S)
    if p['group'] == 'hostel-cost':
        body = re.sub(r'(<p class="note">.*?</p>)', lambda m: m.group(1) + '<p>' + swap(*TEN[p['lang']]) + '</p>', body, count=1, flags=re.S)
    if p['slug'] in ('bunk-bed-bunker-cot-price-guide', 'steel-single-cot-for-hostel', 'hostel-beds-wholesale-factory-price') or p['group'] == 'hostel-cost':
        body = re.sub(r'(<p class="lede">.*?</p>)', lambda m: m.group(1) + offer_box(p['lang']), body, count=1, flags=re.S)
    p['body'] = body

# ---------------- new posts (topics from Google India autocomplete) ----------------
NEW = []

def price_table(lang):
    L = {'en': (('Bunk bed type', 'Typical 2026 price per unit'),
                [('Light painted steel (thin tubes, sheet or strip base)', 'roughly ₹5,000–₹7,000'),
                 ('Standard steel hostel bunk bed', 'roughly ₹7,000–₹10,000'),
                 ('Heavy-duty or galvanised steel', 'roughly ₹9,000–₹15,000'),
                 ('Wooden bunk bed', 'varies widely, usually higher')], 'Bunkworks galvanised steel bunk bed'),
         'ml': (('ബങ്ക് ബെഡ് തരം', '2026-ലെ ഏകദേശ വില (ഒരെണ്ണം)'),
                [('കനം കുറഞ്ഞ പെയിന്റ് ചെയ്ത സ്റ്റീൽ', 'ഏകദേശം ₹5,000–₹7,000'),
                 ('സാധാരണ സ്റ്റീൽ ഹോസ്റ്റൽ ബങ്ക് ബെഡ്', 'ഏകദേശം ₹7,000–₹10,000'),
                 ('ഹെവി-ഡ്യൂട്ടി / ഗാൽവനൈസ്ഡ് സ്റ്റീൽ', 'ഏകദേശം ₹9,000–₹15,000'),
                 ('മരം കൊണ്ടുള്ള ബങ്ക് ബെഡ്', 'വ്യത്യാസപ്പെടും, സാധാരണ കൂടുതൽ')], 'Bunkworks ഗാൽവനൈസ്ഡ് സ്റ്റീൽ ബങ്ക് ബെഡ്'),
         'hi': (('बंक बेड का प्रकार', '2026 की अनुमानित कीमत (प्रति यूनिट)'),
                [('हल्का पेंट किया स्टील (पतली ट्यूब, शीट या पट्टी बेस)', 'लगभग ₹5,000–₹7,000'),
                 ('सामान्य स्टील हॉस्टल बंक बेड', 'लगभग ₹7,000–₹10,000'),
                 ('हेवी-ड्यूटी या गैल्वनाइज़्ड स्टील', 'लगभग ₹9,000–₹15,000'),
                 ('लकड़ी का बंक बेड', 'काफ़ी अलग-अलग, आमतौर पर ज़्यादा')], 'Bunkworks गैल्वनाइज़्ड स्टील बंक बेड')}[lang]
    rows = ''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a, b in L[1])
    ours = swap(f'₹{B} <s>₹{BR}</s>', f'₹{PB}')
    note = {'en': 'Market ranges are indicative, before mattresses.', 'ml': 'വിപണി നിരക്കുകൾ ഏകദേശമാണ്, മെത്ത ഇല്ലാതെ.', 'hi': 'बाज़ार भाव अनुमानित हैं, गद्दे के बिना।'}[lang]
    return (f'<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">{L[0][0]}</th><th scope="col">{L[0][1]}</th></tr></thead><tbody>{rows}'
            f'<tr class="ours"><td>{L[2]}</td><td>{ours}</td></tr></tbody></table></div><p class="note">{note}</p>')

NEW.append(dict(slug='cheapest-bunk-bed-price-india', lang='en', group='bunk-price', read=6,
 title=f'Cheapest Bunk Bed Price in India (2026): Double Decker Beds from ₹{BX}',
 seo=f'Cheap Bunk Bed Price in India 2026: From ₹{BX}', short='Cheapest bunk bed price',
 desc=f'Affordable bunk bed and double decker cot prices in India and Kerala for 2026, what a bunk bed under ₹5,000 really gets you, and steel bunk beds at ₹{BX}.',
 keywords='cheap bunk beds, bunk bed price in india, double decker bed under 5000, double decker bed price in kerala, bunker cot price, bunk bed for hostel price',
 thumb='blog-cheapest-bunk-bed-price', alt='Affordable galvanised steel double decker bed with plywood decks and ladder handle',
 excerpt='What an affordable bunk bed costs in India in 2026, what “under ₹5,000” really gets you, and the cheapest way to add beds.',
 body=quick('en', f'Basic steel bunk beds (double decker beds) in India commonly sell for about ₹7,000–₹15,000 per unit in 2026. The Bunkworks galvanised steel bunk bed is ' + swap(f'on anniversary offer at ₹{B} per piece (MRP ₹{BR}) until {OFFER["end_label"]["en"]} or while stock lasts', f'₹{PB} per piece') + f'. Orders above {OFFER["bulk_min"]} pieces get a bulk quote.') + f'''
<p class="lede">If you are furnishing a hostel, PG or dormitory on a tight budget, the bunk bed is the single cheapest way to add sleepers. Here is what affordable really means in 2026.</p>
{offer_box('en')}
<h2>What does a cheap bunk bed cost in India?</h2>
<p>Price depends on the steel, the base and the finish far more than on the brand. Here is how the market breaks down:</p>
{price_table('en')}
<h2>Can you buy a double decker bed under ₹5,000?</h2>
<p>Sometimes — but check what is missing at that price. The usual savings come from thinner tubes, a sheet or strip base instead of solid plywood, and paint instead of galvanising. In humid and coastal climates, painted mild steel starts rusting once the coating chips. Before you buy, ask for the tube size and thickness, the base thickness, and a load rating per deck.</p>
<h2>{swap(f'Why is the Bunkworks bunk bed priced at ₹{B}?', 'How much is the Bunkworks bunk bed?')}</h2>
<p>{swap('It is a 5th Anniversary Offer on existing stock, sold factory-direct from our workshop in Kerala with no dealer margin.', 'It is sold factory-direct from our workshop in Kerala with no dealer margin.')} You still get a galvanised steel frame, 12mm plywood decks, an epoxy coating, bolted joints, a height of 1.40 m and a 200 kg total weight-bearing capacity (100 kg per deck). {swap(f"Limited pieces are available at this price (MRP ₹{BR}).", f"The current price is ₹{PB} per piece.")}</p>
<h2>What is the cheapest cost per sleeper?</h2>
<p>One bunk bed sleeps two people, so {swap(f"at ₹{B} the frame costs about ₹3,000 per sleeper", f"at ₹{PB} the frame costs ₹{inr(OFFER['bunk_after']//2)} per sleeper")} — and it uses the floor space of one bed. Two single cots take twice the floor area, which matters when you pay rent per square foot.</p>
<h2>Bunk bed price in Kerala</h2>
<p>Bunkworks manufactures in Kerala, so hostels and PGs in Kochi, Thrissur, Kottayam and nearby districts avoid long-distance freight. Send your city and quantity for a delivered price.</p>
<h2>Ordering more than {OFFER["bulk_min"]} pieces?</h2>
<p>Large orders get a separate bulk quote with delivery planned for your opening date — <a href="{WA_BULK}" target="_blank" rel="noopener">message us on WhatsApp</a> or email <a href="{MAIL_BULK}">{EMAIL}</a>. See <a href="/blog/hostel-beds-wholesale-factory-price/">how factory-direct wholesale pricing works</a>, or go straight to the <a href="/bunker-cot-double-decker-bed/">steel bunk bed product page</a>.</p>
''',
 faqs=[('What is the cheapest price for a double decker bed in India?', f'Basic steel double decker beds commonly start around ₹5,000–₹7,000, with standard hostel models at ₹7,000–₹10,000 in 2026. The Bunkworks galvanised bunk bed is ' + (f'₹{B} on the 5th Anniversary Offer until {OFFER["end_label"]["en"]} or while stock lasts, then ₹{PB}.' if ACTIVE else f'₹{PB}.')),
       ('Is a double decker bed under ₹5,000 good for a hostel?', 'It can be, but check the tube thickness, base thickness, rust protection and load rating first. Low prices usually come from thinner steel and weaker bases.'),
       ('Is a bunk bed cheaper than two single cots?', 'Yes, per sleeper and per square foot. One bunk bed sleeps two people in the floor space of one bed.'),
       ('Do you give bulk discounts on bunk beds?', f'Yes. Orders of more than {OFFER["bulk_min"]} pieces get a separate bulk quote from Bunkworks.')]))

NEW.append(dict(slug='bunk-bed-price-malayalam', lang='ml', group='bunk-price', read=5,
 title=f'ബങ്ക് ബെഡ് / ഡബിൾ ഡെക്കർ കട്ടിൽ വില കേരളത്തിൽ (2026): ₹{BX} മുതൽ',
 seo='ബങ്ക് ബെഡ് / ഡബിൾ ഡെക്കർ കട്ടിൽ വില 2026', short='ബങ്ക് ബെഡ് വില (മലയാളം)',
 desc=f'കേരളത്തിൽ ബങ്ക് ബെഡ്, ബങ്കർ കോട്ട്, ഡബിൾ ഡെക്കർ കട്ടിൽ എന്നിവയുടെ 2026-ലെ വില, വാങ്ങുമ്പോൾ ശ്രദ്ധിക്കേണ്ടവ, ₹{BX}-ന് സ്റ്റീൽ ബങ്ക് ബെഡ്.',
 keywords='ബങ്ക് ബെഡ് വില, ഡബിൾ ഡെക്കർ കട്ടിൽ വില, ബങ്കർ കോട്ട്, ഇരുമ്പ് കട്ടിൽ വില, ഹോസ്റ്റൽ കട്ടിൽ, double decker bed price in kerala',
 thumb='blog-bunk-bed-price-ml', alt='ഹോസ്റ്റൽ മുറിയിലെ സ്റ്റീൽ ബങ്ക് ബെഡ്ഡുകൾ',
 excerpt='ബങ്ക് ബെഡ്, ഡബിൾ ഡെക്കർ കട്ടിൽ എന്നിവയുടെ 2026-ലെ വിലയും വാങ്ങുമ്പോൾ ശ്രദ്ധിക്കേണ്ട കാര്യങ്ങളും.',
 body=quick('ml', 'കേരളത്തിൽ സാധാരണ സ്റ്റീൽ ബങ്ക് ബെഡ്ഡിന് (ഡബിൾ ഡെക്കർ കട്ടിൽ) 2026-ൽ ഏകദേശം ₹7,000–₹15,000 വിലയുണ്ട്. Bunkworks ഗാൽവനൈസ്ഡ് സ്റ്റീൽ ബങ്ക് ബെഡ് ' + swap(f'{OFFER["end_label"]["ml"]} വരെ (അല്ലെങ്കിൽ സ്റ്റോക്ക് തീരുന്നതുവരെ) ₹{B}-ന് ലഭിക്കും (MRP ₹{BR})', f'₹{PB}-ന് ലഭിക്കും') + f'. {OFFER["bulk_min"]}-ൽ കൂടുതൽ എണ്ണത്തിന് ബൾക്ക് ക്വട്ടേഷൻ.') + f'''
<p class="lede">ഹോസ്റ്റലിനോ പിജിക്കോ ഡോർമിറ്ററിക്കോ വേണ്ടി കുറഞ്ഞ ചെലവിൽ കൂടുതൽ കിടക്കകൾ ഒരുക്കാൻ ഏറ്റവും നല്ല വഴി ബങ്ക് ബെഡ്ഡാണ്. 2026-ലെ വിലയും വാങ്ങുമ്പോൾ നോക്കേണ്ട കാര്യങ്ങളും ഇതാ.</p>
{offer_box('ml')}
<h2>ബങ്ക് ബെഡ് എന്നാൽ എന്ത്?</h2>
<p>ഒരേ ഫ്രെയിമിൽ മുകളിലും താഴെയുമായി രണ്ട് കിടക്കകൾ ഉള്ള കട്ടിലാണ് ബങ്ക് ബെഡ്. ബങ്കർ കോട്ട്, ഡബിൾ ഡെക്കർ കട്ടിൽ, ഡബിൾ ഡെക്കർ ബെഡ് എന്നീ പേരുകളിലും ഇത് അറിയപ്പെടുന്നു — എല്ലാം ഒന്നുതന്നെ.</p>
<h2>ബങ്ക് ബെഡ്ഡിന് എത്ര വിലയുണ്ട്?</h2>
{price_table('ml')}
<h2>₹5,000-ൽ താഴെ ഡബിൾ ഡെക്കർ കട്ടിൽ കിട്ടുമോ?</h2>
<p>ചിലപ്പോൾ കിട്ടും — പക്ഷേ ആ വിലയിൽ എന്താണ് കുറയുന്നതെന്ന് നോക്കണം. കനം കുറഞ്ഞ ട്യൂബ്, പ്ലൈവുഡിന് പകരം ഷീറ്റോ പട്ടയോ, ഗാൽവനൈസിംഗിന് പകരം പെയിന്റ് — ഇവയാണ് സാധാരണ വില കുറയ്ക്കുന്നത്. കേരളത്തിലെ ഈർപ്പമുള്ള കാലാവസ്ഥയിൽ പെയിന്റ് അടർന്നാൽ സാധാരണ സ്റ്റീൽ തുരുമ്പെടുക്കും. ട്യൂബിന്റെ കനം, ബേസിന്റെ കനം, ഓരോ തട്ടിന്റെയും ഭാരശേഷി എന്നിവ എഴുതി വാങ്ങുക.</p>
<h2>ഒരാൾക്ക് എത്ര ചെലവ് വരും?</h2>
<p>ഒരു ബങ്ക് ബെഡ്ഡിൽ രണ്ടുപേർക്ക് കിടക്കാം. {swap(f"₹{B} വിലയിൽ ഒരാൾക്ക് ഏകദേശം ₹3,000 മാത്രം", f"₹{PB} വിലയിൽ ഒരാൾക്ക് ₹{inr(OFFER['bunk_after']//2)}")} — അതും ഒരു കട്ടിലിന്റെ സ്ഥലത്ത്. രണ്ട് സിംഗിൾ കട്ടിലുകൾക്ക് ഇരട്ടി സ്ഥലം വേണം.</p>
<h2>കേരളത്തിൽ ഡെലിവറി</h2>
<p>Bunkworks കേരളത്തിലാണ് നിർമ്മിക്കുന്നത്. കൊച്ചി, തൃശൂർ, കോട്ടയം ഉൾപ്പെടെയുള്ള ജില്ലകളിലേക്ക് ദൂരെനിന്നുള്ള ചരക്കുകൂലി ഒഴിവാകും. നഗരവും എണ്ണവും അറിയിച്ചാൽ ഡെലിവറി ഉൾപ്പെടെയുള്ള വില അറിയിക്കാം.</p>
''',
 faqs=[('ഡബിൾ ഡെക്കർ കട്ടിലിന് കേരളത്തിൽ എത്ര വിലയുണ്ട്?', 'സാധാരണ സ്റ്റീൽ ഹോസ്റ്റൽ ബങ്ക് ബെഡ്ഡിന് 2026-ൽ ഏകദേശം ₹7,000–₹10,000. Bunkworks ബങ്ക് ബെഡ് ' + (f'വാർഷിക ഓഫറിൽ ₹{B} (MRP ₹{BR}).' if ACTIVE else f'₹{PB}.')),
       ('ബങ്കർ കോട്ടും ബങ്ക് ബെഡ്ഡും ഒന്നാണോ?', 'അതെ. ബങ്കർ കോട്ട്, ഡബിൾ ഡെക്കർ കട്ടിൽ, ബങ്ക് ബെഡ് — എല്ലാം ഒരേ ഫ്രെയിമിൽ രണ്ട് കിടക്കകളുള്ള കട്ടിലാണ്.'),
       ('മെത്ത വിലയിൽ ഉൾപ്പെടുമോ?', 'ഇല്ല. വില ഫ്രെയിമിനും പ്ലൈവുഡ് ബേസിനും മാത്രമാണ്; മെത്ത വേണമെങ്കിൽ ക്വട്ടേഷനിൽ ചോദിക്കാം.'),
       ('ബൾക്ക് ഓർഡറിന് ഡിസ്കൗണ്ട് ഉണ്ടോ?', f'{OFFER["bulk_min"]}-ൽ കൂടുതൽ എണ്ണത്തിന് പ്രത്യേക ബൾക്ക് ക്വട്ടേഷൻ നൽകും.')]))

NEW.append(dict(slug='bunk-bed-price-hindi', lang='hi', group='bunk-price', read=5,
 title=f'बंक बेड क्या होता है और इसकी कीमत कितनी है? (2026) — ₹{BX} से',
 seo='बंक बेड क्या होता है? डबल डेकर बेड कीमत 2026', short='बंक बेड कीमत (हिंदी)',
 desc=f'बंक बेड, बंकर कॉट और डबल डेकर बेड क्या होते हैं, 2026 में इनकी कीमत कितनी है, 5000 से कम में क्या मिलता है, और ₹{BX} में स्टील बंक बेड।',
 keywords='बंक बेड क्या होता है, बंक बेड कीमत, डबल डेकर बेड, डबल डेकर बेड under 5000, बंकर कॉट, हॉस्टल बेड',
 thumb='blog-bunk-bed-price-hi', alt='प्लाइवुड डेक वाला गैल्वनाइज़्ड स्टील डबल डेकर बेड',
 excerpt='बंक बेड क्या होता है, 2026 में कीमत कितनी है और सस्ता बंक बेड खरीदते समय क्या देखें।',
 body=quick('hi', 'बंक बेड (डबल डेकर बेड या बंकर कॉट) एक ही फ़्रेम पर ऊपर-नीचे दो बेड होते हैं। भारत में सामान्य स्टील बंक बेड 2026 में लगभग ₹7,000–₹15,000 प्रति यूनिट मिलते हैं। Bunkworks गैल्वनाइज़्ड स्टील बंक बेड ' + swap(f'वर्षगांठ ऑफ़र में ₹{B} (MRP ₹{BR}) — {OFFER["end_label"]["hi"]} तक या स्टॉक रहने तक', f'₹{PB}') + '।') + f'''
<p class="lede">हॉस्टल, पीजी या डॉरमिटरी में कम खर्च में ज़्यादा बेड लगाने का सबसे आसान तरीका बंक बेड है। जानिए यह क्या होता है, इसकी कीमत कितनी है और खरीदते समय क्या देखें।</p>
{offer_box('hi')}
<h2>बंक बेड क्या होता है?</h2>
<p>बंक बेड ऐसा पलंग है जिसमें एक ही फ़्रेम पर ऊपर और नीचे दो सोने की जगहें होती हैं। इसे बंकर कॉट, डबल डेकर बेड या डबल डेकर कॉट भी कहते हैं — सब एक ही चीज़ हैं। इससे एक बेड की जगह में दो लोग सो सकते हैं।</p>
<h2>बंक बेड की कीमत कितनी है?</h2>
{price_table('hi')}
<h2>क्या 5000 से कम में डबल डेकर बेड मिलता है?</h2>
<p>कभी-कभी मिल जाता है — लेकिन देखें कि उस कीमत में क्या कम है। आमतौर पर पतली ट्यूब, प्लाइवुड की जगह शीट या पट्टी, और गैल्वनाइज़िंग की जगह सिर्फ़ पेंट से कीमत घटाई जाती है। नमी वाले मौसम में पेंट उखड़ते ही साधारण स्टील में जंग लगती है। खरीदने से पहले ट्यूब की मोटाई, बेस की मोटाई और हर डेक की भार क्षमता लिखित में लें।</p>
<h2>एक व्यक्ति पर कितना खर्च आता है?</h2>
<p>एक बंक बेड पर दो लोग सोते हैं, इसलिए {swap(f"₹{B} में प्रति व्यक्ति लगभग ₹3,000", f"₹{PB} में प्रति व्यक्ति ₹{inr(OFFER['bunk_after']//2)}")} — और जगह सिर्फ़ एक बेड की लगती है।</p>
<h2>बंक बेड डिज़ाइन: हॉस्टल के लिए क्या चुनें?</h2>
<ul><li>गैल्वनाइज़्ड स्टील फ़्रेम, जिसमें जंग न लगे</li><li>12mm मोटा प्लाइवुड बेस, जो झुकता नहीं</li><li>ऊपर वाले डेक पर मज़बूत गार्ड रेल और सीढ़ी</li><li>बोल्ट वाले जोड़, ताकि बेड खोलकर कहीं और ले जा सकें</li></ul>
''',
 faqs=[('बंक बेड क्या होता है?', 'एक ही फ़्रेम पर ऊपर-नीचे दो बेड वाला पलंग। इसे बंकर कॉट और डबल डेकर बेड भी कहते हैं।'),
       ('डबल डेकर बेड की कीमत कितनी है?', 'सामान्य स्टील हॉस्टल बंक बेड 2026 में लगभग ₹7,000–₹10,000 में मिलते हैं। Bunkworks बंक बेड ' + (f'वर्षगांठ ऑफ़र में ₹{B} (MRP ₹{BR})।' if ACTIVE else f'₹{PB}।')),
       ('क्या कीमत में गद्दा शामिल है?', 'नहीं। कीमत फ़्रेम और प्लाइवुड बेस की है; गद्दा चाहिए तो कोटेशन में बताएँ।'),
       ('बल्क ऑर्डर पर छूट मिलती है?', f'हाँ, {OFFER["bulk_min"]} से ज़्यादा पीस के लिए अलग बल्क कोटेशन दिया जाता है।')]))

NEW.append(dict(slug='iron-cot-vs-steel-cot-price', lang='en', group='cot-price', read=5,
 title=f'Iron Cot vs Steel Cot: Price and Which Lasts Longer (2026)',
 seo='Iron Cot Price vs Steel Cot Price (2026)', short='Iron vs steel cot price',
 desc=f'Iron cot or steel cot? 2026 single cot prices in India and Kerala, how painted mild steel compares with galvanised steel, and a steel single cot at ₹{SX}.',
 keywords='iron cot price, steel cot price single, single cot price in kerala, cot price steel, iron cot price in india, steel cot price',
 thumb='blog-iron-vs-steel-cot-price', alt='Galvanised steel single cot with plywood base and dark grey finish',
 excerpt='What “iron cot” usually means, how it compares with galvanised steel, and 2026 single cot prices.',
 body=quick('en', f'Most “iron cots” sold in India are painted mild steel frames. They cost less up front but rust once the paint chips. Galvanised steel cots resist rust for much longer. Steel single cots for hostels commonly cost ₹3,500–₹8,000 in 2026; the Bunkworks galvanised single cot is ' + swap(f'₹{S} on the 5th Anniversary Offer (MRP ₹{SR})', f'₹{PS}') + '.') + f'''
<p class="lede">Search for a single cot and you will see “iron cot” and “steel cot” used almost interchangeably. The difference that actually matters is how the steel is protected.</p>
{offer_box('en')}
<h2>Is an iron cot the same as a steel cot?</h2>
<p>Almost always, yes. Pure iron is rarely used for furniture; what shops call an iron cot is usually a mild steel (MS) frame with paint. The real choice is between painted mild steel and galvanised steel.</p>
<h2>Iron cot vs steel cot at a glance</h2>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col"></th><th scope="col">Painted mild steel (“iron cot”)</th><th scope="col">Galvanised steel cot</th></tr></thead><tbody>
<tr><td>Rust resistance</td><td>Rusts where paint chips</td><td>Zinc layer protects even when scratched</td></tr>
<tr><td>Best for</td><td>Dry rooms, short-term use</td><td>Humid, coastal and high-use rooms</td></tr>
<tr><td>Up-front price</td><td>Lower</td><td>Slightly higher</td></tr>
<tr><td>Replacement cycle</td><td>Shorter</td><td>Longer</td></tr>
</tbody></table></div>
<h2>How much does a single cot cost in 2026?</h2>
<p>Steel single cots for hostel use commonly cost roughly ₹3,500–₹8,000 each, depending on steel, base and finish. The Bunkworks steel single cot — galvanised frame, 12mm plywood base, rated up to 100 kg — is {swap(f"₹{S} per piece on the 5th Anniversary Offer until {OFFER['end_label']['en']} or while stock lasts (MRP ₹{SR})", f"₹{PS} per piece")}.</p>
<h2>Single cot price in Kerala</h2>
<p>We manufacture in Kerala, where monsoon humidity is exactly the condition that ruins painted frames. Local manufacturing also keeps freight low for hostels across the state. Full specs are on the <a href="/steel-single-cot/">steel single cot page</a>; sizes are covered in our <a href="/blog/steel-single-cot-for-hostel/">single cot size guide</a>.</p>
''',
 faqs=[('Is an iron cot better than a steel cot?', 'What is sold as an iron cot is usually painted mild steel. A galvanised steel cot resists rust better and lasts longer in humid rooms.'),
       ('What is the price of a steel single cot?', 'Commonly ₹3,500–₹8,000 in 2026. The Bunkworks galvanised single cot is ' + (f'₹{S} on the 5th Anniversary Offer (MRP ₹{SR}).' if ACTIVE else f'₹{PS}.')),
       ('What is the load capacity of the Bunkworks single cot?', 'Up to 100 kg, with a 12mm plywood base and galvanised steel frame.')]))

NEW.append(dict(slug='iron-cot-price-malayalam', lang='ml', group='cot-price', read=4,
 title=f'ഇരുമ്പ് കട്ടിൽ വില / സ്റ്റീൽ സിംഗിൾ കട്ടിൽ വില (2026): ₹{SX} മുതൽ',
 seo='ഇരുമ്പ് കട്ടിൽ വില / സ്റ്റീൽ കട്ടിൽ വില 2026', short='ഇരുമ്പ് കട്ടിൽ വില (മലയാളം)',
 desc=f'ഇരുമ്പ് കട്ടിലും സ്റ്റീൽ കട്ടിലും തമ്മിലുള്ള വ്യത്യാസം, 2026-ലെ സിംഗിൾ കട്ടിൽ വില, ₹{SX}-ന് ഗാൽവനൈസ്ഡ് സ്റ്റീൽ സിംഗിൾ കട്ടിൽ.',
 keywords='ഇരുമ്പ് കട്ടിൽ വില, കട്ടിൽ വില, സ്റ്റീൽ കട്ടിൽ, സിംഗിൾ കട്ടിൽ വില, കട്ടിൽ വിലക്കുറവിൽ, single cot price in kerala',
 thumb='blog-iron-cot-price-ml', alt='പ്ലൈവുഡ് ബേസുള്ള സ്റ്റീൽ സിംഗിൾ കട്ടിൽ',
 excerpt='ഇരുമ്പ് കട്ടിലോ സ്റ്റീൽ കട്ടിലോ? 2026-ലെ വിലയും വ്യത്യാസവും.',
 body=quick('ml', 'കടകളിൽ "ഇരുമ്പ് കട്ടിൽ" എന്ന് വിൽക്കുന്നത് മിക്കതും പെയിന്റ് ചെയ്ത മൈൽഡ് സ്റ്റീൽ ആണ്; പെയിന്റ് പോയാൽ തുരുമ്പെടുക്കും. ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിൽ കൂടുതൽ കാലം നിലനിൽക്കും. Bunkworks സ്റ്റീൽ സിംഗിൾ കട്ടിൽ ' + swap(f'വാർഷിക ഓഫറിൽ ₹{S} (MRP ₹{SR})', f'₹{PS}') + '.') + f'''
<p class="lede">കുറഞ്ഞ വിലയിൽ നല്ല കട്ടിൽ തിരയുമ്പോൾ "ഇരുമ്പ് കട്ടിൽ", "സ്റ്റീൽ കട്ടിൽ" എന്നീ പേരുകൾ കാണാം. യഥാർത്ഥ വ്യത്യാസം സ്റ്റീലിനെ തുരുമ്പിൽ നിന്ന് എങ്ങനെ സംരക്ഷിക്കുന്നു എന്നതിലാണ്.</p>
{offer_box('ml')}
<h2>ഇരുമ്പ് കട്ടിലും സ്റ്റീൽ കട്ടിലും ഒന്നാണോ?</h2>
<p>മിക്കപ്പോഴും അതെ. ഫർണിച്ചറിന് ശുദ്ധമായ ഇരുമ്പ് ഉപയോഗിക്കാറില്ല; "ഇരുമ്പ് കട്ടിൽ" സാധാരണ പെയിന്റ് ചെയ്ത മൈൽഡ് സ്റ്റീൽ (MS) ഫ്രെയിമാണ്. പെയിന്റ് ചെയ്ത സ്റ്റീലോ ഗാൽവനൈസ്ഡ് സ്റ്റീലോ എന്നതാണ് യഥാർത്ഥ തിരഞ്ഞെടുപ്പ്.</p>
<h2>സിംഗിൾ കട്ടിലിന് എത്ര വിലയുണ്ട്?</h2>
<p>ഹോസ്റ്റലിനുള്ള സ്റ്റീൽ സിംഗിൾ കട്ടിലിന് 2026-ൽ ഏകദേശം ₹3,500–₹8,000 വിലയുണ്ട്. Bunkworks കട്ടിൽ — ഗാൽവനൈസ്ഡ് ഫ്രെയിം, 12mm പ്ലൈവുഡ് ബേസ്, 100 കിലോ വരെ ഭാരശേഷി — {swap(f"₹{S}-ന് ലഭിക്കും (MRP ₹{SR})", f"₹{PS}-ന് ലഭിക്കും")}.</p>
<h2>വലിപ്പം</h2>
<p>6 × 2.5 അടി (183 × 76 സെ.മീ.), ഉയരം 40 സെ.മീ. സാധാരണ സിംഗിൾ മെത്തയ്ക്ക് യോജിക്കും.</p>
<h2>കേരളത്തിലെ കാലാവസ്ഥയ്ക്ക് ഏത്?</h2>
<p>മഴക്കാലത്തെ ഈർപ്പത്തിൽ പെയിന്റ് ചെയ്ത ഫ്രെയിമുകൾ വേഗം തുരുമ്പെടുക്കും. ഹോസ്റ്റലുകൾക്കും പിജികൾക്കും ഗാൽവനൈസ്ഡ് സ്റ്റീലാണ് ദീർഘകാലത്തേക്ക് ലാഭം.</p>
''',
 faqs=[('ഇരുമ്പ് കട്ടിലിന് എത്ര വിലയുണ്ട്?', 'സ്റ്റീൽ/ഇരുമ്പ് സിംഗിൾ കട്ടിലിന് 2026-ൽ ഏകദേശം ₹3,500–₹8,000. Bunkworks സിംഗിൾ കട്ടിൽ ' + (f'₹{S} (MRP ₹{SR}).' if ACTIVE else f'₹{PS}.')),
       ('ഏതാണ് നല്ലത്: ഇരുമ്പ് കട്ടിലോ സ്റ്റീൽ കട്ടിലോ?', 'ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിൽ. പോറൽ വീണാലും തുരുമ്പെടുക്കാൻ സാധ്യത കുറവാണ്.'),
       ('Bunkworks സിംഗിൾ കട്ടിലിന്റെ വലിപ്പം എത്ര?', '6 × 2.5 അടി (183 × 76 സെ.മീ.), ഉയരം 40 സെ.മീ., 100 കിലോ വരെ ഭാരശേഷി.')]))

NEW.append(dict(slug='iron-cot-price-hindi', lang='hi', group='cot-price', read=4,
 title=f'लोहे का पलंग कीमत 2026: प्लाई वाला स्टील सिंगल पलंग ₹{SX} में',
 seo='लोहे का पलंग प्राइस 2026: प्लाई वाला सिंगल कॉट', short='लोहे का पलंग कीमत (हिंदी)',
 desc=f'लोहे का पलंग और स्टील पलंग में फ़र्क, 2026 में सिंगल कॉट की कीमत, प्लाई वाला पलंग क्यों बेहतर है, और ₹{SX} में गैल्वनाइज़्ड स्टील सिंगल कॉट।',
 keywords='लोहे का पलंग प्राइस, लोहे का पलंग प्लाई वाला, स्टील पलंग कीमत, सिंगल कॉट कीमत, हॉस्टल बेड',
 thumb='blog-iron-cot-price-hi', alt='प्लाइवुड बेस वाला स्टील सिंगल पलंग',
 excerpt='लोहे का पलंग या स्टील पलंग? 2026 की कीमत और प्लाई वाले पलंग के फ़ायदे।',
 body=quick('hi', 'बाज़ार में "लोहे का पलंग" ज़्यादातर पेंट किया हुआ माइल्ड स्टील होता है, जिसमें पेंट उखड़ने पर जंग लगती है। गैल्वनाइज़्ड स्टील पलंग ज़्यादा टिकता है। Bunkworks प्लाई वाला स्टील सिंगल पलंग ' + swap(f'वर्षगांठ ऑफ़र में ₹{S} (MRP ₹{SR})', f'₹{PS}') + '।') + f'''
<p class="lede">सस्ता और मज़बूत सिंगल पलंग ढूँढते समय "लोहे का पलंग" और "स्टील पलंग" दोनों नाम मिलते हैं। असली फ़र्क इस बात में है कि स्टील को जंग से कैसे बचाया गया है।</p>
{offer_box('hi')}
<h2>क्या लोहे का पलंग और स्टील पलंग एक ही हैं?</h2>
<p>ज़्यादातर हाँ। फ़र्नीचर में शुद्ध लोहा कम ही लगता है; "लोहे का पलंग" आमतौर पर पेंट किया माइल्ड स्टील (MS) फ़्रेम होता है। असली चुनाव पेंट किए स्टील और गैल्वनाइज़्ड स्टील के बीच है।</p>
<h2>प्लाई वाला पलंग क्यों बेहतर है?</h2>
<p>12mm मोटा प्लाइवुड बेस पूरे गद्दे को बराबर सहारा देता है और झुकता नहीं। लोहे की पट्टियों वाला बेस सस्ता होता है, पर समय के साथ मुड़ सकता है और गद्दे में धँसता है।</p>
<h2>सिंगल कॉट की कीमत कितनी है?</h2>
<p>हॉस्टल के लिए स्टील सिंगल कॉट 2026 में आमतौर पर ₹3,500–₹8,000 में मिलते हैं। Bunkworks पलंग — गैल्वनाइज़्ड फ़्रेम, 12mm प्लाई बेस, 100 किलो तक भार क्षमता — {swap(f"₹{S} प्रति पीस (MRP ₹{SR}), {OFFER['end_label']['hi']} तक या स्टॉक रहने तक", f"₹{PS} प्रति पीस")}।</p>
<h2>साइज़</h2>
<p>6 × 2.5 फ़ीट (183 × 76 सेमी), ऊँचाई 40 सेमी। सामान्य सिंगल गद्दे के लिए सही।</p>
''',
 faqs=[('लोहे के पलंग की कीमत कितनी है?', 'स्टील/लोहे के सिंगल पलंग 2026 में लगभग ₹3,500–₹8,000 में मिलते हैं। Bunkworks सिंगल कॉट ' + (f'₹{S} (MRP ₹{SR})।' if ACTIVE else f'₹{PS}।')),
       ('प्लाई वाला पलंग अच्छा है या पट्टी वाला?', 'प्लाई वाला। 12mm प्लाई बेस झुकता नहीं और गद्दे को बराबर सहारा देता है।'),
       ('Bunkworks सिंगल कॉट का साइज़ क्या है?', '6 × 2.5 फ़ीट (183 × 76 सेमी), ऊँचाई 40 सेमी, 100 किलो तक भार क्षमता।')]))

NEW.append(dict(slug='bunk-bed-size-guide', lang='en', group=None, read=5,
 title='Bunk Bed Size in Feet, cm and Inches: Hostel Bed Size Guide (2026)',
 seo='Bunk Bed Size in Feet, cm & Inches (2026 Guide)', short='Bunk bed size guide',
 desc='Standard bunk bed and hostel bed sizes in feet, inches, cm and mm, how much ceiling height you need, and how to plan a hostel room around bunk beds.',
 keywords='bunk bed size, bunk bed size in feet, bunk bed size in cm, bunk bed size in inches, hostel bed size, bunk bed size for adults',
 thumb='blog-bunk-bed-size-guide', alt='Line diagram of a bunk bed showing length, gap between decks and overall height',
 excerpt='Standard bunk bed and hostel bed sizes in feet, inches, cm and mm — plus ceiling and room planning.',
 body=quick('en', 'Most hostel bunk beds in India take a standard single mattress of 6 × 2.5 ft (72 × 30 in, about 183 × 76 cm) or 6 × 3 ft (72 × 36 in, about 183 × 91 cm). Always check the ceiling height and leave enough headroom above the top mattress for the sleeper to sit up.') + '''
<p class="lede">Size decides three things: which mattress you buy, how many beds fit in a room, and whether the top deck is comfortable. Here are the numbers.</p>
<h2>What is the standard bunk bed size?</h2>
<p>A bunk bed is sized around its mattress. In India, hostel bunk beds are almost always built for single mattresses:</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Size</th><th scope="col">Feet</th><th scope="col">Inches</th><th scope="col">cm</th><th scope="col">mm</th></tr></thead><tbody>
<tr><td>Standard single</td><td>6 × 2.5</td><td>72 × 30</td><td>183 × 76</td><td>1829 × 762</td></tr>
<tr><td>Wide single</td><td>6 × 3</td><td>72 × 36</td><td>183 × 91</td><td>1829 × 914</td></tr>
</tbody></table></div>
<p class="note">Frame dimensions are slightly larger than the mattress. Confirm the exact outside size with your supplier before planning the room.</p>
<h2>How much ceiling height do you need for a bunk bed?</h2>
<p>Measure from the top mattress surface to the ceiling. The person on the top deck should be able to sit up without hitting the ceiling or a fan — check fan blades especially. Low ceilings and ceiling fans are the most common reasons to choose single cots instead.</p>
<h2>How much gap should there be between the two decks?</h2>
<p>Enough for the lower sleeper to sit up comfortably. When you compare models, sit on the lower deck yourself or ask the supplier for the clear height between decks.</p>
<h2>How many bunk beds fit in a hostel room?</h2>
<ul><li>Each bunk bed uses the floor area of one single cot but sleeps two.</li><li>Leave a clear walkway along the long side of each bed.</li><li>Keep windows, switches and doors reachable.</li><li>Place ladders on the walkway side, never against a wall.</li></ul>
<h2>Bunkworks bed dimensions</h2>
<p>Our steel bunk bed stands 1.40 m (140 cm) tall, and our steel single cot is 6 × 2.5 ft (183 × 76 cm) and 40 cm high, both with 12mm plywood bases. A 1.40 m bunk bed leaves generous headroom above the top deck in a standard room. See the <a href="/bunker-cot-double-decker-bed/">bunk bed page</a> and the <a href="/steel-single-cot/">single cot page</a> for full specs.</p>
''',
 faqs=[('What is the standard bunk bed size in feet?', 'Most hostel bunk beds take a 6 × 2.5 ft or 6 × 3 ft single mattress.'),
       ('What is the bunk bed size in cm?', 'About 183 × 76 cm for a standard single mattress and 183 × 91 cm for a wide single. The frame is slightly larger.'),
       ('What size bunk bed is best for adults?', 'A 6 × 3 ft deck is roomier for adults; 6 × 2.5 ft fits more beds per room. Check the load rating per deck as well as the size.')]))

NEW.append(dict(slug='bunk-beds-for-adults', lang='en', group=None, read=5,
 title='Bunk Beds for Adults: Size, Weight Capacity and Safety Checklist',
 seo='Bunk Beds for Adults: Size, Weight & Safety Guide', short='Bunk beds for adults',
 desc='What to check in a bunk bed or double decker bed for adults: deck size, load rating, steel, base, guard rails and ladder — for hostels, PGs and staff housing.',
 keywords='bunk bed for adults, double decker bed for adults, bunk bed for adults hostel, heavy duty bunk bed, bunker cot for hostel',
 thumb='blog-bunk-bed-for-adults', alt='Steel bunk beds with mattresses in an adult hostel dormitory',
 excerpt='Adult hostels and staff housing need stronger bunk beds. Here is the checklist.',
 body=quick('en', 'A bunk bed for adults needs a stated load rating per deck, a full-size single deck (6 × 2.5 ft or 6 × 3 ft), a rigid steel frame, a solid base such as 12mm plywood, a top guard rail and a secure ladder. Kids’ bunk beds are usually too light for adult hostels.') + f'''
<p class="lede">Many bunk beds sold online are designed for children. Adult hostels, PGs, labour camps and staff quarters need beds built for adult weight and daily use.</p>
<h2>What makes a bunk bed suitable for adults?</h2>
<ul>
<li><strong>Load rating per deck.</strong> Ask for it in writing. Adults climbing, sitting and turning put far more force on a frame than their static weight.</li>
<li><strong>Full-size decks.</strong> 6 × 2.5 ft at minimum; 6 × 3 ft for more comfort.</li>
<li><strong>Frame steel.</strong> Heavier square tubes flex less. Galvanised steel resists rust in shared bathrooms and humid weather.</li>
<li><strong>Solid base.</strong> 12mm plywood spreads the load evenly and does not sag like thin sheet or widely spaced strips.</li>
<li><strong>Guard rail and ladder.</strong> A top rail on the open side and a ladder that stays rigid under adult weight.</li>
<li><strong>Bolted joints.</strong> Easy to tighten, repair and move.</li>
</ul>
<h2>Is a double decker bed safe for adults?</h2>
<p>Yes, when it is rated for adult weight and assembled correctly. Tighten bolts after the first few weeks, and check them during routine room inspections.</p>
<h2>What does an adult bunk bed cost?</h2>
<p>Heavy-duty steel bunk beds commonly cost ₹9,000–₹15,000 in 2026. The Bunkworks galvanised steel bunk bed has a 200 kg total weight-bearing capacity (100 kg per deck), 12mm plywood decks and an epoxy coating, and is {swap(f"₹{B} on the 5th Anniversary Offer until {OFFER['end_label']['en']} or while stock lasts (MRP ₹{BR})", f"₹{PB}")}. See the <a href="/bunker-cot-double-decker-bed/">bunk bed page</a> or read our <a href="/blog/bunk-bed-size-guide/">bunk bed size guide</a>.</p>
''',
 faqs=[('Can adults sleep on bunk beds?', 'Yes, if the bed has a stated adult load rating, full-size decks, a solid base and proper guard rails.'),
       ('What size bunk bed is best for adults?', '6 × 3 ft decks are the most comfortable; 6 × 2.5 ft fits more beds per room.'),
       ('What should I check before buying bunk beds for an adult hostel?', 'Load rating per deck, steel type and thickness, base thickness, guard rail, ladder and bolted joints.')]))


GTAB = {
 'en': (('', 'Painted mild steel', 'Bunkworks galvanised steel + epoxy'),
        [('Outside of the tube', 'Paint layer only', 'Zinc layer plus epoxy coating'),
         ('Inside of the tube', 'Bare steel — paint cannot reach inside', 'Zinc-coated'),
         ('When scratched', 'Bare steel exposed, rust starts', 'Surrounding zinc keeps protecting the steel'),
         ('In humid, coastal rooms', 'Rusts from inside and at chips', 'Resists rust far better'),
         ('Up-front price', 'Lower', 'Slightly higher'),
         ('Replacement cycle', 'Shorter', 'Longer')]),
 'ml': (('', 'പെയിന്റ് ചെയ്ത മൈൽഡ് സ്റ്റീൽ', 'Bunkworks ഗാൽവനൈസ്ഡ് സ്റ്റീൽ + എപ്പോക്സി'),
        [('ട്യൂബിന്റെ പുറംഭാഗം', 'പെയിന്റ് മാത്രം', 'സിങ്ക് പാളിയും എപ്പോക്സി കോട്ടിംഗും'),
         ('ട്യൂബിന്റെ ഉൾഭാഗം', 'സംരക്ഷണമില്ല — ഉള്ളിൽ പെയിന്റ് എത്തില്ല', 'സിങ്ക് കോട്ടിംഗ് ഉണ്ട്'),
         ('പോറൽ വീണാൽ', 'സ്റ്റീൽ പുറത്താകും, തുരുമ്പ് തുടങ്ങും', 'ചുറ്റുമുള്ള സിങ്ക് സംരക്ഷണം തുടരും'),
         ('ഈർപ്പമുള്ള മുറികളിൽ', 'ഉള്ളിൽ നിന്നും പോറലുകളിൽ നിന്നും തുരുമ്പെടുക്കും', 'തുരുമ്പിനെ വളരെ നന്നായി ചെറുക്കും'),
         ('ആദ്യ വില', 'കുറവ്', 'അൽപം കൂടുതൽ'),
         ('ആയുസ്സ്', 'കുറവ്', 'കൂടുതൽ')]),
 'hi': (('', 'पेंट किया माइल्ड स्टील', 'Bunkworks गैल्वनाइज़्ड स्टील + एपॉक्सी'),
        [('ट्यूब का बाहरी हिस्सा', 'सिर्फ़ पेंट की परत', 'ज़िंक की परत और एपॉक्सी कोटिंग'),
         ('ट्यूब का अंदरूनी हिस्सा', 'खुला स्टील — अंदर पेंट नहीं पहुँचता', 'ज़िंक कोटिंग वाला'),
         ('खरोंच लगने पर', 'स्टील खुल जाता है, जंग शुरू', 'आसपास का ज़िंक स्टील को बचाता रहता है'),
         ('नमी वाले कमरों में', 'अंदर से और खरोंच से जंग', 'जंग से कहीं बेहतर बचाव'),
         ('शुरुआती कीमत', 'कम', 'थोड़ी ज़्यादा'),
         ('चलने की अवधि', 'कम', 'ज़्यादा')]),
}
def gtable(lang):
    h, rows = GTAB[lang]
    return ('<div class="table-wrap"><table class="cost-table"><thead><tr>' + ''.join(f'<th scope="col">{x}</th>' for x in h) + '</tr></thead><tbody>' +
            ''.join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>' for a, b, c in rows) + '</tbody></table></div>')

GALV_POSTS = []
GALV_POSTS.append(dict(slug='galvanised-steel-vs-painted-steel-beds', lang='en', group='galv', read=5,
 title='Galvanised Steel vs Painted Steel Beds: Why Galvanised Resists Rust Better',
 seo='Galvanised vs Painted Steel Cots: Rust Resistance', short='Why galvanised steel',
 desc='Why galvanised steel bunk beds and cots resist rust better than painted steel: paint cannot reach inside a hollow tube, while zinc protects inside and out.',
 keywords='galvanised steel bed, galvanised steel cot, rust proof bunk bed, painted steel vs galvanised, anti rust cot, GI bunk bed',
 thumb='blog-galvanised-steel-advantage', alt='Galvanised steel bed frame corner joint with epoxy coating and plywood base',
 excerpt='Paint only covers the outside of a steel tube. Here is why galvanised steel beds last longer.',
 body=quick('en', 'Galvanised steel resists rust better than painted steel because the zinc coating protects the steel on the inside of the tube as well as the outside, and keeps protecting it where it gets scratched. A painted tube is only painted on the outside — paint cannot be applied inside a hollow tube, so the inside stays bare and can rust from within.') + f"""
<p class="lede">Most steel cots look the same on the day they arrive. The difference shows up after a few monsoons — and it starts where you cannot see it: inside the tube.</p>
<h2>Why can't a steel tube be painted from the inside?</h2>
<p>Bed frames are made from hollow square or round tubes. Spray and brush painting reach only the outer surface; there is no practical way to coat the inside of a long, closed tube after it is made. So a painted mild steel frame is really bare steel on the inside, protected only on the outside.</p>
<h2>What happens inside a painted tube?</h2>
<p>Humid air gets into the tube through bolt holes, cut ends and joints. Moisture condenses on the bare inner surface, and rust starts there — out of sight. Over time it weakens the tube from within and shows up as bubbling paint, rust stains around bolt holes and loose joints.</p>
<h2>How does galvanised steel protect the tube?</h2>
<ul>
<li><strong>Zinc on the inside too.</strong> Galvanised tube carries its zinc coating on the inner surface as well, so there is no bare steel hiding inside.</li>
<li><strong>Protection at scratches.</strong> Zinc corrodes in preference to steel, so the surrounding zinc keeps protecting small scratches and chips instead of letting rust spread.</li>
<li><strong>Bonded, not just painted on.</strong> The zinc layer is part of the steel surface, so it does not peel away like paint.</li>
</ul>
<h2>Galvanised vs painted steel at a glance</h2>
{gtable('en')}
<h2>What about the finish on Bunkworks beds?</h2>
<p>Bunkworks frames are galvanised steel with an <strong>epoxy coating</strong> on top — not powder coating. The zinc protects the steel; the epoxy gives the grey finish and an extra barrier on the outside. The single cot carries up to 100 kg and the bunk bed has a 200 kg total weight-bearing capacity (100 kg per deck).</p>
<h2>Why this matters in Kerala</h2>
<p>Monsoon humidity, coastal air, wet floors and clothes drying in rooms are exactly the conditions that rust painted frames. For hostels and PGs that replace furniture only when it fails, galvanised steel is the cheaper choice over the life of the bed. Compare prices on the <a href="/bunker-cot-double-decker-bed/">bunk bed page</a> and the <a href="/steel-single-cot/">single cot page</a>.</p>
""",
 faqs=[('Does galvanised steel rust?', 'It resists rust far better than painted steel. The zinc coating protects the steel inside and outside the tube, and keeps protecting it at small scratches.'),
       ('Why does a painted steel cot rust from inside?', 'Paint cannot be applied inside a hollow tube. Moisture that gets in through holes and joints condenses on the bare inner steel and rusts it from within.'),
       ('Are Bunkworks beds powder coated?', 'No. Bunkworks frames are galvanised steel with an epoxy coating.')]))

GALV_POSTS.append(dict(slug='galvanised-steel-cot-malayalam', lang='ml', group='galv', read=4,
 title='ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിൽ തുരുമ്പിനെ എന്തുകൊണ്ട് കൂടുതൽ ചെറുക്കുന്നു?',
 seo='ഗാൽവനൈസ്ഡ് സ്റ്റീൽ vs പെയിന്റ് ചെയ്ത കട്ടിൽ', short='ഗാൽവനൈസ്ഡ് സ്റ്റീൽ (മലയാളം)',
 desc='പെയിന്റ് ചെയ്ത സ്റ്റീൽ കട്ടിലിനേക്കാൾ ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിൽ തുരുമ്പിനെ ചെറുക്കുന്നത് എന്തുകൊണ്ട്? ട്യൂബിനുള്ളിൽ പെയിന്റ് എത്താത്തതിന്റെ പ്രശ്നം.',
 keywords='ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിൽ, തുരുമ്പെടുക്കാത്ത കട്ടിൽ, ഇരുമ്പ് കട്ടിൽ തുരുമ്പ്, ബങ്ക് ബെഡ്, സ്റ്റീൽ കട്ടിൽ',
 thumb='blog-galvanised-steel-advantage-ml', alt='എപ്പോക്സി കോട്ടിംഗുള്ള ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിലിന്റെ മൂല',
 excerpt='പെയിന്റ് ട്യൂബിന്റെ പുറത്ത് മാത്രം. ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കൂടുതൽ കാലം നിലനിൽക്കുന്നത് എന്തുകൊണ്ട്?',
 body=quick('ml', 'ഗാൽവനൈസ്ഡ് സ്റ്റീലിലെ സിങ്ക് കോട്ടിംഗ് ട്യൂബിന്റെ പുറത്തും ഉള്ളിലും സംരക്ഷണം നൽകുന്നു; പോറൽ വീണാലും സംരക്ഷണം തുടരും. പെയിന്റ് ചെയ്ത ട്യൂബിൽ പുറത്ത് മാത്രമേ പെയിന്റുള്ളൂ — പൊള്ളയായ ട്യൂബിന്റെ ഉള്ളിൽ പെയിന്റ് ചെയ്യാൻ കഴിയില്ല, അതിനാൽ ഉള്ളിൽ നിന്ന് തുരുമ്പെടുക്കാം.') + f"""
<p class="lede">വാങ്ങുന്ന ദിവസം എല്ലാ സ്റ്റീൽ കട്ടിലുകളും ഒരുപോലെ തോന്നും. വ്യത്യാസം കാണുന്നത് ഏതാനും മഴക്കാലങ്ങൾക്ക് ശേഷമാണ് — അതും കാണാൻ കഴിയാത്തിടത്ത്: ട്യൂബിനുള്ളിൽ.</p>
<h2>ട്യൂബിന്റെ ഉള്ളിൽ പെയിന്റ് ചെയ്യാൻ കഴിയാത്തത് എന്തുകൊണ്ട്?</h2>
<p>കട്ടിലിന്റെ ഫ്രെയിം പൊള്ളയായ ട്യൂബുകൾ കൊണ്ടാണ് നിർമ്മിക്കുന്നത്. സ്പ്രേയോ ബ്രഷോ പുറംഭാഗത്ത് മാത്രമേ എത്തൂ; നീളമുള്ള ട്യൂബിന്റെ ഉള്ളിൽ പെയിന്റ് ചെയ്യാൻ പ്രായോഗികമായി മാർഗ്ഗമില്ല. അതിനാൽ പെയിന്റ് ചെയ്ത കട്ടിലിന്റെ ട്യൂബിനുള്ളിൽ സ്റ്റീൽ സംരക്ഷണമില്ലാതെ കിടക്കും.</p>
<h2>പെയിന്റ് ചെയ്ത ട്യൂബിനുള്ളിൽ എന്ത് സംഭവിക്കുന്നു?</h2>
<p>ബോൾട്ട് ദ്വാരങ്ങളിലൂടെയും ജോയിന്റുകളിലൂടെയും ഈർപ്പമുള്ള വായു ഉള്ളിൽ കയറും. ഉള്ളിലെ സ്റ്റീലിൽ ഈർപ്പം പറ്റിപ്പിടിച്ച് തുരുമ്പ് തുടങ്ങും — പുറത്ത് കാണാതെ. പിന്നീട് പെയിന്റ് പൊങ്ങിവരുന്നതും ബോൾട്ടുകൾക്ക് ചുറ്റും തുരുമ്പ് പാടുകളും ജോയിന്റുകൾ ഇളകുന്നതും കാണാം.</p>
<h2>ഗാൽവനൈസ്ഡ് സ്റ്റീൽ എങ്ങനെ സംരക്ഷിക്കുന്നു?</h2>
<ul>
<li><strong>ഉള്ളിലും സിങ്ക്.</strong> ഗാൽവനൈസ്ഡ് ട്യൂബിന്റെ ഉൾഭാഗത്തും സിങ്ക് കോട്ടിംഗ് ഉണ്ട്.</li>
<li><strong>പോറലുകളിലും സംരക്ഷണം.</strong> സ്റ്റീലിന് മുൻപ് സിങ്ക് ദ്രവിക്കുന്നതിനാൽ, ചെറിയ പോറലുകളിൽ ചുറ്റുമുള്ള സിങ്ക് സ്റ്റീലിനെ സംരക്ഷിക്കുന്നു.</li>
<li><strong>അടർന്നുപോകില്ല.</strong> സിങ്ക് പാളി സ്റ്റീലിനോട് ചേർന്നിരിക്കുന്നതിനാൽ പെയിന്റ് പോലെ അടർന്നുപോകില്ല.</li>
</ul>
<h2>താരതമ്യം</h2>
{gtable('ml')}
<h2>Bunkworks കട്ടിലുകളുടെ ഫിനിഷ്</h2>
<p>Bunkworks ഫ്രെയിമുകൾ ഗാൽവനൈസ്ഡ് സ്റ്റീലിൽ <strong>എപ്പോക്സി കോട്ടിംഗ്</strong> ചെയ്തതാണ് — പൗഡർ കോട്ടിംഗ് അല്ല. സിംഗിൾ കട്ടിലിന് 100 കിലോ വരെയും ബങ്ക് ബെഡ്ഡിന് ആകെ 200 കിലോ വരെയും (ഓരോ തട്ടിനും 100 കിലോ) ഭാരശേഷിയുണ്ട്. കേരളത്തിലെ മഴക്കാല ഈർപ്പത്തിനും തീരദേശ കാലാവസ്ഥയ്ക്കും ഹോസ്റ്റലുകൾക്കും ഏറ്റവും അനുയോജ്യം.</p>
""",
 faqs=[('ഗാൽവനൈസ്ഡ് സ്റ്റീൽ തുരുമ്പെടുക്കുമോ?', 'പെയിന്റ് ചെയ്ത സ്റ്റീലിനേക്കാൾ വളരെ നന്നായി തുരുമ്പിനെ ചെറുക്കും. സിങ്ക് കോട്ടിംഗ് ട്യൂബിന്റെ അകത്തും പുറത്തും സംരക്ഷണം നൽകുന്നു.'),
       ('പെയിന്റ് ചെയ്ത കട്ടിൽ ഉള്ളിൽ നിന്ന് തുരുമ്പെടുക്കുന്നത് എന്തുകൊണ്ട്?', 'പൊള്ളയായ ട്യൂബിന്റെ ഉള്ളിൽ പെയിന്റ് ചെയ്യാൻ കഴിയില്ല. ഉള്ളിൽ കയറുന്ന ഈർപ്പം സംരക്ഷണമില്ലാത്ത സ്റ്റീലിനെ തുരുമ്പെടുപ്പിക്കും.'),
       ('Bunkworks കട്ടിലുകൾ പൗഡർ കോട്ട് ചെയ്തതാണോ?', 'അല്ല. ഗാൽവനൈസ്ഡ് സ്റ്റീലിൽ എപ്പോക്സി കോട്ടിംഗ് ആണ്.')]))

GALV_POSTS.append(dict(slug='galvanised-steel-bed-hindi', lang='hi', group='galv', read=4,
 title='गैल्वनाइज़्ड स्टील पलंग में जंग क्यों कम लगती है? पेंट वाले पलंग से तुलना',
 seo='गैल्वनाइज़्ड बनाम पेंट वाला स्टील पलंग: जंग से बचाव', short='गैल्वनाइज़्ड स्टील (हिंदी)',
 desc='गैल्वनाइज़्ड स्टील पलंग और बंक बेड पेंट वाले स्टील से बेहतर जंग क्यों रोकते हैं: ट्यूब के अंदर पेंट नहीं पहुँचता, जबकि ज़िंक अंदर-बाहर दोनों तरफ़ बचाता है।',
 keywords='गैल्वनाइज़्ड स्टील पलंग, जंग न लगने वाला पलंग, लोहे का पलंग जंग, बंक बेड, स्टील कॉट',
 thumb='blog-galvanised-steel-advantage-hi', alt='एपॉक्सी कोटिंग वाले गैल्वनाइज़्ड स्टील पलंग का कोना',
 excerpt='पेंट सिर्फ़ ट्यूब के बाहर लगता है। गैल्वनाइज़्ड स्टील पलंग ज़्यादा क्यों चलता है?',
 body=quick('hi', 'गैल्वनाइज़्ड स्टील पेंट वाले स्टील से बेहतर जंग रोकता है, क्योंकि ज़िंक की परत ट्यूब के बाहर और अंदर दोनों तरफ़ स्टील को बचाती है, और खरोंच लगने पर भी बचाव जारी रखती है। पेंट वाले पलंग में पेंट सिर्फ़ बाहर होता है — खोखली ट्यूब के अंदर पेंट नहीं किया जा सकता, इसलिए अंदर से जंग लग सकती है।') + f"""
<p class="lede">नए दिन हर स्टील पलंग एक जैसा दिखता है। फ़र्क कुछ बरसातों के बाद दिखता है — और वह वहाँ शुरू होता है जहाँ नज़र नहीं जाती: ट्यूब के अंदर।</p>
<h2>ट्यूब के अंदर पेंट क्यों नहीं हो सकता?</h2>
<p>पलंग का फ़्रेम खोखली ट्यूबों से बनता है। स्प्रे या ब्रश सिर्फ़ बाहरी सतह तक पहुँचते हैं; लंबी ट्यूब के अंदर पेंट करने का कोई व्यावहारिक तरीका नहीं है। इसलिए पेंट वाले पलंग की ट्यूब अंदर से खुला स्टील ही रहती है।</p>
<h2>पेंट वाली ट्यूब के अंदर क्या होता है?</h2>
<p>बोल्ट के छेद और जोड़ों से नमी वाली हवा अंदर जाती है। अंदर के खुले स्टील पर नमी जमती है और जंग शुरू हो जाती है — बिना दिखे। बाद में पेंट फूलना, बोल्ट के पास जंग के दाग और ढीले जोड़ दिखने लगते हैं।</p>
<h2>गैल्वनाइज़्ड स्टील कैसे बचाता है?</h2>
<ul>
<li><strong>अंदर भी ज़िंक।</strong> गैल्वनाइज़्ड ट्यूब की अंदरूनी सतह पर भी ज़िंक की परत होती है।</li>
<li><strong>खरोंच पर भी बचाव।</strong> ज़िंक स्टील से पहले घिसता है, इसलिए छोटी खरोंच पर आसपास का ज़िंक स्टील को बचाता रहता है।</li>
<li><strong>उखड़ता नहीं।</strong> ज़िंक की परत स्टील से जुड़ी होती है, पेंट की तरह उखड़ती नहीं।</li>
</ul>
<h2>तुलना</h2>
{gtable('hi')}
<h2>Bunkworks पलंग की फ़िनिश</h2>
<p>Bunkworks के फ़्रेम गैल्वनाइज़्ड स्टील पर <strong>एपॉक्सी कोटिंग</strong> वाले हैं — पाउडर कोटिंग नहीं। सिंगल कॉट 100 किलो तक और बंक बेड कुल 200 किलो तक (प्रति डेक 100 किलो) भार सहता है। नमी वाले मौसम, तटीय इलाकों और हॉस्टलों के लिए सबसे सही।</p>
""",
 faqs=[('क्या गैल्वनाइज़्ड स्टील में जंग लगती है?', 'पेंट वाले स्टील की तुलना में बहुत कम। ज़िंक की परत ट्यूब को अंदर और बाहर दोनों तरफ़ से बचाती है।'),
       ('पेंट वाले पलंग में अंदर से जंग क्यों लगती है?', 'खोखली ट्यूब के अंदर पेंट नहीं किया जा सकता। अंदर गई नमी खुले स्टील में जंग लगा देती है।'),
       ('क्या Bunkworks पलंग पाउडर कोटेड हैं?', 'नहीं। ये गैल्वनाइज़्ड स्टील पर एपॉक्सी कोटेड हैं।')]))

POSTS = [GALV_POSTS[0]] + NEW[:6] + GALV_POSTS[1:] + [NEW[6], NEW[7]] + BASE

POST_ALTS = {
 'hostel-setup-cost-india': 'Hostel dormitory with steel bunk beds — cost to start a 20-bed hostel or PG in India',
 'bunk-bed-bunker-cot-price-guide': 'Galvanised steel bunk bed (bunker cot, double decker bed) with plywood decks — bunk bed price guide for hostels',
 'steel-single-cot-for-hostel': 'Steel single cot with plywood base in a hostel room — single cot size and price guide',
 'hostel-beds-wholesale-factory-price': 'Stacked steel hostel bed frames ready for wholesale dispatch — factory price hostel beds and bulk discount',
 'galvanised-steel-vs-painted-steel-beds': 'Galvanised steel bed corner joint with 12mm plywood base — galvanised vs painted steel cot rust resistance',
 'cheapest-bunk-bed-price-india': 'Affordable steel double decker bed (bunk bed) for hostels — cheapest bunk bed price in India',
 'iron-cot-vs-steel-cot-price': 'Steel single cot with plywood base — iron cot vs steel cot price for hostels and PGs',
 'bunk-bed-size-guide': 'Bunk bed size diagram in feet, cm and inches — hostel bunk bed length, height and deck gap',
 'bunk-beds-for-adults': 'Steel bunk beds for adults in a hostel dormitory — heavy duty double decker bed, 200 kg total (100 kg per deck)',
 'hostel-setup-cost-malayalam': 'ഹോസ്റ്റൽ തുടങ്ങാൻ ചെലവ് — സ്റ്റീൽ ബങ്ക് ബെഡ്ഡുകളുള്ള ഹോസ്റ്റൽ മുറി, പിജി ഫർണിച്ചർ',
 'bunk-bed-price-malayalam': 'ബങ്ക് ബെഡ് വില കേരളത്തിൽ — ഹോസ്റ്റൽ മുറിയിലെ സ്റ്റീൽ ഡബിൾ ഡെക്കർ കട്ടിൽ (ബങ്കർ കോട്ട്)',
 'iron-cot-price-malayalam': 'ഇരുമ്പ് കട്ടിൽ വില — പ്ലൈവുഡ് ബേസുള്ള ഗാൽവനൈസ്ഡ് സ്റ്റീൽ സിംഗിൾ കട്ടിൽ, ഹോസ്റ്റൽ കട്ടിൽ',
 'galvanised-steel-cot-malayalam': 'ഗാൽവനൈസ്ഡ് സ്റ്റീൽ കട്ടിലിന്റെ എപ്പോക്സി കോട്ടിംഗുള്ള ഫ്രെയിം — തുരുമ്പെടുക്കാത്ത ബങ്ക് ബെഡ്, സിംഗിൾ കട്ടിൽ',
 'hostel-setup-cost-hindi': 'हॉस्टल शुरू करने का खर्च — स्टील बंक बेड वाला हॉस्टल और पीजी का कमरा',
 'bunk-bed-price-hindi': 'बंक बेड क्या होता है और कीमत — हॉस्टल के लिए स्टील डबल डेकर बेड (बंकर कॉट)',
 'iron-cot-price-hindi': 'लोहे का पलंग प्लाई वाला — हॉस्टल के लिए गैल्वनाइज़्ड स्टील सिंगल कॉट की कीमत',
 'galvanised-steel-bed-hindi': 'एपॉक्सी कोटिंग वाला गैल्वनाइज़्ड स्टील पलंग — जंग रोधी बंक बेड और सिंगल कॉट',
}
for _p in POSTS:
    _p['alt'] = POST_ALTS.get(_p['slug'], _p['alt'])
