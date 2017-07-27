#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encoding=utf8  
import sys  
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')

CC = u"""<span class="checkspan"><img class="check" src="images/cc.png"/></span>"""
WIKI = u"""<span class="sourcespan"><img class="source" src="images/wiki.png"/></span>"""
CHECK = u"""<span class="checkspan"><img class="check" src="images/check.png"/></span>"""
NONE = u""

# read in iso-639-3.tab
lang2code = {}
with codecs.open("iso-639-3.tab", 'rb', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        split = line.split("\t")
        if len(split) == 8:
            split = split[:7]
        code, _, _, _, scope, T,  name = split
        lang2code[name] = code

def replace(flag, name,_type, forms, lemmata, check1, check2, check3, wiki, License):
    return u"""
  <tr>
    <td><span class="flagspan"><img class="flag" src={0}/></span></td>
    <td>{1}</td>
    <td>{2}</td>
    <td>{4}</td>
    <td>{5}</td>
    <td>{6}</td>
    <td>{7}</td>
    <td>{8}</td>
    <td>{9}</td>
    <td>{10}</td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <h4>Additional information</h4>
      <ul>
      <li><a href="{11}">Wikipedia Page</a></li>
      </ul>   
    </td>
</tr>
""".format(*map(unicode, [flag, name, lang2code[name], _type, forms, lemmata, CHECK if check1 else "", CHECK if check2 else "", CHECK if check3 else "", wiki, License, "https://en.wikipedia.org/wiki/"+name+"_language"]))

           
data_annotated = [
    ('"images/flags/SA-AL.svg"'   , 'Arabic'           , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/AM.svg"'      , 'Armenian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ES-PV.svg"'   , 'Basque'           , 'agglutinative',  0,      0,    True, True, True, NONE, CC),
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
    ('"images/flags/GR.svg"'      , 'Modern Greek'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IL.svg"'      , 'Hebrew'    , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IN.svg"'      , 'Hindi'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/HU.svg"'      , 'Hungarian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ID.svg"'      , 'Irish'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IT.svg"'      , 'Italian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/IQ-KRD.svg"'  , 'Northern Kurdish' , 'fusional',       0,      0,    True, True, True, NONE, CC),
    ('"images/flags/VA.svg"'      , 'Latin'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/LA.svg"'      , 'Latvian'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/LT.svg"'      , 'Lithuanian'       , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/MT.svg"'      , 'Maltese'          , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SAMI.svg"'    , 'Northern Sami'    , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NO.svg"'      , u'Norwegian Bokmål' , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NO.svg"'      , 'Norwegian Nynorsk', 'fusional',       0,      0,    True, True, True, WIKI, CC),
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
    ('"images/flags/IQ-KRD.svg"'  , 'Central Kurdish'   , 'fusional',       0,      0,    True, True, True, NONE, CC),
    ('"images/flags/IC.svg"'      , 'Icelandic'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/AL.svg"'      , 'Albanian'         , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/NP.svg"'      , 'Khaling'          , 'agglutinative',  0,      0,    True, True, True, NONE, CC),
    ('"images/flags/WA.svg"'      , 'Welsh'            , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/GE.svg"'      , 'Georgian'         , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/HA.png"'      , 'Haida'            , 'agglutinative',  0,      0,    True, True, True, NONE, CC),
    ('"images/flags/NV.svg"'      , 'Navajo'           , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/SB.svg"'      , 'Lower Sorbian'    , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/MK.svg"'      , 'Macedonian'       , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/ST.svg"'      , 'Scottish Gaelic'  , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/UK.svg"'      , 'Ukrainian'        , 'fusional',       0,      0,    True, True, True, WIKI, CC),
    ('"images/flags/QU.svg"'      , 'Quechua'          , 'agglutinative',  0,      0,    True, True, True, WIKI, CC),
]

data_annotated_new = []
for entry in data_annotated:
    lexicon = "-".join(map(lambda x: x.lower(), entry[1].split(" ")))
    fname = "/Volumes/albatross/research/mwc++/unimorph-lexica/" + lexicon
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
        tmp[3] = form_count
        tmp[4] = lemma_count
        tmp[5] = N
        tmp[6] = V
        tmp[7] = A
        data_annotated_new.append(tmp)
        
    except IOError:
        data_annotated_new.append(entry)

data_annotated = data_annotated_new        

data_coming = [
('"images/flags/JP.svg"' ,"Japanese", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/GR.svg"' ,"Ancient Greek", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/KO.svg"' ,"Korean", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/FR-ROYAL.svg"' ,"Old French", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/AM.svg"' ,"Classical Armenian", 0, 0, "fusional",  True, True, True, WIKI, CC),
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
('"images/flags/AZ.svg"' ,"Azerbaijani", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/GO.svg"' ,"Gothic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/BA.svg"' ,"Bashkir", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TA.svg"' ,"Crimean Tatar", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LD.svg"' ,"Ladin", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/RA.svg"' ,"Old Norse", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/IM.svg"' ,"Manx", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LI.svg"' ,"Limburgan", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/DE.svg"' ,"Low German", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/FL.svg"' ,"Friulian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/JE.svg"' ,u"Jèrriais", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/LV.svg"' ,"Liv", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/IN.svg"' ,"Kannada", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KA.svg"' ,"Kabardian", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IL.svg"' ,"Yiddish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TJ.svg"' ,"Tajik", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SA.svg"' ,"Zulu", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/UZ.svg"' ,"Uzbek", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/BY.svg"' ,"Buriat", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KG.svg"' ,"Kirghiz", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/SA.svg"' ,"Afrikaans", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/ID.svg"' ,"Old Irish", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/CH.svg"' ,"Romansh", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NF.svg"' ,"Northern Frisian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SC.svg"' ,"Sicilian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NE.svg"' ,"Neapolitan", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/MY.svg"' ,"Malay", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/MORAVA.svg"' ,"Church Slavic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/VO.svg"' ,"Votic", 0, 0, "agglutinatve",  True, True, True, WIKI, CC),
('"images/flags/AR.svg"' ,"Aragonese", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/KH.svg"' ,"Khakas", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/KL.svg"' ,"Karelian", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IN.svg"' ,"Telugu", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/IG.svg"' ,"Ingrian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/WF.svg"' ,"Western Frisian", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/SY.svg"' ,"Aramaic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/TM.svg"' ,"Turkmen", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/MA.svg"' ,"Mapudungun", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/DE.svg"' ,"Middle High German", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/EG.svg"' ,"Egyptian Arabic", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/NL.svg"' ,"Old Dutch", 0, 0, "fusional",  True, True, True, WIKI, CC),
('"images/flags/GL.svg"' ,"Kalaallisut", 0, 0, "agglutinative",  True, True, True, WIKI, CC),
('"images/flags/DE.svg"', "Middle Low German", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/AO.svg"', "Macedo-Romanian", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/TT.svg"', "Tatar", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/SD.svg"', "Sardinian", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/IL.svg"', "Ladino", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/TB.svg"', "Tibetan", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/NL.svg"', "Middle Dutch", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/WI.svg"', "Wymysorys", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/MN.svg"', "Yucatec Maya", 0, 0, "agglutinative", True, True, True, WIKI, CC),
('"images/flags/CN.svg"', "Mandarin Chinese", 0, 0, "isolating", True, True, True, WIKI, CC),
('"images/flags/KB.svg"', "Kashubian", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/SF.svg"', "Saterfriesisch", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/PR.svg"', u"Old Provençal", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/NMX.svg"', "Northern Tiwa", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CW.svg"', "Cornish", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/BR.svg"', "Breton", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/GG.svg"', "Gagauz", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/KZ.svg"', "Kazakh", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/MI.svg"', "Mirandese", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/NI.svg"', "Hausa", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CE.svg"', "Chechen", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CH.svg"', "Swiss German", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/IN.svg"', "Malayalam", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/PT.svg"', "Old Portuguese", 0, 0, "fusional", True, True, True, WIKI, CC),
    ('"images/flags/TR.svg"', "Hittite", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/RM.svg"', "Romany", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/NN.svg"', "Inuktitut", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/IN.svg"', "Panjabi", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/BO.svg"', u"!Xóõ", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/SAMI.svg"', "Skolt Sami", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/MD.svg"', "Malagasy", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/MX.svg"', "Classical Nahuatl", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/WL.svg"', "Walloon", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CA.svg"', "Ojibwa", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/AF.svg"', "Pushto", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/VR.svg"', u"Võro", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/IS.svg"', "Istriot", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/SA.svg"', "Tswana", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CO.svg"', "Corsican", 0, 0, "fusional", True, True, True, WIKI, CC),
('"images/flags/CN.svg"', "Uighur", 0, 0, "fusional", True, True, True, WIKI, CC)
]

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
