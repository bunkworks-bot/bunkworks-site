# -*- coding: utf-8 -*-
"""All long-form page copy. Imported by site_extra.py (which is exec'd inside build_site.py)."""
import html as H
from content import inr
from content2 import OFFER, ACTIVE, B, BR, S, SR, PB, PS, swap, WA_BULK, MAIL_BULK, EMAIL

PCT = OFFER['off_pct']; NMIN = OFFER['bulk_min']; END = OFFER['end_label']['en']
PHONE_TXT = '+91 90724 31550'
UPDATED = '28 September 2026'
def T(n, p): return inr(n * p)

# ---------------------------------------------------------------- BUNKER COT / DOUBLE DECKER ----------
def bunk_price_fn():
    now = f'''<p>The Bunkworks steel bunker cot is priced at <strong>₹{B} per piece</strong> in our 5th Anniversary Offer — {PCT}% below the MRP of ₹{BR} — until {END} or while limited stock lasts. The price is per piece for the frame with its two plywood decks; mattresses are not included.</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Bunker cots</th><th scope="col">Sleepers</th><th scope="col">Offer price total</th></tr></thead><tbody>
<tr><td>10</td><td>20</td><td>₹{T(10, OFFER['bunk'])}</td></tr><tr><td>20</td><td>40</td><td>₹{T(20, OFFER['bunk'])}</td></tr><tr><td>40</td><td>80</td><td>₹{T(40, OFFER['bunk'])}</td></tr></tbody></table></div>
<p>Because one bunker cot sleeps two people, the frame works out at about ₹3,000 per sleeper. Ordering more than {NMIN} pieces? Ask for a <a href="#bulk-quote">bulk quote</a> instead of the standard price.</p>'''
    after = f'''<p>The Bunkworks steel bunker cot is priced at <strong>₹{PB} per piece</strong> for the frame with its two plywood decks, without mattress. Ask for a written quote for your quantity and delivery city.</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Bunker cots</th><th scope="col">Sleepers</th><th scope="col">Total at ₹{PB}</th></tr></thead><tbody>
<tr><td>10</td><td>20</td><td>₹{T(10, OFFER['bunk_after'])}</td></tr><tr><td>20</td><td>40</td><td>₹{T(20, OFFER['bunk_after'])}</td></tr><tr><td>40</td><td>80</td><td>₹{T(40, OFFER['bunk_after'])}</td></tr></tbody></table></div>
<p>Ordering more than {NMIN} pieces? Ask for a <a href="#bulk-quote">bulk quote</a>.</p>'''
    return swap(now, after, 'div')

BUNK_SECTIONS = [
('What is a bunker cot (double decker bed)?', '''
<p>In India, <strong>bunker cot</strong>, <strong>double decker bed</strong>, <strong>double decker cot</strong> and <strong>bunk bed</strong> all describe the same thing: a bed with two sleeping decks stacked on one frame. "Bunk bed" is the international term, "double decker bed" is what most buyers type into search, and "bunker cot" is the everyday word across Kerala and South India.</p>
<p>Whatever you call it, the advantage is the same — two people sleep in the floor space of one bed. For a hostel or PG owner that means twice the residents in the same room, so the rent you pay per bed falls sharply. The Bunkworks steel bunker cot is built for exactly that job: heavy-duty, bolted together and finished to withstand daily hostel use.</p>'''),

('Bunkworks steel bunker cot — specifications', '''
<div class="table-wrap"><table class="spec-table"><tbody>
<tr><th scope="row">Product</th><td>Bunkworks steel bunker cot (double decker bed / bunk bed)</td></tr>
<tr><th scope="row">Overall height</th><td>1.40 m (140 cm)</td></tr>
<tr><th scope="row">Deck size</th><td>183 × 76 cm (6 × 2.5 ft) per deck — two decks</td></tr>
<tr><th scope="row">Deck base</th><td>12mm thick plywood</td></tr>
<tr><th scope="row">Frame</th><td>Galvanised anti-rust steel</td></tr>
<tr><th scope="row">Coating</th><td>Epoxy coating (not powder coating)</td></tr>
<tr><th scope="row">Weight bearing</th><td>200 kg total (100 kg per deck)</td></tr>
<tr><th scope="row">Safety features</th><td>Top guard rail and ladder handle</td></tr>
<tr><th scope="row">Assembly</th><td>Bolt-together; legs and platforms supplied separately for easy transport</td></tr>
<tr><th scope="row">Mattress</th><td>Not included</td></tr>
<tr><th scope="row">Made in</th><td>Kerala, India (Bunkworks workshop)</td></tr>
</tbody></table></div>
<p>Need a different size? Custom sizes are available on request — mention them when you <a href="#bulk-quote">ask for a quote</a>.</p>'''),

('How much does a bunker cot cost?', None),   # price block injected (dynamic)

('Why galvanised steel with an epoxy coating?', '''
<p>Most low-cost bunker cots are made from mild steel and simply painted. Paint only covers the outside of a hollow steel tube — it cannot be applied inside — so the inner surface stays bare and can rust from within, especially in humid or coastal climates like Kerala's.</p>
<p>Galvanised steel carries a zinc coating on the inside as well as the outside of the tube, and the surrounding zinc keeps protecting the steel where it gets scratched. Bunkworks bunker cots are galvanised and then given an <strong>epoxy coating</strong> (not powder coating) for a durable finish. Read the full explanation in our guide: <a href="/blog/galvanised-steel-vs-painted-steel-beds/">galvanised vs painted steel beds</a>.</p>'''),

('What makes it strong enough for hostel use?', '''
<ul>
<li><strong>12mm plywood decks</strong> spread the load evenly and resist the bowing that thin 8mm boards show over time.</li>
<li><strong>Bolted joints</strong> can be tightened, repaired and dismantled — no cutting or re-welding when you move or refurbish a room.</li>
<li><strong>Top guard rail and ladder handle</strong> make the upper deck safer to climb and sleep on.</li>
<li><strong>Rated 200 kg in total, 100 kg per deck</strong> — plan each sleeper's weight within the per-deck limit; see our guide to <a href="/blog/bunk-beds-for-adults/">bunk beds for adults</a> for what else to check.</li>
<li><strong>Protected feet</strong> help guard tiled and polished floors.</li>
</ul>'''),

('Who buys bunker cots?', '''
<ul>
<li>Student hostels and working-professional PGs</li>
<li>Dormitories in schools, colleges and training institutes</li>
<li>Staff and labour accommodation</li>
<li>Guest houses, hostels and homestays that sell dormitory beds</li>
<li>Any institution that needs to sleep more people in less space</li>
</ul>
<p>Starting from scratch? Our <a href="/blog/hostel-setup-cost-india/">hostel setup cost guide</a> (also in <a href="/blog/hostel-setup-cost-malayalam/" lang="ml">മലയാളം</a> and <a href="/blog/hostel-setup-cost-hindi/" lang="hi">हिंदी</a>) shows where furniture fits in the budget.</p>'''),

('How many bunker cots does a hostel room need?', '''
<p>Each bunker cot uses the floor area of one single bed and sleeps two, so the maths is simple — divide the number of residents by two.</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Residents to accommodate</th><th scope="col">Bunker cots needed</th></tr></thead><tbody>
<tr><td>10</td><td>5</td></tr><tr><td>20</td><td>10</td></tr><tr><td>50</td><td>25</td></tr><tr><td>100</td><td>50</td></tr><tr><td>200</td><td>100</td></tr></tbody></table></div>
<p>Before you finalise, measure the room, keep a clear walkway along each bed, place ladders on the walkway side and check the position of ceiling fans, windows and switches. Our <a href="/blog/bunk-bed-size-guide/">bunk bed size guide</a> covers the numbers in feet, cm and inches.</p>'''),

('Delivery and assembly', '''
<p>Bunkworks bunker cots are supplied with the legs and platforms separate, which makes them easy to carry through stairwells and doors and keeps transport cost down. Assembly is bolt-together:</p>
<ol>
<li><strong>Lay the frames sideways</strong> — place each leg-end pair flat on its side.</li>
<li><strong>Position the platform</strong> between the matching leg pairs.</li>
<li><strong>Bolt evenly</strong> — hand-start every bolt first, then tighten in sequence.</li>
<li><strong>Stand upright</strong> with a second person and check every joint.</li>
</ol>
<p>Delivery cost and timing depend on your quantity and city, so both are confirmed in your written quote. See also our <a href="/shipping-delivery/">shipping and delivery</a> page.</p>'''),

('Bunker cot or two single cots?', '''
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col"></th><th scope="col">One bunker cot</th><th scope="col">Two single cots</th></tr></thead><tbody>
<tr><td>Sleepers</td><td>2</td><td>2</td></tr>
<tr><td>Floor space used</td><td>Footprint of one bed</td><td>Footprint of two beds</td></tr>
<tr><td>Height</td><td>1.40 m</td><td>40 cm each</td></tr>
<tr><td>Best for</td><td>Maximum beds per room</td><td>Low ceilings, easy access, private rooms</td></tr>
</tbody></table></div>
<p>Choose bunker cots when the goal is the most beds per room; choose <a href="/steel-single-cot/">steel single cots</a> when ceilings are low or residents need easy access. Many hostels use both.</p>'''),

('Questions to ask any supplier before a bulk order', '''
<ul>
<li>What steel is the frame made from, and is it galvanised inside the tube?</li>
<li>What is the finish — epoxy, powder coat or plain paint?</li>
<li>How thick is the deck base (12mm or thinner)?</li>
<li>What weight-bearing capacity is stated in writing?</li>
<li>Is it bolted and flat-packed for delivery?</li>
<li>What is the per-piece price at my quantity, delivered to my city?</li>
</ul>
<p>Bunkworks answers all of these in the quote. See how factory-direct pricing works in <a href="/blog/hostel-beds-wholesale-factory-price/">hostel beds wholesale</a>.</p>'''),
]

def bunk_faqs():
    return [
     ('What is the price of the Bunkworks bunker cot (double decker bed)?',
      (f'₹{B} per piece in the 5th Anniversary Offer ({PCT}% off the MRP of ₹{BR}) until {END} or while stock lasts. ' if ACTIVE else f'₹{PB} per piece. ') + 'The price is for the frame with two plywood decks, without mattress. Orders above ' + str(NMIN) + ' pieces get a bulk quote.'),
     ('Is a bunker cot the same as a double decker bed or bunk bed?', 'Yes. Bunker cot, double decker bed, double decker cot and bunk bed all describe two sleeping decks on one frame.'),
     ('What is the weight-bearing capacity?', 'The Bunkworks steel bunker cot has a 200 kg total weight-bearing capacity, which is 100 kg per deck. Do not exceed the per-deck limit.'),
     ('What is the height and size?', 'It is 1.40 m (140 cm) high. Each deck is 183 × 76 cm (6 × 2.5 ft) on a 12mm plywood base.'),
     ('Is it powder coated?', 'No. The frame is galvanised steel with an epoxy coating.'),
     ('Will it rust in Kerala\'s humid climate?', 'Galvanised steel resists rust far better than painted mild steel because the zinc coating protects the tube inside and out and keeps protecting it at scratches.'),
     ('Is the mattress included?', 'No. The price covers the steel frame with its two 12mm plywood decks, guard rail and ladder handle. Tell us if you also need mattresses.'),
     ('How is it delivered and assembled?', 'Legs and platforms are supplied separately for easy transport, and the bed is assembled with bolts — no welding on site.'),
     ('Can I order custom sizes?', 'Yes, custom sizes are available on request. Mention the size in your quote request.'),
     ('Do you offer bulk pricing?', f'Yes. For more than {NMIN} pieces request a bulk quote on WhatsApp ({PHONE_TXT}) or by email at {EMAIL}.'),
     ('Where is it made and can you deliver to my city?', 'It is made in our workshop in Kerala, India. Tell us your delivery city and we confirm the delivery cost and timeline in your quote.'),
    ]

# ---------------------------------------------------------------- STEEL SINGLE COT ----------
def single_price_fn():
    now = f'''<p>The Bunkworks steel single cot is priced at <strong>₹{S} per piece</strong> in our 5th Anniversary Offer — {PCT}% below the MRP of ₹{SR} — until {END} or while limited stock lasts. The price is per piece for the frame with its 12mm plywood base; mattresses are not included.</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Single cots</th><th scope="col">Offer price total</th></tr></thead><tbody>
<tr><td>10</td><td>₹{T(10, OFFER['single'])}</td></tr><tr><td>20</td><td>₹{T(20, OFFER['single'])}</td></tr><tr><td>40</td><td>₹{T(40, OFFER['single'])}</td></tr></tbody></table></div>
<p>Ordering more than {NMIN} pieces? Ask for a <a href="#bulk-quote">bulk quote</a>.</p>'''
    after = f'''<p>The Bunkworks steel single cot is priced at <strong>₹{PS} per piece</strong> for the frame with its 12mm plywood base, without mattress. Ask for a written quote for your quantity and delivery city.</p>
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Single cots</th><th scope="col">Total at ₹{PS}</th></tr></thead><tbody>
<tr><td>10</td><td>₹{T(10, OFFER['single_after'])}</td></tr><tr><td>20</td><td>₹{T(20, OFFER['single_after'])}</td></tr><tr><td>40</td><td>₹{T(40, OFFER['single_after'])}</td></tr></tbody></table></div>
<p>Ordering more than {NMIN} pieces? Ask for a <a href="#bulk-quote">bulk quote</a>.</p>'''
    return swap(now, after, 'div')

SINGLE_SECTIONS = [
('What is a steel single cot?', '''
<p>A <strong>single cot</strong> — also called a <strong>single bed</strong> or, in everyday speech, an <strong>iron cot</strong> or <strong>steel cot</strong> — is a one-person bed on a metal frame. The Bunkworks steel single cot is a low, sturdy hostel bed: 6 × 2.5 ft (183 × 76 cm), just 40 cm high, with a solid 12mm plywood base and a galvanised steel frame.</p>
<p>It is the right choice when a bunk bed does not suit the room — low ceilings, ceiling fans, residents who need easy access, or private single rooms that you rent at a premium.</p>'''),

('Bunkworks steel single cot — specifications', '''
<div class="table-wrap"><table class="spec-table"><tbody>
<tr><th scope="row">Product</th><td>Bunkworks steel single cot (single bed for hostels)</td></tr>
<tr><th scope="row">Size (L × W)</th><td>6 × 2.5 ft (183 × 76 cm)</td></tr>
<tr><th scope="row">Height</th><td>40 cm</td></tr>
<tr><th scope="row">Base</th><td>12mm thick plywood</td></tr>
<tr><th scope="row">Frame</th><td>Galvanised anti-rust steel</td></tr>
<tr><th scope="row">Coating</th><td>Epoxy coating (not powder coating), grey</td></tr>
<tr><th scope="row">Load capacity</th><td>Up to 100 kg</td></tr>
<tr><th scope="row">Feet</th><td>Anti-skid leg bushes protect the floor</td></tr>
<tr><th scope="row">Assembly</th><td>Bolt-together; one person can assemble it</td></tr>
<tr><th scope="row">Mattress</th><td>Not included</td></tr>
<tr><th scope="row">Made in</th><td>Kerala, India (Bunkworks workshop)</td></tr>
</tbody></table></div>
<p>Need a different size? Custom sizes are available on request — mention them when you <a href="#bulk-quote">ask for a quote</a>.</p>'''),

('How much does a steel single cot cost?', None),

('Why galvanised steel instead of an ordinary painted "iron cot"?', '''
<p>Most cots sold as "iron cots" are painted mild steel. The paint protects only the outside of the tube; the inside stays bare and can rust from within, and any chip in the paint lets rust start. Galvanised steel is zinc-coated inside and out, and the zinc keeps protecting the steel around scratches.</p>
<p>Bunkworks single cots are galvanised and finished with an <strong>epoxy coating</strong> (not powder coating). The result lasts longer in humid Kerala rooms, which is why it costs less over the life of the bed. More detail in <a href="/blog/iron-cot-vs-steel-cot-price/">iron cot vs steel cot</a> and <a href="/blog/galvanised-steel-vs-painted-steel-beds/">galvanised vs painted steel beds</a>.</p>'''),

('Why a 12mm plywood base?', '''
<p>A thick, solid base spreads the load evenly under the mattress and does not sag or press into the mattress the way thin sheets or widely spaced steel strips can. Bunkworks uses <strong>12mm plywood</strong> rather than 8mm boards, so the cot stays flat through years of daily use. The single cot is rated for up to 100 kg.</p>'''),

('Where does a single cot fit best?', '''
<ul>
<li>Rooms with low ceilings or ceiling fans, where a bunk bed would be uncomfortable</li>
<li>Private single rooms in hostels and PGs</li>
<li>Residents who need easy access — the 40 cm frame is simple to get on and off</li>
<li>Staff quarters, guest rooms and institutional rooms</li>
<li>Homes that need a sturdy extra bed</li>
</ul>
<p>Comparing options? Read our <a href="/blog/steel-single-cot-for-hostel/">steel single cot size and price guide</a> and the <a href="/blog/bunk-bed-size-guide/">bunk bed size guide</a>.</p>'''),

('Steel single cot size guide', '''
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Unit</th><th scope="col">Length</th><th scope="col">Width</th><th scope="col">Height</th></tr></thead><tbody>
<tr><td>Feet</td><td>6 ft</td><td>2.5 ft</td><td>—</td></tr><tr><td>Inches</td><td>72 in</td><td>30 in</td><td>—</td></tr>
<tr><td>Centimetres</td><td>183 cm</td><td>76 cm</td><td>40 cm</td></tr><tr><td>Millimetres</td><td>1830 mm</td><td>760 mm</td><td>400 mm</td></tr></tbody></table></div>
<p>The cot takes a standard single mattress. The frame is slightly larger than the mattress, so confirm the outside dimensions when you plan room layouts.</p>'''),

('Delivery and assembly', '''
<p>The single cot is bolt-together and light enough for one person to assemble without help:</p>
<ol>
<li><strong>Attach the legs</strong> — bolt each leg bracket to the frame corners.</li>
<li><strong>Fit the base</strong> — slot the 12mm plywood base onto the frame ledges.</li>
<li><strong>Bolt evenly</strong> — hand-start every bolt first, then tighten in sequence.</li>
<li><strong>Check and level</strong> — confirm all four anti-skid feet sit flat on the floor.</li>
</ol>
<p>Delivery cost and timing depend on your quantity and city and are confirmed in your written quote. See our <a href="/shipping-delivery/">shipping and delivery</a> page.</p>'''),

('Single cot or bunker cot?', '''
<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col"></th><th scope="col">Steel single cot</th><th scope="col">Steel bunker cot</th></tr></thead><tbody>
<tr><td>Sleepers per unit</td><td>1</td><td>2</td></tr><tr><td>Height</td><td>40 cm</td><td>1.40 m</td></tr>
<tr><td>Load</td><td>Up to 100 kg</td><td>200 kg total (100 kg per deck)</td></tr><tr><td>Best for</td><td>Low ceilings, easy access, private rooms</td><td>Most beds per room</td></tr></tbody></table></div>
<p>Need maximum capacity? See the <a href="/bunker-cot-double-decker-bed/">steel bunker cot (double decker bed)</a>.</p>'''),

('Care and maintenance', '''
<ul>
<li>Wipe the frame with a dry or lightly damp cloth; avoid abrasive or acidic cleaners on the epoxy finish.</li>
<li>Recheck and retighten the bolts after the first few weeks of use, then every few months.</li>
<li>Keep bedding directly on the plywood base provided — do not add a rigid board on top.</li>
<li>Tell us early about any scratch through to the galvanised layer so touch-up can stop rust spreading.</li>
</ul>'''),

('Questions to ask any supplier before a bulk order', '''
<ul>
<li>Is the frame galvanised, and what is the finish — epoxy, powder coat or plain paint?</li>
<li>How thick is the base, and is it solid plywood rather than strips or thin sheet?</li>
<li>What load is stated in writing?</li>
<li>Is it bolted, and can it be dismantled and moved?</li>
<li>What is the per-piece price at my quantity, delivered to my city?</li>
</ul>
<p>Bunkworks answers all of these in the quote. See <a href="/blog/hostel-beds-wholesale-factory-price/">how factory-direct wholesale works</a>.</p>'''),
]

def single_faqs():
    return [
     ('What is the price of the Bunkworks steel single cot?',
      (f'₹{S} per piece in the 5th Anniversary Offer ({PCT}% off the MRP of ₹{SR}) until {END} or while stock lasts. ' if ACTIVE else f'₹{PS} per piece. ') + 'The price is for the frame with its 12mm plywood base, without mattress. Orders above ' + str(NMIN) + ' pieces get a bulk quote.'),
     ('What size is the single cot?', '6 × 2.5 ft (183 × 76 cm) and 40 cm high. It takes a standard single mattress.'),
     ('How much weight can it take?', 'The Bunkworks steel single cot is rated for up to 100 kg.'),
     ('Is a single cot the same as a single bed or an iron cot?', 'Yes. Single cot, single bed, iron cot and steel cot are everyday names for a one-person bed on a metal frame. The Bunkworks cot is galvanised steel rather than painted mild steel.'),
     ('Is it powder coated?', 'No. The frame is galvanised steel with an epoxy coating.'),
     ('Will it rust?', 'Galvanised steel resists rust far better than painted mild steel because the zinc protects the tube inside and out and keeps protecting it at scratches.'),
     ('Is a plywood base better than steel strips?', 'A solid 12mm plywood base spreads the load evenly and does not sag or press into the mattress the way thin sheets or strips can.'),
     ('Can one person assemble it?', 'Yes. It is bolt-together and light enough for one person to assemble without help.'),
     ('Can I order custom sizes?', 'Yes, custom sizes are available on request. Mention the size in your quote request.'),
     ('Do you offer bulk pricing?', f'Yes. For more than {NMIN} pieces request a bulk quote on WhatsApp ({PHONE_TXT}) or by email at {EMAIL}.'),
    ]

# ---------------------------------------------------------------- BULK QUOTE page ----------
BULK_FAQS = [
 ('What counts as a bulk order?', f'Orders of more than {NMIN} pieces get a separate bulk quote from Bunkworks. Smaller orders are priced at the standard per-piece price shown on our product pages.'),
 ('What should I include in a bulk quote request?', 'The number of bunker cots and single cots, any custom size, your delivery city, whether the site has stairs or a lift, your opening date and whether you also need mattresses.'),
 ('How do I request a bulk quote?', f'Use the form on this page, message us on WhatsApp at {PHONE_TXT}, or email {EMAIL}. The form opens WhatsApp or your email app with your details pre-filled.'),
 ('Can you supply a whole hostel — bunker cots and single cots together?', 'Yes. We can supply coordinated bunker cots and single cots for an entire hostel, PG or institution in one order.'),
 ('Can deliveries be planned to match my opening date?', 'Tell us your opening date in the quote request; delivery timing is confirmed in the written quote.'),
 ('Where are the beds made?', 'In the Bunkworks workshop in Kerala, India, and supplied factory-direct.'),
]

def bulk_body():
    steps = ('<ol class="steps-list"><li><strong>Send your requirement</strong> — quantities, sizes, delivery city and opening date.</li>'
             '<li><strong>Get a written quote</strong> — factory-direct per-piece price, delivery cost and timing.</li>'
             '<li><strong>Confirm the order</strong> — payment and delivery terms are agreed in writing.</li>'
             '<li><strong>Delivery and assembly</strong> — beds arrive flat-packed with legs and platforms separate; assembly is bolt-together.</li></ol>')
    plan = ('<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">Hostel size (beds)</th><th scope="col">All bunker cots</th><th scope="col">All single cots</th></tr></thead><tbody>'
            '<tr><td>20</td><td>10 bunker cots</td><td>20 single cots</td></tr><tr><td>50</td><td>25 bunker cots</td><td>50 single cots</td></tr>'
            '<tr><td>100</td><td>50 bunker cots</td><td>100 single cots</td></tr><tr><td>200</td><td>100 bunker cots</td><td>200 single cots</td></tr></tbody></table></div>')
    return steps, plan

# ---------------------------------------------------------------- ABOUT ----------
ABOUT_HTML = f'''
<p class="lede"><strong>Bunkworks</strong> is a steel furniture manufacturer in Kerala, India. We design and build bunker cots (double decker beds), single cots and related hostel furniture for hostels, PGs, dormitories and institutions — and we sell direct to businesses, by the piece or in bulk. This year Bunkworks turns five.</p>
<h2>What we make</h2>
<ul>
<li><a href="/bunker-cot-double-decker-bed/"><strong>Steel bunker cots (double decker beds)</strong></a> — two decks on one galvanised steel frame, 1.40 m high, 200 kg total weight bearing (100 kg per deck).</li>
<li><a href="/steel-single-cot/"><strong>Steel single cots</strong></a> — 6 × 2.5 ft, 40 cm high, 12mm plywood base, up to 100 kg.</li>
<li><strong>Cots and folding beds</strong> and two named collections, <strong>Swadesh</strong> and <strong>Perunthachan</strong>, on request.</li>
</ul>
<h2>How we build</h2>
<p>Every frame is made from galvanised steel — zinc-coated inside and out — and finished with an epoxy coating. Decks and bases are 12mm plywood rather than thinner boards. Joints are bolted, and legs and platforms ship separately, so the furniture is easy to transport, assemble and repair.</p>
<h2>Who we serve</h2>
<p>Student hostels, working-professional PGs, dormitories, staff accommodation and institutions across Kerala and beyond. Because we manufacture in our own workshop, we can quote coordinated furniture for an entire project, from a single room to hundreds of beds.</p>
<h2>Why factory-direct</h2>
<p>Buying from the maker removes dealer margin, gives you identical batches, and lets us discuss custom sizes and delivery plans directly. Read how it works in our guide to <a href="/blog/hostel-beds-wholesale-factory-price/">buying hostel beds wholesale</a>.</p>
<h2>Our promise: furniture for spaces that work</h2>
<p>Our tagline is a design brief. Hostel furniture has to survive humidity, daily use and constant moving — so we choose materials for durability first and ask you to compare specifications, not just prices.</p>
'''

# ---------------------------------------------------------------- LEGAL ----------
def privacy_html():
    return f'''
<p><em>Last updated: {UPDATED}</em></p>
<p>This policy explains how Bunkworks ("we", "us"), a steel furniture manufacturer in Kerala, India, handles personal information when you use www.bunkworks.com or contact us about our products.</p>
<h2>Information we collect</h2>
<p>When you contact us by WhatsApp, email, phone or the enquiry form, you may give us your name, organisation or hostel name, city, phone number, email address, the products and quantities you are interested in, and any message you write. We do not run user accounts and we do not take payments on this website.</p>
<h2>How the enquiry form works</h2>
<p>The quote form on our website does not send your details to our servers. When you press a button it opens WhatsApp or your email app with your message pre-filled, and nothing is sent until you press send in that app. Messages you send are then processed by the messaging or email provider you use (for example WhatsApp or Gmail) under their own privacy policies.</p>
<h2>Technical information and cookies</h2>
<p>Our web host and Google Fonts (fonts.googleapis.com and fonts.gstatic.com) may receive your IP address and basic browser details when pages load. We do not currently use advertising cookies. Our offer pop-up stores a small flag in your browser's session storage so that it is not shown repeatedly during one visit; it stays on your device and disappears when you close the browser tab.</p>
<h2>How we use information</h2>
<ul><li>to reply to your enquiry and prepare quotes;</li><li>to take and deliver orders, and provide after-sales support;</li><li>to keep records required by law, tax and accounting rules;</li><li>to improve our website and products.</li></ul>
<h2>Sharing</h2>
<p>We do not sell personal information. We share it only where needed to fulfil your order (for example transport partners), with professional advisers, or when the law requires it.</p>
<h2>Retention and security</h2>
<p>We keep enquiry and order records for as long as needed for the purposes above and to meet legal obligations, and take reasonable steps to protect them.</p>
<h2>Your choices</h2>
<p>You may ask us to access, correct or delete the personal information we hold about you, or to stop contacting you, by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. We handle personal data in line with applicable Indian law, including the Digital Personal Data Protection Act, 2023.</p>
<h2>Children</h2>
<p>Our website is intended for businesses and adults and is not directed at children.</p>
<h2>Changes to this policy</h2>
<p>We may update this policy and will change the date above when we do.</p>
<h2>Contact</h2>
<p>Bunkworks, Kerala, India · <a href="tel:+919072431550">{PHONE_TXT}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''

def terms_html():
    return f'''
<p><em>Last updated: {UPDATED}</em></p>
<p>These terms cover your use of www.bunkworks.com and the sale of Bunkworks products. By using the website or placing an order you agree to them.</p>
<h2>1. Product information</h2>
<p>We describe our products as accurately as we can. Photographs and renderings on this website are illustrative; colours, grain and finish may vary slightly. The specification stated in your written quote or invoice prevails.</p>
<h2>2. Prices and offers</h2>
<p>Prices are per piece, without mattress, unless stated otherwise. Whether GST and delivery are included is stated in your written quote. Offers such as anniversary or seasonal offers apply for the period shown or while limited stock lasts, and may be changed or withdrawn. "MRP" means the maximum retail price we declare for the product.</p>
<h2>3. Quotes and orders</h2>
<p>An order is confirmed only when we confirm it in writing (WhatsApp, email or invoice) and any advance payment stated in the quote has been received. Payment terms are as agreed in the quote. Bulk orders are priced by written quote.</p>
<h2>4. Delivery</h2>
<p>Delivery cost and timing are confirmed per order. See our <a href="/shipping-delivery/">shipping and delivery</a> page.</p>
<h2>5. Use of the products</h2>
<p>Follow the assembly instructions, keep within the stated load — up to 100 kg for the single cot and 200 kg in total (100 kg per deck) for the bunker cot — and tighten bolts periodically. Misuse or overloading is at the user's risk.</p>
<h2>6. Warranty, changes and cancellation</h2>
<p>Any warranty terms are stated in your quote or invoice. Custom-size and bulk orders are made to order, so changes or cancellation after production has started are subject to our written agreement.</p>
<h2>7. Liability</h2>
<p>To the extent permitted by law, we are not liable for indirect or consequential loss. Nothing in these terms limits any right or liability that cannot be limited by law, including your rights under applicable consumer-protection law.</p>
<h2>8. Intellectual property</h2>
<p>The Bunkworks name, logo, text and images on this website belong to Bunkworks and may not be reused without permission.</p>
<h2>9. Governing law</h2>
<p>These terms are governed by the laws of India, and the courts in Kerala have jurisdiction, subject to any mandatory consumer-protection rules.</p>
<h2>10. Contact</h2>
<p><a href="tel:+919072431550">{PHONE_TXT}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
'''

def shipping_html():
    return f'''
<p><em>Last updated: {UPDATED}</em></p>
<h2>Made in Kerala, delivered to your site</h2>
<p>Bunkworks beds are made in our workshop in Kerala, India. Delivery cost and timing depend on your quantity, delivery city and site access, and are confirmed in your written quote.</p>
<h2>Flat-packed for easy transport</h2>
<p>Legs and platforms are supplied separately, so beds are easy to carry through stairwells and doors and take up less space in transport. Assembly is bolt-together — see the assembly steps on the <a href="/bunker-cot-double-decker-bed/">bunker cot</a> and <a href="/steel-single-cot/">single cot</a> pages.</p>
<h2>Before delivery</h2>
<ul><li>Tell us your delivery address, a contact person and phone number.</li><li>Mention stairs, lifts and any access limits so we can plan unloading.</li><li>For large projects, tell us your opening date; deliveries can be planned around it.</li></ul>
<h2>On delivery</h2>
<p>Please check the packages when they arrive and tell us immediately, ideally with photos, about visible damage or missing parts, so we can put it right quickly.</p>
<h2>Timelines and costs</h2>
<p>Lead times depend on stock and the size of the order and are stated in your quote. Delivery charges, GST and installation, where applicable, are also stated in the quote.</p>
<h2>Questions?</h2>
<p>WhatsApp <a href="tel:+919072431550">{PHONE_TXT}</a> or email <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
'''
