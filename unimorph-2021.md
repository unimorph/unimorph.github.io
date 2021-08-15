---
layout: page
permalink: /unimorph2021/
title: UniMorph Seminar 2021
---

# General Information

*Date: August -- September 2021  Format: Online (Zoom+Jamboard)*

The seminar focuses on development of consistent cross-linguistic annotation for Universal Dependencies and UniMorph as well as deveopment of well-designed linguistically motivated evaluation for  SIGMORPHON Shared Task on Morphological Reinflection. 

The seminar is organized as a series of 1-3 hour modules (slots), having one module a week. Each module is devoted to a specific topic and has a leading speaker. 

---




# Keynote Speakers

- [Reut Tsarfaty](https://nlp.biu.ac.il/~rtsarfaty/onlp), Associate Professor at Bar Ilan University.

- [Khuyagbaatar Batsuren](https://scholar.google.it/citations?user=JsMdM8oAAAAJ&hl=en), Associate Professor at National University of Mongolia.


# Agenda

We propose using Jamboard during the seminar: [https://jamboard.google.com/d/1EVw2bq7Toff6C6yGwUm-XOTdyAzX8TpWeYU9YL7_00I/edit?usp=sharing](https://jamboard.google.com/d/1EVw2bq7Toff6C6yGwUm-XOTdyAzX8TpWeYU9YL7_00I/edit?usp=sharing)

1. **Module #1: Aug, 16th 1pm--3pm UTC** (9am--11am EDT; 3pm--5pm Zurich; 4pm --6pm Haifa; 9pm--11pm Ulaanbaatar; 11pm--01am, Aug17th Melbourne).   
 Theme: **Word forms, phrases, or clauses in UniMorph: what level of granularity do we need?**  
 Leading Speaker: **[Reut Tsarfaty](https://nlp.biu.ac.il/~rtsarfaty/onlp)**  
 Title: More Than Morphs: Getting More Out of UniMorph  
 Abstract: Morphological processes such as inflection and reinflection are studied and evaluated in NLP nowadays with the help of UniMorph (UM), a large collection of labeled inflection tables of over a hundred typologically different languages. In this talk we look closely at the current version of UniMorph and assess its design and content. Specifically, we ask whether UM is a necessary component of morphological reinflection (or would minimal supervision be enough), whether the current version of UM is sufficient for morphological reinflection (or whether there are some aspects missing), and, importantly, whether the word forms in UM provide the right level of granularity for annotating morphology (as opposed to, for instance, phrase-level or clause-level). We derive answers to these questions from both theoretical arguments and empirical evidence, and conclude with concrete suggestions on steps that may be taken to push UM to the next level of studying computational morphology, in accord with contextualized embeddings and downstream tasks. 

Related:  
    - Annotation of clitics. How should we store the paradigms with clitics (they typically(?) copy those that are without; maybe allow rules to be stored and paradigms for them generated on the fly?)  
    - Annotation of MWEs that require dependencies. Samples in some language require syntactic information, e.g. "legkaja_ADJ promyshlennost_N"  vs. genitive constructions "sindrom_N Aspergera_N". This issue has been [reported here](https://aclanthology.org/K19-1014/).  


2.  Module #2: Sept, TBA
 
Theme: Derivational and Inflectional Morphology:
Leading Speaker: [Khuyagbaatar Batsuren](https://scholar.google.it/citations?user=JsMdM8oAAAAJ&hl=en)
  
    - Incorporation of derivational morphology into UM (derivational paradigms). Khuygaabaatar has extracted derivational paradigms from Wiktionary. [Examples for Finnish](https://drive.google.com/drive/folders/1zRE3GrtkZ6NDTwB8lB2tAxIdbLrnH8Jf), [Examples for Russian](https://drive.google.com/drive/folders/1ZmRyLzwOARy4eI5yvlP89t-pkKmwei-A)

    - Paradigms that incorporate both inflectional and derivational word formation: shall disentangle them? Here is an example from Witold's Polish data: (jeździć, jeżdżenia, V.MSDR;NEUT;ACC;PL;IPFV),(jeździć, jeżdżeniach, V.MSDR;NEUT;ESS;PL;IPFV). It contains two types of transformation: nominalization and declension. 
 
    - Polysynthetic languages. UM has very few polysynthetic languages ([e.g. Adyghe](https://github.com/unimorph/ady)) and provides a small part of their paradigms.

3. Module #3: Sept, TBA
Theme: Discussion of annotation schemas for UniMorph and Universal Dependencies:

    - Annotation consistency. Consistency between UM and UD annotation. Consistency within UM. In 2020 and 2021, all languages added to UniMorph were checked in terms of their annotation consistency & correctness (tags' presence in the schema) using [um-canonicalize tool](https://github.com/unimorph/um-canonicalize). 
  
    - UD <---> UM interface. So far, there exists [UD-to-UM conversion tool](https://github.com/unimorph/ud-compatibility).


4. Module #4: Sept, TBA
Theme: Demonstration session:  WebUI for UniMorph annotation [http://unimorph.ethz.ch/](http://unimorph.ethz.ch/)

5. Module #5: Sept, TBA
Theme:  Incorporation of declension/conjugation classes (?) This will allow us to run more meaningful evaluation/comparison
   
6. Module #5: Oct, TBA
Theme: Administrative session:

    - A pipeline for publication & incorporation of new languages. Unimorph schema/language updates are primarily published on LREC (once in two years). Now we are trying to extend it to SIGMORPHON (as a part of SM Shared Task on morphological reinflection report). One possible option for future: book chapters at langsci press (?) 

    - Linguistic working groups and their management. UniMorph created [a number of working groups](https://docs.google.com/spreadsheets/d/1OA3m_kTnhYMZK762x1SiWy7wMSijxtTfAyDXB9V3wGY/edit#gid=977915123) (primarily based on language families) but they are not actively monitored.

    - UM Schema updates & maintaining its documentation. Ideally some wiki format. At the moment the UM annotation is static and is stored in [the pdf file](https://unimorph.github.io/doc/unimorph-schema.pdf) that isn't updated.

# Participants

TBA
