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
    <td><span class="flagspan"><img class="flag" src={0}/>{1}</span> </td>
    <td>{2}</td>
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

           
data = [
    ('"images/flags/SA-AL.svg"'   , 'Arabic'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/AM.svg"'      , 'Armenian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES-PV.svg"'   , 'Basque'           , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/BG.svg"'      , 'Bulgarian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES-CT.svg"'   , 'Catalan'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/CZ.svg"'      , 'Czech'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/DK.svg"'      , 'Danish'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NL.svg"'      , 'Dutch'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/US.svg"'      , 'English'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
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
    ('"images/flags/TR.svg"'      , 'Kurmanji Kurdish' , 'fusional',       0,      0,    True, True, True, WIKI, CC),
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

entries = []
for datum in sorted(data, key=lambda x: x[1]):
    entries.append(replace(*datum))

table = "\n\n".join(entries)

print len(entries)
# replace the table
import sys
import codecs
with codecs.open(sys.argv[1], 'rb', encoding='utf-8') as f:
    with codecs.open(sys.argv[2], 'wb', encoding='utf-8') as g:
        for line in f:
            if line.strip() == u"TABLE":
                g.write(table+"\n")
            else:
                g.write(line)
