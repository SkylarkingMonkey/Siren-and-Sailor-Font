"""Remove sub-unit quantization burrs, preserving every longer outline segment."""
from fontTools.ttLib.tables._g_l_y_f import GlyphCoordinates
from array import array

def clean(font):
 removed=0
 for name in font.getGlyphOrder():
  g=font['glyf'][name]
  if g.isComposite() or g.numberOfContours<=0:continue
  points=[];flags=[];ends=[];start=0
  for end in g.endPtsOfContours:
   src=list(zip(g.coordinates[start:end+1],g.flags[start:end+1]));start=end+1;out=[]
   for pt,flag in src:
    if out and (pt[0]-out[-1][0][0])**2+(pt[1]-out[-1][0][1])**2<=1:
     # Retain an explicit curve endpoint in preference to a coincident control.
     if flag&1 and not out[-1][1]&1:out[-1]=(pt,flag)
     removed+=1;continue
    out.append((pt,flag))
   while len(out)>3 and (out[-1][0][0]-out[0][0][0])**2+(out[-1][0][1]-out[0][0][1])**2<=1:
    out.pop();removed+=1
   if len(out)<3:removed+=len(out);continue
   points.extend([p for p,_ in out]);flags.extend([f for _,f in out]);ends.append(len(points)-1)
  g.coordinates=GlyphCoordinates(points);g.flags=array('B',flags);g.endPtsOfContours=ends;g.numberOfContours=len(ends)
 return removed
