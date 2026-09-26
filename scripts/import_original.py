"""Import the approved cubic outlines without retracing source photographs."""
import json, sys, shutil
from pathlib import Path
from fontTools.agl import UV2AGL
from ufoLib2 import Font
from ufoLib2.objects import Component
from fontTools.pens.reverseContourPen import ReverseContourPen
ROOT=Path(__file__).resolve().parents[1]
def name(cp): return UV2AGL.get(cp, f'uni{cp:04X}')
def import_original(path):
 data=json.loads(Path(path).read_text()); f=Font(); f.info.unitsPerEm=1400
 f.info.familyName='Siren and Sailor';f.info.styleName='Regular';f.info.capHeight=1000;f.info.xHeight=680
 g=f.newGlyph('.notdef');g.width=740;p=g.getPen()
 for pts in [[(60,0),(60,1000),(660,1000),(660,0)],[(105,45),(615,45),(615,955),(105,955)]]:
  p.moveTo(pts[0]);[p.lineTo(v) for v in pts[1:]];p.closePath()
 g=f.newGlyph('space');g.unicode=32;g.width=380
 for ch,cs in data['glyphs'].items():
  g=f.newGlyph(name(ord(ch)));g.unicode=ord(ch);g.width=data['advances'][ch]
  for c in cs:
   cubes=c['cubics'];pts=[q[0] for q in cubes]
   area=sum(a[0]*b[1]-b[0]*a[1] for a,b in zip(pts,pts[1:]+pts[:1]))/2
   # UFO expects outer CCW, inner CW; source is downward-positive.
   if (area<0)==c['hole']:cubes=[list(reversed(q)) for q in reversed(cubes)]
   coord=lambda v:(round(v[0],4),round(1000-v[1],4))
   p=g.getPen();p.moveTo(coord(cubes[0][0]))
   for q in cubes:
    # Only remove truly empty segments, never closed-loop cubics.
    if max(abs(v[k]-q[0][k]) for v in q for k in [0,1])<.0001:continue
    p.curveTo(*(coord(v) for v in q[1:]))
   p.closePath()
 g=f.newGlyph('zero');g.unicode=48;g.width=f['O'].width;g.components.append(Component('O'))
 g=f.newGlyph('uni00A0');g.unicode=160;g.width=f['space'].width
 f.glyphOrder=['.notdef','space']+[g.name for g in f if g.name not in ['.notdef','space']]
 return f
if __name__=='__main__':
 src=Path(sys.argv[1]) if len(sys.argv)>1 else ROOT/'upstream/glyph-construction.json'
 f=import_original(src);f.save(ROOT/'sources/base.ufo',overwrite=True)
 print(len(f),'base glyphs')
