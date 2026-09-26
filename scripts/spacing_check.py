"""Measure near-collisions in rendered glyph pairs; optionally correct source kerning."""
import json,math,sys
from pathlib import Path
import numpy as np
from PIL import ImageFont
from fontTools.ttLib import TTFont
from ufoLib2 import Font
ROOT=Path(__file__).resolve().parents[1]

def run(fix=False):
 uf=Font.open(ROOT/'sources/SirenandSailor-Regular.ufo');tf=TTFont(ROOT/'fonts/ttf/SirenandSailor-Regular.ttf');cm=tf.getBestCmap()
 font=ImageFont.truetype(str(ROOT/'fonts/ttf/SirenandSailor-Regular.ttf'),2048)
 chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?()\u2018\u2019\u201c\u201d'
 profiles={}
 for ch in chars:
  mask,(ox,oy)=font.getmask2(ch,mode='L',anchor='ls');arr=np.array(mask).reshape(mask.size[1],mask.size[0]);inside=arr>100
  ys=np.any(inside,axis=1);left=np.full(inside.shape[0],10000);right=np.full(inside.shape[0],-10000)
  for y in np.where(ys)[0]:
   xx=np.flatnonzero(inside[y]);left[y]=xx[0]+ox;right[y]=xx[-1]+ox
  profiles[ch]=(oy,left,right)
 membership=[{},{}]
 for n,gs in uf.groups.items():
  if n.startswith('public.kern1.'):membership[0].update({g:n for g in gs})
  elif n.startswith('public.kern2.'):membership[1].update({g:n for g in gs})
 def kern(a,b):
  la=membership[0].get(a,a);rb=membership[1].get(b,b)
  for key in [(a,b),(a,rb),(la,b),(la,rb)]:
   if key in uf.kerning:return uf.kerning[key],key
  return 0,(la,rb)
 issues=[]
 for a in chars:
  ay,al,ar=profiles[a]
  for b in chars:
   by,bl,br=profiles[b];lo=max(ay,by);hi=min(ay+len(ar),by+len(bl))
   if lo>=hi:continue
   an,bn=cm[ord(a)],cm[ord(b)];k,key=kern(an,bn);adv=tf['hmtx'][an][0]
   gap=float(np.min(adv+k+bl[lo-by:hi-by]-ar[lo-ay:hi-ay]))
   if gap<14:
    new=math.ceil(k+14-gap)
    issues.append({'pair':a+b,'minimum_gap_units':gap,'previous_kern':k,'new_kern':new,'key':key})
    if fix:uf.kerning[key]=new
 if fix:uf.save(overwrite=True)
 out={'units_per_em':2048,'sampled_pairs':len(chars)**2,'minimum_gap_threshold':14,'corrections_applied':fix,'issues':issues}
 (ROOT/'qa'/('spacing-adjustments.json' if fix else 'spacing-verification.json')).write_text(json.dumps(out,indent=2))
 print(len(issues),'near-collisions;',len(chars)**2,'pairs checked')
if __name__=='__main__':run('--fix-source' in sys.argv)
