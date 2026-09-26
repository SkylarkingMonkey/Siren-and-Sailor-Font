"""Draw family-specific nautical accents and assemble GF Latin Core composites."""
import unicodedata
from fontTools.agl import UV2AGL
from ufoLib2.objects import Component, Anchor

def gn(cp):return UV2AGL.get(cp,f'uni{cp:04X}')
def draw(g,commands):
 p=g.getPen()
 for op,args in commands:
  getattr(p,op)(*args)
def path(g,pts):
 p=g.getPen();p.moveTo(pts[0])
 for pt in pts[1:]:p.lineTo(pt)
 p.closePath()
def curve(g,start,segments):
 p=g.getPen();p.moveTo(start)
 for s in segments:
  if len(s)==1:p.lineTo(s[0])
  else:p.curveTo(*s)
 p.closePath()
def ellipse(g,x,y,rx,ry,reverse=False):
 k=.55228475;seq=[('moveTo',[(x+rx,y)]),('curveTo',[(x+rx,y+ry*k),(x+rx*k,y+ry),(x,y+ry)]),('curveTo',[(x-rx*k,y+ry),(x-rx,y+ry*k),(x-rx,y)]),('curveTo',[(x-rx,y-ry*k),(x-rx*k,y-ry),(x,y-ry)]),('curveTo',[(x+rx*k,y-ry),(x+rx,y-ry*k),(x+rx,y)]),('closePath',[])]
 if reverse:
  from fontTools.pens.reverseContourPen import ReverseContourPen
  p=ReverseContourPen(g.getPen())
  for op,args in seq:getattr(p,op)(*args)
 else:draw(g,seq)

def add_diacritics(f,core):
 marks={}
 def new(cp):
  g=f.newGlyph(gn(cp));g.unicode=cp;g.width=0;marks[cp]=g
  return g
 # Swept taper instead of disconnected ornaments; small acute hooks preserve legibility.
 g=new(0x301);curve(g,(-65,10),[[(-22,62),(21,129),(45,181)],[(71,192),(99,184),(112,170)],[(72,138),(10,53),(-35,6)],[(-65,10)]])
 g=new(0x300);g.components.append(Component(gn(0x301),(-1,0,0,1,0,0)))
 g=new(0x302);path(g,[(-145,15),(-26,179),(26,179),(145,15),(104,5),(0,119),(-104,5)])
 g=new(0x30C);path(g,[(-145,175),(-103,184),(0,68),(103,184),(145,175),(26,8),(-26,8)])
 g=new(0x303);curve(g,(-166,49),[[(-115,134),(-54,137),(16,94)],[(76,52),(108,39),(160,106)],[(149,36),(97,2),(33,29)],[(-48,69),(-87,119),(-166,49)]])
 g=new(0x304);curve(g,(-158,63),[[(-56,78),(44,79),(154,63)],[(154,30)],[ (48,39),(-53,43),(-158,31)],[(-158,63)]])
 g=new(0x306);curve(g,(-151,158),[[(-105,24),(101,24),(149,158)],[(111,168)],[(70,76),(-72,76),(-114,168)],[(-151,158)]])
 # Small pointed lozenges echo the apostrophe dots, without copying their excessive height.
 g=new(0x307);curve(g,(-36,79),[[(-32,125),(-11,157),(34,173)],[(32,130),(22,91),(5,69)],[(-16,61),(-31,61),(-36,79)]])
 g=new(0x308);g.components.extend([Component(gn(0x307),(1,0,0,1,-100,0)),Component(gn(0x307),(1,0,0,1,100,0))])
 g=new(0x30A);ellipse(g,0,110,93,93);ellipse(g,0,110,58,58,True)
 g=new(0x30B);g.components.extend([Component(gn(0x301),(.84,0,0,1,-91,0)),Component(gn(0x301),(.84,0,0,1,78,0))])
 g=new(0x326);curve(g,(-34,-61),[[(-63,-114),(-33,-154),(19,-144)],[(6,-180),(-25,-202),(-59,-223)],[(-14,-218),(58,-169),(65,-116)],[(70,-71),(9,-42),(-34,-61)]])
 g=new(0x327);curve(g,(18,10),[[(-31,-73)],[(27,-80),(83,-114),(73,-161)],[(63,-225),(-30,-244),(-94,-204)],[(-82,-176)],[(-36,-200),(31,-197),(35,-157)],[(39,-127),(-15,-109),(-72,-104)],[(-17,10)],[(18,10)]])
 g=new(0x328);curve(g,(23,10),[[(-60,-39),(-107,-119),(-63,-163)],[(-33,-195),(11,-176),(43,-143)],[(59,-163)],[ (15,-218),(-71,-235),(-108,-177)],[(-151,-112),(-97,-29),(-16,10)],[(23,10)]])
 for cp,g in marks.items():
  anchor='_bottom' if cp in [0x326,0x327,0x328] else '_top'
  g.anchors.append(Anchor(0,0,anchor))
  # Stack accents with mark-to-mark positioning.
  g.anchors.append(Anchor(0,-245 if anchor=='_bottom' else 225,anchor[1:]))
  g.lib['public.openTypeCategory']='mark'
 # Contextual caron for d, l, L and t is a compact side apostrophe.
 g=f.newGlyph('caroncomb.alt');g.width=0
 curve(g,(-20,0),[[(-1,92),(2,159),(28,207)],[(72,202),(69,184),(54,143)],[(27,71),(14,40),(-20,0)]])
 g.anchors.append(Anchor(0,0,'_top'));g.lib['public.openTypeCategory']='mark'
 g=f.newGlyph('commaabovecomb');g.width=0
 g.components.append(Component(gn(0x326),(-1,0,0,-1,0,-30)))
 g.anchors.append(Anchor(0,0,'_top'));g.lib['public.openTypeCategory']='mark'
 # Materialize reflected/nested marks now; final accents remain simple components.
 from fontTools.pens.recordingPen import DecomposingRecordingPen
 recs={}
 for mg in list(marks.values())+[f['commaabovecomb']]:
  pen=DecomposingRecordingPen(f, reverseFlipped=True);mg.draw(pen);recs[mg.name]=pen
 for n,p in recs.items():
  mg=f[n];mg.clearContours();mg.clearComponents();p.replay(mg.getPen())
 # Every base gets anchors; accent positions use optical stem axes for narrow I/l.
 for g in list(f):
  if not g.unicodes or not any(unicodedata.category(chr(c)).startswith('L') for c in g.unicodes):continue
  b=g.getBounds(f)
  if not b:continue
  x=(b[0]+b[2])/2; y=max(680,b[3])+70
  g.anchors.extend([Anchor(round(x),round(y),'top'),Anchor(round(x),min(0,round(b[1])),'bottom')])
 spacing={0x60:0x300,0xB4:0x301,0x2C6:0x302,0x2DC:0x303,0xAF:0x304,0x2D8:0x306,0x2D9:0x307,0xA8:0x308,0x2DA:0x30A,0x2DD:0x30B,0x2C7:0x30C,0xB8:0x327,0x2DB:0x328}
 for cp,mark in spacing.items():
  g=f.newGlyph(gn(cp));g.unicode=cp;g.width=460
  g.components.append(Component(gn(mark),(1,0,0,1,230,0 if mark in [0x327,0x328] else 760)))
 bycp={c:g.name for g in f for c in g.unicodes}
 composites={}
 for cp in core:
  if cp in bycp:continue
  decomp=unicodedata.normalize('NFD',chr(cp))
  if len(decomp)<2 or ord(decomp[0]) not in bycp:continue
  bcp=ord(decomp[0]);mcp=ord(decomp[1])
  if mcp not in marks:continue
  base=bycp[bcp]
  if bcp==ord('i') and mcp not in [0x328]:base=bycp[0x131]
  if bcp==ord('j'):base=bycp[0x237]
  mark=gn(mcp); b=f[base].getBounds(f); cx=(b[0]+b[2])/2
  below=mcp in [0x326,0x327,0x328]
  x=cx;y=min(0,b[1]) if below else max(680,b[3])+70
  if mcp==0x328:
   x=b[2]-45
   if chr(bcp) in 'Aa':x=b[2]-120
  # Latvian G K L N use comma below; lowercase g takes inverted comma above.
  if mcp==0x327 and chr(bcp) in 'GK LNgkln'.replace(' ',''):
   mark=gn(0x326)
   if chr(bcp)=='g':mark='commaabovecomb';x=cx;y=max(680,b[3])+70
  if cp in [0x10F,0x13D,0x13E,0x165]:
   mark='caroncomb.alt';x=b[2]+38;y=785 if chr(bcp)!='t' else 655
  g=f.newGlyph(gn(cp));g.unicode=cp;g.width=f[base].width
  g.components.extend([Component(base),Component(mark,(1,0,0,1,round(x),round(y)))])
  if cp in [0x10F,0x13D,0x13E,0x165]:g.width=max(g.width,round(x)+120)
  g.anchors.extend([Anchor(round(cx),round(max(680,b[3])+70),'top'),Anchor(round(cx),round(min(0,b[1])),'bottom')])
  composites[g.name]=base
 return composites
