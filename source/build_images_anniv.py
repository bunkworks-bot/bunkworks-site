import json, os
from PIL import Image, ImageDraw, ImageFont
import numpy as np
OUT='/home/claude/site'; IMG=OUT+'/images'; U='/mnt/user-data/uploads/'
meta=json.load(open('/home/claude/img_meta.json'))

def save(im,path,q):
    im=im.convert('RGB'); im.save(path,'JPEG',quality=q,optimize=True,progressive=True); im.save(path[:-4]+'.webp','WEBP',quality=q-6,method=6)
def resp(key,im,lg=1500,sm=720,q=82):
    w,h=im.size
    L=im if w<=lg else im.resize((lg,round(h*lg/w)),Image.LANCZOS)
    save(L,f'{IMG}/{key}.jpg',q); e={'lg':L.size}
    S=im.resize((sm,round(h*sm/w)),Image.LANCZOS); save(S,f'{IMG}/{key}-sm.jpg',q-2); e['sm']=S.size
    meta[key]=e

resp('anniversary-bunk-bed-terracotta-room',Image.open(U+'1000455226.png').convert('RGB'))
resp('anniversary-bunk-bed-warm-lit-room',Image.open(U+'1000455228.png').convert('RGB'))
resp('anniversary-single-cot-wood-top',Image.open(U+'1000455229.png').convert('RGB'))

# studio cutout -> composite on the card tone, tight crop, 4:3 canvas
cut=Image.open(U+'1000455227.png').convert('RGBA'); a=np.array(cut)[...,3]
ys,xs=np.where(a>12); box=(xs.min(),ys.min(),xs.max(),ys.max())
cut=cut.crop(box); w,h=cut.size; pad=int(max(w,h)*0.07)
cw=max(w+2*pad,int((h+2*pad)*4/3)); ch=int(cw*3/4)
bg=Image.new('RGBA',(cw,ch),(239,231,216,255)); bg.alpha_composite(cut,((cw-w)//2,(ch-h)//2))
resp('bunk-bed-studio-cutout',bg.convert('RGB'),lg=1400,sm=700,q=86)

# ---- OG image 1200x630 ----
hero=Image.open(U+'1000455226.png').convert('RGB'); W,H=1200,630
sc=max(W/hero.width,H/hero.height); hr=hero.resize((round(hero.width*sc),round(hero.height*sc)),Image.LANCZOS)
og=hr.crop((hr.width-W-40 if hr.width-W-40>0 else 0,(hr.height-H)//2,(hr.width-40 if hr.width-40>W else hr.width),(hr.height-H)//2+H)).resize((W,H)).convert('RGBA')
ov=np.zeros((H,W,4),dtype=np.uint8)
xs=np.linspace(0,1,W); al=np.clip((0.66-xs)/0.66,0,1)**0.8*245
ov[...,0]=58; ov[...,1]=12; ov[...,2]=7; ov[...,3]=al[None,:].astype(np.uint8)
og.alpha_composite(Image.fromarray(ov,'RGBA'))
d=ImageDraw.Draw(og)
GV=ImageFont.truetype('fonts/GreatVibes.ttf',82); PF=ImageFont.truetype('fonts/Playfair-Black.ttf',74); PI=ImageFont.truetype('fonts/Playfair-BoldItalic.ttf',34)
IB=ImageFont.truetype('fonts/Inter-Bold.ttf',30); IS=ImageFont.truetype('fonts/Inter-SemiBold.ttf',22); IB2=ImageFont.truetype('fonts/Inter-Bold.ttf',46)
gold=(240,182,64); cream=(255,243,220)
logo=Image.open('fonts/logo-onwhite-to-ondark-sm.png').convert('RGBA'); lw=250; logo=logo.resize((lw,round(logo.height*lw/logo.width)),Image.LANCZOS); og.alpha_composite(logo,(48,34))
d.text((48,118),'Our 5th',font=GV,fill=gold)
d.text((48,198),'ANNIVERSARY',font=PF,fill=cream)
d.text((52,286),'O F F E R',font=PI,fill=gold)
d.rounded_rectangle((48,344,352,412),radius=8,fill=(240,182,64)); d.text((66,356),'UP TO',font=IS,fill=(58,12,7)); d.text((140,346),'40% OFF',font=IB2,fill=(58,12,7))
d.text((48,440),'Steel bunk bed',font=IS,fill=cream); d.text((48,470),'\u20b95,999',font=IB2,fill=(255,226,154)); 
d.text((228,484),'\u20b99,999',font=IS,fill=(210,180,150)); d.line((228,496,306,496),fill=(210,180,150),width=2)
d.text((400,440),'Steel single cot',font=IS,fill=cream); d.text((400,470),'\u20b93,300',font=IB2,fill=(255,226,154))
d.text((572,484),'\u20b95,500',font=IS,fill=(210,180,150)); d.line((572,496,650,496),fill=(210,180,150),width=2)
d.rounded_rectangle((48,548,504,590),radius=21,fill=(142,22,22)); d.text((66,556),'Limited pieces left \u2014 book now',font=IS,fill=(255,243,220))
og.convert('RGB').save(OUT+'/og-image.jpg',quality=86,optimize=True)

# ---- new single cot photo (dressed bed) ----
resp('single-cot-terracotta-dressed-bed',Image.open(U+'1000455230.png').convert('RGB'))

# ---- favicon / app icon set built from the logo mark (white + gold on brand dark) ----
from PIL import ImageDraw
logo_dark=Image.open('/home/claude/fonts/logo-onwhite-to-ondark.png').convert('RGBA')
mk=logo_dark.crop((60,115,540,610))
bb=np.array(mk)[...,3]; ys,xs=np.where(bb>20); mk=mk.crop((xs.min(),ys.min(),xs.max()+1,ys.max()+1))
DARK=(21,18,15,255)
def icon(size,fill=0.74,rounded=True,bg=DARK):
    big=size*4
    cv=Image.new('RGBA',(big,big),(0,0,0,0)); d=ImageDraw.Draw(cv)
    if rounded: d.rounded_rectangle((0,0,big-1,big-1),radius=int(big*0.2),fill=bg)
    else: d.rectangle((0,0,big,big),fill=bg)
    sc=(big*fill)/max(mk.size); m=mk.resize((max(1,round(mk.width*sc)),max(1,round(mk.height*sc))),Image.LANCZOS)
    cv.alpha_composite(m,((big-m.width)//2,(big-m.height)//2))
    return cv.resize((size,size),Image.LANCZOS)
for n in (16,32,48): icon(n,fill=0.80).save(f'{OUT}/favicon-{n}.png',optimize=True)
icon(48,fill=0.80).save(f'{OUT}/favicon.ico',sizes=[(16,16),(32,32),(48,48)]) if False else None
ico=[icon(n,fill=0.80) for n in (16,32,48,64)]; ico[3].save(f'{OUT}/favicon.ico',format='ICO',sizes=[(16,16),(32,32),(48,48),(64,64)],append_images=ico[:3])
icon(180,fill=0.70,rounded=False).convert('RGB').save(f'{OUT}/apple-touch-icon.png',optimize=True)
icon(192,fill=0.74).save(f'{IMG}/icon-192.png',optimize=True); icon(512,fill=0.74).save(f'{IMG}/icon-512.png',optimize=True)
icon(512,fill=0.56,rounded=False).convert('RGB').save(f'{IMG}/icon-maskable-512.png',optimize=True)
icon(512,fill=0.74).save(f'{IMG}/bunkworks-icon.png',optimize=True)
sheet=Image.new('RGB',(640,200),(240,236,228)); x=10
for n,f in ((16,0.8),(32,0.8),(48,0.8),(64,0.8),(96,0.74),(160,0.7)):
    im=icon(n,fill=f); sheet.paste(im,(x,20),im); x+=n+18
sheet.save('/home/claude/icon_sheet.png')

json.dump(meta,open('/home/claude/img_meta.json','w'),indent=1)
print('ok',[k for k in meta if k.startswith(('anniv','bunk-bed-studio'))])
