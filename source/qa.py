import re,glob,os,json,sys
R=sys.argv[1] if len(sys.argv)>1 else 'site'
files=sorted(glob.glob(R+'/**/*.html',recursive=True))
def path_of(f): 
    p='/'+os.path.relpath(f,R).replace('index.html','')
    return '/' if p=='/' else p
problems=[]
existing=set()
for f in glob.glob(R+'/**/*',recursive=True):
    if os.path.isfile(f): existing.add('/'+os.path.relpath(f,R))
def resolves(u):
    u=u.split('#')[0].split('?')[0]
    if u in ('','/'): return True
    if u.endswith('/'): return (u+'index.html') in existing
    return u in existing or (u+'/index.html') in existing
for f in files:
    t=open(f,encoding='utf-8').read(); p=path_of(f)
    # links
    for h in set(re.findall(r'href="(/[^"]*)"',t)):
        if h.startswith('//'): continue
        if not resolves(h): problems.append(f'BROKEN LINK {p} -> {h}')
    ids=set(re.findall(r'\bid="([^"]+)"',t))
    for a in set(re.findall(r'href="#([\w-]+)"',t)):
        if a not in ids and a!='main': problems.append(f'MISSING ANCHOR {p} #{a}')
    for src in set(re.findall(r'(?:src|srcset)="(/images/[\w.-]+)',t)):
        if src not in existing: problems.append(f'MISSING IMG {p} {src}')
    # images alt
    for m in re.finditer(r'<img [^>]*>',t):
        a=re.search(r'alt="([^"]*)"',m.group())
        if not a or len(a.group(1).strip())<12: problems.append(f'WEAK/NO ALT {p} {m.group()[:90]}')
    h1=len(re.findall(r'<h1[ >]',t))
    if h1!=1: problems.append(f'H1 count {h1} on {p}')
    if not re.search(r'<link rel="canonical" href="https://www.bunkworks.com'+re.escape(p)+'">',t) and p!='/404.html': problems.append(f'CANONICAL mismatch {p}')
    for x in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S):
        try: json.loads(x)
        except Exception as e: problems.append(f'BAD JSON-LD {p}')
    if 'PASTE-YOUR' in t or 'lorem' in t.lower(): problems.append(f'PLACEHOLDER {p}')
# sitemap vs pages
sm=open(R+'/sitemap.xml',encoding='utf-8').read(); urls=set(re.findall(r'<loc>https://www.bunkworks.com(/[^<]*)</loc>',sm))
pg={path_of(f) for f in files if not f.endswith('404.html')}
if urls!=pg: problems.append(f'SITEMAP diff: only-in-sitemap={urls-pg} only-in-pages={pg-urls}')
# redirects
for l in open(R+'/_redirects',encoding='utf-8'):
    l=l.strip()
    if not l or l.startswith('#') or l.startswith('http'): continue
    src,dst,code=l.split()[:3]
    if not resolves(dst): problems.append(f'REDIRECT target missing {src}->{dst}')
    if src.rstrip('/')==dst.rstrip('/'): problems.append(f'REDIRECT loop {src}')
    if src in pg and src!='/index.html' and src!='/home/': problems.append(f'REDIRECT source is a live page {src}')
home=open(R+'/index.html',encoding='utf-8').read()
print('HOME TITLE :',re.search(r'<title>(.*?)</title>',home).group(1))
d=re.search(r'name="description" content="([^"]*)"',home).group(1).replace('&amp;','&'); print('HOME DESC  :',d,f'({len(d)} chars)')
for p_ in ['/bunker-cot-double-decker-bed/','/steel-single-cot/','/bulk-quote/']:
    t=open(R+p_+'index.html',encoding='utf-8').read(); 
    print(p_,'|',re.search(r'<title>(.*?)</title>',t).group(1).replace('&amp;','&'),'|',len(re.search(r'name="description" content="([^"]*)"',t).group(1).replace('&amp;','&')),'chars desc')
print('pages',len(files),'| problems:',len(problems)); print('\n'.join(problems[:40]))
