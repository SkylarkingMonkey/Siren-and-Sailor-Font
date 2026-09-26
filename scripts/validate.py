"""Coverage, shaping, metrics and deterministic-build evidence for the release candidate."""
from pathlib import Path
import json,unicodedata,hashlib
from fontTools.ttLib import TTFont
import uharfbuzz as hb
ROOT=Path(__file__).resolve().parents[1]
path=ROOT/'fonts/ttf/SirenandSailor-Regular.ttf';raw=path.read_bytes();f=TTFont(path);cm=f.getBestCmap()
required={int(s.split()[0],16) for s in (ROOT/'sources/GF_Latin_Core.nam').read_text().splitlines() if s.startswith('0x')}
face=hb.Face(raw);font=hb.Font(face);font.scale=(f['head'].unitsPerEm,)*2

def shape(text,features=None):
 b=hb.Buffer();b.add_str(text);b.guess_segment_properties();hb.shape(font,b,features or {})
 return {'glyphs':[f.getGlyphOrder()[g.codepoint] for g in b.glyph_infos],'positions':[[p.x_advance,p.y_advance,p.x_offset,p.y_offset] for p in b.glyph_positions]}
examples=['Café','façade','blåbær','cœur','Straße','Příliš žluťoučký kůň','Ģimene, ķīlis','a\u0301','i\u0308','j\u0308','į\u0301']
shapes={s:shape(s) for s in examples}
assert required<=set(cm)
assert all('.notdef' not in r['glyphs'] for r in shapes.values())
checks=[]
for cp in required:
 ch=chr(cp);decomp=unicodedata.normalize('NFD',ch)
 if ch!=decomp:
  a=shape(ch);b=shape(decomp);checks.append(a==b)
assert all(checks),'Canonical normalization changes shaping'
# Both figure sets must be available and correct.
tab=shape('0123456789',{'tnum':True});prop=shape('0123456789')
assert len({p[0] for p in tab['positions']})==1
assert len({p[0] for p in prop['positions']})>1
bad_lsb=[];clip=[]
for n in f.getGlyphOrder():
 g=f['glyf'][n]
 if not hasattr(g,'xMin'):continue
 if f['hmtx'][n][1]!=g.xMin:bad_lsb.append(n)
 if g.yMax>f['OS/2'].usWinAscent or g.yMin < -f['OS/2'].usWinDescent:clip.append(n)
assert not bad_lsb and not clip
woff=TTFont(ROOT/'fonts/woff2/SirenandSailor-Regular.woff2');assert woff.getBestCmap()==cm
r={'glyphs':len(f.getGlyphOrder()),'encoded_characters':len(cm),'latin_core_required':len(required),'latin_core_covered':len(required&set(cm)),'canonical_equivalence_tests':len(checks),'metric_errors':bad_lsb,'clipped_glyphs':clip,'tabular_width':tab['positions'][0][0],'proportional_digit_widths':[p[0] for p in prop['positions']],'features':sorted({x.FeatureTag for t in ['GSUB','GPOS'] if t in f for x in f[t].table.FeatureList.FeatureRecord}),'shaping_samples':shapes,'sha256':hashlib.sha256(raw).hexdigest()}
(ROOT/'qa/validation.json').write_text(json.dumps(r,indent=2,ensure_ascii=False));print({k:v for k,v in r.items() if k!='shaping_samples'})
