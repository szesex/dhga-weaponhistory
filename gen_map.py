#!/usr/bin/env python3
"""PNG map generator from scratch - only zlib needed"""
import zlib, struct

def make_png(w, h, raw_rgb):
    def chunk(t, d):
        c = t + d
        return struct.pack('>I', len(d)) + t + d + struct.pack('>I', zlib.crc32(c) & 0xffffffff)
    sig = b'\x89PNG\r\n\x1a\n'
    ihdr = chunk(b'IHDR', struct.pack('>IIBBBBB', w, h, 8, 2, 0, 0, 0))
    idat = chunk(b'IDAT', zlib.compress(bytes(raw_rgb), 6))
    iend = chunk(b'IEND', b'')
    return sig + ihdr + idat + iend

def rgb(r,g,b): return (r,g,b)
GREEN = rgb(50,200,80)
ORANGE = rgb(255,160,30)
RED = rgb(220,50,50)
BLACK = rgb(20,20,30)
WHITE = rgb(255,255,255)
GRAY = rgb(80,90,100)
YELLOW = rgb(255,230,50)
DARK_GREEN = rgb(50,70,50)
OCEAN1 = rgb(10,30,80)
OCEAN2 = rgb(20,60,130)
GRID = rgb(40,50,70)

W, H = 1200, 700

def lat_lon_to_xy(lon, lat):
    x = max(0, min(W-1, int((lon + 180) / 360 * W)))
    y = max(0, min(H-1, int((90 - lat) / 180 * H)))
    return x, y

def blend(c1, c2, t):
    return tuple(int(c1[i] + (c2[i]-c1[i])*t) for i in range(3))

def draw_line(img, x1,y1,x2,y2, col, steps=30):
    for i in range(steps+1):
        xi = int(x1 + (x2-x1)*i/steps)
        yi = int(y1 + (y2-y1)*i/steps)
        if 0<=xi<W and 0<=yi<H:
            img[yi][xi] = col

def draw_arc(img, x1,y1,x2,y2, col, steps=40, height=0.18):
    for i in range(steps+1):
        t = i/steps
        xi = int(x1 + (x2-x1)*t)
        dy = (t-0.5)**2
        yi = int(y1 + (y2-y1)*t - dy*(y2-y1)*height - 55*dy)
        if 0<=xi<W and 0<=yi<H:
            img[yi][xi] = col

def fill_circle(img, cx, cy, r, col):
    for dy in range(-r, r+1):
        for dx in range(-r, r+1):
            if dx*dx + dy*dy <= r*r:
                ny = cy+dy; nx = cx+dx
                if 0<=ny<H and 0<=nx<W:
                    img[ny][nx] = col

def fill_rect(img, x,y,w,h, col):
    for dy in range(h):
        for dx in range(w):
            ny=y+dy; nx=x+dx
            if 0<=ny<H and 0<=nx<W:
                img[ny][nx] = col

def point_in_poly(x, y, poly):
    inside = False
    for i in range(len(poly)):
        p1 = poly[i]; p2 = poly[(i+1)%len(poly)]
        if ((p1[1] > y) != (p2[1] > y)) and x < (p2[0]-p1[0])*(y-p1[1])/(p2[1]-p1[1])+p1[0]:
            inside = not inside
    return inside

PIXEL_FONT = {
    'A':[0b01110,0b10001,0b11111,0b10001,0b10001],
    'B':[0b11110,0b10001,0b11110,0b10001,0b11110],
    'C':[0b01111,0b10000,0b10000,0b10000,0b01111],
    'D':[0b11110,0b10001,0b10001,0b10001,0b11110],
    'E':[0b11111,0b10000,0b11110,0b10000,0b11111],
    'F':[0b11111,0b10000,0b11110,0b10000,0b10000],
    'G':[0b01111,0b10000,0b10111,0b10001,0b01110],
    'H':[0b10001,0b10001,0b11111,0b10001,0b10001],
    'I':[0b11111,0b00100,0b00100,0b00100,0b11111],
    'J':[0b00111,0b00001,0b00001,0b10001,0b01110],
    'K':[0b10001,0b10010,0b11100,0b10010,0b10001],
    'L':[0b10000,0b10000,0b10000,0b10000,0b11111],
    'M':[0b10001,0b11011,0b10101,0b10001,0b10001],
    'N':[0b10001,0b11001,0b10101,0b10011,0b10001],
    'O':[0b01110,0b10001,0b10001,0b10001,0b01110],
    'P':[0b11110,0b10001,0b11110,0b10000,0b10000],
    'Q':[0b01110,0b10001,0b10101,0b10010,0b01101],
    'R':[0b11110,0b10001,0b11110,0b10010,0b10001],
    'S':[0b01111,0b10000,0b01110,0b00001,0b11110],
    'T':[0b11111,0b00100,0b00100,0b00100,0b00100],
    'U':[0b10001,0b10001,0b10001,0b10001,0b01110],
    'V':[0b10001,0b10001,0b10001,0b01010,0b00100],
    'W':[0b10001,0b10001,0b10101,0b11011,0b10001],
    'X':[0b10001,0b01010,0b00100,0b01010,0b10001],
    'Y':[0b10001,0b01010,0b00100,0b00100,0b00100],
    'Z':[0b11111,0b00010,0b00100,0b01000,0b11111],
    '0':[0b01110,0b10011,0b10101,0b11001,0b01110],
    '1':[0b00100,0b01100,0b00100,0b00100,0b01110],
    '2':[0b01110,0b10001,0b00110,0b01000,0b11111],
    '3':[0b11110,0b00001,0b01110,0b00001,0b11110],
    '4':[0b10001,0b10001,0b11111,0b00001,0b00001],
    '5':[0b11111,0b10000,0b11110,0b00001,0b11110],
    '6':[0b01110,0b10000,0b11110,0b10001,0b01110],
    '7':[0b11111,0b00001,0b00010,0b00100,0b00100],
    '8':[0b01110,0b10001,0b01110,0b10001,0b01110],
    '9':[0b01110,0b10001,0b01111,0b00001,0b01110],
    ' ':[0b00000,0b00000,0b00000,0b00000,0b00000],
    '/':[0b00001,0b00010,0b00100,0b01000,0b10000],
    '-':[0b00000,0b00000,0b11111,0b00000,0b00000],
    '.':[0b00000,0b00000,0b00000,0b00000,0b00100],
    ':':[0b00000,0b00100,0b00000,0b00100,0b00000],
    ',':[0b00000,0b00000,0b00000,0b00100,0b01000],
    '\'':[0b00100,0b01000,0b00000,0b00000,0b00000],
    '(':[0b00011,0b00100,0b01000,0b00100,0b00011],
    ')':[0b11000,0b00100,0b00010,0b00100,0b11000],
}

def draw_text(img, x, y, text, col, scale=1):
    sx = x
    for ch in text.upper():
        if ch not in PIXEL_FONT: continue
        for row in range(5):
            for col_idx in range(7):
                if PIXEL_FONT[ch][row] & (1 << (6-col_idx)):
                    py = y + row*scale
                    px = sx + col_idx*scale
                    for dy in range(scale):
                        for dx in range(scale):
                            if 0<=py+dy<H and 0<=px+dx<W:
                                img[py+dy][px+dx] = col
        sx += 8*scale

# ===== SUPPLY CHAIN DATA =====
edges = [
    ("中國鞍鋼","德國萊茵金屬",5,"supply",122.9942,41.1067,8.6821,50.1109),
    ("中國鞍鋼","俄羅斯軍甲",8,"supply",122.9942,41.1067,37.6173,55.7558),
    ("澳洲BHP","法國空客",7,"supply",151.2152,-33.8688,2.3522,48.8566),
    ("俄羅斯VSMPO","美國康明斯",9,"supply",61.3960,54.8950,-86.8025,36.1627),
    ("日本東京電子","美國諾格導引",10,"supply",139.7454,35.6586,-118.2437,34.0522),
    ("台灣台積電","以色列拉斐爾",10,"supply",121.5598,24.9737,34.8516,31.0461),
    ("中國包頭稀土","日本松下",8,"supply",109.8400,40.6560,138.2529,36.2048),
    ("以色列埃爾比爾","中國北方工業",6,"supply",34.8516,31.0461,116.4074,39.9042),
    ("美國Albemarle","美國特斯拉",7,"supply",-93.0000,37.0000,-122.4194,37.7749),
    ("澳洲BHP","法國達索",6,"supply",151.2152,-33.8688,2.3522,48.8566),
    ("德國萊茵金屬","美國萊文沃思",5,"assembly",8.6821,50.1109,95.2350,39.3489),
    ("俄羅斯軍甲","俄羅斯杜丁",9,"assembly",37.6173,55.7558,37.6173,55.7558),
    ("法國空客","日本三菱",8,"assembly",2.3522,48.8566,138.2529,36.2048),
    ("美國康明斯","美國萊文沃思",7,"assembly",-86.8025,36.1627,95.2350,39.3489),
    ("美國通用原子","日本三菱",8,"assembly",-117.1492,32.7157,138.2529,36.2048),
    ("美國諾格導引","以色列埃爾比爾",10,"assembly",-118.2437,34.0522,34.8516,31.0461),
    ("以色列拉斐爾","以色列埃爾比爾",10,"assembly",34.8516,31.0461,34.8516,31.0461),
    ("日本松下","中國北方工業",8,"assembly",138.2529,36.2048,116.4074,39.9042),
    ("美國特斯拉","以色列埃爾比爾",7,"assembly",-122.4194,37.7749,34.8516,31.0461),
    ("法國達索","日本三菱",7,"assembly",2.3522,48.8566,138.2529,36.2048),
    ("中國北方工業","以色列埃爾比爾",6,"assembly",116.4074,39.9042,34.8516,31.0461),
    ("美國萊文沃思","阿拉斯加",4,"deploy",95.2350,39.3489,-149.9000,61.2180),
    ("日本三菱","横須賀",9,"deploy",138.2529,36.2048,139.6386,35.3228),
    ("日本三菱","冲繩",8,"deploy",138.2529,36.2048,127.6780,26.5018),
    ("日本三菱","關島",8,"deploy",138.2529,36.2048,144.7937,13.4443),
    ("以色列埃爾比爾","阿拉斯加",10,"deploy",34.8516,31.0461,-149.9000,61.2180),
    ("以色列埃爾比爾","夏威夷",8,"deploy",34.8516,31.0461,-157.8260,21.3069),
    ("以色列埃爾比爾","横田",9,"deploy",34.8516,31.0461,139.3600,35.7400),
    ("中國北方工業","釜山",7,"deploy",116.4074,39.9042,129.0403,35.1798),
    ("中國北方工業","大邱",6,"deploy",116.4074,39.9042,128.6000,35.8700),
    ("俄羅斯杜丁","横須賀",8,"deploy",37.6173,55.7558,139.6386,35.3228),
]

type_colors = {"supply": GREEN, "assembly": ORANGE, "deploy": RED}

# ===== DRAW MAP =====
img = [[BLACK for _ in range(W)] for _ in range(H)]

# Ocean gradient
for y in range(H):
    t = y / H
    ocean = blend(OCEAN1, OCEAN2, t*0.5)
    for x in range(W):
        img[y][x] = ocean

# Grid lines
for lon in range(-180, 181, 30):
    x, _ = lat_lon_to_xy(lon, 0)
    if 0<=x<W:
        for y in range(H):
            img[y][x] = GRID
for lat in range(-90, 91, 30):
    _, y = lat_lon_to_xy(0, lat)
    if 0<=y<H:
        for x in range(W):
            img[y][x] = GRID

# Simplified continental outlines
continents = [
    [(-170,65),(-140,70),(-95,70),(-80,45),(-95,25),(-120,30),(-125,45),(-165,60)],
    [(-80,10),(-35,0),(-40,-15),(-55,-25),(-70,-55),(-75,-50),(-80,10)],
    [(0,70),(30,70),(40,60),(20,45),(5,35),(0,40),(-10,45),(-10,55),(0,70)],
    [(10,35),(40,35),(50,10),(35,-10),(20,-35),(-10,-35),(-10,10),(10,35)],
    [(40,70),(60,70),(100,75),(145,60),(180,70),(180,50),(140,30),(120,25),(100,30),(70,25),(60,20),(50,10),(40,20),(30,30),(40,70)],
    [(115,-20),(150,-15),(155,-30),(145,-40),(115,-35),(110,-25),(115,-20)],
    [(128,45),(132,38),(142,35),(145,40),(138,45),(128,45)],
]

for poly in continents:
    minx = min(p[0] for p in poly); maxx = max(p[0] for p in poly)
    miny = min(p[1] for p in poly); maxy = max(p[1] for p in poly)
    for test_y in range(int(miny), int(maxy)+1):
        for test_x in range(int(minx), int(maxx)+1):
            if point_in_poly(test_x, test_y, poly):
                if -170 <= test_x <= 180 and -70 <= test_y <= 75:
                    tx, ty = lat_lon_to_xy(test_x, test_y)
                    if 0<=tx<W and 0<=ty<H:
                        img[ty][tx] = DARK_GREEN

# Draw edges
for src, tgt, weight, etype, slon, slat, tlon, tlat in edges:
    col = type_colors[etype]
    x1,y1 = lat_lon_to_xy(slon, slat)
    x2,y2 = lat_lon_to_xy(tlon, tlat)
    if etype == "deploy":
        draw_line(img, x1,y1,x2,y2, col, steps=50)
    else:
        draw_arc(img, x1,y1,x2,y2, col, steps=60, height=0.18)

# Draw node points
nodes = [
    (122.9942,41.1067,"鞍鋼"),(8.6821,50.1109,"萊茵金屬"),(37.6173,55.7558,"俄軍甲"),
    (151.2152,-33.8688,"BHP"),(2.3522,48.8566,"空客"),(-86.8025,36.1627,"康明斯"),
    (139.7454,35.6586,"東京電子"),(-118.2437,34.0522,"諾格"),(121.5598,24.9737,"台積電"),
    (34.8516,31.0461,"埃爾比爾"),(109.8400,40.6560,"包頭稀土"),(138.2529,36.2048,"松下/三菱"),
    (116.4074,39.9042,"北方工業"),(-93.0000,37.0000,"Albemarle"),(-122.4194,37.7749,"特斯拉"),
    (95.2350,39.3489,"萊文沃思"),(-117.1492,32.7157,"通用原子"),(61.3960,54.8950,"VSMPO"),
    (-149.9000,61.2180,"阿拉斯加"),(139.6386,35.3228,"横須賀"),(127.6780,26.5018,"冲繩"),
    (144.7937,13.4443,"關島"),(-157.8260,21.3069,"夏威夷"),(139.3600,35.7400,"横田"),
    (129.0403,35.1798,"釜山"),(128.6000,35.8700,"大邱"),
]
for lon, lat, name in nodes:
    x, y = lat_lon_to_xy(lon, lat)
    fill_circle(img, x, y, 5, YELLOW)

# Legend box
fill_rect(img, 15, 15, 190, 105, rgb(10,15,30))
draw_text(img, 20, 20, "SUPPLY CHAIN MAP", WHITE, 2)
draw_text(img, 20, 42, "GREEN = SUPPLY", GREEN, 1)
draw_text(img, 20, 58, "ORANGE = ASSEMBLY", ORANGE, 1)
draw_text(img, 20, 74, "RED = DEPLOY", RED, 1)
draw_text(img, 20, 90, "YELLOW = NODES", YELLOW, 1)

# Title
draw_text(img, 420, 20, "US WEAPONS SUPPLY CHAIN: 1776-2026", WHITE, 2)
draw_text(img, 420, 50, "TRANS-PACIFIC EVOLUTION", WHITE, 2)
draw_text(img, 420, 75, "Pacific Link + Middle East + Control Comparison", rgb(150,180,200), 1)

# Bottom bar
fill_rect(img, 0, H-28, W, 28, rgb(10,15,30))
draw_text(img, 15, H-20, "Sources: obsidian-vault/supply_chain_edges_georeferenced.csv | DHGA Project 2026", GRAY, 1)

# Generate PNG
flat = [c for row in img for px in row for c in px]
png_data = make_png(W, H, flat)

with open('/home/node/.openclaw/workspace/obsidian-vault/qgis_supply_chain_map.png', 'wb') as f:
    f.write(png_data)
print(f"Generated: {len(png_data)} bytes PNG saved to qgis_supply_chain_map.png")