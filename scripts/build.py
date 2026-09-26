"""Deterministic TTF and WOFF2 build from the editable UFO master."""
import os,subprocess,sys,json,hashlib
from pathlib import Path
from fontTools.ttLib import TTFont, newTable
from fontTools.otlLib.builder import buildStatTable
from clean_glyf import clean
from fontTools.ttLib.removeOverlaps import removeOverlaps
ROOT=Path(__file__).resolve().parents[1]
def main():
 os.environ['SOURCE_DATE_EPOCH']='1790337600'
 target=ROOT/'fonts/ttf/SirenandSailor-Regular.ttf';target.parent.mkdir(parents=True,exist_ok=True)
 subprocess.run([sys.executable,'-m','fontmake','-u',str(ROOT/'sources/SirenandSailor-Regular.ufo'),'-o','ttf','--output-path',str(target),'--overlaps-backend','pathops','--conversion-error','0.00035','--flatten-components','--drop-implied-oncurves','--no-autohint','--verbose','WARNING'],check=True)
 f=TTFont(target,recalcTimestamp=False)
 # Re-union quantized output, removing degeneracies introduced by grid rounding.
 removeOverlaps(f,glyphNames=[n for n in f.getGlyphOrder() if not f['glyf'][n].isComposite()],removeHinting=True)
 print('Removed',clean(f),'quantization duplicates/burrs')
 buildStatTable(f,[{'tag':'wght','name':'Weight','values':[{'value':400,'name':'Regular','flags':2}]},{'tag':'ital','name':'Italic','values':[{'value':0,'name':'Roman','flags':2}]}])
 f['meta']=newTable('meta');f['meta'].data={'dlng':'Latn','slng':'Latn'}
 # Controlled metadata and bounds recomputation, with no legacy kern duplication.
 f['head'].created=f['head'].modified=3873182400
 for gn in f.getGlyphOrder():
  g=f['glyf'][gn];g.recalcBounds(f['glyf']);aw,_=f['hmtx'][gn];f['hmtx'][gn]=(aw,getattr(g,'xMin',0))
 f['head'].flags |= 8
 f['OS/2'].fsSelection |= (1<<6)|(1<<7)|(1<<8)
 f['OS/2'].fsSelection &= ~(1|32)
 f['OS/2'].fsType=0
 f.save(target)
 # Stage the exact same binary in Google's expected family directory.
 import shutil
 stage=ROOT/'googlefonts/ofl/sirenandsailor';stage.mkdir(parents=True,exist_ok=True)
 shutil.copyfile(target,stage/target.name)
 final_license=ROOT/'OFL.txt'
 proposed=ROOT/'documentation/OFL-proposed.txt'
 if final_license.exists():shutil.copyfile(final_license,stage/'OFL.txt')
 elif proposed.exists():shutil.copyfile(proposed,stage/'OFL.txt')
 w=ROOT/'fonts/woff2/SirenandSailor-Regular.woff2';w.parent.mkdir(parents=True,exist_ok=True);f.flavor='woff2';f.save(w)
 print('Built',target.name, target.stat().st_size,'bytes')
 print('Built',w.name,w.stat().st_size,'bytes')
if __name__=='__main__':main()
