---
layout: page
permalink: /task2021/
title: Shared Task on Morphological Reinflection 2021
---

In 2021 we will scale up our ``traditional'' SIGMOPHON shared task on morphological reinflection to more languages and different sources of data. 
This year, the task will comprise two parts that both focus on the evaluation of submitted systems' ability to generalize. 

## Part 1: Generalization Across Languages

The development of robust models and technologies that can be applied across the whole variety of nearly 7,000 world languages is a long-standing research goal in NLP. 
Earlier iterations of this shared task have followed a general trend of increasing the number of languages and, specifically, their typological diversity (see Cotterell et al. (2016, 2017,2018), McCarthy et al. (2019)). 
While the data for 2016--2019 shared tasks was primarily derived from Wiktionary (Kirov et al, 2018), the data for the 2020 iteration involved a huge collaborative effort with many linguists involved in data preparation (Vylomova et al, 2020). 
The task organizers digitized, reformatted and converted into the universal schema many less well-documented languages, partially contributing to their preservation.

In 2021, we will continue this annotation effort. We are planning to add several Native American, Papuan, Caucasian, Austronesian, Australian, Dravidian, Turkic, Indo-Aryan, and Semitic languages. The data come from language-specific resources, which we will further transform into the UniMorph format and include into the UniMorph database.
Following the task's popularity in earlier years and current interest in contributing to data annotation, we expect the task will continue being successful and will benefit both NLP and linguistics communities.

[Proceed to Languages/Annotation]({{ site.baseurl }}/shared-task-2021-p1-languages)


## Part 2: Human-Like Generalization (led by Ben Ambridge)

The second objective of the proposed shared task is to study the systems' ability to generalize in the same way as humans would.
We will conduct a ``wug test`` evaluation (Berko, 29158) to compare with human adults (Can the models in the competition predict the results of the adult ``wug test''?)

### ``Wug test'' for adults
Since the ``wug test`` neutralizes, reduces effects of form frequency, animacy, aspect, and various other grammatical features, the form of a word becomes the only basis on which adults can make their inflections. Although earlier ``wug tests'' used orthography, there is evidence from human studies (adults as well as kids) that generalization to novel items is phonologically based (Linzen and Galagher, 2017; Albright and Hayes, 2003; Kerkhoff, 2007). Therefore, in our experiments we mainly rely on phonological representations.
In more orthographically transparent languages, e.g. Polish and Finnish, the orthographic form of a word could be used as a proxy, therefore we also consider running experiments using orthography.

Our literature review suggests that researchers follow one of two approaches to nonword stimuli creation : 1) alteration of initial word stimuli by changing 1-2 characters in each word (as in Balota et al (2007); 2) n-gram or neural word generators (as in Duyck et al., (2004) and Keuleers and Brysbaert (2010)). 
Phonological neighborhoods are important for a ``wug test``, and we will produce nonce words in the way similar to Albright and Hayes (2003)'s approach: build a model that does distance-based phonological clustering of lemma and inflected form pairs into an arbitrary number of ``bins'' (``islands of reliability, a phonological context in which a  particular morphological change works especially well in the existing lexicon'') and then sample a number of items from each bin.


## Organizers
Ekaterina Vylomova, Maria Ryskina,  Salam Khalifa, Xingyuan Zhao, Eleanor Chodroff, Lane Schwartz, Kairit Sirts, Sabrina J. Mielke, Garrett Nicolai, Adina Williams, Francis Tyers, Edoardo M. Ponti,   Tiago Pimentel, Ryan Cotterell, David Yarowsky, Mans Hulden, Ben Ambridge


## Volunteers to Help with Data
Aakanksha Naik, Adam Wiemerslage, Aibek Makazhanov, Alexandra Marley, Alexey Sorokin, Alexis Palmer, Andrew Krizhanovsky, Antonis Anastasopoulos, Arturo Oncevay, Badr Abdullah, Binyam Ephrem, Carmel O'shannessy,Charbel El-Khaissi, Clara Meister, Clara Vania, Claudia Borg, Elena Klyachko, Elizabeth Salesky, Emi Baylor, Grant Aiton, Jennifer White, Jonathan Amith, Karina Mishchenkova, Kate Lindsey, Luke Hartwig, Maneesh Singh, Marc Canby, Natalia Krizhanovsky, Naomi Saphra, Nizar Habash, Omer Goldman, Oyesh Mann Singh, Reut Tsarfaty, Ritesh Kumar, Sai Prasanna, Saliha Muradoglu, Sanjay Kamath, Tihomir Rangelov, William Lane, Yustinus Ghanggo Ate, Yuval Pinter, Matt Coler, Daniel Wilson, Nicholas Howell, Marat M. Yavrumyan, Svetlana Toldova, Samuel Rutunda, Jared Desjardins, Michael Gasser, Aakanksha Naik, Sanjay Kamath, Oyesh Mann Singh, Sushil Awale, Sai Prasanna,  Totok Suhardijanto, Sevilay Bayatlı, Karolina Stanczak

