"""One-time, fully recorded production-source preparation from the approved artwork.
The saved UFO is the editable master; regular builds do not retrace or regenerate it.
"""
import json,math,copy,unicodedata
from pathlib import Path
from ufoLib2 import Font
from ufoLib2.objects import Component, Anchor
from fontTools.pens.recordingPen import DecomposingRecordingPen
from fontTools.pens.transformPen import TransformPen
from import_original import import_original, name
from diacritics import add_diacritics
ROOT=Path(__file__).resolve().parents[1]

def materialize(g,f):
 p=DecomposingRecordingPen(f);g.draw(p);g.clearContours();g.clearComponents();p.replay(g.getPen())
def shift(g,dx):
 for c in g.contours:
  for p in c.points:p.x+=dx
 for c in g.components:
  a,b,cx,d,e,fy=c.transformation;c.transformation=(a,b,cx,d,e+dx,fy)
 for a in g.anchors:a.x+=dx

def clean_wave_spurs(f):
 # Remove tracing seams that travel down and back along a sub-unit sliver.
 # Limited to the three wave dashes; preserve all actual swept terminals.
 removed=0
 for name_ in ['hyphen','endash','emdash']:
  g=f[name_]
  for contour in g.contours:
   changed=True
   while changed:
    changed=False;pts=contour.points;ons=[i for i,p in enumerate(pts) if p.type]
    for a,b,c in zip(ons,ons[1:],ons[2:]):
     p,q,r=pts[a],pts[b],pts[c]
     if math.hypot(p.x-r.x,p.y-r.y)>1.5 or math.hypot(p.x-q.x,p.y-q.y)<20:continue
     def straight(i,j):
      x,y=pts[i],pts[j];dx=y.x-x.x;dy=y.y-x.y;length=math.hypot(dx,dy)
      return length and all(abs(dx*(v.y-x.y)-dy*(v.x-x.x))/length<.6 for v in pts[i+1:j])
     if straight(a,b) and straight(b,c):
      pts[c].type='line';del pts[a+1:c];removed+=1;changed=True;break
 return removed

def spacing(f):
 report=[]
 caps={'A':(29,29),'B':(57,43),'C':(45,39),'D':(56,44),'E':(53,37),'F':(54,26),'G':(45,45),'H':(60,60),'I':(47,47),'J':(34,48),'K':(57,33),'L':(52,24),'M':(52,52),'N':(58,57),'O':(44,44),'P':(57,33),'Q':(44,30),'R':(56,35),'S':(39,38),'T':(25,25),'U':(58,50),'V':(25,25),'W':(25,25),'X':(28,28),'Y':(26,26),'Z':(37,37)}
 lower={'a':(39,44),'b':(46,38),'c':(36,31),'d':(38,46),'e':(36,31),'f':(27,20),'g':(38,41),'h':(46,46),'i':(47,47),'j':(28,44),'k':(46,29),'l':(43,43),'m':(46,46),'n':(46,46),'o':(37,37),'p':(46,38),'q':(38,46),'r':(45,23),'s':(33,32),'t':(30,27),'u':(45,46),'v':(22,22),'w':(22,22),'x':(27,27),'y':(22,25),'z':(32,32)}
 for g in list(f):
  if g.name=='.notdef' or not g.unicodes:continue
  cp=g.unicode;ch=chr(cp);bounds=g.getBounds(f)
  if not bounds:continue
  # Full materialization before moving bases prevents cascading component shifts.
  if ch in caps:l,r=caps[ch]
  elif ch in lower:l,r=lower[ch]
  elif ch=='0':l,r=caps['O']
  elif ch.isdecimal():l,r=40,40
  elif unicodedata.category(ch).startswith('L'):l,r=(45,42) if ch.isupper() else (40,40)
  elif ch in '-–—':
   target={'-':560,'–':700,'—':1400}[ch];l,r=40,40
   factor=(target-l-r)/(bounds[2]-bounds[0]);p=DecomposingRecordingPen(f);g.draw(p);g.clearContours();g.clearComponents();p.replay(TransformPen(g.getPen(),(factor,0,0,1,0,0)));bounds=g.getBounds(f)
  elif ch in '.,:;':l,r=65,65
  else:l,r=55,55
  old=g.width;dx=l-bounds[0];shift(g,dx);g.width=round(bounds[2]-bounds[0]+l+r)
  report.append({'glyph':g.name,'left':l,'right':r,'advance_before':old,'advance_after':g.width})
 return report

def meta(f):
 i=f.info;i.familyName='Siren and Sailor';i.styleName='Regular';i.styleMapFamilyName='Siren and Sailor';i.styleMapStyleName='regular'
 i.versionMajor=1;i.versionMinor=0;i.unitsPerEm=1400;i.ascender=1430;i.descender=-470;i.capHeight=1000;i.xHeight=680
 i.copyright='Copyright 2026 Jean-Marc Daecius'
 i.openTypeNameDesigner='Jean-Marc Daecius'
 i.openTypeNameManufacturer='Jean-Marc Daecius'
 i.openTypeNameDescription='A nautical display serif designed by Jean-Marc Daecius. Swept serifs, hook terminals and calligraphic contrast. Best at display sizes.'
 i.openTypeNameLicense='This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://openfontlicense.org'
 i.openTypeNameLicenseURL='https://openfontlicense.org'
 i.openTypeNameVersion='Version 1.000'
 i.openTypeNameUniqueID='1.000;NONE;SirenandSailor-Regular'
 i.postscriptFontName='SirenandSailor-Regular';i.postscriptFullName='Siren and Sailor Regular';i.postscriptWeightName='Regular'
 i.openTypeOS2WeightClass=400;i.openTypeOS2WidthClass=5;i.openTypeOS2VendorID='NONE';i.openTypeOS2Selection=[7,8];i.openTypeOS2Type=[]
 i.openTypeOS2Panose=[2,2,5,3,6,5,6,2,2,4]
 i.postscriptUnderlinePosition=-135;i.postscriptUnderlineThickness=55
 i.openTypeOS2StrikeoutSize=48;i.openTypeOS2StrikeoutPosition=385
 i.openTypeOS2SubscriptXSize=910;i.openTypeOS2SubscriptYSize=910;i.openTypeOS2SubscriptXOffset=0;i.openTypeOS2SubscriptYOffset=190
 i.openTypeOS2SuperscriptXSize=910;i.openTypeOS2SuperscriptYSize=910;i.openTypeOS2SuperscriptXOffset=0;i.openTypeOS2SuperscriptYOffset=490
 i.openTypeHeadCreated='2026/09/25 12:00:00';i.italicAngle=0
 i.openTypeGaspRangeRecords=[{'rangeMaxPPEM':65535,'rangeGaspBehavior':[0,1,2,3]}]

def kerning(f,comps):
 bases={}
 bycp={cp:g.name for g in f for cp in g.unicodes}
 for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':bases[bycp[ord(ch)]]=ch
 for n,b in comps.items():
  ch=next((c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' if b==bycp[ord(c)]),None)
  if b==bycp.get(0x131):ch='i'
  if b==bycp.get(0x237):ch='j'
  if ch:bases[n]=ch
 for cp,base in {0xD0:'D',0x110:'D',0x111:'d',0x126:'H',0x127:'h',0x141:'L',0x142:'l',0xD8:'O',0xF8:'o',0x131:'i',0x237:'j'}.items():
  if cp in bycp:bases[bycp[cp]]=base
 for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
  members=[n for n,b in bases.items() if b==ch]
  for side in [1,2]:f.groups[f'public.kern{side}.{ch}']=members
 pairs={}
 def kp(left,right,val):
  for a in left:
   for b in right:pairs[a,b]=val
 kp('A','TVWY',-83);kp('A','COGQ',-20);kp('VWY','A',-76);kp('T','AOQCSG',-62)
 kp('L','TVWY',-88);kp('F','AOQCSG',-38);kp('P','A',-49);kp('R','TVWY',-34)
 kp('VWY','OQCGS',-38);kp('OQCG','AVWY',-28);kp('D','AVWY',-28)
 kp('T','aceorsuvwy',-76);kp('VWY','aceos',-46);kp('F','aceos',-36)
 kp('a','vwxy',-18);kp('vwxy','aceos',-22);kp('r','aceos',-23)
 kp('f','aceo',-20);kp('o','vwxy',-18);kp('k','aceo',-21)
 kp('P','a',-34);kp('T','p',-23);kp('Y','p',-38)
 kp('A','U',-12);kp('L','OQCG',-12);kp('Y','u',-45)
 for (a,b),v in pairs.items():f.kerning[f'public.kern1.{a}',f'public.kern2.{b}']=v
 for left,val in [('F',-100),('P',-110),('T',-90),('V',-100),('W',-80),('Y',-100),('r',-50)]:
  for right in ['period','comma']:f.kerning[f'public.kern1.{left}',right]=val
 return len(f.kerning)

def main():
 from extended_letters import add_extended_letters
 from symbols import add_symbols
 f=import_original(ROOT/'upstream/glyph-construction.json')
 add_extended_letters(f);add_symbols(f)
 # Freeze component-dependent geometry before independent sidebearing changes.
 records={}
 for g in f:
  p=DecomposingRecordingPen(f);g.draw(p);records[g.name]=p
 for g in f:g.clearContours();g.clearComponents();records[g.name].replay(g.getPen())
 clean_wave_spurs(f)
 sr=spacing(f)
 core=[int(line.split()[0],16) for line in (ROOT/'sources/GF_Latin_Core.nam').read_text().splitlines() if line.startswith('0x')]
 # Supplementary European accents use the same established construction system.
 extra=[0x114,0x115,0x12C,0x12D,0x14C,0x14D,0x14E,0x14F,0x16C,0x16D]
 comps=add_diacritics(f,core+extra)
 # Mathematical signs share width and optical center.
 math_names=['plus','equal','minus','multiply','divide','less','greater']
 mw=max(f[n].width for n in math_names)
 for n in math_names:
  g=f[n];shift(g,round((mw-g.width)/2));g.width=mw
 from diacritics import ellipse
 g=f.newGlyph('uni25CC');g.unicode=0x25CC;g.width=800
 for a in range(0,360,30):
  rad=math.radians(a);ellipse(g,400+280*math.cos(rad),340+280*math.sin(rad),21,21)
 g.anchors.extend([Anchor(400,770,'top'),Anchor(400,0,'bottom')])
 
 # Add required standalone anchors for .notdef, etc. Keep space/nbsp exactly equal.
 f['uni00A0'].width=f['space'].width
 meta(f);nk=kerning(f,comps)
 bycp={cp:g.name for g in f for cp in g.unicodes}
 # Dot removal before upper combining accents, including iogonek.
 dotted_i=bycp[0x131];dotted_j=bycp[0x237];iog=bycp[0x12F]
 g=f.newGlyph('iogonek.nodot');g.width=f[iog].width
 g.components.append(Component(dotted_i))
 for comp in f[iog].components:
  if comp.baseGlyph!=bycp[ord('i')]:g.components.append(copy.deepcopy(comp))
 g.anchors=[copy.deepcopy(a) for a in f[iog].anchors]
 # Nonspacing characters useful for interoperable text and shaping.
 for cp in [0x200B,0x200C,0x200D,0x2028,0x2029,0x2060,0xFEFF]:
  g=f.newGlyph(name(cp));g.unicode=cp;g.width=0
 # Proportional default digits and fixed-width alternates.
 digits=[bycp[ord(c)] for c in '0123456789'];tw=max(f[n].width for n in digits)
 for n in digits:
  g=f.newGlyph(n+'.tnum');g.width=tw;g.components.append(Component(n,(1,0,0,1,round((tw-f[n].width)/2),0)))
 f.features.text='languagesystem DFLT dflt;\nlanguagesystem latn dflt;\nlanguagesystem latn TRK;\nlanguagesystem latn AZE;\nlanguagesystem latn ROM;\nlanguagesystem latn MOL;\nfeature tnum {\n'+''.join(f'  sub {n} by {n}.tnum;\n' for n in digits)+'} tnum;\n'
 above=[name(cp) for cp in [0x300,0x301,0x302,0x303,0x304,0x306,0x307,0x308,0x30A,0x30B,0x30C]]
 f.features.text+='\n@Above=['+' '.join(above)+'];\n@SoftDotted=[i j '+iog+'];\n@NoDot=['+dotted_i+' '+dotted_j+' iogonek.nodot];\nfeature ccmp { sub @SoftDotted\' @Above by @NoDot; } ccmp;\n'
 # Source glyph class labels improve GDEF and mark lookup generation.
 for g in f:
  if g.lib.get('public.openTypeCategory')!='mark':g.lib['public.openTypeCategory']='base'
 order=['.notdef','space']+sorted([g.name for g in f if g.name not in ['.notdef','space']],key=lambda n:(not bool(f[n].unicodes),f[n].unicode or 0,n))
 f.glyphOrder=order
 bounds=[g.getBounds(f) for g in f if g.getBounds(f)]
 ymax=math.ceil(max(b[3] for b in bounds));ymin=math.floor(min(b[1] for b in bounds))
 asc=max(1430,ymax+20);desc=min(-470,ymin-20)
 f.info.ascender=asc;f.info.descender=desc
 for key,v in {'openTypeHheaAscender':asc,'openTypeHheaDescender':desc,'openTypeHheaLineGap':0,'openTypeOS2TypoAscender':asc,'openTypeOS2TypoDescender':desc,'openTypeOS2TypoLineGap':0,'openTypeOS2WinAscent':asc,'openTypeOS2WinDescent':-desc}.items():setattr(f.info,key,v)
 missing=sorted(set(core)-{cp for g in f for cp in g.unicodes})
 if missing:raise ValueError('Missing Core characters: '+repr([(hex(c),chr(c),unicodedata.name(chr(c))) for c in missing]))
 # Normalize production em size without changing relative drawing proportions.
 scale=2048/1400
 for g in f:
  for contour in g.contours:
   for p in contour.points:p.x=round(p.x*scale,4);p.y=round(p.y*scale,4)
  for c in g.components:
   a,b,cx,d,e,fy=c.transformation;c.transformation=(a,b,cx,d,round(e*scale),round(fy*scale))
  for a in g.anchors:a.x=round(a.x*scale);a.y=round(a.y*scale)
  g.width=round(g.width*scale)
 for pair in list(f.kerning):f.kerning[pair]=round(f.kerning[pair]*scale)
 for attr in ['unitsPerEm','ascender','descender','capHeight','xHeight','openTypeHheaAscender','openTypeHheaDescender','openTypeOS2TypoAscender','openTypeOS2TypoDescender','openTypeOS2WinAscent','openTypeOS2WinDescent','postscriptUnderlinePosition','postscriptUnderlineThickness','openTypeOS2StrikeoutSize','openTypeOS2StrikeoutPosition','openTypeOS2SubscriptXSize','openTypeOS2SubscriptYSize','openTypeOS2SubscriptXOffset','openTypeOS2SubscriptYOffset','openTypeOS2SuperscriptXSize','openTypeOS2SuperscriptYSize','openTypeOS2SuperscriptXOffset','openTypeOS2SuperscriptYOffset']:
  setattr(f.info,attr,round(getattr(f.info,attr)*scale))
 f.save(ROOT/'sources/SirenandSailor-Regular.ufo',overwrite=True)
 (ROOT/'qa/source-preparation.json').write_text(json.dumps({'glyphs':len(f),'encoded_characters':len({cp for g in f for cp in g.unicodes}),'latin_core_required':len(core),'missing':missing,'kern_pairs':nk,'vertical_bounds':[ymin,ymax],'vertical_metrics':[asc,desc],'spacing':sr},indent=2))
 print('Prepared',len(f),'glyphs;',len(core),'GF Latin Core entries;',nk,'kerning pairs; bounds',ymin,ymax)
if __name__=='__main__':main()
