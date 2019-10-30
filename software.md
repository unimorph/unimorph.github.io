---
layout: page
permalink: /software/
title: Software
---


### GitHub

All of our datasets and source are available for collaboration and use in our [GitHub repositories](https://github.com/unimorph).

You can find:

- A [Python package](https://github.com/unimorph/unimorph) for downloading and searching morphological paradigms
- [Pre-trained morphological analyzers in several languages](https://github.com/unimorph/analyzers); for pre-trained models in 1200 languages see [Nicolai and Yarowsky (2019)](https://www.aclweb.org/anthology/P19-1172/).
- [A tool for reannotating Universal Dependencies corpora into the UniMorph morphosyntactic schema](https://github.com/unimorph/ud-compatibility), optimized for harmony between UD and UniMorph and hand-engineered for a number of languages. If you use it, please cite [McCarthy et al. (2018)](https://www.aclweb.org/anthology/W18-6011/).


### Dataset creation tools

The majority of our data is extracted from [Wiktionary](https://www.wiktionary.org). We provide tools for such extraction [here](https://github.com/unimorph/wiktionary-tools). Revisions and pull requests are welcome. 

<!--

### Pre-trained Tools

We provide a number of pre-trained models for morphological analysis, i.e., mapping (possibly unseen) forms to UniMorph tags, [here](https://github.com/unimorph/analyzers). 

The UniMorph project will also release pre-trained tools for morphological generation, i.e., mapping tags (and a lemma) to forms. Please stay tuned.

### Compatibility with Universal Dependencies

The [Universal Dependencies project](http://universaldependencies.org) also annotates morphosyntactic features of language. Their resources are token-level (annotating running text), unlike our type-level tables. To inter-operate between these resources, we recommend using [our UD to UniMorph converter](https://github.com/unimorph/ud-compatibility). It is designed to maximize harmony between UD and UniMorph annotations, and it has been hand-engineered for a number of languages. If you use it, please [cite it](https://www.aclweb.org/anthology/papers/W/W18/W18-6011.bib).
-->

### Additional tools

The following software artifacts have been released for use on data annotated according to the UniMorph schema. Please let us know if you would like your software listed on this part of the website.

- [Aharoni and Goldberg (2017)](https://github.com/roeeaharoni/morphological-reinflection)
- [CoNLL–SIGMORPHON 2017 baseline system](https://github.com/sigmorphon/conll2017/tree/master/baseline)
- [CoNLL–SIGMORPHON 2018 baseline system](https://github.com/sigmorphon/conll2018)
