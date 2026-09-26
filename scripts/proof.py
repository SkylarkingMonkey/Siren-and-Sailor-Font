from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from fontTools.ttLib import TTFont
import unicodedata,math
ROOT=Path(__file__).resolve().parents[1]
FONT=ROOT/'fonts/ttf/SirenandSailor-Regular.ttf'
def run():
 W=2000;H=3000;bg='#faf6ec';ink='#182d32';accent='#967240'
 im=Image.new('RGB',(W,H),bg);d=ImageDraw.Draw(im)
 sans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
 label=ImageFont.truetype(sans,27);small=ImageFont.truetype(sans,22)
 d.text((90,65),'SIREN&S A I L O R  /  PRODUCTION PROOF'.replace('&S A I L O R','&SAILOR'),font=label,fill=accent)
 y=165
 lines=[('Siren & Sailor',200),('Nautical letters, drawn with a sharp hook.',92),('ABCDEFGHIJKLMNOPQRSTUVWXYZ',69),('abcdefghijklmnopqrstuvwxyz',112),('0123456789  $ £ € ¥  % @ &',106),('À Á Â Ã Ä Å  Æ Ç È É Ê Ë',93),('Ì Í Î Ï Ñ Ò Ó Ô Õ Ö Ø  Œ',93),('Ù Ú Û Ü Ý Ÿ  Ð Þ ß ẞ',95),('ā ă ą ć ċ č ď đ ē ė ę ě',96),('ğ ġ ģ ħ ī į ı ķ ļ ľ ł ń ņ ň',96),('ő ř ś ş š ť ū ů ű ų ŵ ŷ ź ż ž',86),('á à â ã ä å æ ç é è ê ë ð ø œ',87),('“Quay?” ‘Aye!’  ¡Sí!  ¿Qué tal?',95),('Café, façade, blåbær, cœur, Straße.',87),('Příliš žluťoučký kůň.  Ģimene, ķīlis.',80),('HAMBURG  AVATAR  TOWAVY',85),('nnonn  minimum  rhythm  fj  ff  fi',96)]
 for text,size in lines:
  ft=ImageFont.truetype(str(FONT),size)
  while d.textlength(text,font=ft)>W-180:size-=1;ft=ImageFont.truetype(str(FONT),size)
  d.text((90,y),text,font=ft,fill=ink,anchor='lt');y+=round(size*1.12)+20
 im.crop((0,0,W,min(H,y+70))).save(ROOT/'proofs/SirenandSailor-Specimen.png')
 f=TTFont(FONT);codes=sorted(f.getBestCmap());codes=[c for c in codes if c not in [32,160,0x200B,0x200C,0x200D,0x2060,0xFEFF]]
 cols=12;cw=155;ch=180;rows=math.ceil(len(codes)/cols)
 im=Image.new('RGB',(cols*cw+80,rows*ch+100),bg);d=ImageDraw.Draw(im);ft=ImageFont.truetype(str(FONT),100)
 for i,cp in enumerate(codes):
  x=40+(i%cols)*cw;y=50+(i//cols)*ch
  d.line((x,y+150,x+cw-10,y+150),fill='#ddd4c3')
  text=chr(cp)
  if unicodedata.category(text)=='Mn':text='a'+text
  d.text((x+cw/2,y+105),text,font=ft,fill=ink,anchor='ms')
  d.text((x+8,y+153),f'U+{cp:04X}',font=small,fill=accent)
 im.save(ROOT/'proofs/SirenandSailor-Glyphs.png')
 print('Rendered proofs')
if __name__=='__main__':run()
