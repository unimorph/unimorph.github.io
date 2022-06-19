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

Plus, we're now available in a [Python package](https://pypi.org/project/unimorph/)! `pip install unimorph`

## UniMorph Events
- [SIGMORPHON 2022 Shared Task](https://github.com/sigmorphon/2022InflectionST)
- [SIGMORPHON 2021 Shared Task](https://github.com/sigmorphon/2021Task0)
- [SIGMORPHON 2020 Shared Task](https://sigmorphon.github.io/sharedtasks/2020/)
- [SIGMORPHON 2019 Shared Task](https://sigmorphon.github.io/sharedtasks/2019/)
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
      <th style="text-align:right">Forms</th>
      <th style="text-align:right">Paradigms</th>
      <th style="text-align:right">Nouns</th>
      <th style="text-align:right">Verbs</th>
      <th style="text-align:right">Adjectives</th>
      <th style="text-align:right">Source</th>
      <th style="text-align:right">License</th>
      <th></th>
    </tr>

    {% for language in sorted_langs %}
    <tr>
    <td>{% if language.flag %}<span class="flagspan"><img class="flag"     src="{{ site.baseurl }}/images/flags/{{ language.flag }}"/></span>{% endif %}</td>
    <td>{{ language.name }}</td>
    <td style="font-family: monospace">{{ language.iso }}</td>
    <td style="text-align:right">{{ language.forms }}</td>
    <td style="text-align:right">{{ language.paradigms }}</td>
    <td style="text-align:right">{% if language.nouns %}&#x2714;{% endif %}</td>
    <td style="text-align:right">{% if language.verbs %}&#x2714;{% endif %}</td>
    <td style="text-align:right">{% if language.adjectives %}&#x2714;{% endif %}</td>
    <td>{% case language.source %}
	{% when 'ling' %}
	 <span><a rel="source" href="">&#8466;</a></span>
	{% when 'surrey' %}
	 <a rel="source" href="https://oto-manguean.surrey.ac.uk/">Surrey</a>
	{% when 'vepkar' %}
	<a rel="source" href="http://dictorpus.krc.karelia.ru/">VepKar</a>	
       {% when nil %}
	<span><img class="source" src="{{ site.baseurl }}/images/wiki.png"/></span>
	{% endcase %}
      </td>
    <td style="text-align:right">{% case language.license %}
      {% when 'unknown' %}
      	–
      {% when 'lgpllr' %}
       <a rel="license" href="https://spdx.org/licenses/LGPLLR.html">LGPLLR</a>
      {% when nil %}
       <a rel="license" href="http://creativecommons.org/licenses/by-sa/3.0/">
       	<img class="check" alt="Creative Commons License"  src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" />
       </a>
    {% endcase %}</td>
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

<!-- ## Coming Attractions!

The following languages are in the process of being annotated according to the UniMorph specification.

{% assign sorted_coming = site.data.coming | sort:"name" %}

<div class="table-wrapper" markdown="block" style="overflow-x: scroll">

  <table class="table table-responsive" id="coming">
    <tr>
      <th></th>
      <th>Language</th>
      <th>ISO 639-3</th>
      <th></th>
    </tr>

  {% for language in sorted_coming %}
  <tr>
    <td>{% if language.flag %}<span class="flagspan"><img class="flag"     src="{{ site.baseurl }}/images/flags/{{ language.flag }}"/></span>    {% endif %}</td>
    <td>{{ language.name }}</td>
    <td style="font-family: monospace">{{ language.iso }}</td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
        <div class="mylist">
          <ul class="unstyled">
            <li><span class="detail2"><b>Typology:</b></span> {{ language.typology }}</li>
            <li><span class="detail2"><b>Templatic:</b></span> {{ language.templatic }}</li>
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
-->
<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>



