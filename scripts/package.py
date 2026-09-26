"""Package the reviewed sources, fonts, proofs and evidence; omit tool binaries."""
import hashlib,json,shutil,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def main():
 out=ROOT/'dist';out.mkdir(exist_ok=True)
 files=[ROOT/n for n in ['README.md','AUTHORS.txt','CONTRIBUTORS.txt','requirements.txt','requirements-qa.txt']]
 if (ROOT/'OFL.txt').exists():files.append(ROOT/'OFL.txt')
 for folder in ['scripts','documentation','fonts','proofs','googlefonts']:
  files.extend(p for p in (ROOT/folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
 files.extend(p for p in (ROOT/'sources/SirenandSailor-Regular.ufo').rglob('*') if p.is_file())
 files.extend([ROOT/'sources/GF_Latin_Core.nam',ROOT/'upstream/glyph-construction.json'])
 for n in ['READINESS.md','fontspector.json','fontspector.md','fontspector.html','fontspector.log','validation.json','spacing-verification.json','source-preparation.json','reproducibility.json','fontspector-tool.json']:
  files.append(ROOT/'qa'/n)
 manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(set(files))}
 (ROOT/'SHA256SUMS.json').write_text(json.dumps(manifest,indent=2));files.append(ROOT/'SHA256SUMS.json')
 zip_path=out/'SirenAndSailor-Font-Package.zip'
 with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for p in sorted(set(files)):z.write(p,Path('Siren-and-Sailor')/p.relative_to(ROOT))
 with zipfile.ZipFile(zip_path) as z:assert z.testzip() is None
 exports={ROOT/'fonts/ttf/SirenandSailor-Regular.ttf':'SirenandSailor-Regular.ttf',ROOT/'proofs/SirenAndSailor-Type-Tester.html':'SirenAndSailor-Type-Tester.html',ROOT/'proofs/SirenandSailor-Specimen.png':'SirenAndSailor-Alphabet.png',ROOT/'qa/READINESS.md':'SirenAndSailor-Submission-Readiness.md',ROOT/'proofs/SirenAndSailor-Symbols.png':'SirenAndSailor-Symbols.png'}
 for src,name in exports.items():shutil.copyfile(src,out/name)
 print('Packaged',len(files),'files;',zip_path.stat().st_size,'bytes')
if __name__=='__main__':main()
