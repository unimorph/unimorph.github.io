---
layout: default
---

<!-- jQuery -->
<script src="js/jquery.js"></script>

<script type="text/javascript">
  $(document).ready(function(){
    $("#annotated tr:odd").addClass("odd");
    $("#annotated tr:not(.odd)").hide();
    $("#annotated tr:first-child").show();
    $("#annotated tr.odd").click(function(){
      $(this).next("tr").toggle();
      $(this).find(".arrow").toggleClass("up");
    });
  });

  $(document).ready(function(){
    $("#coming tr:odd").addClass("odd");
    $("#coming tr:not(.odd)").hide();
    $("#coming tr:first-child").show();
    $("#coming tr.odd").click(function(){
      $(this).next("tr").toggle();
      $(this).find(".arrow").toggleClass("up");
    });
  });
</script>

<!-- Custom CSS UniMorph CSS -->
<link rel="stylesheet" type="text/css" href="css/style.css"/>
<link rel="stylesheet" href="css/bib-publication-list.css"/>

# UniMorph

The Universal Morphology (UniMorph) project is a collaborative effort to improve how NLP handles complex morphology in the world's languages.
The goal of UniMorph is to annotate morphological data in a universal schema that allows an inflected word from any language to be defined by its lexical meaning, typically carried by the lemma, and by a rendering of its inflectional form in terms of a bundle of morphological features from our schema.
The specification of the schema is described [here]({{ site.baseurl }}/schema) and in [Sylak-Glassman (2016)]({{ site.baseurl }}/doc/unimorph-schema.pdf).

## UniMorph Events

- [CoNLL–SIGMORPHON 2018 Shared Task](https://sigmorphon.github.io/sharedtasks/2018/)
- [CoNLL–SIGMORPHON 2017 Shared Task](https://sigmorphon.github.io/sharedtasks/2017/)
- [SIGMORPHON 2016 Shared Task](https://sigmorphon.github.io/sharedtasks/2016/)

## Annotated Languages

The following {{ site.data.languages | size }} languages have been annotated according to the UniMorph schema. Missing parts of speech will be filled in soon.

{% assign sorted_langs = site.data.languages | sort:"name" %}

<div class="table-wrapper" markdown="block" style="overflow-x: scroll">

  <table class="table table-responsive" id="annotated">
    <tr>
      <th></th>
      <th>Language</th>
      <th>ISO 639-3</th>
      <th>Forms</th>
      <th>Paradigms</th>
      <th>Nouns</th>
      <th>Verbs</th>
      <th>Adjectives</th>
      <th>Source</th>
      <th>License</th>
      <th></th>
    </tr>

    {% for language in sorted_langs %}
    <tr>
    <td>{% if language.flag %}<span class="flagspan"><img class="flag"     src="{{ site.baseurl }}/images/flags/{{ language.flag }}"/></span>{% endif %}</td>
    <td>{{ language.name }}</td>
    <td>{{ language.iso }}</td>
    <td>{{ language.forms }}</td>
    <td>{{ language.paradigms }}</td>
    <td>{% if language.nouns %}&#x2714;{% endif %}</td>
    <td>{% if language.verbs %}&#x2714;{% endif %}</td>
    <td>{% if language.adjectives %}&#x2714;{% endif %}</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
    </tr>
    <tr>
    <td colspan="11">
    <div class="detail-box">
    <div class="mylist">
    <ul class="unstyled">
    <li>
    <span class="detail1">
    <b>Download Data:</b>
    </span>
    <a href="https://github.com/unimorph/{{ language.iso }}">repo</a>
    </li>
    <li><span class="detail1"><b>Report Errors:</b></span> <a href="https://github.com/unimorph/{{ language.iso }}/issues">issues</a></li>
    </ul>
    </div>
    <div class="mylist">
    <ul class="unstyled">
    <li><span class="detail4"><b>2016 Shared Task Splits:</b></span> {% if language.splits.sixteen %}<a href=" https://github.com/ryancotterell/sigmorphon2016/">yes</a>{% else %}no{% endif %}</li>
    <li><span class="detail4"><b>2017 Shared Task Splits:</b></span> {% if language.splits.seventeen %}<a href="https://github.com/sigmorphon/conll2017">yes</a>{% else %}no{% endif %}</li>  
    </ul>
    </div>
    <div class="mylist">
    <ul class="unstyled">
    <li><span class="detail2"><b>Typology:</b></span> {{ language.typology }}</li>
    <li><span class="detail2"><b>Templatic:</b></span> {{ language.templatic }}</li>
    </ul>
    </div>
    <div class="mylist">
    <ul class="unstyled">
    <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/{{ language.name }}_language">wikipedia</a></li>
    <li><span class="detail3"><b>Type:</b></span> {{ language.type }}</li>  
    </ul>
    </div>
    </div>
    </td>
    </tr>
    {% endfor %}

  </table>

</div>

## Coming Attractions!

The following languages are in the process of being annotated according to the UniMorph specification.

{% assign sorted_coming = site.data.coming | sort:"name" %}

<div class="table-wrapper" markdown="block" style="overflow-x: scroll">

  <table class="table table-responsive" id="coming">
    <tr>
      <th></th>
      <th>Language</th>
      <th>ISO 639-3</th>
      <th>Forms</th>
      <th>Paradigms</th>
      <th>Nouns</th>
      <th>Verbs</th>
      <th>Adjectives</th>
      <th>Source</th>
      <th>License</th>
      <th></th>
    </tr>


    <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/BO.svg"/></span></td>
    <td>!Xóõ</td>
    <td>nmn</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nmn">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nmn/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/!Xóõ_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>

  {% for language in sorted_coming %}
  <tr>
    <td>{% if language.flag %}<span class="flagspan"><img class="flag"     src="{{ site.baseurl }}/images/flags/{{ language.flag }}"/></span>    {% endif %}</td>
    <td>{{ language.name }}</td>
    <td>{{ language.iso }}</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span> {{ language.typology }}</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Templatic:</b></span> {{ language.templatic }}</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/{{ language.name }}_language">wikipedia</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Type:</b></span> {{ language.type }}</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>

  {% endfor %}

  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SA.svg"/></span></td>
    <td>Afrikaans</td>
    <td>afr</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/afr">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/afr/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span>{{ language.typology }}</li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/{{ language.name }}_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>{{ language.type }}</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/GR.svg"/></span></td>
    <td>Ancient Greek</td>
    <td>grc</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/grc">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/grc/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ancient Greek_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/AR.svg"/></span></td>
    <td>Aragonese</td>
    <td>arg</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/arg">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/arg/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Aragonese_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SY.svg"/></span></td>
    <td>Aramaic</td>
    <td>arc</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/arc">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/arc/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>yes</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Aramaic_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/BY.svg"/></span></td>
    <td>Buriat</td>
    <td>bua</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bua">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bua/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Buriat_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CE.svg"/></span></td>
    <td>Chechen</td>
    <td>che</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/che">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/che/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Chechen_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/MX.svg"/></span></td>
    <td>Classical Nahuatl</td>
    <td>nci</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nci">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nci/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Classical Nahuatl_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CO.svg"/></span></td>
    <td>Corsican</td>
    <td>cos</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/cos">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/cos/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Corsican_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/EG.svg"/></span></td>
    <td>Egyptian Arabic</td>
    <td>arz</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/arz">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/arz/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>yes</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Egyptian Arabic_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/GG.svg"/></span></td>
    <td>Gagauz</td>
    <td>gag</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gag">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gag/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Gagauz_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/NI.svg"/></span></td>
    <td>Hausa</td>
    <td>hau</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hau">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hau/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>yes</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Hausa_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/TR.svg"/></span></td>
    <td>Hittite</td>
    <td>hit</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hit">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hit/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Hittite_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/NN.svg"/></span></td>
    <td>Inuktitut</td>
    <td>iku</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/iku">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/iku/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Inuktitut_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/IS.svg"/></span></td>
    <td>Istriot</td>
    <td>ist</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ist">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ist/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Istriot_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/JP.svg"/></span></td>
    <td>Japanese</td>
    <td>jpn</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/jpn">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/jpn/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Japanese_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/JE.svg"/></span></td>
    <td>Jèrriais</td>
    <td>nrf</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nrf">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nrf/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Jèrriais_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/GL.svg"/></span></td>
    <td>Kalaallisut</td>
    <td>kal</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kal">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kal/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kalaallisut_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/KG.svg"/></span></td>
    <td>Kirghiz</td>
    <td>kir</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kir">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kir/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kirghiz_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/KO.svg"/></span></td>
    <td>Korean</td>
    <td>kor</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kor">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kor/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Korean_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/IL.svg"/></span></td>
    <td>Ladino</td>
    <td>lad</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lad">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lad/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ladino_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/LI.svg"/></span></td>
    <td>Limburgan</td>
    <td>lim</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lim">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lim/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Limburgan_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/LU.svg"/></span></td>
    <td>Luxembourgish</td>
    <td>ltz</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ltz">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ltz/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Luxembourgish_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/AO.svg"/></span></td>
    <td>Macedo-Romanian</td>
    <td>rup</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/rup">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/rup/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Macedo-Romanian_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/MD.svg"/></span></td>
    <td>Malagasy</td>
    <td>mlg</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/mlg">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/mlg/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Malagasy_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/MY.svg"/></span></td>
    <td>Malay</td>
    <td>msa</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/msa">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/msa/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Malay_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/IN.svg"/></span></td>
    <td>Malayalam</td>
    <td>mal</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/mal">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/mal/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Malayalam_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CN.svg"/></span></td>
    <td>Mandarin Chinese</td>
    <td>cmn</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/cmn">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/cmn/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">isolating</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Mandarin Chinese_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/NL.svg"/></span></td>
    <td>Middle Dutch</td>
    <td>dum</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/dum">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/dum/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Middle Dutch_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/MI.svg"/></span></td>
    <td>Mirandese</td>
    <td>mwl</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/mwl">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/mwl/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Mirandese_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/NMX.svg"/></span></td>
    <td>Northern Tiwa</td>
    <td>twf</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/twf">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/twf/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Northern Tiwa_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CA.svg"/></span></td>
    <td>Ojibwa</td>
    <td>oji</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/oji">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/oji/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ojibwa_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/NL.svg"/></span></td>
    <td>Old Dutch</td>
    <td>odt</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/odt">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/odt/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Dutch_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/RA.svg"/></span></td>
    <td>Old Norse</td>
    <td>non</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/non">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/non/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Norse_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/PT.svg"/></span></td>
    <td>Old Portuguese</td>
    <td>pto</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/pto">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/pto/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Portuguese_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/PR.svg"/></span></td>
    <td>Old Provençal</td>
    <td>pro</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/pro">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/pro/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Provençal_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/IN.svg"/></span></td>
    <td>Panjabi</td>
    <td>pan</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/pan">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/pan/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Panjabi_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CH.svg"/></span></td>
    <td>Romansh</td>
    <td>roh</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/roh">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/roh/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Romansh_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/RM.svg"/></span></td>
    <td>Romany</td>
    <td>rom</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/rom">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/rom/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Romany_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SD.svg"/></span></td>
    <td>Sardinian</td>
    <td>srd</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/srd">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/srd/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Sardinian_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SF.svg"/></span></td>
    <td>Saterfriesisch</td>
    <td>stq</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/stq">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/stq/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Saterfriesisch_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/RS.svg"/></span></td>
    <td>Serbian</td>
    <td>srp</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/srp">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/srp/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Serbian_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SC.svg"/></span></td>
    <td>Sicilian</td>
    <td>scn</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/scn">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/scn/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Sicilian_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SAMI.svg"/></span></td>
    <td>Skolt Sami</td>
    <td>sms</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/sms">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/sms/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Skolt Sami_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CH.svg"/></span></td>
    <td>Swiss German</td>
    <td>gsw</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gsw">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gsw/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Swiss German_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/SA.svg"/></span></td>
    <td>Tswana</td>
    <td>tsn</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tsn">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tsn/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Tswana_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/CN.svg"/></span></td>
    <td>Uighur</td>
    <td>uig</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/uig">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/uig/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Uighur_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/VR.svg"/></span></td>
    <td>Võro</td>
    <td>vro</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/vro">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/vro/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Võro_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/WL.svg"/></span></td>
    <td>Walloon</td>
    <td>wln</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/wln">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/wln/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Walloon_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/WI.svg"/></span></td>
    <td>Wymysorys</td>
    <td>wym</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/wym">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/wym/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Wymysorys_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>


  <tr>
    <td><span class="flagspan"><img class="flag" src="{{ site.baseurl }}/images/flags/MN.svg"/></span></td>
    <td>Yucatec Maya</td>
    <td>yua</td>
    <td>0</td>
    <td>0</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td>&#x2714;</td>
    <td><span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span></td>
    <td><span><img class="check" src="{{ site.baseurl }}/images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/yua">repo</a></li>
            <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/yua/issues">issues</a></li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
            <li><span class="detail4"><b>2017 Shared Task Splits:</b></span>no</li>  
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Agglutinative_language">agglutinative</a></li>
            <li><span class="detail2"><b>Templatic:</b></span>no</li>
          </ul>
        </div>
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Yucatec Maya_language">wikipedia</a></li>
            <li><span class="detail3"><b>Type:</b></span>living</li>  
          </ul>
        </div>
      </div>
    </td>
  </tr>
  
</table>

</div>

<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>



