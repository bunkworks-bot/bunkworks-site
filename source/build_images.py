import os, json
from PIL import Image, ImageDraw

OUT = '/home/claude/site'
IMG = os.path.join(OUT, 'images')
os.makedirs(IMG, exist_ok=True)
meta = {}

def save_jpg(im, path, q=80):
    im = im.convert('RGB')
    im.save(path, 'JPEG', quality=q, optimize=True, progressive=True)
    if '/images/' in path: im.save(path[:-4] + '.webp', 'WEBP', quality=q - 4, method=6)

def responsive(key, src, lg=1400, sm=640, q=80, crop=None):
    im = Image.open(src).convert('RGB')
    if crop: im = im.crop(crop)
    w, h = im.size
    entry = {}
    L = im if w <= lg else im.resize((lg, round(h * lg / w)), Image.LANCZOS)
    save_jpg(L, f'{IMG}/{key}.jpg', q); entry['lg'] = L.size
    if w > sm * 1.3:
        S = im.resize((sm, round(h * sm / w)), Image.LANCZOS)
        save_jpg(S, f'{IMG}/{key}-sm.jpg', q); entry['sm'] = S.size
    meta[key] = entry

def thumb(key, src, cx=0.5, cy=0.5, frac_w=1.0):
    im = Image.open(src).convert('RGB'); w, h = im.size
    cw = int(w * frac_w); ch = int(cw * 9 / 16)
    if ch > h: ch = h; cw = int(ch * 16 / 9)
    x0 = int(min(max(cx * w - cw / 2, 0), w - cw)); y0 = int(min(max(cy * h - ch / 2, 0), h - ch))
    c = im.crop((x0, y0, x0 + cw, y0 + ch)).resize((960, 540), Image.LANCZOS)
    c = brand(c)
    save_jpg(c, f'{IMG}/{key}.jpg', 80)
    save_jpg(c.resize((480, 270), Image.LANCZOS), f'{IMG}/{key}-sm.jpg', 78)
    meta[key] = {'lg': (960, 540), 'sm': (480, 270)}

U = '/mnt/user-data/uploads/'
C = '/home/claude/crops/'

# Logo (already transparent)
logo = Image.open(U + '1000452098.png').convert('RGBA').crop((50, 105, 2096, 619))
lw = 720; logo_s = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
logo_s.save(f'{IMG}/bunkworks-logo.png', optimize=True)
meta['logo'] = logo_s.size

# Mark-only icon for favicons
mark = Image.open(U + '1000452098.png').convert('RGBA').crop((60, 115, 540, 610))
side = max(mark.size) + 40
sq = Image.new('RGBA', (side, side), (255, 255, 255, 255))
sq.paste(mark, ((side - mark.width) // 2, (side - mark.height) // 2), mark)
sq.resize((180, 180), Image.LANCZOS).save(f'{OUT}/apple-touch-icon.png', optimize=True)
sq.resize((512, 512), Image.LANCZOS).save(f'{IMG}/icon-512.png', optimize=True)
sq.resize((192, 192), Image.LANCZOS).save(f'{IMG}/icon-192.png', optimize=True)
sq.resize((32, 32), Image.LANCZOS).save(f'{OUT}/favicon-32.png', optimize=True)
sq.resize((16, 16), Image.LANCZOS).save(f'{OUT}/favicon-16.png', optimize=True)
sq.resize((48, 48), Image.LANCZOS).save(f'{OUT}/favicon-48.png', optimize=True)
mk = Image.new('RGBA', (512, 512), (246, 242, 234, 255)); mm = mark.resize((300, round(mark.height * 300 / mark.width)), Image.LANCZOS)
mk.alpha_composite(mm, ((512 - mm.width) // 2, (512 - mm.height) // 2)); mk.save(f'{IMG}/icon-maskable-512.png', optimize=True)
sq.save(f'{OUT}/favicon.ico', sizes=[(16, 16), (32, 32), (48, 48)])

# Page photos
responsive('bunk-bed-galvanised-steel-plywood', U + '1000406526.png')
responsive('hostel-dormitory-bunk-beds', U + '1000379809.png', lg=1100)
responsive('steel-bed-frames-factory-kerala', U + '1000423115.png', lg=1100)
responsive('steel-single-bed-hostel-room', C + 'single_bed_room.png', sm=480)
responsive('bolted-steel-corner-joint-plywood', C + 'joint_hero2.png', q=88)
responsive('steel-single-cot-minimal-room', C + 'single_bed_minimal.png', q=86)

LOGO_FULL = Image.open(U + '1000452098.png').convert('RGBA').crop((50, 105, 2096, 619))
def brand(c, top=False):
    c = c.convert('RGBA'); pw = 300
    pl = LOGO_FULL.resize((pw - 32, round(LOGO_FULL.height * (pw - 32) / LOGO_FULL.width)), Image.LANCZOS)
    plate = Image.new('RGBA', (pw, pl.height + 24), (246, 242, 234, 240)); plate.paste(pl, (16, 12), pl)
    c.alpha_composite(plate, (c.width - pw - 22, 22) if top else (22, c.height - plate.height - 22)); return c.convert('RGB')

# Blog thumbnails (16:9)
thumb('blog-hostel-setup-cost', U + '1000379809.png', cy=0.42)
thumb('blog-hostel-setup-cost-ml', U + '1000379809.png', cx=0.3, cy=0.48, frac_w=0.8)
thumb('blog-hostel-setup-cost-hi', U + '1000379809.png', cx=0.7, cy=0.38, frac_w=0.72)
thumb('blog-bunk-bed-price-guide', U + '1000406526.png', cy=0.48)
thumb('blog-steel-single-cot', C + 'single_bed_room.png', cy=0.55)
thumb('blog-wholesale-hostel-beds', U + '1000423115.png', cy=0.5)
thumb('blog-cheapest-bunk-bed-price', U + '1000406526.png', cx=0.55, cy=0.5, frac_w=0.9)
thumb('blog-bunk-bed-price-ml', U + '1000379809.png', cx=0.62, cy=0.36, frac_w=0.76)
thumb('blog-bunk-bed-price-hi', U + '1000406526.png', cx=0.47, cy=0.33, frac_w=0.7)
thumb('blog-iron-vs-steel-cot-price', C + 'single_bed_room.png', cx=0.5, cy=0.62, frac_w=0.86)
thumb('blog-iron-cot-price-ml', C + 'single_bed_room.png', cx=0.38, cy=0.62, frac_w=0.74)
thumb('blog-iron-cot-price-hi', C + 'single_bed_room.png', cx=0.62, cy=0.5, frac_w=0.72)
thumb('blog-galvanised-steel-advantage', C + 'joint_hero2.png', cy=0.5)
thumb('blog-galvanised-steel-advantage-ml', U + '1000423115.png', cx=0.5, cy=0.3, frac_w=0.7)
thumb('blog-galvanised-steel-advantage-hi', U + '1000406526.png', cx=0.2, cy=0.25, frac_w=0.5)
thumb('blog-bunk-bed-for-adults', U + '1000379809.png', cx=0.45, cy=0.7, frac_w=0.82)

# Size-guide diagram thumbnail (drawn, crisp)
from PIL import ImageFont
F = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
d_im = Image.new('RGB', (960, 540), (246, 242, 234)); d = ImageDraw.Draw(d_im)
ink, gold = (18, 18, 18), (158, 94, 24)
d.rectangle((250, 120, 690, 140), fill=ink); d.rectangle((250, 300, 690, 320), fill=ink)
d.rectangle((250, 126, 690, 134), fill=(185, 121, 60)); d.rectangle((250, 306, 690, 314), fill=(185, 121, 60))
for x in (250, 674): d.rectangle((x, 70, x + 16, 440), fill=ink)
d.rectangle((250, 70, 690, 80), fill=ink)
d.line((710, 70, 710, 440), fill=gold, width=3); d.line((700, 70, 720, 70), fill=gold, width=3); d.line((700, 440, 720, 440), fill=gold, width=3)
d.line((250, 470, 690, 470), fill=gold, width=3); d.line((250, 460, 250, 480), fill=gold, width=3); d.line((690, 460, 690, 480), fill=gold, width=3)
d.line((200, 140, 200, 300), fill=gold, width=3); d.line((190, 140, 210, 140), fill=gold, width=3); d.line((190, 300, 210, 300), fill=gold, width=3)
f1 = ImageFont.truetype(F, 26); f2 = ImageFont.truetype(F, 20)
d.text((470, 490), 'Length 6 ft = 72 in = 183 cm', font=f1, fill=ink, anchor='mt')
d.text((730, 255), 'Overall height', font=f2, fill=ink); d.text((730, 282), '(check ceiling)', font=f2, fill=(88, 82, 74))
d.text((40, 205), 'Gap between', font=f2, fill=ink); d.text((40, 232), 'decks', font=f2, fill=ink)
d.text((40, 24), 'Bunk bed size guide', font=ImageFont.truetype(F, 30), fill=ink)
d.line((0, 440, 960, 440), fill=(214, 200, 173), width=2)
d_im = brand(d_im, top=True)
save_jpg(d_im, f'{IMG}/blog-bunk-bed-size-guide.jpg', 86)
save_jpg(d_im.resize((480, 270), Image.LANCZOS), f'{IMG}/blog-bunk-bed-size-guide-sm.jpg', 84)
meta['blog-bunk-bed-size-guide'] = {'lg': (960, 540), 'sm': (480, 270)}

# Square logo + thumbnails for social / Google Business Profile
MARK = Image.open(U + '1000452098.png').convert('RGBA').crop((60, 115, 540, 610))
WORD = Image.open(U + '1000452098.png').convert('RGBA').crop((650, 280, 2090, 545))
sqL = Image.new('RGBA', (1024, 1024), (255, 255, 255, 255))
m = MARK.resize((430, round(MARK.height * 430 / MARK.width)), Image.LANCZOS); sqL.alpha_composite(m, ((1024 - m.width) // 2, 170))
wd = WORD.resize((820, round(WORD.height * 820 / WORD.width)), Image.LANCZOS); sqL.alpha_composite(wd, ((1024 - wd.width) // 2, 170 + m.height + 60))
sqL.convert('RGB').save(f'{IMG}/bunkworks-logo-square.png', optimize=True)
sqL.convert('RGB').resize((400, 400), Image.LANCZOS).save(f'{IMG}/bunkworks-logo-thumb.png', optimize=True)
meta['logo-square'] = (1024, 1024)

# OG image 1200x630 with logo plate
hero = Image.open(U + '1000406526.png').convert('RGB')
w, h = hero.size; ch = int(w * 630 / 1200); y0 = (h - ch) // 2
og = hero.crop((0, y0, w, y0 + ch)).resize((1200, 630), Image.LANCZOS).convert('RGBA')
plate_w = 520; pl = logo.resize((plate_w - 60, round(logo.height * (plate_w - 60) / logo.width)), Image.LANCZOS)
plate = Image.new('RGBA', (plate_w, pl.height + 50), (246, 242, 234, 245))
plate.paste(pl, (30, 25), pl)
og.paste(plate, (48, 630 - plate.height - 48), plate)
save_jpg(og, f'{OUT}/og-image.jpg', 84)

json.dump(meta, open('/home/claude/img_meta.json', 'w'), indent=1)
for f in sorted(os.listdir(IMG)): print(f, os.path.getsize(f'{IMG}/{f}'))
