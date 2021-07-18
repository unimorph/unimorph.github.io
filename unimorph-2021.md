---
layout: page
permalink: /unimorph2021/
title: UniMorph Seminar 2021
---

# General Information

*Date: July,26th 2021  Format: Online (Zoom+Jamboard)*

The seminar will focus on development of consistent cross-linguistic annotation for Universal Dependencies and UniMorph. 

---




# Keynote Speakers

- [Khuyagbaatar Batsuren](https://scholar.google.it/citations?user=JsMdM8oAAAAJ&hl=en), Associate Professor at National University of Mongolia.

- [Reut Tsarfaty](https://www.openu.ac.il/en/personalsites/ReutTsarfaty.aspx), Associate Professor at Bar Ilan University.

# Agenda

We propose using Jamboard during the seminar: [https://jamboard.google.com/d/1EVw2bq7Toff6C6yGwUm-XOTdyAzX8TpWeYU9YL7_00I/edit?usp=sharing](https://jamboard.google.com/d/1EVw2bq7Toff6C6yGwUm-XOTdyAzX8TpWeYU9YL7_00I/edit?usp=sharing)

1. Discussion of annotation schemas for UniMorph and Universal Dependencies:

    - Annotation consistency. Consistency between UM and UD annotation. Consistency within UM. In 2020 and 2021, all languages added to UniMorph were checked in terms of their annotation consistency & correctness (tags' presence in the schema) using [um-canonicalize tool](https://github.com/unimorph/um-canonicalize). 
  
    - UD <---> UM interface. So far, there exists [UD-to-UM conversion tool](https://github.com/unimorph/ud-compatibility).


2. Derivational + Inflectional Morphology:
  
    - Incorporation of derivational morphology into UM (derivational paradigms). Khuygaabaatar has extracted derivational paradigms from Wiktionary. [Examples for Finnish](https://drive.google.com/drive/folders/1zRE3GrtkZ6NDTwB8lB2tAxIdbLrnH8Jf), [Examples for Russian](https://drive.google.com/drive/folders/1ZmRyLzwOARy4eI5yvlP89t-pkKmwei-A)

    - Paradigms that incorporate both inflectional and derivational word formation: shall disentangle them? Here is an example from Witold's Polish data: (jeździć, jeżdżenia, V.MSDR;NEUT;ACC;PL;IPFV),(jeździć, jeżdżeniach, V.MSDR;NEUT;ESS;PL;IPFV). It contains two types of transformation: nominalization and declension. 
 
    - Polysynthetic languages. UM has very few polysynthetic languages ([e.g. Adyghe](https://github.com/unimorph/ady)) and provides a small part of their paradigms.

3. Demonstration session:  WebUI for UniMorph annotation [http://unimorph.ethz.ch/](http://unimorph.ethz.ch/)

4. MWEs in paradigms:

    - Annotation of clitics. How should we store the paradigms with clitics (they typically(?) copy those that are without; maybe allow rules to be stored and paradigms for them generated on the fly?)

    - Annotation of MWEs that require dependencies. Samples in some language require syntactic information, e.g. `legkaja_ADJ promyshlennost_N'  vs. genitive constructions 'sindrom_N Aspergera_N'. This issue has been [reported here](https://aclanthology.org/K19-1014/).  

5. Administrative session:

    - A pipeline for publication & incorporation of new languages. Unimorph schema/language updates are primarily published on LREC (once in two years). Now we are trying to extend it to SIGMORPHON (as a part of SM Shared Task on morphological reinflection report). One possible option for future: book chapters at langsci press (?) 

    - Linguistic working groups and their management. UniMorph created [a number of working groups](https://docs.google.com/spreadsheets/d/1OA3m_kTnhYMZK762x1SiWy7wMSijxtTfAyDXB9V3wGY/edit#gid=977915123) (primarily based on language families) but they are not actively monitored.

    - UM Schema updates & maintaining its documentation. Ideally some wiki format. At the moment the UM annotation is static and is stored in [the pdf file](https://unimorph.github.io/doc/unimorph-schema.pdf) that isn't updated.

# Participants


