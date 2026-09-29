# -*- coding: utf-8 -*-
DATE = '2026-09-27'

def inr(n):
    s = str(n)
    if len(s) <= 3: return s
    last, rest, g = s[-3:], s[:-3], []
    while len(rest) > 2: g.insert(0, rest[-2:]); rest = rest[:-2]
    if rest: g.insert(0, rest)
    return ','.join(g) + ',' + last

COST_ROWS = [('bunk', 70000, 150000), ('mattress', 40000, 100000), ('linen', 16000, 40000),
             ('lockers', 50000, 100000), ('study', 50000, 120000), ('reno', 50000, 300000),
             ('water', 30000, 80000), ('power', 25000, 80000), ('cctv', 25000, 75000),
             ('fire', 10000, 30000), ('licence', 10000, 50000), ('kitchen', 0, 250000)]

LABELS = {
 'en': {'head': ('Item', 'Low', 'High'), 'total': 'Total setup cost',
   'bunk': 'Steel bunk beds (10 units = 20 beds)', 'mattress': 'Mattresses (20)', 'linen': 'Pillows and bedsheets (2 sets per bed)',
   'lockers': 'Lockers (20)', 'study': 'Study tables and chairs (20)', 'reno': 'Renovation, painting and electrical work',
   'water': 'Water purifier and geysers', 'power': 'Power backup (inverter)', 'cctv': 'CCTV and Wi-Fi',
   'fire': 'Fire safety (extinguishers, signage)', 'licence': 'Licences and registrations', 'kitchen': 'Kitchen (only if you run a mess)'},
 'ml': {'head': ('ഇനം', 'കുറഞ്ഞത്', 'കൂടിയത്'), 'total': 'ആകെ സജ്ജീകരണ ചെലവ്',
   'bunk': 'സ്റ്റീൽ ബങ്ക് ബെഡ് (10 എണ്ണം = 20 കിടക്കകൾ)', 'mattress': 'മെത്തകൾ (20)', 'linen': 'തലയണയും ബെഡ്ഷീറ്റും (ഓരോ കിടക്കയ്ക്കും 2 സെറ്റ്)',
   'lockers': 'ലോക്കറുകൾ (20)', 'study': 'പഠന മേശയും കസേരയും (20)', 'reno': 'നവീകരണം, പെയിന്റിംഗ്, ഇലക്ട്രിക്കൽ ജോലികൾ',
   'water': 'വാട്ടർ പ്യൂരിഫയറും ഗീസറും', 'power': 'പവർ ബാക്കപ്പ് (ഇൻവെർട്ടർ)', 'cctv': 'സിസിടിവിയും വൈ-ഫൈയും',
   'fire': 'അഗ്നി സുരക്ഷ (എക്സ്റ്റിംഗ്വിഷറുകൾ, സൂചനാ ബോർഡുകൾ)', 'licence': 'ലൈസൻസുകളും രജിസ്ട്രേഷനും', 'kitchen': 'അടുക്കള (മെസ് നടത്തുന്നുണ്ടെങ്കിൽ മാത്രം)'},
 'hi': {'head': ('मद', 'न्यूनतम', 'अधिकतम'), 'total': 'कुल सेटअप खर्च',
   'bunk': 'स्टील बंक बेड (10 यूनिट = 20 बेड)', 'mattress': 'गद्दे (20)', 'linen': 'तकिये और चादरें (हर बेड के लिए 2 सेट)',
   'lockers': 'लॉकर (20)', 'study': 'स्टडी टेबल और कुर्सी (20)', 'reno': 'मरम्मत, पेंटिंग और बिजली का काम',
   'water': 'वॉटर प्यूरीफायर और गीज़र', 'power': 'पावर बैकअप (इन्वर्टर)', 'cctv': 'सीसीटीवी और वाई-फ़ाई',
   'fire': 'अग्नि सुरक्षा (फ़ायर एक्सटिंग्विशर, संकेत बोर्ड)', 'licence': 'लाइसेंस और पंजीकरण', 'kitchen': 'रसोई (केवल अगर आप मेस चलाते हैं)'},
}

def cost_table(lang):
    L = LABELS[lang]; lo = sum(r[1] for r in COST_ROWS); hi = sum(r[2] for r in COST_ROWS)
    rows = ''.join(f'<tr><td>{L[k]}</td><td>₹{inr(a)}</td><td>₹{inr(b)}</td></tr>' for k, a, b in COST_ROWS)
    h = L['head']
    return (f'<div class="table-wrap"><table class="cost-table"><thead><tr><th scope="col">{h[0]}</th><th scope="col">{h[1]}</th><th scope="col">{h[2]}</th></tr></thead>'
            f'<tbody>{rows}</tbody><tfoot><tr><th scope="row">{L["total"]}</th><td>₹{inr(lo)}</td><td>₹{inr(hi)}</td></tr></tfoot></table></div>')

UI = {
 'en': {'faq': 'Frequently asked questions', 'more': 'Keep reading', 'read': 'Read in', 'min': 'min read', 'date': '27 September 2026',
        'cta': 'Planning a hostel? Get a factory-direct quote for bunk beds and single cots.', 'cta_btn': 'Get a Quote', 'chip': 'English'},
 'ml': {'faq': 'പതിവായി ചോദിക്കുന്ന ചോദ്യങ്ങൾ', 'more': 'കൂടുതൽ വായിക്കാൻ', 'read': 'ഈ ലേഖനം വായിക്കാം', 'min': 'മിനിറ്റ് വായന', 'date': '2026 സെപ്റ്റംബർ 27',
        'cta': 'ഹോസ്റ്റൽ തുടങ്ങാൻ പ്ലാൻ ചെയ്യുന്നുണ്ടോ? ബങ്ക് ബെഡ്ഡുകൾക്കും സിംഗിൾ കട്ടിലുകൾക്കും ഫാക്ടറി നിരക്കിൽ ക്വട്ടേഷൻ നേടൂ.', 'cta_btn': 'ക്വട്ടേഷൻ ചോദിക്കൂ', 'chip': 'മലയാളം'},
 'hi': {'faq': 'अक्सर पूछे जाने वाले सवाल', 'more': 'और पढ़ें', 'read': 'यह लेख पढ़ें', 'min': 'मिनट में पढ़ें', 'date': '27 सितंबर 2026',
        'cta': 'हॉस्टल शुरू करने की योजना है? बंक बेड और सिंगल कॉट के लिए फ़ैक्टरी रेट पर कोटेशन पाएँ।', 'cta_btn': 'कोटेशन माँगें', 'chip': 'हिंदी'},
}

POSTS = []

POSTS.append(dict(
 slug='hostel-setup-cost-india', lang='en', group='hostel-cost', read=7,
 title='How Much Does It Cost to Start a Hostel or PG in India? (2026 Guide)',
 desc='A line-by-line 2026 budget for starting a 20-bed hostel or PG in India: rent deposit, bunk beds, mattresses, renovation, licences and working capital.',
 keywords='cost to start a hostel, PG business cost, hostel setup cost India, hostel furniture cost, bunk bed price',
 thumb='blog-hostel-setup-cost', alt='Hostel dormitory fitted with steel bunk beds, used to illustrate the cost of starting a hostel',
 excerpt='A line-by-line budget for a 20-bed hostel or PG — furniture, renovation, licences and the cash you need before opening.',
 body=f'''
<p class="lede">Demand for student and working-professional hostels keeps growing across India. Before you sign a lease, the first question is always the same: how much money do you actually need? Here is a realistic budget for a 20-bed hostel.</p>
<h2>The short answer</h2>
<p>For a 20-bed hostel or PG in a rented building, setup costs in 2026 commonly land between about <strong>₹3.8 lakh and ₹13.8 lakh</strong>, before the rental deposit and working capital. Where you fall in that range depends mostly on whether you run a mess, how much renovation the building needs, and the quality of furniture you buy.</p>
<h2>What goes into the budget</h2>
<ul>
<li><strong>The building.</strong> Rental advances vary widely by city; many owners ask for several months' rent up front. Negotiate a long lease so your setup spend has time to pay back.</li>
<li><strong>Furniture.</strong> Bunk beds, mattresses, lockers and study tables — the largest cost you directly control.</li>
<li><strong>Renovation.</strong> Painting, wiring, plumbing and bathroom repairs.</li>
<li><strong>Utilities.</strong> Water purifier, geysers, power backup, Wi-Fi and CCTV.</li>
<li><strong>Safety and compliance.</strong> Fire extinguishers, signage and local licences.</li>
</ul>
<h2>Sample budget: a 20-bed hostel</h2>
{cost_table('en')}
<p class="note">These are indicative 2026 market ranges, not quotes. They change with city, quality and quantity.</p>
<p>On top of this, keep the rental deposit and at least three months of running costs aside — rent, salaries, electricity, internet and food if you run a mess. Occupancy rarely hits 100% in the first months.</p>
<h2>Where to save money — and where not to</h2>
<p><strong>Use bunk beds.</strong> A room that fits four single cots can often sleep eight with bunk beds, as long as the ceiling leaves comfortable headroom above the top deck. That halves the floor area, and the rent, you pay per bed.</p>
<p><strong>Buy furniture direct from the factory, in bulk.</strong> You skip dealer margins and get every bed in the same design and finish, which makes repairs and replacements simpler later.</p>
<p><strong>Don't save on the frame.</strong> In humid and coastal climates, painted mild steel starts rusting as soon as the coating chips. Galvanised steel and a thick 12mm plywood base last far longer. Replacing cheap cots after a few monsoons costs more than buying right once.</p>
<h2>Licences and approvals to check</h2>
<ul>
<li>A trade licence from your panchayat, municipality or corporation</li>
<li>Permission to use the building for this purpose</li>
<li>Fire safety requirements, which depend on building size</li>
<li>GST registration where it applies to you</li>
<li>Police verification of residents, required in many cities</li>
<li>FSSAI registration if you serve food</li>
</ul>
<p>Rules vary by state and city. Confirm with your local body before you sign a lease.</p>
<p>Want to see how bunk bed pricing works in detail? Read our <a href="/blog/bunk-bed-bunker-cot-price-guide/">bunk bed and bunker cot price guide</a>.</p>
''',
 faqs=[('How much does it cost to start a 20-bed hostel in India?', 'In 2026, setup costs commonly range from about ₹3.8 lakh to ₹13.8 lakh, excluding the rental deposit and working capital. These are indicative figures that vary with city, renovation needs and furniture quality.'),
       ('What is the biggest expense when starting a hostel?', 'After the rental deposit, it is usually furniture and renovation. Running a mess adds a significant kitchen cost.'),
       ('Are bunk beds a good idea for a hostel?', 'Yes, where the ceiling height allows. Bunk beds roughly double the number of sleepers per room, which lowers the furniture and rent cost per bed.')]))

POSTS.append(dict(
 slug='hostel-setup-cost-malayalam', lang='ml', group='hostel-cost', read=6,
 title='ഹോസ്റ്റൽ അല്ലെങ്കിൽ പിജി തുടങ്ങാൻ എത്ര ചെലവ് വരും? (2026 ഗൈഡ്)',
 desc='20 കിടക്കകളുള്ള ഒരു ഹോസ്റ്റൽ അല്ലെങ്കിൽ പിജി തുടങ്ങാനുള്ള 2026-ലെ ഏകദേശ ചെലവ്: ബങ്ക് ബെഡ്, മെത്ത, നവീകരണം, ലൈസൻസുകൾ എന്നിവ വിശദമായി.',
 keywords='ഹോസ്റ്റൽ തുടങ്ങാൻ ചെലവ്, പിജി ബിസിനസ്, ബങ്ക് ബെഡ് വില, ഡബിൾ ഡെക്കർ കട്ടിൽ, ഹോസ്റ്റൽ ഫർണിച്ചർ',
 thumb='blog-hostel-setup-cost-ml', alt='സ്റ്റീൽ ബങ്ക് ബെഡ്ഡുകളുള്ള ഹോസ്റ്റൽ മുറി',
 excerpt='20 കിടക്കകളുള്ള ഹോസ്റ്റലിന്റെ ഫർണിച്ചർ, നവീകരണം, ലൈസൻസുകൾ എന്നിവയുടെ ഏകദേശ ബജറ്റ്.',
 body=f'''
<p class="lede">കേരളത്തിൽ വിദ്യാർത്ഥികൾക്കും ജോലിക്കാർക്കും വേണ്ടിയുള്ള ഹോസ്റ്റലുകൾക്കും പിജികൾക്കും ആവശ്യം കൂടിവരികയാണ്. തുടങ്ങുന്നതിനു മുൻപ് മിക്കവരും ചോദിക്കുന്നത് ഒരേ ചോദ്യമാണ് — മൊത്തം എത്ര രൂപ വേണ്ടിവരും? 20 കിടക്കകളുള്ള ഒരു ഹോസ്റ്റലിന്റെ ഏകദേശ ചെലവ് ഇവിടെ വിശദമാക്കുന്നു.</p>
<h2>ചുരുക്കത്തിൽ</h2>
<p>വാടകക്കെട്ടിടത്തിൽ 20 കിടക്കകളുള്ള ഒരു ഹോസ്റ്റൽ അല്ലെങ്കിൽ പിജി തുടങ്ങാൻ 2026-ൽ ഏകദേശം <strong>₹3.8 ലക്ഷം മുതൽ ₹13.8 ലക്ഷം വരെ</strong> ചെലവ് വരാം. വാടക ഡെപ്പോസിറ്റും പ്രവർത്തന മൂലധനവും ഇതിൽ ഉൾപ്പെടുന്നില്ല. മെസ് നടത്തുന്നുണ്ടോ, കെട്ടിടത്തിന് എത്ര നവീകരണം വേണം, ഫർണിച്ചറിന്റെ ഗുണനിലവാരം എന്നിവയാണ് തുക നിശ്ചയിക്കുന്ന പ്രധാന ഘടകങ്ങൾ.</p>
<h2>പ്രധാന ചെലവുകൾ</h2>
<ul>
<li><strong>കെട്ടിടം:</strong> വാടക അഡ്വാൻസ് നഗരം അനുസരിച്ച് വളരെ വ്യത്യാസപ്പെടും; പലയിടത്തും നിരവധി മാസത്തെ വാടക അഡ്വാൻസായി ചോദിക്കാറുണ്ട്. ദീർഘകാല കരാർ ചർച്ച ചെയ്യുന്നത് നല്ലതാണ്.</li>
<li><strong>ഫർണിച്ചർ:</strong> ബങ്ക് ബെഡ് (ബങ്കർ കോട്ട്, ഡബിൾ ഡെക്കർ കട്ടിൽ), മെത്ത, ലോക്കർ, പഠന മേശ — നിങ്ങൾക്ക് നേരിട്ട് നിയന്ത്രിക്കാവുന്ന ഏറ്റവും വലിയ ചെലവ്.</li>
<li><strong>നവീകരണം:</strong> പെയിന്റിംഗ്, വയറിംഗ്, പ്ലംബിംഗ്, കുളിമുറി അറ്റകുറ്റപ്പണികൾ.</li>
<li><strong>സൗകര്യങ്ങൾ:</strong> വാട്ടർ പ്യൂരിഫയർ, ഗീസർ, ഇൻവെർട്ടർ, വൈ-ഫൈ, സിസിടിവി.</li>
<li><strong>സുരക്ഷയും ലൈസൻസുകളും:</strong> ഫയർ എക്സ്റ്റിംഗ്വിഷറുകൾ, തദ്ദേശ സ്ഥാപനത്തിൽ നിന്നുള്ള ലൈസൻസ്.</li>
</ul>
<h2>20 കിടക്കകളുള്ള ഹോസ്റ്റലിന്റെ ഏകദേശ ബജറ്റ്</h2>
{cost_table('ml')}
<p class="note">ഇവ 2026-ലെ ഏകദേശ വിപണി നിരക്കുകളാണ്, ക്വട്ടേഷനുകളല്ല. നഗരം, ഗുണനിലവാരം, എണ്ണം എന്നിവ അനുസരിച്ച് മാറും.</p>
<p>ഇതിനു പുറമേ വാടക ഡെപ്പോസിറ്റും കുറഞ്ഞത് മൂന്നു മാസത്തെ നടത്തിപ്പ് ചെലവും (വാടക, ശമ്പളം, വൈദ്യുതി, ഇന്റർനെറ്റ്, മെസ് ഉണ്ടെങ്കിൽ ഭക്ഷണം) കൈയിൽ കരുതുക. ആദ്യ മാസങ്ങളിൽ എല്ലാ കിടക്കകളും നിറയണമെന്നില്ല.</p>
<h2>ഫർണിച്ചറിൽ എങ്ങനെ ലാഭിക്കാം</h2>
<p><strong>ബങ്ക് ബെഡ് ഉപയോഗിക്കുക.</strong> സാധാരണ 4 സിംഗിൾ കട്ടിലുകൾ ഇടാവുന്ന മുറിയിൽ, സീലിംഗ് ഉയരം അനുവദിക്കുമെങ്കിൽ, ബങ്ക് ബെഡ് ഉപയോഗിച്ച് 8 പേർക്ക് കിടക്കാം. ഒരു കിടക്കയ്ക്കുള്ള വാടകച്ചെലവ് ഇതോടെ ഗണ്യമായി കുറയും.</p>
<p><strong>ഫാക്ടറിയിൽ നിന്ന് നേരിട്ട് മൊത്തമായി വാങ്ങുക.</strong> ഇടനിലക്കാരുടെ മാർജിൻ ഒഴിവാകും; എല്ലാ കട്ടിലുകളും ഒരേ ഡിസൈനിലും നിലവാരത്തിലും ലഭിക്കും.</p>
<p><strong>ഫ്രെയിമിന്റെ ഗുണനിലവാരത്തിൽ വിട്ടുവീഴ്ച ചെയ്യരുത്.</strong> കേരളത്തിലെ ഈർപ്പമുള്ള കാലാവസ്ഥയിൽ പെയിന്റ് അടർന്നാൽ സാധാരണ സ്റ്റീൽ തുരുമ്പെടുക്കും. ഗാൽവനൈസ്ഡ് സ്റ്റീലും കട്ടിയുള്ള 12mm പ്ലൈവുഡ് ബേസും കൂടുതൽ കാലം നിലനിൽക്കും. ഏതാനും മഴക്കാലങ്ങൾക്കുള്ളിൽ വിലകുറഞ്ഞ കട്ടിലുകൾ മാറ്റേണ്ടിവരുന്നത്, ആദ്യം തന്നെ നല്ലത് വാങ്ങുന്നതിനേക്കാൾ ചെലവേറിയതാണ്.</p>
<h2>ശ്രദ്ധിക്കേണ്ട ലൈസൻസുകൾ</h2>
<ul>
<li>പഞ്ചായത്ത്, മുനിസിപ്പാലിറ്റി അല്ലെങ്കിൽ കോർപ്പറേഷനിൽ നിന്നുള്ള ലൈസൻസ്</li>
<li>കെട്ടിടം ഈ ആവശ്യത്തിന് ഉപയോഗിക്കാനുള്ള അനുമതി</li>
<li>കെട്ടിടത്തിന്റെ വലിപ്പമനുസരിച്ചുള്ള അഗ്നി സുരക്ഷാ നിബന്ധനകൾ</li>
<li>ബാധകമാണെങ്കിൽ ജിഎസ്ടി രജിസ്ട്രേഷൻ</li>
<li>താമസക്കാരുടെ പോലീസ് വെരിഫിക്കേഷൻ</li>
<li>ഭക്ഷണം നൽകുന്നുണ്ടെങ്കിൽ FSSAI രജിസ്ട്രേഷൻ</li>
</ul>
<p>നിയമങ്ങൾ സ്ഥലം അനുസരിച്ച് വ്യത്യാസപ്പെടാം. കരാർ ഒപ്പിടുന്നതിനു മുൻപ് തദ്ദേശ സ്ഥാപനവുമായി ഉറപ്പാക്കുക.</p>
''',
 faqs=[('20 കിടക്കകളുള്ള ഹോസ്റ്റൽ തുടങ്ങാൻ എത്ര ചെലവ് വരും?', '2026-ൽ ഏകദേശം ₹3.8 ലക്ഷം മുതൽ ₹13.8 ലക്ഷം വരെ, വാടക ഡെപ്പോസിറ്റും പ്രവർത്തന മൂലധനവും ഒഴികെ. ഇവ ഏകദേശ കണക്കുകൾ മാത്രമാണ്.'),
       ('ഹോസ്റ്റൽ തുടങ്ങുമ്പോൾ ഏറ്റവും വലിയ ചെലവ് ഏതാണ്?', 'വാടക ഡെപ്പോസിറ്റ് കഴിഞ്ഞാൽ സാധാരണയായി ഫർണിച്ചറും നവീകരണവുമാണ്. മെസ് നടത്തുന്നുണ്ടെങ്കിൽ അടുക്കളയുടെ ചെലവും കൂടും.'),
       ('ഹോസ്റ്റലിന് ബങ്ക് ബെഡ് നല്ലതാണോ?', 'സീലിംഗ് ഉയരം അനുവദിക്കുമെങ്കിൽ, അതെ. ഒരു മുറിയിൽ കിടക്കാവുന്നവരുടെ എണ്ണം ഏകദേശം ഇരട്ടിയാകും; ഒരു കിടക്കയ്ക്കുള്ള ചെലവ് കുറയും.')]))

POSTS.append(dict(
 slug='hostel-setup-cost-hindi', lang='hi', group='hostel-cost', read=6,
 title='हॉस्टल या पीजी शुरू करने में कितना खर्च आता है? (2026 गाइड)',
 desc='20 बेड वाला हॉस्टल या पीजी शुरू करने का 2026 का अनुमानित खर्च: बंक बेड, गद्दे, मरम्मत, लाइसेंस और वर्किंग कैपिटल की पूरी जानकारी।',
 keywords='हॉस्टल शुरू करने का खर्च, पीजी बिज़नेस, बंक बेड कीमत, डबल डेकर बेड, हॉस्टल फ़र्नीचर',
 thumb='blog-hostel-setup-cost-hi', alt='स्टील बंक बेड वाला हॉस्टल का कमरा',
 excerpt='20 बेड वाले हॉस्टल के फ़र्नीचर, मरम्मत और लाइसेंस का अनुमानित बजट।',
 body=f'''
<p class="lede">भारत में छात्रों और कामकाजी लोगों के लिए हॉस्टल और पीजी की मांग लगातार बढ़ रही है। शुरू करने से पहले ज़्यादातर लोग एक ही सवाल पूछते हैं — कुल कितना पैसा लगेगा? यहाँ 20 बेड वाले हॉस्टल का अनुमानित खर्च विस्तार से दिया गया है।</p>
<h2>संक्षेप में</h2>
<p>किराए की इमारत में 20 बेड वाला हॉस्टल या पीजी शुरू करने का सेटअप खर्च 2026 में लगभग <strong>₹3.8 लाख से ₹13.8 लाख</strong> तक आ सकता है। इसमें किराए की डिपॉज़िट और वर्किंग कैपिटल शामिल नहीं है। आप मेस चलाते हैं या नहीं, इमारत में कितनी मरम्मत चाहिए और फ़र्नीचर की गुणवत्ता कैसी है — यही तय करते हैं कि आपका खर्च इस दायरे में कहाँ आएगा।</p>
<h2>मुख्य खर्च</h2>
<ul>
<li><strong>इमारत:</strong> किराए की एडवांस राशि शहर के अनुसार बहुत अलग होती है; कई जगह कई महीनों का किराया एडवांस में माँगा जाता है। लंबी अवधि के एग्रीमेंट पर बातचीत करें।</li>
<li><strong>फ़र्नीचर:</strong> बंक बेड (बंकर कॉट, डबल डेकर बेड), गद्दे, लॉकर, स्टडी टेबल — यह सबसे बड़ा खर्च है जिसे आप सीधे नियंत्रित कर सकते हैं।</li>
<li><strong>मरम्मत:</strong> पेंटिंग, वायरिंग, प्लंबिंग और बाथरूम की मरम्मत।</li>
<li><strong>सुविधाएँ:</strong> वॉटर प्यूरीफायर, गीज़र, इन्वर्टर, वाई-फ़ाई, सीसीटीवी।</li>
<li><strong>सुरक्षा और लाइसेंस:</strong> फ़ायर एक्सटिंग्विशर और स्थानीय निकाय से लाइसेंस।</li>
</ul>
<h2>20 बेड वाले हॉस्टल का अनुमानित बजट</h2>
{cost_table('hi')}
<p class="note">ये 2026 के अनुमानित बाज़ार भाव हैं, कोटेशन नहीं। शहर, गुणवत्ता और मात्रा के अनुसार बदल सकते हैं।</p>
<p>इसके अलावा किराए की डिपॉज़िट और कम से कम तीन महीने का चालू खर्च (किराया, वेतन, बिजली, इंटरनेट, मेस हो तो खाना) अलग रखें। शुरुआती महीनों में सभी बेड भरें, यह ज़रूरी नहीं।</p>
<h2>फ़र्नीचर पर पैसे कैसे बचाएँ</h2>
<p><strong>बंक बेड इस्तेमाल करें।</strong> जिस कमरे में आमतौर पर 4 सिंगल कॉट आते हैं, वहाँ छत की ऊँचाई पर्याप्त हो तो बंक बेड से 8 लोग सो सकते हैं। इससे प्रति बेड किराए का खर्च काफ़ी कम हो जाता है।</p>
<p><strong>फ़ैक्टरी से सीधे थोक में खरीदें।</strong> बिचौलियों का मार्जिन बचता है और सभी बेड एक जैसे डिज़ाइन और गुणवत्ता के मिलते हैं।</p>
<p><strong>फ़्रेम की गुणवत्ता से समझौता न करें।</strong> नमी वाले मौसम में पेंट उखड़ते ही साधारण स्टील में जंग लगने लगती है। गैल्वनाइज़्ड स्टील और मोटा 12mm प्लाइवुड बेस ज़्यादा समय तक चलते हैं। कुछ बरसातों के बाद सस्ते कॉट बदलना, पहली बार में सही खरीदने से महँगा पड़ता है।</p>
<h2>ज़रूरी लाइसेंस और अनुमतियाँ</h2>
<ul>
<li>नगर निगम, नगर पालिका या पंचायत से ट्रेड लाइसेंस</li>
<li>इमारत को इस काम के लिए इस्तेमाल करने की अनुमति</li>
<li>इमारत के आकार के अनुसार अग्नि सुरक्षा नियम</li>
<li>जहाँ लागू हो, जीएसटी पंजीकरण</li>
<li>निवासियों का पुलिस वेरिफ़िकेशन</li>
<li>खाना देते हैं तो FSSAI पंजीकरण</li>
</ul>
<p>नियम राज्य और शहर के अनुसार अलग हो सकते हैं। एग्रीमेंट पर हस्ताक्षर करने से पहले स्थानीय अधिकारियों से पुष्टि कर लें।</p>
''',
 faqs=[('20 बेड वाला हॉस्टल शुरू करने में कितना खर्च आता है?', '2026 में लगभग ₹3.8 लाख से ₹13.8 लाख, किराए की डिपॉज़िट और वर्किंग कैपिटल छोड़कर। ये केवल अनुमानित आंकड़े हैं।'),
       ('हॉस्टल शुरू करने में सबसे बड़ा खर्च क्या है?', 'किराए की डिपॉज़िट के बाद आमतौर पर फ़र्नीचर और मरम्मत। मेस चलाने पर रसोई का खर्च भी जुड़ता है।'),
       ('क्या हॉस्टल के लिए बंक बेड सही हैं?', 'हाँ, अगर छत की ऊँचाई पर्याप्त हो। एक कमरे में सोने वालों की संख्या लगभग दोगुनी हो जाती है और प्रति बेड खर्च घटता है।')]))

POSTS.append(dict(
 slug='bunk-bed-bunker-cot-price-guide', lang='en', group=None, read=6,
 title='Bunk Bed Price Guide for Hostels: Bunker Cots & Double Decker Beds (2026)',
 desc='What a steel bunk bed, bunker cot or double decker bed costs for a hostel in 2026, what drives the price, and a safety checklist before you buy in bulk.',
 keywords='bunk bed price, bunker cot price, double decker bed price, double decker cot, steel bunk bed for hostel',
 thumb='blog-bunk-bed-price-guide', alt='Galvanised steel bunk bed, also called a bunker cot or double decker bed, with plywood decks',
 excerpt='Bunker cot, double decker bed or bunk bed — what drives the price, and what to check before a bulk order.',
 body='''
<p class="lede">Whether you call it a bunk bed, a bunker cot or a double decker bed, it is the single biggest lever a hostel owner has on capacity. Here is what drives the price in 2026 and what to check before you order in bulk.</p>
<h2>Bunk bed, bunker cot, double decker bed — the same thing?</h2>
<p>Yes. "Bunk bed" is the international term. Across India, and especially in Kerala, you will also hear "bunker cot", "double decker bed" or "double decker cot". They all mean two sleeping decks stacked on one frame.</p>
<h2>How much does a steel bunk bed cost in India?</h2>
<p>In 2026, a standard steel bunk bed for hostel use commonly sells for roughly <strong>₹7,000 to ₹15,000 per unit</strong> (two beds), before mattresses. Heavy-duty frames, galvanised steel and thicker bases sit toward the top of that range; lighter painted frames sit toward the bottom. Bulk orders placed directly with a manufacturer usually cost less per unit than retail. Treat these as market ranges, not quotes.</p>
<h2>What drives the price</h2>
<ul>
<li><strong>Steel type.</strong> Galvanised steel resists rust even where the paint chips. Painted mild steel is cheaper but starts rusting once the coating is damaged — a real problem in humid, coastal climates.</li>
<li><strong>Tube size and wall thickness.</strong> Heavier square tubes cost more and flex less. Ask for the tube size and thickness in writing.</li>
<li><strong>The base.</strong> A solid plywood base spreads load evenly. 12mm plywood holds up far better over the years than an 8mm sheet or widely spaced strips.</li>
<li><strong>Finish.</strong> A coating such as epoxy protects the steel and stays presentable for longer than ordinary paint. Bunkworks beds are epoxy coated over galvanised steel.</li>
<li><strong>Joints.</strong> Bolted joints let you dismantle, move and repair beds. Fully welded frames are hard to transport and cannot be flat-packed.</li>
<li><strong>Quantity and delivery.</strong> Per-unit prices usually drop with volume. Delivery distance and whether the bed ships flat-packed affect the final number.</li>
</ul>
<h2>Safety checklist before you buy</h2>
<ul>
<li>A guard rail on the open side of the top deck that sits well above the mattress — check it with the mattress thickness you will actually use.</li>
<li>A ladder or rungs that stay rigid under an adult's weight.</li>
<li>Enough gap between decks for the lower sleeper to sit up.</li>
<li>A stated load rating for each deck.</li>
<li>Rounded edges, end caps on every tube, and anti-skid feet that protect the floor.</li>
</ul>
<h2>Why hostels choose bunk beds</h2>
<p>A room that fits four single cots can often sleep eight with bunk beds, as long as the ceiling leaves comfortable headroom above the top deck. That halves the floor area — and the rent — you pay per bed. See how that plays out in a full budget in our guide to <a href="/blog/hostel-setup-cost-india/">the cost of starting a hostel</a>.</p>
<h2>Questions to ask a supplier</h2>
<ul>
<li>What steel, tube size and thickness is the frame made from?</li>
<li>Is it galvanised, and what is the finish?</li>
<li>How thick is the base?</li>
<li>What is the load rating per deck?</li>
<li>Is it bolted and flat-packed for delivery?</li>
<li>What is the per-unit price at my quantity, including delivery?</li>
</ul>
''',
 faqs=[('Is a bunker cot the same as a bunk bed?', 'Yes. Bunker cot, double decker bed, double decker cot and bunk bed all describe two sleeping decks stacked on one frame.'),
       ('What is the price of a double decker bed for a hostel?', 'In 2026, steel double decker beds for hostel use commonly sell for roughly ₹7,000 to ₹15,000 per unit before mattresses, depending on steel, base, finish and quantity.'),
       ('Is galvanised or painted steel better for hostel beds?', 'Galvanised steel. It resists rust even where the paint is scratched, which matters in humid and coastal climates. Painted mild steel is cheaper but rusts once the coating chips.')]))

POSTS.append(dict(
 slug='steel-single-cot-for-hostel', lang='en', group=None, read=5,
 title='Steel Single Cot for Hostels: Sizes, Price and What to Check (2026)',
 desc='Standard single cot sizes, 2026 price ranges for steel single beds for hostels and PGs, and a checklist for frame, base and finish before you buy.',
 keywords='single cot price, steel single cot, single bed for hostel, steel cot for hostel, hostel single bed size',
 thumb='blog-steel-single-cot', alt='Steel single cot with a plywood base in a hostel room',
 excerpt='Standard sizes, 2026 price ranges and a buying checklist for steel single cots in hostels and PGs.',
 body='''
<p class="lede">Not every room suits a bunk bed. Low ceilings, older residents or premium single rooms often call for a single cot. Here is how to choose one that lasts.</p>
<h2>Standard single cot sizes</h2>
<p>The most common single cot sizes in India are <strong>6 × 2.5 feet</strong> (about 183 × 76 cm) and <strong>6 × 3 feet</strong> (about 183 × 91 cm). The 6 × 2.5 feet size fits more beds per room; 6 × 3 feet is roomier for adults. Match the cot to your mattress size before you order.</p>
<h2>How much does a steel single cot cost?</h2>
<p>In 2026, steel single cots for hostel use commonly sell for roughly <strong>₹3,500 to ₹8,000 each</strong>, depending on the steel, base and finish. Bulk orders placed directly with a factory generally cost less per unit than buying one at a time. These are market ranges, not quotes.</p>
<h2>Single cot or bunk bed?</h2>
<p>Choose single cots when the ceiling is low, when residents need easy access (older adults, people recovering from injuries), or when you sell premium single rooms. Choose bunk beds when the goal is the most beds per room. Our <a href="/blog/bunk-bed-bunker-cot-price-guide/">bunk bed price guide</a> covers that side.</p>
<h2>What to check before you buy</h2>
<ul>
<li><strong>Frame:</strong> galvanised steel resists rust where the paint chips.</li>
<li><strong>Base:</strong> a solid 12mm plywood base does not sag and spreads the load; thin sheets and steel strips are cheaper but wear faster.</li>
<li><strong>Load rating:</strong> ask for it in writing.</li>
<li><strong>Construction:</strong> bolted joints make moving and repairs easy.</li>
<li><strong>Feet:</strong> anti-skid leg bushes protect tiled floors and stop the cot sliding.</li>
</ul>
<h2>The Bunkworks steel single bed</h2>
<div class="table-wrap"><table class="spec-table"><tbody>
<tr><th scope="row">Bed size (L × W)</th><td>6 × 2.5 feet (183 × 76 cm)</td></tr>
<tr><th scope="row">Height</th><td>40 cm</td></tr>
<tr><th scope="row">Frame</th><td>Galvanised anti-rust steel</td></tr>
<tr><th scope="row">Finish</th><td>Epoxy coating (not powder coating), grey</td></tr>
<tr><th scope="row">Base</th><td>12mm thick plywood</td></tr>
<tr><th scope="row">Load capacity</th><td>Up to 100 kg</td></tr>
<tr><th scope="row">Use</th><td>Hostels, PGs, dorms, institutions, homes</td></tr>
</tbody></table></div>
''',
 faqs=[('What is the standard size of a single cot?', 'The most common sizes in India are 6 × 2.5 feet (about 183 × 76 cm) and 6 × 3 feet (about 183 × 91 cm).'),
       ('How much does a steel single cot cost for a hostel?', 'In 2026, steel single cots for hostels commonly cost roughly ₹3,500 to ₹8,000 each, depending on steel, base, finish and order quantity.'),
       ('Is a plywood base or a steel strip base better?', 'A solid 12mm plywood base spreads load evenly and does not sag. Steel strips are cheaper but can bend over time and press into the mattress.')]))

POSTS.append(dict(
 slug='hostel-beds-wholesale-factory-price', lang='en', group=None, read=5,
 title='Hostel Beds Wholesale: How Factory-Direct Pricing and Bulk Discounts Work',
 desc='How to buy hostel beds and cots wholesale, direct from the factory: how bulk discounts work, what to include in a quote request, and how to compare quotes.',
 keywords='hostel beds wholesale, bunk bed factory price, cot wholesale, hostel furniture manufacturer, bulk discount beds',
 thumb='blog-wholesale-hostel-beds', alt='Stack of steel hostel bed frames with plywood bases, ready for wholesale dispatch',
 excerpt='How bulk discounts on beds actually work, what to put in a quote request, and how to compare quotes fairly.',
 body='''
<p class="lede">If you are furnishing 20, 50 or 200 beds, buying one cot at a time from a furniture shop is the most expensive way to do it. Here is how factory-direct wholesale buying works.</p>
<h2>Factory direct versus a dealer</h2>
<p>A dealer adds margin to cover showroom, storage and staff. Buying direct from the manufacturer removes that layer — and you deal with the people who actually make the bed, which makes custom sizes, consistent batches and spare parts later much easier.</p>
<h2>How bulk discounts usually work</h2>
<ul>
<li><strong>Volume.</strong> Per-unit prices generally drop as quantity rises, because cutting, welding and coating are more efficient in batches.</li>
<li><strong>Standard sizes.</strong> Standard designs cost less than custom sizes, which need new cutting lists and jigs.</li>
<li><strong>Flat-pack delivery.</strong> Beds shipped as separate legs and platforms fit more per truck, which lowers transport cost per bed.</li>
<li><strong>Timing.</strong> Demand peaks before the academic year. Ordering early gets you better lead times and more room to negotiate.</li>
<li><strong>Payment terms.</strong> The split between advance and balance can affect the price; ask.</li>
</ul>
<h2>What to put in a quote request</h2>
<ul>
<li>Number of units of each type (bunk beds, single cots)</li>
<li>Size, if you need anything other than standard</li>
<li>Delivery city, and whether the site has stairs or a lift</li>
<li>Your opening date</li>
<li>Whether you also need mattresses</li>
<li>Whether you need a GST invoice</li>
</ul>
<h2>Compare quotes like for like</h2>
<p>Two quotes for the same number of beds can hide different steel thickness, base thickness or finish. Ask each supplier for a spec sheet, see a sample if you can, and confirm the load rating, warranty and whether delivery and installation are included.</p>
<h2>A price far below the market is a warning</h2>
<p>It usually means thinner steel, a thinner base or skipped rust protection — costs you pay later in repairs and replacements. For a full picture of what the rest of a hostel costs, read <a href="/blog/hostel-setup-cost-india/">how much it costs to start a hostel</a>.</p>
''',
 faqs=[('Can I buy hostel beds directly from the factory?', 'Yes. Bunkworks manufactures steel bunk beds and single beds in its own workshop in Kerala and supplies directly to hostels, PGs and institutions in bulk.'),
       ('Do you get discounts on bulk orders of hostel beds?', 'Per-unit prices generally fall as quantity rises. The exact figure depends on quantity, size and delivery, so ask for a quote at your quantity.'),
       ('How early should I order beds for a new hostel?', 'Well before your opening date, especially ahead of the academic year when demand peaks. Confirm the lead time in writing.')]))
