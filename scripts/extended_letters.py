"""Additional Latin letters for Siren and Sailor.

These drawings derive from the designer's approved cubic outlines.  The original
alphabet is never edited.  Ligatures are fused outlines, stroked letters keep the
original letter as a component, and dots are removed without redrawing the stem.
Coordinates are conventional, upward-positive font units (1400 UPM).
"""

from copy import deepcopy

import pathops
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen
from ufoLib2.objects import Component


IDENTITY = (1, 0, 0, 1, 0, 0)


def _path(font, name, transform=IDENTITY):
    p = pathops.Path()
    font[name].draw(TransformPen(p.getPen(font), transform))
    return p


def _polygon(points):
    p = pathops.Path()
    pen = p.getPen()
    pen.moveTo(points[0])
    for pt in points[1:]:
        pen.lineTo(pt)
    pen.closePath()
    return p


def _rect(x0, y0, x1, y1):
    return _polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)])


def _clip(p, x0=-3000, y0=-3000, x1=3000, y1=3000):
    return pathops.op(p, _rect(x0, y0, x1, y1), pathops.PathOp.INTERSECTION)


def _union(*paths):
    result = paths[0]
    for p in paths[1:]:
        result = pathops.op(result, p, pathops.PathOp.UNION)
    return result


def _difference(p, mask):
    return pathops.op(p, mask, pathops.PathOp.DIFFERENCE)


def _bezier(commands):
    p = pathops.Path()
    pen = p.getPen()
    for op, pts in commands:
        getattr(pen, op)(*pts)
    return p


def _stroke(x0, y0, x1, y1, thickness):
    """A pointed, gently swept cross-stroke, with continuous tapered ends."""
    from math import hypot

    length = hypot(x1 - x0, y1 - y0)
    ux, uy = (x1 - x0) / length, (y1 - y0) / length
    nx, ny = -uy, ux

    def pt(t, off):
        return (x0 + t * (x1 - x0) + off * nx,
                y0 + t * (y1 - y0) + off * ny)

    w = thickness / 2
    return _bezier([
        ("moveTo", [pt(0, -w * .9)]),
        ("curveTo", [pt(.12, -w * .55), pt(.22, w), pt(.34, w)]),
        ("lineTo", [pt(.78, w)]),
        ("curveTo", [pt(.88, w), pt(.96, w * 1.3), pt(1, w * 2.0)]),
        ("curveTo", [pt(.98, w * .8), pt(.99, -w * .9), pt(1, -w * 1.6)]),
        ("curveTo", [pt(.87, -w), pt(.85, -w), pt(.73, -w)]),
        ("lineTo", [pt(.24, -w)]),
        ("curveTo", [pt(.14, -w), pt(.07, -w * 1.45), pt(0, -w * .9)]),
        ("closePath", []),
    ])


def _new(font, name, codepoint, width, comment):
    if name in font:
        del font[name]
    g = font.newGlyph(name)
    g.unicodes = [codepoint]
    g.width = width
    g.note = comment
    return g


def _draw(glyph, p):
    # Match the counterclockwise exterior direction of the imported masters.
    # Otherwise a clockwise cross-stroke would cancel its base where they meet.
    recording = RecordingPen()
    pathops.simplify(p, fix_winding=True, clockwise=False).draw(recording)
    clean = []
    first = current = None

    def same(a, b):
        return abs(a[0] - b[0]) < 1e-6 and abs(a[1] - b[1]) < 1e-6

    for op, args in recording.value:
        if op == "moveTo":
            first = current = args[0]
        elif op == "lineTo":
            if same(args[0], current):
                continue
            current = args[0]
        elif op in ("curveTo", "qCurveTo"):
            if all(same(pt, current) for pt in args):
                continue
            current = args[-1]
        elif op == "closePath":
            # closePath already supplies this last straight edge.  Pathops can
            # emit it explicitly as well, creating a duplicated closing point.
            if clean and clean[-1][0] == "lineTo" and same(clean[-1][1][0], first):
                clean.pop()
        clean.append((op, args))
    recording.value = clean
    recording.replay(glyph.getPen())


def _component(glyph, name, transform=IDENTITY):
    glyph.components.append(Component(name, transform))


def _dotless(font, name, original, codepoint):
    src = font[original]
    g = _new(font, name, codepoint, src.width,
             "Exact approved stem/hook; apostrophe-shaped dot removed.")
    # A dot is the separate contour wholly above x-height.  Use this geometric
    # condition rather than contour index, which can change during cleanup.
    kept = []
    for c in src.contours:
        if min(p.y for p in c.points) < 720:
            kept.append(deepcopy(c))
    if len(kept) == len(src.contours):
        raise ValueError(f"Cannot identify the dot of {original}")
    g.contours.extend(kept)
    for a in src.anchors:
        g.anchors.append(deepcopy(a))
    return g


def add_extended_letters(font):
    """Add non-decomposing Latin letters; return their names in creation order."""
    added = []

    def new(name, cp, width, note):
        added.append(name)
        return _new(font, name, cp, width, note)

    # Capital ligatures share E's vertical.  Clipping the redundant inner
    # serifs prevents a dark bar joining the two feet at the baseline.
    a_left = _clip(_path(font, "A"), x1=536)
    e_right = _clip(_path(font, "E", (1, 0, 0, 1, 259, 0)), x0=489)
    g = new("AE", 0x00C6, 1236,
            "A's approved left diagonal and angled crossbar fused to E's vertical; shared serif joins.")
    _draw(g, _union(a_left, e_right))

    o_left = _clip(_path(font, "O"), x1=550)
    e_right = _clip(_path(font, "E", (1, 0, 0, 1, 263, 0)), x0=499)
    g = new("OE", 0x0152, 1240,
            "O's original left bowl fused to E at a single shared upright.")
    _draw(g, _union(o_left, e_right))

    # Lowercase ligatures retain the oblique e crossbar and returning hook.
    # Trim only the redundant a foot where it would intrude into e's counter.
    a_part = _difference(_path(font, "a"), _rect(510, -120, 900, 140))
    e_part = _path(font, "e", (1, 0, 0, 1, 427, 0))
    g = new("ae", 0x00E6, 1044,
            "Approved a and e joined at their common stroke; inner a foot removed.")
    _draw(g, _union(a_part, e_part))

    g = new("oe", 0x0153, 1087,
            "Approved o and oblique-bar e fused through their adjacent strokes.")
    _draw(g, _union(_path(font, "o"), _path(font, "e", (1, 0, 0, 1, 470, 0))))

    # Barred letters preserve each base as a component; the final build removes
    # overlaps after decomposition.  Crossbars are gently tapered, not pasted
    # rectangular strips, and sit on uninterrupted portions of their stems.
    variants = [
        ("Eth", 0x00D0, "D", (124, 514, 466, 514, 35)),
        ("Dcroat", 0x0110, "D", (124, 514, 466, 514, 35)),
        ("dcroat", 0x0111, "d", (333, 813, 610, 813, 29)),
        ("Hbar", 0x0126, "H", (153, 766, 1052, 766, 32)),
        ("hbar", 0x0127, "h", (61, 810, 298, 810, 27)),
        ("Lslash", 0x0141, "L", (87, 405, 430, 659, 38)),
        ("lslash", 0x0142, "l", (41, 396, 281, 609, 30)),
        ("Oslash", 0x00D8, "O", (151, 44, 750, 956, 39)),
        ("oslash", 0x00F8, "o", (103, 26, 508, 670, 28)),
    ]
    for name, cp, base, stroke in variants:
        g = new(name, cp, font[base].width,
                f"Unchanged {base} outline with an integrated swept cross-stroke.")
        _component(g, base)
        _draw(g, _stroke(*stroke))

    # Capital thorn: I's full serifed upright with P's bowl lowered between the
    # cap line and baseline.  The cut lies inside I, so no clipped edge shows.
    thorn_bowl = _clip(_path(font, "P", (1, 0, 0, 1, 0, -210)),
                       x0=276, y0=200)
    g = new("Thorn", 0x00DE, font["P"].width,
            "Original I upright; P bowl lowered to give thorn its ascender and foot.")
    _draw(g, _union(_path(font, "I"), thorn_bowl))

    # Lowercase thorn has both ascender and descender.  Remove p's x-height
    # head where l supplies the uninterrupted stem, retaining p's entire bowl.
    p_part = _difference(_path(font, "p"), _rect(-200, 625, 211, 900))
    l_top = _clip(_path(font, "l", (1, 0, 0, 1, 7, 0)), y0=535)
    g = new("thorn", 0x00FE, font["p"].width,
            "Original p bowl and descending foot with a continuous l ascender.")
    _draw(g, _union(p_part, l_top))

    # Eth requires a bent ascender, not a d with an arbitrary line pasted on.
    # The ascender narrows continuously into its pointed upper terminal.
    eth_outer = _bezier([
        ("moveTo", [(306, 693)]),
        ("curveTo", [(468, 693), (576, 544), (576, 337)]),
        ("curveTo", [(576, 117), (460, -16), (306, -16)]),
        ("curveTo", [(130, -16), (36, 119), (36, 337)]),
        ("curveTo", [(36, 542), (144, 693), (306, 693)]),
        ("closePath", []),
    ])
    eth_inner = _bezier([
        ("moveTo", [(305, 658)]),
        ("curveTo", [(180, 658), (96, 525), (96, 337)]),
        ("curveTo", [(96, 143), (172, 17), (306, 17)]),
        ("curveTo", [(443, 17), (511, 155), (511, 337)]),
        ("curveTo", [(511, 526), (432, 658), (305, 658)]),
        ("closePath", []),
    ])
    eth_stem = _bezier([
        ("moveTo", [(511, 337)]),
        ("curveTo", [(520, 612), (466, 841), (318, 968)]),
        ("curveTo", [(272, 1008), (221, 1034), (170, 1041)]),
        ("curveTo", [(209, 1043), (248, 1054), (270, 1080)]),
        ("curveTo", [(280, 1049), (307, 1022), (341, 994)]),
        ("curveTo", [(506, 856), (594, 617), (576, 337)]),
        ("lineTo", [(511, 337)]),
        ("closePath", []),
    ])
    g = new("eth", 0x00F0, 632,
            "Drawn eth: contrasting oval bowl, continuous bent ascender, swept slash.")
    _draw(g, _union(_difference(eth_outer, eth_inner), eth_stem,
                   _stroke(223, 824, 494, 953, 27)))

    # Sharp s is constructed as a single continuous returning stroke.  The
    # lower opening and angular inner turn distinguish it from B or beta.
    ss = _bezier([
        ("moveTo", [(170, 60)]), ("lineTo", [(170, 730)]),
        ("curveTo", [(170, 923), (247, 1014), (363, 1014)]),
        ("curveTo", [(479, 1014), (550, 944), (550, 844)]),
        ("curveTo", [(550, 739), (458, 651), (350, 545)]),
        ("curveTo", [(483, 517), (606, 406), (606, 239)]),
        ("curveTo", [(606, 85), (516, -16), (385, -16)]),
        ("curveTo", [(326, -16), (278, 11), (250, 52)]),
        ("curveTo", [(280, 41), (298, 54), (304, 83)]),
        ("curveTo", [(318, 49), (347, 32), (377, 32)]),
        ("curveTo", [(478, 32), (534, 117), (534, 238)]),
        ("curveTo", [(534, 395), (456, 483), (313, 506)]),
        ("lineTo", [(277, 510)]), ("lineTo", [(278, 543)]),
        ("curveTo", [(405, 663), (480, 755), (480, 843)]),
        ("curveTo", [(480, 929), (428, 979), (362, 979)]),
        ("curveTo", [(277, 979), (231, 900), (231, 748)]),
        ("lineTo", [(231, 60)]), ("closePath", []),
    ])
    # A shortened inner foot keeps the lower S terminal open; a complete l foot
    # would touch it and accidentally make an extra enclosed counter.
    foot = _bezier([
        ("moveTo", [(170, 106)]), ("lineTo", [(231, 106)]),
        ("lineTo", [(231, 60)]),
        ("curveTo", [(231, 25), (242, 6), (265, -7)]),
        ("curveTo", [(242, 1), (224, 10), (204, 10)]),
        ("curveTo", [(152, 10), (114, 2), (60, -18)]),
        ("curveTo", [(90, 13), (127, 18), (149, 33)]),
        ("curveTo", [(164, 46), (170, 70), (170, 106)]),
        ("closePath", []),
    ])
    g = new("germandbls", 0x00DF, 646,
            "Continuous sharp-s drawing with a swept foot and hooked, open lower terminal.")
    _draw(g, _union(ss, foot))

    cap_ss = _bezier([
        ("moveTo", [(180, 68)]), ("lineTo", [(180, 1000)]),
        ("lineTo", [(441, 1000)]),
        ("curveTo", [(608, 1000), (694, 917), (694, 803)]),
        ("curveTo", [(694, 688), (590, 610), (456, 541)]),
        ("curveTo", [(623, 509), (750, 416), (750, 241)]),
        ("curveTo", [(750, 68), (629, -14), (468, -14)]),
        ("curveTo", [(376, -14), (307, 11), (272, 38)]),
        ("curveTo", [(303, 32), (324, 53), (326, 84)]),
        ("curveTo", [(360, 44), (405, 24), (459, 24)]),
        ("curveTo", [(593, 24), (667, 104), (667, 247)]),
        ("curveTo", [(667, 391), (571, 477), (420, 506)]),
        ("lineTo", [(338, 521)]), ("lineTo", [(338, 558)]),
        ("lineTo", [(526, 720)]),
        ("curveTo", [(583, 768), (610, 794), (610, 844)]),
        ("curveTo", [(610, 922), (548, 961), (438, 961)]),
        ("lineTo", [(243, 961)]), ("lineTo", [(243, 68)]),
        ("closePath", []),
    ])
    cap_foot = _bezier([
        ("moveTo", [(180, 116)]), ("lineTo", [(243, 116)]),
        ("lineTo", [(243, 62)]),
        ("curveTo", [(243, 26), (251, 6), (276, -9)]),
        ("curveTo", [(247, 3), (223, 10), (202, 10)]),
        ("curveTo", [(145, 10), (91, -2), (37, -24)]),
        ("curveTo", [(86, 19), (135, 20), (158, 39)]),
        ("curveTo", [(173, 54), (180, 76), (180, 116)]),
        ("closePath", []),
    ])
    cap_head = _clip(_path(font, "I", (.75, 0, 0, 1, 0, 0)), y0=900)
    g = new("uni1E9E", 0x1E9E, 795,
            "Broad capital sharp-s with angular returning upper stroke, I head and swept open foot.")
    _draw(g, _union(cap_ss, cap_foot, cap_head))

    for name, base, cp in [("dotlessi", "i", 0x0131),
                           ("dotlessj", "j", 0x0237)]:
        _dotless(font, name, base, cp)
        added.append(name)

    # Raised ordinals remain recognizably related to the lowercase, including
    # the a's wave and the o's barb.  No underline is required for either form.
    for name, base, cp in [("ordfeminine", "a", 0x00AA),
                           ("ordmasculine", "o", 0x00BA)]:
        scale = .62
        g = new(name, cp, round(font[base].width * scale + 28),
                "Raised, proportionately scaled approved lowercase ordinal.")
        _component(g, base, (scale, 0, 0, scale, 14, 460))

    return added
