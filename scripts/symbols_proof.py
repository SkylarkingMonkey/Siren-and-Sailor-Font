from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
fp=ROOT/'fonts/ttf/SirenandSailor-Regular.ttf'
W,H=1920,1540;im=Image.new('RGB',(W,H),'#faf6ec');d=ImageDraw.Draw(im)
sans='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
lab=ImageFont.truetype(sans,22);sub=ImageFont.truetype(sans,24)
d.text((72,48),'SIREN&SAILOR   /   NAUTICAL SYMBOLS',font=sub,fill='#9b7546')
ft=ImageFont.truetype(str(fp),405)
for i,ch in enumerate('$%*(#)'):
 col=i%3;row=i//3;x=col*592+72;y=row*526+128;w=560;h=470
 d.rounded_rectangle((x,y,x+w,y+h),radius=10,outline='#d4cdbc',width=2)
 box=d.textbbox((0,0),ch,font=ft,anchor='ls')
 px=x+w/2-(box[0]+box[2])/2;py=y+215-(box[1]+box[3])/2
 d.text((px,py),ch,font=ft,fill='#183038',anchor='ls')
 names={'$':'DOUBLE HARPOON DOLLAR','%':'BARBED PERCENT','*':'NAUTICAL ASTERISK','(':'OPEN PARENTHESIS','#':'NUMBER SIGN',')':'CLOSE PARENTHESIS'}
 d.text((x+w/2,y+h-42),names[ch],font=lab,fill='#85683f',anchor='mm')
font=ImageFont.truetype(str(fp),124);text='$125.00  ·  99%  ·  (Aye!)  ·  #1*'
while d.textlength(text,font=font)>W-144:font=ImageFont.truetype(str(fp),font.size-1)
d.text((72,1270),text,font=font,fill='#183038',anchor='lt')
d.text((72,1480),'Rendered from the actual installable font.',font=lab,fill='#607477')
im.save(ROOT/'proofs/SirenAndSailor-Symbols.png')
