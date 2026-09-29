import os, re, glob
from html.parser import HTMLParser
ROOT='site'; problems=[]
files=[f for f in glob.glob(ROOT+'/**/*.html',recursive=True)]
ids_by_file={}
class P(HTMLParser):
    def __init__(s): super().__init__(); s.h1=0; s.imgs=[]; s.links=[]; s.ids=set(); s.heads=[]
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=='h1': s.h1+=1
        if t in('h1','h2','h3','h4'): s.heads.append(int(t[1]))
        if t=='img': s.imgs.append(a)
        if t=='a' and 'href' in a: s.links.append(a['href'])
        if 'id' in a: s.ids.add(a['id'])
parsed={}
for f in files:
    s=open(f,encoding='utf-8').read(); p=P(); p.feed(s); parsed[f]=(s,p)
for f,(s,p) in parsed.items():
    t=re.search(r'<title>(.*?)</title>',s).group(1); d=re.search(r'name="description" content="([^"]*)"',s).group(1)
    if p.h1!=1: problems.append(f'{f}: {p.h1} h1')
    if 'noindex' in s and not f.endswith('404.html'): problems.append(f'{f}: noindex')
    if 'rel="canonical"' not in s: problems.append(f'{f}: no canonical')
    if 'og:image' not in s: problems.append(f'{f}: no og:image')
    if len(t)>70: problems.append(f'{f}: title {len(t)} chars')
    if not 50<=len(d)<=170: problems.append(f'{f}: desc {len(d)} chars')
    for i in p.imgs:
        if not i.get('alt'): problems.append(f'{f}: img missing alt {i.get("src")}')
        if not (i.get('width') and i.get('height')): problems.append(f'{f}: img missing dims')
        src=i['src']
        if src.startswith('/') and not os.path.exists(ROOT+src): problems.append(f'{f}: missing image {src}')
    # heading skips
    for a,b in zip(p.heads,p.heads[1:]):
        if b>a+1: problems.append(f'{f}: heading jump h{a}->h{b}'); break
    for h in p.links:
        if h.startswith(('http','mailto:','tel:')): continue
        path,_,frag=h.partition('#')
        if path=='': target=f
        else:
            target=ROOT+path+('index.html' if path.endswith('/') else '')
            if not os.path.exists(target): problems.append(f'{f}: broken link {h}'); continue
        if frag and target.endswith('.html') and frag not in parsed[target][1].ids: problems.append(f'{f}: missing anchor {h}')
print(len(files),'pages audited'); print('\n'.join(problems) or 'NO PROBLEMS')
for f,(s,p) in parsed.items(): print(f, '| title', len(re.search(r'<title>(.*?)</title>',s).group(1)))
