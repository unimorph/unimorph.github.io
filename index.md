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

  <p>
  The Universal Morphology (UniMorph) project is a collaborative
  effort to improve how NLP handles complex morphology in the world's
  languages. The goal of UniMorph is to annotate morphological data in
  a universal schema that allows an inflected word from any language
  to be defined by its lexical meaning, typically carried by the
  lemma, and by a rendering of its inflectional form in terms of a
  bundle of morphological features from our schema. The specification
  of the schema is described <a href="{{ site.baseurl }}/schema">here</a> and
  in <a href="{{ site.baseurl }}/doc/unimorph-schema.pdf">Sylak-Glassman (2016)</a>.
  <p>

  <h3>UniMorph Events</h3>
      <ul>

  <li><a href="http://ryancotterell.github.io/sigmorphon2016/">SIGMORPHON
  2016 Shared Task</a></li>
  <li><a href="https://sites.google.com/view/conll-sigmorphon2017/">CoNLL-SIGMORPHON 2017 Shared Task</a></li>
   </ul>
<h3>Annotated Languages</h3>
<p>The following 51 languages have been annotated according to the UniMorph schema. Missing parts of speech will be filled in soon. </p>
<table id="annotated">
  <tr>
    <th></th>
    <th>Language</th>
    <th>ISO-639-3</th>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/AL.svg"/></span></td>
    <td>Albanian</td>
    <td>sqi</td>
    <td>33483</td>
    <td>589</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/sqi">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/sqi/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Albanian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SA-AL.svg"/></span></td>
    <td>Arabic</td>
    <td>ara</td>
    <td>140003</td>
    <td>4134</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ara">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ara/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Arabic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/AM.svg"/></span></td>
    <td>Armenian</td>
    <td>hye</td>
    <td>338461</td>
    <td>7033</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hye">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hye/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Armenian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ES-PV.svg"/></span></td>
    <td>Basque</td>
    <td>eus</td>
    <td>11889</td>
    <td>26</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/eus">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/eus/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Basque_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BD.svg"/></span></td>
    <td>Bengali</td>
    <td>ben</td>
    <td>4443</td>
    <td>136</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ben">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ben/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Bengali_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BG.svg"/></span></td>
    <td>Bulgarian</td>
    <td>bul</td>
    <td>55730</td>
    <td>2468</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bul">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bul/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Bulgarian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ES-CT.svg"/></span></td>
    <td>Catalan</td>
    <td>cat</td>
    <td>81576</td>
    <td>1547</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/cat">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/cat/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Catalan_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IQ-KRD.svg"/></span></td>
    <td>Central Kurdish</td>
    <td>ckb</td>
    <td>22990</td>
    <td>274</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ckb">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ckb/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Central Kurdish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CZ.svg"/></span></td>
    <td>Czech</td>
    <td>ces</td>
    <td>134527</td>
    <td>5125</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ces">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ces/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Czech_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/DK.svg"/></span></td>
    <td>Danish</td>
    <td>dan</td>
    <td>25503</td>
    <td>3193</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/dan">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/dan/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Danish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NL.svg"/></span></td>
    <td>Dutch</td>
    <td>nld</td>
    <td>55467</td>
    <td>4993</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nld">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nld/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Dutch_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/EN.svg"/></span></td>
    <td>English</td>
    <td>eng</td>
    <td>115523</td>
    <td>22765</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/eng">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/eng/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/English_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/EE.svg"/></span></td>
    <td>Estonian</td>
    <td>est</td>
    <td>38215</td>
    <td>886</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/est">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/est/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Estonian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/FO.svg"/></span></td>
    <td>Faroese</td>
    <td>fao</td>
    <td>45474</td>
    <td>3077</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fao">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fao/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Faroese_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/FI.svg"/></span></td>
    <td>Finnish</td>
    <td>fin</td>
    <td>2490377</td>
    <td>57642</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fin">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fin/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Finnish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/FR.svg"/></span></td>
    <td>French</td>
    <td>fra</td>
    <td>367732</td>
    <td>7535</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fra">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fra/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/French_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/GE.svg"/></span></td>
    <td>Georgian</td>
    <td>kat</td>
    <td>74412</td>
    <td>3782</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kat">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kat/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Georgian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/DE.svg"/></span></td>
    <td>German</td>
    <td>deu</td>
    <td>179339</td>
    <td>15060</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/deu">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/deu/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/German_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/HA.png"/></span></td>
    <td>Haida</td>
    <td>hai</td>
    <td>7040</td>
    <td>41</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hai">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hai/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Haida_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IL.svg"/></span></td>
    <td>Hebrew</td>
    <td>heb</td>
    <td>13818</td>
    <td>510</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/heb">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/heb/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Hebrew_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Hindi</td>
    <td>hin</td>
    <td>54438</td>
    <td>258</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hin">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hin/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Hindi_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/HU.svg"/></span></td>
    <td>Hungarian</td>
    <td>hun</td>
    <td>490394</td>
    <td>13989</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/hun">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/hun/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Hungarian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IC.svg"/></span></td>
    <td>Icelandic</td>
    <td>isl</td>
    <td>76915</td>
    <td>4775</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/isl">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/isl/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Icelandic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ID.svg"/></span></td>
    <td>Irish</td>
    <td>gle</td>
    <td>107298</td>
    <td>7464</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gle">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gle/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Irish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IT.svg"/></span></td>
    <td>Italian</td>
    <td>ita</td>
    <td>509574</td>
    <td>10009</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ita">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ita/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Italian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NP.svg"/></span></td>
    <td>Khaling</td>
    <td>klr</td>
    <td>156097</td>
    <td>591</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/klr">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/klr/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Khaling_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/VA.svg"/></span></td>
    <td>Latin</td>
    <td>lat</td>
    <td>509182</td>
    <td>17214</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lat">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lat/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Latin_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/LA.svg"/></span></td>
    <td>Latvian</td>
    <td>lav</td>
    <td>136998</td>
    <td>7548</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lav">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lav/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Latvian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/LT.svg"/></span></td>
    <td>Lithuanian</td>
    <td>lit</td>
    <td>34130</td>
    <td>1458</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lit">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lit/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Lithuanian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SB.svg"/></span></td>
    <td>Lower Sorbian</td>
    <td>dsb</td>
    <td>20121</td>
    <td>994</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/dsb">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/dsb/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Lower Sorbian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/MK.svg"/></span></td>
    <td>Macedonian</td>
    <td>mkd</td>
    <td>168057</td>
    <td>10313</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/mkd">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/mkd/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Macedonian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NV.svg"/></span></td>
    <td>Navajo</td>
    <td>nav</td>
    <td>12354</td>
    <td>674</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nav">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nav/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Navajo_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IQ-KRD.svg"/></span></td>
    <td>Northern Kurdish</td>
    <td>kmr</td>
    <td>216370</td>
    <td>15083</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kmr">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kmr/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Northern Kurdish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SAMI.svg"/></span></td>
    <td>Northern Sami</td>
    <td>sme</td>
    <td>62677</td>
    <td>2103</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/sme">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/sme/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Northern Sami_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NO.svg"/></span></td>
    <td>Norwegian Bokmål</td>
    <td>nob</td>
    <td>19238</td>
    <td>5527</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nob">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nob/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Norwegian Bokmål_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NO.svg"/></span></td>
    <td>Norwegian Nynorsk</td>
    <td>nno</td>
    <td>15319</td>
    <td>4689</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nno">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nno/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Norwegian Nynorsk_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IR.svg"/></span></td>
    <td>Persian</td>
    <td>fas</td>
    <td>37128</td>
    <td>273</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fas">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fas/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Persian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/PL.svg"/></span></td>
    <td>Polish</td>
    <td>pol</td>
    <td>201024</td>
    <td>10185</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/pol">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/pol/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Polish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/PT.svg"/></span></td>
    <td>Portuguese</td>
    <td>por</td>
    <td>303996</td>
    <td>4001</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/por">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/por/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Portuguese_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/QU.svg"/></span></td>
    <td>Quechua</td>
    <td>que</td>
    <td>180004</td>
    <td>1006</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/que">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/que/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Quechua_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/RO.svg"/></span></td>
    <td>Romanian</td>
    <td>ron</td>
    <td>80266</td>
    <td>4405</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ron">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ron/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Romanian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/RU.svg"/></span></td>
    <td>Russian</td>
    <td>rus</td>
    <td>473481</td>
    <td>28068</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/rus">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/rus/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Russian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ST.svg"/></span></td>
    <td>Scottish Gaelic</td>
    <td>gla</td>
    <td>781</td>
    <td>73</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gla">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gla/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Scottish Gaelic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SK.svg"/></span></td>
    <td>Slovak</td>
    <td>slk</td>
    <td>14796</td>
    <td>1046</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/slk">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/slk/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Slovak_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SI.svg"/></span></td>
    <td>Slovenian</td>
    <td>slv</td>
    <td>60110</td>
    <td>2535</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/slv">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/slv/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Slovenian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ES.svg"/></span></td>
    <td>Spanish</td>
    <td>spa</td>
    <td>382955</td>
    <td>5460</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/spa">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/spa/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Spanish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SE.svg"/></span></td>
    <td>Swedish</td>
    <td>swe</td>
    <td>78411</td>
    <td>10553</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/swe">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/swe/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Swedish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/TR.svg"/></span></td>
    <td>Turkish</td>
    <td>tur</td>
    <td>275460</td>
    <td>3579</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tur">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tur/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Turkish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/UK.svg"/></span></td>
    <td>Ukrainian</td>
    <td>ukr</td>
    <td>20904</td>
    <td>1493</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ukr">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ukr/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ukrainian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/PK.svg"/></span></td>
    <td>Urdu</td>
    <td>urd</td>
    <td>12572</td>
    <td>182</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/urd">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/urd/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Urdu_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/WA.svg"/></span></td>
    <td>Welsh</td>
    <td>cym</td>
    <td>10641</td>
    <td>183</td>
    <td></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/cym">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/cym/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span>no</li>
      <li><span class="detail4"><b>2017 Shared Task Splits:</b></span><a href="http://www.sigmorphon.org/conll2017">yes</a></li>  
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Welsh_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>

  
</table>

<h3>Coming Attractions!</h3>
<p>The following languages are in the process of being annotated according to the UniMorph specification.
</p>
<table id="coming">
  <tr>
    <th></th>
    <th>Language</th>
    <th>ISO-639-3</th>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/BO.svg"/></span></td>
    <td>!Xóõ</td>
    <td>nmn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CI.svg"/></span></td>
    <td>Adyghe</td>
    <td>ady</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ady">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ady/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Adyghe_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SA.svg"/></span></td>
    <td>Afrikaans</td>
    <td>afr</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
      <li><span class="detail2"><b>Typology:</b></span><a href="https://en.wikipedia.org/wiki/Fusional_language">fusional</a></li>
      <li><span class="detail2"><b>Templatic:</b></span>no</li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Afrikaans_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/GR.svg"/></span></td>
    <td>Ancient Greek</td>
    <td>grc</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/AR.svg"/></span></td>
    <td>Aragonese</td>
    <td>arg</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/SY.svg"/></span></td>
    <td>Aramaic</td>
    <td>arc</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/AS.svg"/></span></td>
    <td>Asturian</td>
    <td>ast</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ast">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ast/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Asturian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/AZ.svg"/></span></td>
    <td>Azerbaijani</td>
    <td>aze</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/aze">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/aze/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Azerbaijani_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BA.svg"/></span></td>
    <td>Bashkir</td>
    <td>bak</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bak">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bak/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Bashkir_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BE.svg"/></span></td>
    <td>Belarusian</td>
    <td>bel</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bel">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bel/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Belarusian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BR.svg"/></span></td>
    <td>Breton</td>
    <td>bre</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bre">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bre/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Breton_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/BY.svg"/></span></td>
    <td>Buriat</td>
    <td>bua</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/CE.svg"/></span></td>
    <td>Chechen</td>
    <td>che</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/MORAVA.svg"/></span></td>
    <td>Church Slavic</td>
    <td>chu</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/chu">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/chu/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Church Slavic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/AM.svg"/></span></td>
    <td>Classical Armenian</td>
    <td>xcl</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/xcl">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/xcl/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Classical Armenian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/MX.svg"/></span></td>
    <td>Classical Nahuatl</td>
    <td>nci</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/SY.svg"/></span></td>
    <td>Classical Syriac</td>
    <td>syc</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/syc">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/syc/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Classical Syriac_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CW.svg"/></span></td>
    <td>Cornish</td>
    <td>cor</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/cor">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/cor/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Cornish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CO.svg"/></span></td>
    <td>Corsican</td>
    <td>cos</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/TA.svg"/></span></td>
    <td>Crimean Tatar</td>
    <td>crh</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/crh">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/crh/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Crimean Tatar_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/EG.svg"/></span></td>
    <td>Egyptian Arabic</td>
    <td>arz</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/FL.svg"/></span></td>
    <td>Friulian</td>
    <td>fur</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fur">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fur/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Friulian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/GG.svg"/></span></td>
    <td>Gagauz</td>
    <td>gag</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/GC.svg"/></span></td>
    <td>Galician</td>
    <td>glg</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/glg">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/glg/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Galician_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/GO.svg"/></span></td>
    <td>Gothic</td>
    <td>got</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/got">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/got/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Gothic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NI.svg"/></span></td>
    <td>Hausa</td>
    <td>hau</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/TR.svg"/></span></td>
    <td>Hittite</td>
    <td>hit</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IG.svg"/></span></td>
    <td>Ingrian</td>
    <td>izh</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/izh">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/izh/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ingrian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NN.svg"/></span></td>
    <td>Inuktitut</td>
    <td>iku</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IS.svg"/></span></td>
    <td>Istriot</td>
    <td>ist</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/JP.svg"/></span></td>
    <td>Japanese</td>
    <td>jpn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/JE.svg"/></span></td>
    <td>Jèrriais</td>
    <td>nrf</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/KA.svg"/></span></td>
    <td>Kabardian</td>
    <td>kbd</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kbd">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kbd/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kabardian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/GL.svg"/></span></td>
    <td>Kalaallisut</td>
    <td>kal</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Kannada</td>
    <td>kan</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kan">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kan/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kannada_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/KL.svg"/></span></td>
    <td>Karelian</td>
    <td>krl</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/krl">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/krl/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Karelian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/KB.svg"/></span></td>
    <td>Kashubian</td>
    <td>csb</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/csb">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/csb/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kashubian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/KZ.svg"/></span></td>
    <td>Kazakh</td>
    <td>kaz</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kaz">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kaz/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Kazakh_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/KH.svg"/></span></td>
    <td>Khakas</td>
    <td>kjh</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/kjh">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/kjh/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Khakas_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/KG.svg"/></span></td>
    <td>Kirghiz</td>
    <td>kir</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/KO.svg"/></span></td>
    <td>Korean</td>
    <td>kor</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/LD.svg"/></span></td>
    <td>Ladin</td>
    <td>lld</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/lld">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/lld/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Ladin_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IL.svg"/></span></td>
    <td>Ladino</td>
    <td>lad</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/LI.svg"/></span></td>
    <td>Limburgan</td>
    <td>lim</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/LV.svg"/></span></td>
    <td>Liv</td>
    <td>liv</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/liv">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/liv/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Liv_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/DE.svg"/></span></td>
    <td>Low German</td>
    <td>nds</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nds">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nds/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Low German_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/LU.svg"/></span></td>
    <td>Luxembourgish</td>
    <td>ltz</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/AO.svg"/></span></td>
    <td>Macedo-Romanian</td>
    <td>rup</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/MD.svg"/></span></td>
    <td>Malagasy</td>
    <td>mlg</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/MY.svg"/></span></td>
    <td>Malay</td>
    <td>msa</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Malayalam</td>
    <td>mal</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/MT.svg"/></span></td>
    <td>Maltese</td>
    <td>mlt</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/mlt">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/mlt/issues">issues</a></li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail4"><b>2016 Shared Task Splits:</b></span><a href="http://ryancotterell.github.io/sigmorphon2016/">yes</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Maltese_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CN.svg"/></span></td>
    <td>Mandarin Chinese</td>
    <td>cmn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IM.svg"/></span></td>
    <td>Manx</td>
    <td>glv</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/glv">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/glv/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Manx_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/MA.svg"/></span></td>
    <td>Mapudungun</td>
    <td>arn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/arn">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/arn/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Mapudungun_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NL.svg"/></span></td>
    <td>Middle Dutch</td>
    <td>dum</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/FR.svg"/></span></td>
    <td>Middle French</td>
    <td>frm</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/frm">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/frm/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Middle French_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/DE.svg"/></span></td>
    <td>Middle High German</td>
    <td>gmh</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gmh">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gmh/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Middle High German_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/DE.svg"/></span></td>
    <td>Middle Low German</td>
    <td>gml</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/gml">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/gml/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Middle Low German_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/MI.svg"/></span></td>
    <td>Mirandese</td>
    <td>mwl</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/GR.svg"/></span></td>
    <td>Modern Greek</td>
    <td>ell</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ell">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ell/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Modern Greek_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NE.svg"/></span></td>
    <td>Neapolitan</td>
    <td>nap</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/nap">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/nap/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Neapolitan_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NF.svg"/></span></td>
    <td>Northern Frisian</td>
    <td>frr</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/frr">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/frr/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Northern Frisian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/NMX.svg"/></span></td>
    <td>Northern Tiwa</td>
    <td>twf</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/OC.svg"/></span></td>
    <td>Occitan</td>
    <td>oci</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/oci">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/oci/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Occitan_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CA.svg"/></span></td>
    <td>Ojibwa</td>
    <td>oji</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/NL.svg"/></span></td>
    <td>Old Dutch</td>
    <td>odt</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/EN.svg"/></span></td>
    <td>Old English</td>
    <td>ang</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/ang">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/ang/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old English_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/FR-ROYAL.svg"/></span></td>
    <td>Old French</td>
    <td>fro</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fro">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fro/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old French_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/ID.svg"/></span></td>
    <td>Old Irish</td>
    <td>sga</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/sga">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/sga/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Irish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/RA.svg"/></span></td>
    <td>Old Norse</td>
    <td>non</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/PT.svg"/></span></td>
    <td>Old Portuguese</td>
    <td>pto</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/PR.svg"/></span></td>
    <td>Old Provençal</td>
    <td>pro</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/WE.svg"/></span></td>
    <td>Old Saxon</td>
    <td>osx</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/osx">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/osx/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Old Saxon_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Historical_language">historical</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Panjabi</td>
    <td>pan</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/AF.svg"/></span></td>
    <td>Pushto</td>
    <td>pus</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/pus">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/pus/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Pushto_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CH.svg"/></span></td>
    <td>Romansh</td>
    <td>roh</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/RM.svg"/></span></td>
    <td>Romany</td>
    <td>rom</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Sanskrit</td>
    <td>san</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/san">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/san/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Sanskrit_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span><a href="https://en.wikipedia.org/wiki/Ancient_language">ancient</a></li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SD.svg"/></span></td>
    <td>Sardinian</td>
    <td>srd</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/SF.svg"/></span></td>
    <td>Saterfriesisch</td>
    <td>stq</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/RS.svg"/></span></td>
    <td>Serbian</td>
    <td>srp</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/SC.svg"/></span></td>
    <td>Sicilian</td>
    <td>scn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/SAMI.svg"/></span></td>
    <td>Skolt Sami</td>
    <td>sms</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/KE.svg"/></span></td>
    <td>Swahili</td>
    <td>swa</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/swa">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/swa/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Swahili_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CH.svg"/></span></td>
    <td>Swiss German</td>
    <td>gsw</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/TJ.svg"/></span></td>
    <td>Tajik</td>
    <td>tgk</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tgk">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tgk/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Tajik_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/TT.svg"/></span></td>
    <td>Tatar</td>
    <td>tat</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tat">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tat/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Tatar_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/IN.svg"/></span></td>
    <td>Telugu</td>
    <td>tel</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tel">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tel/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Telugu_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/TB.svg"/></span></td>
    <td>Tibetan</td>
    <td>bod</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/bod">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/bod/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Tibetan_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SA.svg"/></span></td>
    <td>Tswana</td>
    <td>tsn</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/TM.svg"/></span></td>
    <td>Turkmen</td>
    <td>tuk</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/tuk">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/tuk/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Turkmen_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/CN.svg"/></span></td>
    <td>Uighur</td>
    <td>uig</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/UZ.svg"/></span></td>
    <td>Uzbek</td>
    <td>uzb</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/uzb">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/uzb/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Uzbek_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/VE.svg"/></span></td>
    <td>Venetian</td>
    <td>vec</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/vec">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/vec/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Venetian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/VO.svg"/></span></td>
    <td>Votic</td>
    <td>vot</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/vot">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/vot/issues">issues</a></li>
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
      <li><span class="detail2"><b>Templatic:</b></span>yes</li>
      </ul>
      </div>
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Votic_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/VR.svg"/></span></td>
    <td>Võro</td>
    <td>vro</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/WL.svg"/></span></td>
    <td>Walloon</td>
    <td>wln</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/WF.svg"/></span></td>
    <td>Western Frisian</td>
    <td>fry</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/fry">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/fry/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Western Frisian_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/WI.svg"/></span></td>
    <td>Wymysorys</td>
    <td>wym</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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
    <td><span class="flagspan"><img class="flag" src="images/flags/IL.svg"/></span></td>
    <td>Yiddish</td>
    <td>yid</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/yid">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/yid/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Yiddish_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/MN.svg"/></span></td>
    <td>Yucatec Maya</td>
    <td>yua</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
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



  <tr>
    <td><span class="flagspan"><img class="flag" src="images/flags/SA.svg"/></span></td>
    <td>Zulu</td>
    <td>zul</td>
    <td>0</td>
    <td>0</td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/check.png"/></span></td>
    <td><span class="sourcespan"><img class="source" src="images/wiki.png"/></span></td>
    <td><span class="checkspan"><img class="check" src="images/cc.png"/></span></td>
    <td><div class="arrow"></div></td>
  </tr>
  <tr>
    <td colspan="11">
      <div class="detail-box">
      <div class="mylist">
      <ul class="unstyled">
      <li><span class="detail1"><b>Download Data:</b></span><a href="https://github.com/unimorph/zul">repo</a></li>
      <li><span class="detail1"><b>Report Errors:</b></span><a href="https://github.com/unimorph/zul/issues">issues</a></li>
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
      <li><span class="detail3"><b>Info:</b></span> <a href="https://en.wikipedia.org/wiki/Zulu_language">wikipedia</a></li>
      <li><span class="detail3"><b>Type:</b></span>living</li>  
      </ul>
      </div>
      </div>
    </td>
</tr>

  
</table>