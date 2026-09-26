## FontSpector report

fontspector version: 1.8.0



## Checks with FATAL results

These must be addressed first.


<details><summary>[1] googlefonts/ofl/sirenandsailor/SirenandSailor-Regular.ttf</summary>
<div>


<details>
    <summary>💥 <b>ERROR</b> Familyname must be unique according to namecheck.fontdata.com (fontdata_namecheck)</summary>
    <div>


> We need to check names are not already used, and today the best place to check that is http://namecheck.fontdata.com




Original proposal: [https://github.com/fonttools/fontbakery/issues/494]





- 💥 **ERROR** Error: A network error occurred: Failed to access: http://namecheck.fontdata.com/. error sending request for url (http://namecheck.fontdata.com/api/?q=Siren+and+Sailor) 
  
  

</div>
</details>


</div>
</details>







## All other checks




<details><summary>[4] googlefonts/ofl/sirenandsailor/SirenandSailor-Regular.ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * de_Latn (German)           |
|   The following auxiliary characters are missing from the font: ſ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǧ |                              |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ȟ |                              |
|   The following auxiliary characters are missing from the font: Ǩ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŝ |                              |
|   The following auxiliary characters are missing from the font: Ţ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǧ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ȟ |                              |
|   The following auxiliary characters are missing from the font: ǩ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŝ |                              |
|   The following auxiliary characters are missing from the font: ţ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * fr_Latn (French)           |
|   The following auxiliary characters are missing from the font: Ǔ |                              |
|   The following auxiliary characters are missing from the font: ſ |                              |
|   The following auxiliary characters are missing from the font: ǔ |                              |
| Auxiliary orthography codepoints:                                 | * ro_Latn (Romanian)         |
|   The following auxiliary characters are missing from the font: Ţ |                              |
|   The following auxiliary characters are missing from the font: ţ |                              |
| Auxiliary orthography codepoints:                                 | * lt_Latn (Lithuanian)       |
|   The following auxiliary characters are missing from the font: Ẽ |                              |
|   The following auxiliary characters are missing from the font: Ĩ |                              |
|   The following auxiliary characters are missing from the font: Ũ |                              |
|   The following auxiliary characters are missing from the font: ẽ |                              |
|   The following auxiliary characters are missing from the font: ĩ |                              |
|   The following auxiliary characters are missing from the font: ũ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
| Auxiliary orthography codepoints:                                 | * lv_Latn (Latvian)          |
|   The following auxiliary characters are missing from the font: Ŗ |                              |
|   The following auxiliary characters are missing from the font: ŗ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ǎ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ǎ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any jaggy segments? (outline_jaggy_segments)</summary>
    <div>


> This check heuristically detects outline segments which form a particularly small angle, indicative of an outline error. This may cause false positives in cases such as extreme ink traps, so should be regarded as advisory and backed up by manual inspection.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3064]





- ⚠️ **WARN** The following glyphs have jaggy segments:

* dollar (U+0024): Quad(QuadBez { p0: (675.0, 1232.0), p1: (673.0, 1234.0), p2: (672.0, 1239.0) })/Line(Line { p0: (672.0, 1239.0), p1: (672.0, 861.0) }) = 11.309932474020195 degrees
* asterisk (U+002A): Line(Line { p0: (310.0, 1166.0), p1: (289.0, 1002.0) })/Line(Line { p0: (289.0, 1002.0), p1: (269.0, 1166.0) }) = 14.24990362214908 degrees
* asterisk (U+002A): Line(Line { p0: (269.0, 1321.0), p1: (289.0, 1485.0) })/Line(Line { p0: (289.0, 1485.0), p1: (310.0, 1321.0) }) = 14.24990362214908 degrees
* six (U+0036): Quad(QuadBez { p0: (831.0, 833.5), p1: (842.0, 851.0), p2: (852.0, 868.0) })/Quad(QuadBez { p0: (852.0, 868.0), p1: (845.0, 844.0), p2: (839.0, 819.5) }) = 14.20534021114795 degrees
* D (U+0044): Quad(QuadBez { p0: (1370.5, 1311.0), p1: (1372.0, 1313.0), p2: (1373.0, 1315.0) })/Quad(QuadBez { p0: (1373.0, 1315.0), p1: (1368.0, 1295.0), p2: (1362.5, 1275.0) }) = 12.528807709151522 degrees
* D (U+0044): Quad(QuadBez { p0: (163.5, 1369.0), p1: (121.0, 1387.0), p2: (88.0, 1417.0) })/Quad(QuadBez { p0: (88.0, 1417.0), p1: (108.0, 1403.0), p2: (129.5, 1391.5) }) = 7.281668807535042 degrees
* a (U+0061): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* a (U+0061): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* g (U+0067): Line(Line { p0: (207.0, -415.0), p1: (215.0, -415.0) })/Quad(QuadBez { p0: (215.0, -415.0), p1: (200.0, -418.0), p2: (189.0, -424.5) }) = 11.309932474020227 degrees
* sterling (U+00A3): Quad(QuadBez { p0: (350.0, 210.0), p1: (312.0, 148.0), p2: (253.0, 110.0) })/Quad(QuadBez { p0: (253.0, 110.0), p1: (315.0, 133.0), p2: (365.5, 139.5) }) = 12.431051717800296 degrees
* ordfeminine (U+00AA): Line(Line { p0: (422.0, 1051.0), p1: (426.0, 1031.0) })/Line(Line { p0: (426.0, 1031.0), p1: (426.0, 1047.0) }) = 11.309932474020195 degrees
* ordfeminine (U+00AA): Quad(QuadBez { p0: (124.0, 1249.0), p1: (107.0, 1257.0), p2: (93.0, 1268.0) })/Quad(QuadBez { p0: (93.0, 1268.0), p1: (100.0, 1264.0), p2: (107.5, 1260.0) }) = 8.412345290426844 degrees
* questiondown (U+00BF): Quad(QuadBez { p0: (386.0, 926.0), p1: (377.0, 943.0), p2: (358.0, 943.0) })/Line(Line { p0: (358.0, 943.0), p1: (370.0, 944.0) }) = 4.76364169072622 degrees
* Eth (U+00D0): Quad(QuadBez { p0: (147.5, 1369.0), p1: (105.0, 1387.0), p2: (72.0, 1417.0) })/Quad(QuadBez { p0: (72.0, 1417.0), p1: (92.0, 1403.0), p2: (113.5, 1391.5) }) = 7.281668807535042 degrees
* Eth (U+00D0): Quad(QuadBez { p0: (1354.5, 1311.0), p1: (1356.0, 1313.0), p2: (1357.0, 1315.0) })/Quad(QuadBez { p0: (1357.0, 1315.0), p1: (1352.0, 1295.0), p2: (1346.5, 1275.0) }) = 12.528807709151522 degrees
* Oslash (U+00D8): Quad(QuadBez { p0: (284.5, 86.0), p1: (270.0, 68.0), p2: (255.0, 50.0) })/Quad(QuadBez { p0: (255.0, 50.0), p1: (268.0, 72.0), p2: (279.5, 93.0) }) = 9.226344219776202 degrees
* germandbls (U+00DF): Quad(QuadBez { p0: (321.0, 26.5), p1: (333.0, 4.0), p2: (358.0, -10.0) })/Quad(QuadBez { p0: (358.0, -10.0), p1: (333.0, -1.0), p2: (312.0, 7.0) }) = 9.449949982022032 degrees
* agrave (U+00E0): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* agrave (U+00E0): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* aacute (U+00E1): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* aacute (U+00E1): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* acircumflex (U+00E2): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* acircumflex (U+00E2): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* atilde (U+00E3): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* atilde (U+00E3): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* adieresis (U+00E4): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* adieresis (U+00E4): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* aring (U+00E5): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* aring (U+00E5): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* ae (U+00E6): Line(Line { p0: (645.0, 610.0), p1: (652.0, 578.0) })/Line(Line { p0: (652.0, 578.0), p1: (652.0, 748.0) }) = 12.339087278326149 degrees
* ae (U+00E6): Quad(QuadBez { p0: (164.5, 928.5), p1: (137.0, 941.0), p2: (115.0, 960.0) })/Quad(QuadBez { p0: (115.0, 960.0), p1: (126.0, 954.0), p2: (138.0, 947.5) }) = 12.204624208916373 degrees
* eth (U+00F0): Quad(QuadBez { p0: (365.5, 1487.5), p1: (310.0, 1515.0), p2: (255.0, 1523.0) })/Quad(QuadBez { p0: (255.0, 1523.0), p1: (297.0, 1525.0), p2: (337.0, 1538.0) }) = 11.002203820981494 degrees
* oslash (U+00F8): Quad(QuadBez { p0: (197.5, 61.5), p1: (185.0, 44.0), p2: (171.0, 28.0) })/Quad(QuadBez { p0: (171.0, 28.0), p1: (183.0, 49.0), p2: (193.0, 69.0) }) = 11.441043868767382 degrees
* amacron (U+0101): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* amacron (U+0101): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* abreve (U+0103): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* abreve (U+0103): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* aogonek (U+0105): Line(Line { p0: (643.0, 610.0), p1: (650.0, 578.0) })/Line(Line { p0: (650.0, 578.0), p1: (650.0, 603.0) }) = 12.339087278326149 degrees
* aogonek (U+0105): Quad(QuadBez { p0: (163.5, 928.5), p1: (136.0, 941.0), p2: (113.0, 960.0) })/Quad(QuadBez { p0: (113.0, 960.0), p1: (124.0, 954.0), p2: (136.5, 947.5) }) = 10.949208303029309 degrees
* Dcaron (U+010E): Quad(QuadBez { p0: (1370.5, 1311.0), p1: (1372.0, 1313.0), p2: (1373.0, 1315.0) })/Quad(QuadBez { p0: (1373.0, 1315.0), p1: (1368.0, 1295.0), p2: (1362.5, 1275.0) }) = 12.528807709151522 degrees
* Dcaron (U+010E): Quad(QuadBez { p0: (163.5, 1369.0), p1: (121.0, 1387.0), p2: (88.0, 1417.0) })/Quad(QuadBez { p0: (88.0, 1417.0), p1: (108.0, 1403.0), p2: (129.5, 1391.5) }) = 7.281668807535042 degrees
* Dcroat (U+0110): Quad(QuadBez { p0: (147.5, 1369.0), p1: (105.0, 1387.0), p2: (72.0, 1417.0) })/Quad(QuadBez { p0: (72.0, 1417.0), p1: (92.0, 1403.0), p2: (113.5, 1391.5) }) = 7.281668807535042 degrees
* Dcroat (U+0110): Quad(QuadBez { p0: (1354.5, 1311.0), p1: (1356.0, 1313.0), p2: (1357.0, 1315.0) })/Quad(QuadBez { p0: (1357.0, 1315.0), p1: (1352.0, 1295.0), p2: (1346.5, 1275.0) }) = 12.528807709151522 degrees
* gbreve (U+011F): Line(Line { p0: (207.0, -415.0), p1: (215.0, -415.0) })/Quad(QuadBez { p0: (215.0, -415.0), p1: (200.0, -418.0), p2: (189.0, -424.5) }) = 11.309932474020227 degrees
* gdotaccent (U+0121): Line(Line { p0: (207.0, -415.0), p1: (215.0, -415.0) })/Quad(QuadBez { p0: (215.0, -415.0), p1: (200.0, -418.0), p2: (189.0, -424.5) }) = 11.309932474020227 degrees
* uni0123 (U+0123): Line(Line { p0: (207.0, -415.0), p1: (215.0, -415.0) })/Quad(QuadBez { p0: (215.0, -415.0), p1: (200.0, -418.0), p2: (189.0, -424.5) }) = 11.309932474020227 degrees
* Hbar (U+0126): Quad(QuadBez { p0: (316.5, 1093.5), p1: (276.0, 1094.0), p2: (236.0, 1099.0) })/Quad(QuadBez { p0: (236.0, 1099.0), p1: (278.0, 1102.0), p2: (317.5, 1106.0) }) = 11.210633128876657 degrees
* uni1E9E (U+1E9E): Quad(QuadBez { p0: (377.5, 27.0), p1: (388.0, 3.0), p2: (415.0, -13.0) })/Quad(QuadBez { p0: (415.0, -13.0), p1: (384.0, 0.0), p2: (357.0, 7.5) }) = 7.899691614265156 degrees
* uni20B9 (U+20B9): Quad(QuadBez { p0: (982.5, 27.0), p1: (1013.0, 12.0), p2: (1052.0, 0.0) })/Quad(QuadBez { p0: (1052.0, 0.0), p1: (999.0, 14.0), p2: (943.5, 11.0) }) = 2.305966723995073 degrees
* six.tnum: Quad(QuadBez { p0: (998.0, 833.5), p1: (1009.0, 851.0), p2: (1019.0, 868.0) })/Quad(QuadBez { p0: (1019.0, 868.0), p1: (1012.0, 844.0), p2: (1006.0, 819.5) }) = 14.20534021114795 degrees [code: found-jaggy-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Do outlines contain any semi-vertical or semi-horizontal lines? (outline_semi_vertical)</summary>
    <div>


> This check detects line segments which are nearly, but not quite, exactly horizontal or vertical. Sometimes such lines are created by design, but often they are indicative of a design error.
> 
> This check is disabled for italic styles, which often contain nearly-upright lines.




Original proposal: [https://github.com/fonttools/fontbakery/pull/3088]





- ⚠️ **WARN** The following glyphs have semi-vertical/semi-horizontal lines:

* plus (U+002B): Line(Line { p0: (330.0, 635.0), p1: (528.0, 636.0) }) (angle: 0.29 degrees, expected: 0.00 degrees)
* four (U+0034): Line(Line { p0: (927.0, 404.0), p1: (737.0, 403.0) }) (angle: -179.70 degrees, expected: -180.00 degrees)
* four (U+0034): Line(Line { p0: (638.0, 459.0), p1: (637.0, 1327.0) }) (angle: 90.07 degrees, expected: 90.00 degrees)
* B (U+0042): Line(Line { p0: (389.0, 296.0), p1: (388.0, 720.0) }) (angle: 90.14 degrees, expected: 90.00 degrees)
* B (U+0042): Line(Line { p0: (687.0, 742.0), p1: (810.0, 743.0) }) (angle: 0.47 degrees, expected: 0.00 degrees)
* F (U+0046): Line(Line { p0: (892.0, 682.0), p1: (625.0, 683.0) }) (angle: 179.79 degrees, expected: 180.00 degrees)
* H (U+0048): Line(Line { p0: (474.0, 1255.0), p1: (473.0, 992.0) }) (angle: -90.22 degrees, expected: -90.00 degrees)
* M (U+004D): Line(Line { p0: (462.0, 1318.0), p1: (461.0, 986.0) }) (angle: -90.17 degrees, expected: -90.00 degrees)
* N (U+004E): Line(Line { p0: (1217.0, 614.0), p1: (1216.0, 760.0) }) (angle: 90.39 degrees, expected: 90.00 degrees)
* N (U+004E): Line(Line { p0: (409.0, 718.0), p1: (410.0, 321.0) }) (angle: -89.86 degrees, expected: -90.00 degrees)
* P (U+0050): Line(Line { p0: (1003.0, 721.0), p1: (469.0, 720.0) }) (angle: -179.89 degrees, expected: -180.00 degrees)
* T (U+0054): Line(Line { p0: (826.0, 1148.0), p1: (825.0, 945.0) }) (angle: -90.28 degrees, expected: -90.00 degrees)
* U (U+0055): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* a (U+0061): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* d (U+0064): Line(Line { p0: (743.0, 376.0), p1: (744.0, 178.0) }) (angle: -89.71 degrees, expected: -90.00 degrees)
* j (U+006A): Line(Line { p0: (580.0, 96.0), p1: (579.0, 212.0) }) (angle: 90.49 degrees, expected: 90.00 degrees)
* l (U+006C): Line(Line { p0: (223.0, 167.0), p1: (222.0, 1071.0) }) (angle: 90.06 degrees, expected: 90.00 degrees)
* n (U+006E): Line(Line { p0: (781.0, 145.0), p1: (782.0, 290.0) }) (angle: 89.60 degrees, expected: 90.00 degrees)
* q (U+0071): Line(Line { p0: (741.0, 863.0), p1: (740.0, 629.0) }) (angle: -90.24 degrees, expected: -90.00 degrees)
* t (U+0074): Line(Line { p0: (206.0, 878.0), p1: (44.0, 879.0) }) (angle: 179.65 degrees, expected: 180.00 degrees)
* t (U+0074): Line(Line { p0: (206.0, 922.0), p1: (205.0, 1101.0) }) (angle: 90.32 degrees, expected: 90.00 degrees)
* AE (U+00C6): Line(Line { p0: (728.0, 33.0), p1: (727.0, 161.0) }) (angle: 90.45 degrees, expected: 90.00 degrees)
* Ntilde (U+00D1): Line(Line { p0: (1217.0, 614.0), p1: (1216.0, 760.0) }) (angle: 90.39 degrees, expected: 90.00 degrees)
* Ntilde (U+00D1): Line(Line { p0: (409.0, 718.0), p1: (410.0, 321.0) }) (angle: -89.86 degrees, expected: -90.00 degrees)
* Ugrave (U+00D9): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Uacute (U+00DA): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Ucircumflex (U+00DB): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Udieresis (U+00DC): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Thorn (U+00DE): Line(Line { p0: (986.0, 414.0), p1: (451.0, 413.0) }) (angle: -179.89 degrees, expected: -180.00 degrees)
* agrave (U+00E0): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* aacute (U+00E1): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* acircumflex (U+00E2): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* atilde (U+00E3): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* adieresis (U+00E4): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* aring (U+00E5): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* igrave (U+00EC): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* iacute (U+00ED): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* icircumflex (U+00EE): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* idieresis (U+00EF): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* ntilde (U+00F1): Line(Line { p0: (781.0, 145.0), p1: (782.0, 290.0) }) (angle: 89.60 degrees, expected: 90.00 degrees)
* thorn (U+00FE): Line(Line { p0: (228.0, 1071.0), p1: (227.0, 1322.0) }) (angle: 90.23 degrees, expected: 90.00 degrees)
* amacron (U+0101): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* abreve (U+0103): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* aogonek (U+0105): Line(Line { p0: (744.0, 628.0), p1: (745.0, 238.0) }) (angle: -89.85 degrees, expected: -90.00 degrees)
* dcaron (U+010F): Line(Line { p0: (743.0, 376.0), p1: (744.0, 178.0) }) (angle: -89.71 degrees, expected: -90.00 degrees)
* dcroat (U+0111): Line(Line { p0: (746.0, 376.0), p1: (747.0, 178.0) }) (angle: -89.71 degrees, expected: -90.00 degrees)
* dcroat (U+0111): Line(Line { p0: (655.0, 881.0), p1: (656.0, 1168.0) }) (angle: 89.80 degrees, expected: 90.00 degrees)
* Hbar (U+0126): Line(Line { p0: (452.0, 1255.0), p1: (451.0, 1124.0) }) (angle: -90.44 degrees, expected: -90.00 degrees)
* Hbar (U+0126): Line(Line { p0: (1299.0, 1096.0), p1: (552.0, 1097.0) }) (angle: 179.92 degrees, expected: 180.00 degrees)
* hbar (U+0127): Line(Line { p0: (218.0, 375.0), p1: (217.0, 1098.0) }) (angle: 90.08 degrees, expected: 90.00 degrees)
* imacron (U+012B): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* ibreve (U+012D): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* dotlessi (U+0131): Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees)
* lacute (U+013A): Line(Line { p0: (223.0, 167.0), p1: (222.0, 1071.0) }) (angle: 90.06 degrees, expected: 90.00 degrees)
* uni013C (U+013C): Line(Line { p0: (223.0, 167.0), p1: (222.0, 1071.0) }) (angle: 90.06 degrees, expected: 90.00 degrees)
* lcaron (U+013E): Line(Line { p0: (223.0, 167.0), p1: (222.0, 1071.0) }) (angle: 90.06 degrees, expected: 90.00 degrees)
* lslash (U+0142): Line(Line { p0: (218.0, 1071.0), p1: (217.0, 1322.0) }) (angle: 90.23 degrees, expected: 90.00 degrees)
* Nacute (U+0143): Line(Line { p0: (1217.0, 614.0), p1: (1216.0, 760.0) }) (angle: 90.39 degrees, expected: 90.00 degrees)
* Nacute (U+0143): Line(Line { p0: (409.0, 718.0), p1: (410.0, 321.0) }) (angle: -89.86 degrees, expected: -90.00 degrees)
* nacute (U+0144): Line(Line { p0: (781.0, 145.0), p1: (782.0, 290.0) }) (angle: 89.60 degrees, expected: 90.00 degrees)
* uni0145 (U+0145): Line(Line { p0: (1217.0, 614.0), p1: (1216.0, 760.0) }) (angle: 90.39 degrees, expected: 90.00 degrees)
* uni0145 (U+0145): Line(Line { p0: (409.0, 718.0), p1: (410.0, 321.0) }) (angle: -89.86 degrees, expected: -90.00 degrees)
* uni0146 (U+0146): Line(Line { p0: (781.0, 145.0), p1: (782.0, 290.0) }) (angle: 89.60 degrees, expected: 90.00 degrees)
* Ncaron (U+0147): Line(Line { p0: (1217.0, 614.0), p1: (1216.0, 760.0) }) (angle: 90.39 degrees, expected: 90.00 degrees)
* Ncaron (U+0147): Line(Line { p0: (409.0, 718.0), p1: (410.0, 321.0) }) (angle: -89.86 degrees, expected: -90.00 degrees)
* ncaron (U+0148): Line(Line { p0: (781.0, 145.0), p1: (782.0, 290.0) }) (angle: 89.60 degrees, expected: 90.00 degrees)
* Tcaron (U+0164): Line(Line { p0: (826.0, 1148.0), p1: (825.0, 945.0) }) (angle: -90.28 degrees, expected: -90.00 degrees)
* tcaron (U+0165): Line(Line { p0: (206.0, 878.0), p1: (44.0, 879.0) }) (angle: 179.65 degrees, expected: 180.00 degrees)
* tcaron (U+0165): Line(Line { p0: (206.0, 922.0), p1: (205.0, 1101.0) }) (angle: 90.32 degrees, expected: 90.00 degrees)
* Umacron (U+016A): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Ubreve (U+016C): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Uring (U+016E): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Uhungarumlaut (U+0170): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* Uogonek (U+0172): Line(Line { p0: (397.0, 1249.0), p1: (396.0, 963.0) }) (angle: -90.20 degrees, expected: -90.00 degrees)
* uni021A (U+021A): Line(Line { p0: (826.0, 1148.0), p1: (825.0, 945.0) }) (angle: -90.28 degrees, expected: -90.00 degrees)
* uni021B (U+021B): Line(Line { p0: (206.0, 878.0), p1: (44.0, 879.0) }) (angle: 179.65 degrees, expected: 180.00 degrees)
* uni021B (U+021B): Line(Line { p0: (206.0, 922.0), p1: (205.0, 1101.0) }) (angle: 90.32 degrees, expected: 90.00 degrees)
* dotlessj (U+0237): Line(Line { p0: (598.0, 96.0), p1: (597.0, 212.0) }) (angle: 90.49 degrees, expected: 90.00 degrees)
* trademark (U+2122): Line(Line { p0: (931.0, 1389.0), p1: (930.0, 1249.0) }) (angle: -90.41 degrees, expected: -90.00 degrees)
* four.tnum: Line(Line { p0: (1091.0, 404.0), p1: (901.0, 403.0) }) (angle: -179.70 degrees, expected: -180.00 degrees)
* four.tnum: Line(Line { p0: (802.0, 459.0), p1: (801.0, 1327.0) }) (angle: 90.07 degrees, expected: 90.00 degrees)
* iogonek.nodot: Line(Line { p0: (218.0, 714.0), p1: (217.0, 889.0) }) (angle: 90.33 degrees, expected: 90.00 degrees) [code: found-semi-vertical]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'NONE' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] googlefonts/ofl/sirenandsailor</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** googlefonts/ofl/sirenandsailor/SirenandSailor-Regular.ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: yi, canadian-aboriginal
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, tifinagh, coptic, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: math, tifinagh, tai-le, malayalam, coptic, hebrew, syriac, old-permic, todhri, duployan, canadian-aboriginal
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
* U+0326 COMBINING COMMA BELOW: try adding math
* U+0327 COMBINING CEDILLA: try adding math
* U+200C ZERO WIDTH NON-JOINER: try adding one of: syriac, zanabazar-square, khojki, meetei-mayek, devanagari, myanmar, dogra, sogdian, arabic, avestan, cham, lao, tagbanwa, gurmukhi, khudawadi, hatran, mandaic, tai-le, tai-viet, yi, balinese, brahmi, thaana, malayalam, takri, pahawh-hmong, sharada, buhid, hanunoo, sinhala, bengali, syloti-nagri, kannada, phags-pa, tibetan, new-tai-lue, hebrew, sundanese, tagalog, siddham, masaram-gondi, tai-tham, chakma, gunjala-gondi, saurashtra, tamil, limbu, modi, tirhuta, tifinagh, duployan, buginese, oriya, warang-citi, bhaiksuki, khmer, kharoshthi, kayah-li, javanese, mongolian, psalter-pahlavi, gujarati, rejang, batak, hanifi-rohingya, grantha, kaithi, lepcha, manichaean, newa, mahajani, nko, telugu, thai
* U+200D ZERO WIDTH JOINER: try adding one of: rejang, phags-pa, khmer, tirhuta, bhaiksuki, old-hungarian, telugu, tibetan, khudawadi, modi, kharoshthi, hanunoo, thaana, pahawh-hmong, tagalog, yi, lao, hanifi-rohingya, gurmukhi, oriya, new-tai-lue, masaram-gondi, arabic, newa, limbu, lepcha, manichaean, mongolian, sharada, grantha, tai-tham, mandaic, warang-citi, balinese, myanmar, psalter-pahlavi, buginese, devanagari, duployan, saurashtra, avestan, kayah-li, brahmi, cham, javanese, tai-le, tai-viet, thai, bengali, malayalam, chakma, batak, takri, khojki, sundanese, tamil, zanabazar-square, gujarati, gunjala-gondi, dogra, sinhala, kannada, hebrew, meetei-mayek, buhid, nko, syloti-nagri, tagbanwa, siddham, kaithi, syriac, tifinagh, sogdian, mahajani
* U+25CC DOTTED CIRCLE: try adding one of: thai, tirhuta, wancho, tai-viet, caucasian-albanian, myanmar, warang-citi, bhaiksuki, duployan, kharoshthi, bassa-vah, javanese, kannada, khudawadi, lao, mandaic, manichaean, cham, malayalam, marchen, saurashtra, limbu, adlam, mende-kikakui, modi, tagbanwa, buginese, rejang, chakma, devanagari, khojki, math, soyombo, buhid, nko, tagalog, tai-tham, yi, ahom, mongolian, canadian-aboriginal, sinhala, elbasan, brahmi, hebrew, miao, tai-le, tamil, telugu, phags-pa, armenian, symbols, takri, mahajani, zanabazar-square, batak, gurmukhi, gujarati, osage, grantha, sharada, bengali, newa, sundanese, pahawh-hmong, tibetan, khmer, lepcha, music, dogra, kaithi, sogdian, tifinagh, thaana, hanunoo, coptic, meetei-mayek, oriya, balinese, hanifi-rohingya, masaram-gondi, psalter-pahlavi, syloti-nagri, kayah-li, old-permic, siddham, gunjala-gondi, new-tai-lue, syriac

Or you can add the above codepoints to one of the subsets supported by the font: latin-ext, latin [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>






### Summary

| 💥 ERROR | ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|---|
| 1 | 5 | 10 | 121 | 77 | 
| 0% | 2% | 5% | 57% | 36% | 



