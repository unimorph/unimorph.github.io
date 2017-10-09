---
layout: page
permalink: /Schema/
title: Schema
---

The UniMorph schema comprises 23 dimensions of meaning and over 212 features. 
The dimensions of meaning are morphological categories, such as person, number, tense and aspect.
Each represents a coherent semantic space within inflectional morphology.
They include:
Aktionsart,
animacy,
aspect,
case,
comparison,
definiteness,
deixis,
evidentiality,
finiteness,
gender,
information structure,
interrogativity,
mood,
number,
part of speech,
person,
polarity,
politeness,
switch-reference,
tense,
valency,
and voice.
These dimensions contain varying numbers of features, from just 2 for finiteness to 39 for case.
Features represent the finest-grained distinctions in meaning that are possible within a given dimension.

Each inflected word in any given language is represented by its
lemma (as might appear in a dictionary, for example) and a
bundle of UniMorph features.

<figure id="spanish-russian">
    <center>
        ![Spanish and Russian Forms]({{ site.basename }}/images/spanish-russian-paradigm.svg)
    </center>
    <center>
        <figcaption>
            <small>
                Figure 1: Partial Spanish and Russian paradigms. Inflected forms are marked with the UniMorph features.
            </small>
        </figcaption>
    </center>
</figure>

For example, the Spanish word *hablaste* can be represented as the lemma *hablar* plus the bundle [`FIN;IND;PFV;PST;2;SG;INFM`]. More forms are listed in [Figure 1](#spanish-russian). The abbreviations are as follows:

- `FIN` indicates a finite verb.
- `IND` indicates the indicative mood.
- `PFV` indicates the perfective aspect.
- `PST` indicates the past tense.
- `2` indicates the second person.
- `SG` indicates the singular number.
- `INFM` indicates the informal register.

Note that this yields a mapping, which associates the entire inflected word with its meaning, without any indication of the morpheme divisions (segments) within *hablaste* nor how the UniMorph schema features are distributed among those divisions. In other words, this is a paradigmatic treatment of morphology in the [word-based](https://en.wikipedia.org/wiki/Morphology_linguistics#Word-based_morphology) tradition. ([Aronoff 1976](https://mitpress.mit.edu/books/word-formation-generative-grammar)). 

The Russian word *сказал* has a very similar representation as the lemma *сказать* plus the bundle [`FIN;IND;PFV;PST;2;SG;INFM;MASC`], differing from *hablaste* only in the fact that it additionally marks the gender feature.
We remark that the Russian past tense is a case of [syncretism](https://en.wikipedia.org/wiki/Syncretism_linguistics): one form has many possible bundles—a context is required to disambiguate. See [Figure 1](#spanish-russian) for a comparison between Spanish and Russian.
Note that for both languages, the representation differs only by what distinctions in meaning the language marks.
Because the meaning of features does not differ across languages, the featural representation of words from different languages is directly comparable.
This is an essential feature of the UniMorph that allows inflectional material to be faithfully translated and enhances
comparability across languages.

### Comparison to Universal Dependencies features

Discussion on this topic may be found on the [Universal Dependencies website](http://universaldependencies.org/v2/features.html). A conversion script between the two is coming soon.

### Dimensions of meaning and their features

Coming soon! Until then, refer to [Sylak-Glassman, 2016]({{ site.baseurl }}/doc/unimorph-schema.pdf). The document's appendices also provide a complete list of the UniMorph features and their categories.