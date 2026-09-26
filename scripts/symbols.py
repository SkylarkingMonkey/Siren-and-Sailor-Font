"""Siren and Sailor: supplemental Latin punctuation and symbols.

Each drawing uses font units (y upward). Letter-derived signs preserve original
approved outlines. Geometric signs keep the family's 24–40 unit hairline rhythm.
All functions operate on ufoLib2.Font; overlap removal belongs to final build.
"""
from math import cos, sin, pi, hypot
import pathops
from fontTools.agl import AGL2UV
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.areaPen import AreaPen
from fontTools.pens.reverseContourPen import ReverseContourPen
from ufoLib2.objects import Glyph
from fontTools.svgLib.path import parse_path

SYMBOL_UNICODES = {
    'dollar':0x24, 'percent':0x25, 'less':0x3C, 'greater':0x3E, 'at':0x40,
    'asciicircum':0x5E, 'bar':0x7C, 'asciitilde':0x7E, 'cent':0xA2,
    'sterling':0xA3, 'yen':0xA5, 'section':0xA7, 'copyright':0xA9,
    'registered':0xAE, 'degree':0xB0, 'paragraph':0xB6, 'multiply':0xD7,
    'divide':0xF7, 'Euro':0x20AC, 'uni20B9':0x20B9, 'trademark':0x2122, 'minus':0x2212,
    'numbersign':0x23, 'asterisk':0x2A, 'parenleft':0x28, 'parenright':0x29, 'bracketleft':0x5B,
    'backslash':0x5C, 'bracketright':0x5D, 'underscore':0x5F,
    'braceleft':0x7B, 'braceright':0x7D, 'exclamdown':0xA1,
    'guillemotleft':0xAB, 'periodcentered':0xB7, 'guillemotright':0xBB,
    'questiondown':0xBF, 'quoteleft':0x2018, 'quoteright':0x2019,
    'quotesinglbase':0x201A, 'quotedblleft':0x201C,
    'quotedblright':0x201D, 'quotedblbase':0x201E, 'bullet':0x2022,
    'ellipsis':0x2026, 'guilsinglleft':0x2039, 'guilsinglright':0x203A,
}


def add_symbols(font):
    """Add production punctuation and symbols. Return the newly drawn names."""
    created = []

    def glyph(name, width, paths=()):
        if name in font:
            del font[name]
        g = font.newGlyph(name)
        g.width = width
        g.unicode = SYMBOL_UNICODES.get(name, AGL2UV.get(name))
        for d in paths:
            parse_path(d, g.getPen())
        created.append(name)
        return g

    def path(g, d, has_holes=False):
        drawing=Glyph()
        parse_path(d, drawing.getPen())
        first=AreaPen();drawing.contours[0].draw(first)
        for contour in drawing.contours:
            area=AreaPen();contour.draw(area)
            if (first.value if has_holes else area.value) < 0:
                contour.draw(ReverseContourPen(g.getPen()))
            else:
                contour.draw(g.getPen())

    def copy(g, source, transform=(1,0,0,1,0,0)):
        font[source].draw(TransformPen(g.getPen(), transform))

    def fit(g, source, box):
        """Fit a letter to an explicit ink rectangle, not its advance width."""
        b = font[source].getBounds(font)
        x0,y0,x1,y1 = box
        sx=(x1-x0)/(b.xMax-b.xMin); sy=(y1-y0)/(b.yMax-b.yMin)
        copy(g,source,(sx,0,0,sy,x0-sx*b.xMin,y0-sy*b.yMin))

    def oval(g,cx,cy,rx,ry,thickness=None):
        k=0.5522847498307936
        def contour(rx,ry,reverse=False):
            p=g.getPen(); p.moveTo((cx+rx,cy))
            segments=[((cx+rx,cy+k*ry),(cx+k*rx,cy+ry),(cx,cy+ry)),
                      ((cx-k*rx,cy+ry),(cx-rx,cy+k*ry),(cx-rx,cy)),
                      ((cx-rx,cy-k*ry),(cx-k*rx,cy-ry),(cx,cy-ry)),
                      ((cx+k*rx,cy-ry),(cx+rx,cy-k*ry),(cx+rx,cy))]
            if reverse:
                from fontTools.pens.reverseContourPen import ReverseContourPen
                p=ReverseContourPen(g.getPen());p.moveTo((cx+rx,cy))
            for pts in segments:p.curveTo(*pts)
            p.closePath()
        contour(rx,ry)
        if thickness: contour(rx-thickness,ry-thickness,True)

    def horizontal(g, x0,x1,y,t=30,serifs=True):
        if serifs:
            path(g,f'M{x0} {y-t/2-20} C{x0+20} {y-t/2} {x0+20} {y-t/2} {x0+44} {y-t/2} '
                   f'L{x1-44} {y-t/2} C{x1-20} {y-t/2} {x1-20} {y-t/2} {x1} {y-t/2-20} '
                   f'L{x1} {y+t/2+20} C{x1-20} {y+t/2} {x1-20} {y+t/2} {x1-44} {y+t/2} '
                   f'L{x0+44} {y+t/2} C{x0+20} {y+t/2} {x0+20} {y+t/2} {x0} {y+t/2+20} Z')
        else: path(g,f'M{x0} {y-t/2} H{x1} V{y+t/2} H{x0} Z')

    # The actual approved capital-J hook supplies every new harpoon terminal.
    # Only its last 35 units at the attachment are blended to a vertical neck.
    jp=pathops.Path();font['J'].draw(jp.getPen())
    clip=pathops.Path();clip.moveTo(20,150);clip.lineTo(195,150)
    clip.lineTo(195,470);clip.lineTo(20,470);clip.close()
    terminal=Glyph();pathops.op(jp,clip,pathops.PathOp.INTERSECTION).draw(terminal.getPen())
    edge=[p.x for c in terminal.contours for p in c.points if abs(p.y-150)<.001]
    neck_left,neck_right=min(edge),max(edge)
    neck_center=(neck_left+neck_right)/2;neck_width=neck_right-neck_left
    for contour in terminal.contours:
        for point in contour.points:
            if point.y<185:
                t=max(0,min(1,(point.y-150)/35));t=t*t*(3-2*t)
                edge_x=neck_left if point.x<neck_center else neck_right
                point.x=edge_x+(point.x-edge_x)*t
            point.x-=neck_center;point.y-=150

    def harpoon(g,origin,tangent=(0,1),sx=.67,sy=None,mirror=False):
        if sy is None:sy=sx
        if mirror:sx=-sx
        vx,vy=tangent;norm=hypot(vx,vy);vx/=norm;vy/=norm
        shape=Glyph();terminal.draw(TransformPen(shape.getPen(),
                    (vy*sx,-vx*sx,vx*sy,vy*sy,*origin)))
        for c in shape.contours:
            a=AreaPen();c.draw(a)
            c.draw(ReverseContourPen(g.getPen()) if a.value<0 else g.getPen())

    def shaft(g,a,b,width):
        vx=b[0]-a[0];vy=b[1]-a[1];n=hypot(vx,vy)
        nx=vy/n*width/2;ny=-vx/n*width/2
        pts=[(a[0]+nx,a[1]+ny),(b[0]+nx,b[1]+ny),
             (b[0]-nx,b[1]-ny),(a[0]-nx,a[1]-ny)]
        path(g,'M'+' L'.join(f'{x} {y}' for x,y in pts)+' Z')

    # Currency signs: match the approved display capitals' actual curves.
    g=glyph('dollar',770);fit(g,'S',(70,0,700,1000))
    for x,mirror in [(306,True),(464,False)]:
        shaft(g,(x,-112),(x,1003),neck_width*.67)
        harpoon(g,(x,1003),sx=.67,mirror=mirror)
    g=glyph('cent',660);fit(g,'C',(72,45,590,830))
    path(g,'M307 -95 L332 -95 L332 960 L307 960 Z')
    g=glyph('sterling',815)
    # Continuous curled shoulder and a shallow wave foot, rather than a pasted L.
    path(g,'M146 55 C255 126 272 228 272 397 L272 710 '
           'C272 913 395 1030 540 1016 C631 1008 698 961 709 887 '
           'C678 916 650 913 640 885 C629 856 643 831 670 814 '
           'C611 813 582 847 582 891 C582 947 560 982 515 983 '
           'C404 986 341 887 341 724 L341 399 C341 224 305 128 224 75 '
           'C337 117 400 94 486 61 C586 23 666 32 752 91 '
           'C713 0 615 -35 516 -17 C426 0 366 40 293 40 '
           'C227 40 173 18 106 -8 C124 14 140 32 146 55 Z')
    horizontal(g,117,570,461,29)
    g=glyph('yen',910);fit(g,'Y',(65,-15,845,1005))
    horizontal(g,222,688,387,27);horizontal(g,222,688,544,27)
    g=glyph('Euro',870);fit(g,'C',(74,-15,795,1005))
    horizontal(g,65,670,422,27);horizontal(g,65,670,594,27)

    # Indian rupee: the open P-like bowl carries directly into the R-like leg.
    # Its two horizontal bars remain conventionally readable at text sizes.
    g=glyph('uni20B9',800)
    path(g,'M225 982 C419 990 569 919 569 783 '
           'C569 657 447 586 276 576 L622 83 '
           'C656 36 689 17 742 0 C694 13 641 11 596 -10 '
           'C584 22 570 53 548 86 L206 585 L206 615 '
           'C391 613 500 669 500 785 C500 907 397 968 225 968 Z')
    horizontal(g,78,722,982,31)
    horizontal(g,78,688,810,28)

    # Pure circles use the same optical weight as the original thin cap stems.
    g=glyph('percent',1050)
    oval(g,274,798,166,220,31);oval(g,776,202,166,220,31)
    lower=(286,142);upper=(756,842);v=(upper[0]-lower[0],upper[1]-lower[1])
    shaft(g,lower,upper,neck_width*.70)
    harpoon(g,upper,tangent=v,sx=.70)
    harpoon(g,lower,tangent=(-v[0],-v[1]),sx=.70)
    g=glyph('degree',420);oval(g,210,830,143,163,29)
    for name,letter,width in [('copyright','C',1120),('registered','R',1120)]:
        g=glyph(name,width);oval(g,560,500,480,512,30)
        fit(g,letter,(300,203,820,813))
    g=glyph('trademark',1110)
    fit(g,'T',(40,553,507,1007));fit(g,'M',(514,553,1070,1007))

    # @ is a continuous open spiral around a single-storey inner bowl.
    g=glyph('at',1170)
    path(g,'M1052 138 C966 35 832 -22 662 -22 C342 -22 84 170 84 506 '
           'C84 827 305 1021 602 1021 C867 1021 1092 851 1092 603 '
           'C1092 397 992 207 853 207 C773 207 735 251 744 333 '
           'C689 245 626 211 553 211 C406 211 326 318 346 492 '
           'C365 664 473 803 618 803 C694 803 751 765 769 703 '
           'L784 785 L831 785 L784 414 C769 300 789 242 854 242 '
           'C967 242 1055 410 1055 603 C1055 831 850 986 603 986 '
           'C328 986 125 804 125 506 C125 194 359 13 662 13 '
           'C819 13 946 65 1033 162 Z '
           'M406 491 C390 340 445 245 554 245 C665 245 741 374 762 538 '
           'C780 681 727 769 625 769 C509 769 423 643 406 491 Z', has_holes=True)

    # Section sign: two offset calligraphic loops share a light middle counter.
    g=glyph('section',700)
    path(g,'M556 884 C526 958 466 1005 381 1005 C289 1005 218 947 218 873 '
           'C218 797 280 758 388 700 C519 628 603 566 603 460 '
           'C603 357 493 277 365 241 L332 272 C460 309 552 378 552 451 '
           'C552 527 483 576 367 640 C238 711 164 773 164 869 '
           'C164 968 253 1039 379 1039 C473 1039 548 1002 582 938 '
           'C555 948 532 935 530 914 C528 902 540 888 556 884 Z')
    path(g,'M149 77 C179 3 239 -44 324 -44 C416 -44 487 14 487 88 '
           'C487 164 425 203 317 261 C186 333 102 395 102 501 '
           'C102 604 212 684 340 720 L373 689 C245 652 153 583 153 510 '
           'C153 434 222 385 338 321 C467 250 541 188 541 92 '
           'C541 -7 452 -78 326 -78 C232 -78 157 -41 123 23 '
           'C150 13 173 26 175 47 C177 59 165 73 149 77 Z')
    g=glyph('paragraph',760)
    path(g,'M380 1000 L653 1000 L653 974 L601 969 L601 -188 '
           'L632 -196 L651 -215 L508 -215 L529 -196 L560 -188 L560 967 '
           'L436 967 L436 -188 L467 -196 L487 -215 L345 -215 '
           'L365 -196 L396 -188 L396 572 C208 572 90 650 90 790 '
           'C90 922 204 1000 380 1000 Z')

    # Mathematical marks align at y=400 and use deliberately straight rules.
    g=glyph('minus',790);horizontal(g,65,725,400,31)
    g=glyph('multiply',770)
    path(g,'M93 651 L117 675 L677 115 L653 91 Z '
           'M93 115 L117 91 L677 651 L653 675 Z')
    g=glyph('divide',790);horizontal(g,65,725,400,31)
    oval(g,395,635,34,34);oval(g,395,165,34,34)
    g=glyph('less',750)
    path(g,'M680 736 L680 695 L123 400 L680 105 L680 64 L66 390 L66 410 Z')
    g=glyph('greater',750);copy(g,'less',(-1,0,0,1,750,0))
    g=glyph('numbersign',905)
    path(g,'M200 0 L239 0 L451 1000 L412 1000 Z '
           'M497 0 L536 0 L748 1000 L709 1000 Z')
    horizontal(g,60,787,345,30);horizontal(g,128,855,653,30)
    g=glyph('asterisk',420)
    # Six tapered arms are drawn into one central star, without abrupt seams.
    vertices=[]
    for i in range(24):
        ang=pi/2 + i*pi/12
        rad=(165 if i%4==0 else (42 if i%2==0 else 55))
        vertices.append((210+rad*cos(ang),850+rad*sin(ang)))
    path(g,'M'+' L'.join(f'{x:.3f} {y:.3f}' for x,y in vertices)+' Z')
    g=glyph('asciicircum',680)
    path(g,'M69 618 L314 1000 L366 1000 L611 618 L571 618 '
           'L340 963 L109 618 Z')
    g=glyph('bar',295);path(g,'M130 -220 L165 -220 L165 1110 L130 1110 Z')
    g=glyph('asciitilde',820);fit(g,'emdash',(65,343,755,488))
    g=glyph('underscore',800)
    path(g,'M38 -169 C97 -137 140 -148 201 -152 L613 -152 '
           'C676 -152 722 -146 762 -126 C745 -163 709 -186 643 -186 '
           'L198 -186 C137 -186 91 -179 38 -200 Z')

    # Keep the original curved parentheses; replace only the final arcs with
    # J-hook terminals, matched to each arc's actual clipped width and tangent.
    arc=pathops.Path();font['parenleft'].draw(arc.getPen())
    joins=[]
    for origin,v,mirror in [((202,965),(.526,.851),True),
                            ((202,33),(.526,-.851),False)]:
        vx,vy=v;norm=hypot(vx,vy);vx/=norm;vy/=norm;nx,ny=vy,-vx
        def at(u,t):return (origin[0]+u*nx+t*vx,origin[1]+u*ny+t*vy)
        box=pathops.Path();box.moveTo(*at(-2500,-2500));box.lineTo(*at(2500,-2500))
        box.lineTo(*at(2500,0));box.lineTo(*at(-2500,0));box.close()
        arc=pathops.op(arc,box,pathops.PathOp.INTERSECTION)
        points=[]
        for verb,coords in arc.segments:
            for x,y in coords:
                if abs((x-origin[0])*vx+(y-origin[1])*vy)<.015:
                    points.append((x-origin[0])*nx+(y-origin[1])*ny)
        lo,hi=min(points),max(points);middle=(lo+hi)/2
        joins.append(((origin[0]+middle*nx,origin[1]+middle*ny),
                      (vx,vy),(hi-lo)/neck_width,mirror))
    g=glyph('parenleft',font['parenleft'].width)
    raw=Glyph();arc.draw(raw.getPen())
    for c in raw.contours:
        a=AreaPen();c.draw(a)
        c.draw(ReverseContourPen(g.getPen()) if a.value<0 else g.getPen())
    for origin,v,sx,mirror in joins:harpoon(g,origin,tangent=v,sx=sx,sy=.45,mirror=mirror)
    g=glyph('parenright',font['parenright'].width)
    copy(g,'parenleft',(-1,0,0,1,g.width,0))

    # Tall delimiters balance the long descenders, with tiny flared terminals.
    g=glyph('bracketleft',420)
    path(g,'M120 -170 L120 1100 L347 1100 L347 1043 '
           'C323 1063 300 1068 266 1068 L155 1068 L155 -138 L266 -138 '
           'C300 -138 323 -132 347 -112 L347 -170 Z')
    g=glyph('bracketright',420);copy(g,'bracketleft',(-1,0,0,1,420,0))
    g=glyph('braceleft',500)
    path(g,'M412 1100 C263 1100 236 1013 236 884 L236 661 '
           'C236 555 190 504 87 484 L87 451 '
           'C190 431 236 380 236 274 L236 46 '
           'C236 -83 263 -170 412 -170 L412 -137 '
           'C298 -137 278 -71 278 48 L278 274 '
           'C278 376 247 435 150 468 C247 500 278 559 278 661 '
           'L278 884 C278 1003 298 1067 412 1067 Z')
    g=glyph('braceright',500);copy(g,'braceleft',(-1,0,0,1,500,0))
    g=glyph('backslash',font['slash'].width)
    copy(g,'slash',(-1,0,0,1,g.width,0))

    # Inversion preserves the custom harpoon forms exactly.
    g=glyph('exclamdown',font['exclam'].width)
    copy(g,'exclam',(-1,0,0,-1,g.width,680))
    g=glyph('questiondown',font['question'].width)
    copy(g,'question',(-1,0,0,-1,g.width,680))
    g=glyph('periodcentered',250);fit(g,'period',(91,368,159,436))
    g=glyph('bullet',410);oval(g,205,400,64,64)
    g=glyph('ellipsis',660)
    for dx in [0,230,460]:copy(g,'period',(1,0,0,1,dx,0))

    # Curly quotes are the approved comma enlarged only slightly. Opening marks
    # rotate it; closing marks keep its down-hook. Quote pairs preserve rhythm.
    g=glyph('quoteright',244);fit(g,'comma',(73,792,162,1012))
    g=glyph('quoteleft',244);copy(g,'quoteright',(-1,0,0,-1,244,1804))
    g=glyph('quotesinglbase',244);copy(g,'quoteright',(1,0,0,1,0,-964))
    g=glyph('quotedblright',448)
    copy(g,'quoteright');copy(g,'quoteright',(1,0,0,1,204,0))
    g=glyph('quotedblleft',448)
    copy(g,'quoteleft');copy(g,'quoteleft',(1,0,0,1,204,0))
    g=glyph('quotedblbase',448)
    copy(g,'quotesinglbase');copy(g,'quotesinglbase',(1,0,0,1,204,0))
    g=glyph('guilsinglleft',390)
    path(g,'M318 713 L318 665 L122 397 L318 129 L318 81 '
           'L74 378 L74 416 Z')
    g=glyph('guilsinglright',390);copy(g,'guilsinglleft',(-1,0,0,1,390,0))
    g=glyph('guillemotleft',680)
    copy(g,'guilsinglleft');copy(g,'guilsinglleft',(1,0,0,1,290,0))
    g=glyph('guillemotright',680)
    copy(g,'guilsinglright');copy(g,'guilsinglright',(1,0,0,1,290,0))
    return created
