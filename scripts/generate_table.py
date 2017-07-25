#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

CC = u"""<span class="checkspan"><img class="check" src="images/cc.png"/></span>"""
WIKI = u"""<span class="sourcespan"><img class="source" src="images/wiki.png"/></span>"""
CHECK = u"""<span class="checkspan"><img class="check" src="images/check.png"/></span>"""

def replace(flag, name, _type, forms, lemmata, check1, check2, check3, wiki, License):
    return u"""
  <tr>
    <td><img class="flag" src={0}/></td>
    <td>{1}</td>
    <td>{3}</td>
    <td>{4}</td>
    <td>{5}</td>
    <td>{6}</td>
    <td>{7}</td>
    <td>{8}</span></td>
    <td>{9}</td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="10">
      <h4>Additional information</h4>
      <ul>
      <li><a href="{10}">Wikipedia Page</a></li>
      </ul>   
    </td>
</tr>
""".format(*map(unicode, [flag, name, _type, forms, lemmata, CHECK if check1 else "", CHECK if check2 else "", CHECK if check3 else "", wiki, License, "https://en.wikipedia.org/wiki/"+name+"_language"]))

           
data_annotated = [
    ('"images/flags/SA-AL.svg"'   , 'Arabic'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/AM.svg"'      , 'Armenian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES-PV.svg"'   , 'Basque'           , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/BG.svg"'      , 'Bulgarian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES-CT.svg"'   , 'Catalan'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/CZ.svg"'      , 'Czech'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/DK.svg"'      , 'Danish'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NL.svg"'      , 'Dutch'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/EN.svg"'      , 'English'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/EE.svg"'      , 'Estonian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/FI.svg"'      , 'Finnish'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/FR.svg"'      , 'French'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/DE.svg"'      , 'German'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/GR.svg"'      , 'Greek'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IL.svg"'      , 'Hebrew'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IN.svg"'      , 'Hindi'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/HU.svg"'      , 'Hungarian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ID.svg"'      , 'Irish'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IT.svg"'      , 'Italian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IQ-KRD.svg"'  , 'Kurmanji Kurdish' , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/VA.svg"'      , 'Latin'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/LV.svg"'      , 'Latvian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/LT.svg"'      , 'Lithuanian'       , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/MT.svg"'      , 'Maltese'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SAMI.svg"'    , 'Northern Sami'    , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NO.svg"'      , 'Norwegian Bokmål' , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NO.svg"'      , 'Norwegian Nynyork', 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IR.svg"'      , 'Persian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/PL.svg"'      , 'Polish'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/PT.svg"'      , 'Portuguese'       , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/RO.svg"'      , 'Romanian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/RU.svg"'      , 'Russian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/RS.svg"'      , 'Serbian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SK.svg"'      , 'Slovak'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SI.svg"'      , 'Slovenian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES.svg"'      , 'Spanish'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SE.svg"'      , 'Swedish'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/TR.svg"'      , 'Turkish'          , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/PK.svg"'      , 'Urdu'             , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/BD.svg"'      , 'Bengali'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/FO.svg"'      , 'Faroese'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IQ-KRD.svg"'  , 'Sorani Kurdish'   , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IC.svg"'      , 'Icelandic'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/AL.svg"'      , 'Albanian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NP.svg"'      , 'Khaling'          , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/WA.svg"'      , 'Welsh'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/GE.svg"'      , 'Georgian'         , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/HA.png"'      , 'Haida'            , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NV.svg"'      , 'Navajo'           , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SB.svg"'      , 'Lower Sorbian'    , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/MK.svg"'      , 'Macedonian'       , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ST.svg"'      , 'Scottish Gaelic'  , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/UK.svg"'      , 'Ukrainian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/QU.svg"'      , 'Quechua'          , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
]

data_coming = [
('"images/flags/JP.svg"' ,"Japanese", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/GR.svg"' ,"Ancient Greek", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/KO.svg"' ,"Korean", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/FR-ROYAL.svg"' ,"Old French", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/AM.svg"' ,"Old Armenian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LU.svg"' ,"Luxembourgish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SY.svg"' ,"Classical Syriac", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/GC.svg"' ,"Galician", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/FR.svg"' ,"Middle French", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/AS.svg"' ,"Asturian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/IN.svg"' ,"Sanskrit", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/EN.svg"' ,"Old English", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/CI.svg"' ,"Adyghe", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/WE.svg"' ,"Old Saxon", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/BE.svg"' ,"Belarusian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/OC.svg"' ,"Occitan", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/KE.svg"' ,"Swahili", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/VE.svg"' ,"Venetian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/AZ.svg"' ,"Azeri", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/GO.svg"' ,"Gothic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/BA.svg"' ,"Bashkir", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TA.svg"' ,"Crimean Tatar", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LD.svg"' ,"Ladin", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/RA.svg"' ,"Old Norse", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/IM.svg"' ,"Manx", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LI.svg"' ,"Limburgish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/DE.svg"' ,"Low German", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/FL.svg"' ,"Friulian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/JE.svg"' ,"Jerriais", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LV.svg"' ,"Livonian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/IN.svg"' ,"Kannada", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KA.svg"' ,"Kabardian", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IL.svg"' ,"Yiddish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TJ.svg"' ,"Tajik", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SA.svg"' ,"Zulu", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/UZ.svg"' ,"Uzbek", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KG.svg"' ,"Kyrgyz", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/SA.svg"' ,"Afrikaans", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/ID.svg"' ,"Old Irish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/CH.svg"' ,"Romansch", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NF.svg"' ,"North Frisian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SC.svg"' ,"Sicilian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NE.svg"' ,"Neapolitan", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/MY.svg"' ,"Malay", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/MORAVA.svg"' ,"Old Church Slavonic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NM.svg"' ,"Norman", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/VO.svg"' ,"Votic", 0, 0, "agglutinatve",  True, True, True, WIKI, CC),
('"images/flags/AR.svg"' ,"Aragonese", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/KH.svg"' ,"Khakas", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KL.svg"' ,"Karelian", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IN.svg"' ,"Telugu", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IG.svg"' ,"Ingrian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/WF.svg"' ,"West Frisian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SY.svg"' ,"Aramaic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TM.svg"' ,"Turkmen", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/MA.svg"' ,"Mapudungun", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/DE.svg"' ,"Middle High German", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/EG.svg"' ,"Egyptian Arabic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NL.svg"' ,"Old Dutch", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/GL.svg"' ,"Greenlandic", 0, 0, "agglutinative",  True, True, True, WIKI, CC)]

entries_annotated, entries_coming  = [], []
for datum in sorted(data_annotated, key=lambda x: x[1]):
    entries_annotated.append(replace(*datum))
for datum in sorted(data_coming, key=lambda x: x[1]):
    entries_coming.append(replace(*datum))

table_annotated = "\n\n".join(entries_annotated)
table_coming = "\n\n".join(entries_coming)

print len(entries_annotated)
print len(entries_coming)
# replace the table
import sys
import codecs
with codecs.open(sys.argv[1], 'rb', encoding='utf-8') as f:
    with codecs.open(sys.argv[2], 'wb', encoding='utf-8') as g:
        for line in f:
            if line.strip() == u"TABLE1":
                g.write(table_annotated+"\n")
            elif line.strip() == u"TABLE2":
                g.write(table_coming+"\n")
            else:
                g.write(line)
