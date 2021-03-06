#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys  
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')

# constants
CC = u"""<span class="checkspan"><img class="check" src="images/cc.png"/></span>"""
WIKI = u"""<span class="sourcespan"><img class="source" src="images/wiki.png"/></span>"""
CHECK = u"""<span class="checkspan"><img class="check" src="images/check.png"/></span>"""
NONE = u""
FUSIONAL = """<a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a>"""
AGGLUTINATIVE = """<a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a>"""
ISOLATING = """<a href="https://en.wikipedia.org/wiki/Agglutinative_language">isolating</a>"""

# read in iso-639-3.tab
lang2code, lang2type = {}, {}
with codecs.open("iso-639-3.tab", 'rb', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if i == 0:
            continue
        line = line.strip()
        split = line.split("\t")
        if len(split) == 8:
            split = split[:7]
        code, _, _, _, scope, T,  name = split
        if code in ["mis", "mul", "und", "zxx"]:
            continue
        
        if T == "L":
            T = "living"
        elif T == "E":
            T = '<a href="https://en.wikipedia.org/wiki/Extinct_language">extinct</a>'
        elif T == "H":
            T = '<a href="https://en.wikipedia.org/wiki/Historical_language">historical</a>'
        elif T == "A":
            T = '<a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a>'
        elif T == "C":
            T = '<a href="https://en.wikipedia.org/wiki/Constructed_language">constructed</a>'
        else:
            exit(0)
        lang2code[name] = code
        lang2type[name] = T


def replace(flag, name, category, templatic, forms, lemmata, check1, check2, check3, wiki, License, shared1, shared2):
    return u"""
  <tr>
    <td><span class="flagspan"><img class="flag" src={0}/></span></td>
    <td>{1}</td>
    <td>{2}</td>
    <td>{6}</td>
    <td>{7}</td>
    <td>{8}</td>
    <td>{9}</td>
    <td>{10}</td>
    <td>{11}</td>
    <td>{12}</td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/{2}">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/{2}/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>{14}</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>{15}</li>  
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail2"><b>Typology:</b></span>{4}</li>
      <li><span class="detail2"><b>Templatic:</b></span>{5}</li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail3"><b>Info:</b></span> <a href="{13}">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>{3}</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>
""".format(*map(unicode, [flag, name, lang2code[name], lang2type[name], category, "no" if not templatic else "yes", forms, lemmata, CHECK if check1 else "", CHECK if check2 else "", CHECK if check3 else "", wiki, License, "https://en.wikipedia.org/wiki/"+name+"_language", '<a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a>' if shared1 else "no", '<a href="http://www.sigmorphon.org/conll2017">yes</a>' if shared2 else "no"]))

# data to load
data_annotated = [
    ('"images/flags/SA-AL.svg"'   , 'Arabic'           , FUSIONAL, True,          0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/AM.svg"'      , 'Armenian'         , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/ES-PV.svg"'   , 'Basque'           , AGGLUTINATIVE, False,    0,      0,    True, True, True, NONE, CC, False, True),
    ('"images/flags/BG.svg"'      , 'Bulgarian'        , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/ES-CT.svg"'   , 'Catalan'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/CZ.svg"'      , 'Czech'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/DK.svg"'      , 'Danish'           , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/NL.svg"'      , 'Dutch'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/EN.svg"'      , 'English'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/EE.svg"'      , 'Estonian'         , AGGLUTINATIVE, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/FI.svg"'      , 'Finnish'          , AGGLUTINATIVE, False,         0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/FR.svg"'      , 'French'           , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/DE.svg"'      , 'German'           , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/IL.svg"'      , 'Hebrew'           , FUSIONAL, True,          0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/IN.svg"'      , 'Hindi'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/HU.svg"'      , 'Hungarian'        , AGGLUTINATIVE, False,         0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/ID.svg"'      , 'Irish'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/IT.svg"'      , 'Italian'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/IQ-KRD.svg"'  , 'Northern Kurdish' , FUSIONAL, False,         0,      0,    True, True, True, NONE, CC, False, True),
    ('"images/flags/VA.svg"'      , 'Latin'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/LA.svg"'      , 'Latvian'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/LT.svg"'      , 'Lithuanian'       , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/SAMI.svg"'    , 'Northern Sami'    , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/NO.svg"'      , u'Norwegian Bokmål', FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/NO.svg"'      , 'Norwegian Nynorsk', FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/IR.svg"'      , 'Persian'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/PL.svg"'      , 'Polish'           , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/PT.svg"'      , 'Portuguese'       , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/RO.svg"'      , 'Romanian'         , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/RU.svg"'      , 'Russian'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/SK.svg"'      , 'Slovak'           , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/SI.svg"'      , 'Slovenian'        , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/ES.svg"'      , 'Spanish'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/SE.svg"'      , 'Swedish'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/TR.svg"'      , 'Turkish'          , AGGLUTINATIVE, False,    0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/PK.svg"'      , 'Urdu'             , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/BD.svg"'      , 'Bengali'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/FO.svg"'      , 'Faroese'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/IQ-KRD.svg"'  , 'Central Kurdish'  , FUSIONAL, False,         0,      0,    True, True, True, NONE, CC, False, True),
    ('"images/flags/IC.svg"'      , 'Icelandic'        , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/AL.svg"'      , 'Albanian'         , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/NP.svg"'      , 'Khaling'          , AGGLUTINATIVE, False,    0,      0,    True, True, True, NONE, CC, False, True),
    ('"images/flags/WA.svg"'      , 'Welsh'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/GE.svg"'      , 'Georgian'         , AGGLUTINATIVE, False,    0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/HA.png"'      , 'Haida'            , AGGLUTINATIVE, False,    0,      0,    True, True, True, NONE, CC, False, True),
    ('"images/flags/NV.svg"'      , 'Navajo'           , AGGLUTINATIVE, False,    0,      0,    True, True, True, WIKI, CC, True, True),
    ('"images/flags/SB.svg"'      , 'Lower Sorbian'    , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/MK.svg"'      , 'Macedonian'       , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/ST.svg"'      , 'Scottish Gaelic'  , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/UK.svg"'      , 'Ukrainian'        , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, True),
    ('"images/flags/QU.svg"'      , 'Quechua'          , AGGLUTINATIVE, False,    0,      0,    True, True, True, WIKI, CC, False, True)
]

data_annotated_new = []
for entry in data_annotated:
    code = lang2code[entry[1]]
    fname = "/Volumes/albatross/unimorph/{0}/{0}".format(code)
    try:
        print fname
        form_count = 0
        lemmata = set()
        V, A, N = False, False, False
        with codecs.open(fname, 'rb', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line == u"":
                    continue
                lemma, form, tag = line.split("\t")
                lemmata.add(lemma)
                form_count += 1
                if u"V" in tag.split(";"):
                    V = True
                if u"N" in tag.split(";"):
                    N = True
                if u"ADJ" in tag.split(";"):
                    A = True
                    
        lemma_count = len(lemmata)
        tmp = list(entry)
        tmp[4] = form_count
        tmp[5] = lemma_count
        tmp[6] = N
        tmp[7] = V
        tmp[8] = A
        data_annotated_new.append(tmp)
        
    except IOError:
        data_annotated_new.append(entry)

data_annotated = data_annotated_new        

data_coming = [
('"images/flags/RS.svg"'      , 'Serbian'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, False),
('"images/flags/MT.svg"'      , 'Maltese'          , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, True, False),
('"images/flags/GR.svg"'      , 'Modern Greek'            , FUSIONAL, False,         0,      0,    True, True, True, WIKI, CC, False, False),
('"images/flags/JP.svg"' ,"Japanese", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/GR.svg"' ,"Ancient Greek", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/KO.svg"' ,"Korean", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/FR-ROYAL.svg"' ,"Old French", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/AM.svg"' ,"Classical Armenian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/LU.svg"' ,"Luxembourgish", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/SY.svg"' ,"Classical Syriac", FUSIONAL, True,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/GC.svg"' ,"Galician", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/FR.svg"' ,"Middle French", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/AS.svg"' ,"Asturian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/IN.svg"' ,"Sanskrit", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/EN.svg"' ,"Old English", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/CI.svg"' ,"Adyghe", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/WE.svg"' ,"Old Saxon", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/BE.svg"' ,"Belarusian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/OC.svg"' ,"Occitan", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/KE.svg"' ,"Swahili", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/VE.svg"' ,"Venetian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/AZ.svg"' ,"Azerbaijani", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/GO.svg"' ,"Gothic", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/BA.svg"' ,"Bashkir", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/TA.svg"' ,"Crimean Tatar", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/LD.svg"' ,"Ladin", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/RA.svg"' ,"Old Norse", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/IM.svg"' ,"Manx", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/LI.svg"' ,"Limburgan", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/DE.svg"' ,"Low German", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/FL.svg"' ,"Friulian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/JE.svg"' ,u"Jèrriais", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/LV.svg"' ,"Liv", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/IN.svg"' ,"Kannada", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/KA.svg"' ,"Kabardian", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IL.svg"' ,"Yiddish", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/TJ.svg"' ,"Tajik", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/SA.svg"' ,"Zulu", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/UZ.svg"' ,"Uzbek", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/BY.svg"' ,"Buriat", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/KG.svg"' ,"Kirghiz", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/SA.svg"' ,"Afrikaans", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/ID.svg"' ,"Old Irish", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/CH.svg"' ,"Romansh", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/NF.svg"' ,"Northern Frisian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/SC.svg"' ,"Sicilian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/NE.svg"' ,"Neapolitan", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/MY.svg"' ,"Malay", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/MORAVA.svg"' ,"Church Slavic", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/VO.svg"' ,"Votic", AGGLUTINATIVE,  True, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/AR.svg"' ,"Aragonese", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/KH.svg"' ,"Khakas", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/KL.svg"' ,"Karelian", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IN.svg"' ,"Telugu", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IG.svg"' ,"Ingrian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/WF.svg"' ,"Western Frisian", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/SY.svg"' ,"Aramaic", FUSIONAL, True,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/TM.svg"' ,"Turkmen", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/MA.svg"' ,"Mapudungun", AGGLUTINATIVE, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/DE.svg"' ,"Middle High German", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/EG.svg"' ,"Egyptian Arabic", FUSIONAL, True,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/NL.svg"' ,"Old Dutch", FUSIONAL, False,  0, 0,  True, True, True, WIKI, CC, False, False),
('"images/flags/GL.svg"' ,"Kalaallisut", AGGLUTINATIVE, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/DE.svg"', "Middle Low German", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/AO.svg"', "Macedo-Romanian", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/TT.svg"', "Tatar", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/SD.svg"', "Sardinian", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IL.svg"', "Ladino", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/TB.svg"', "Tibetan", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/NL.svg"', "Middle Dutch", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/WI.svg"', "Wymysorys", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/MN.svg"', "Yucatec Maya", AGGLUTINATIVE, False, 0, 0,True, True, True, WIKI, CC, False, False),
('"images/flags/CN.svg"', "Mandarin Chinese", ISOLATING, False, 0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/KB.svg"', "Kashubian", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/SF.svg"', "Saterfriesisch", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/PR.svg"', u"Old Provençal", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/NMX.svg"', "Northern Tiwa", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CW.svg"', "Cornish", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/BR.svg"', "Breton", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/GG.svg"', "Gagauz", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/KZ.svg"', "Kazakh", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/MI.svg"', "Mirandese", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/NI.svg"', "Hausa", FUSIONAL, True,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CE.svg"', "Chechen", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CH.svg"', "Swiss German", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IN.svg"', "Malayalam", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/PT.svg"', "Old Portuguese", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
    ('"images/flags/TR.svg"', "Hittite", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/RM.svg"', "Romany", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/NN.svg"', "Inuktitut", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IN.svg"', "Panjabi", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/BO.svg"', u"!Xóõ", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/SAMI.svg"', "Skolt Sami", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/MD.svg"', "Malagasy", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/MX.svg"', "Classical Nahuatl", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/WL.svg"', "Walloon", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CA.svg"', "Ojibwa", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/AF.svg"', "Pushto", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/VR.svg"', u"Võro", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/IS.svg"', "Istriot", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/SA.svg"', "Tswana", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CO.svg"', "Corsican", FUSIONAL, False,  0, 0, True, True, True, WIKI, CC, False, False),
('"images/flags/CN.svg"', "Uighur", AGGLUTINATIVE, False,  0, 0, True, True, True, WIKI, CC, False, False)
]

entries_annotated, entries_coming  = [], []
for datum in sorted(data_annotated, key=lambda x: x[1]):
    print datum
    entries_annotated.append(replace(*datum))
for datum in sorted(data_coming, key=lambda x: x[1]):
    print datum
    print len(datum)
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
