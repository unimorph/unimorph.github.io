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

# Generalization Across Languages

## Annotated Languages

The following {{ site.data.annotation2021 | size }} languages have been annotated according to the UniMorph schema. Missing parts of speech will be filled in soon.

{% assign sorted_langs = site.data.annotation2021 | sort:"name" %}

<div class="table-wrapper" markdown="block" style="overflow-x: scroll">

  <table class="table table-responsive" id="annotation">
    <tr>
      <th><strong>Language</strong></th>
      <th><strong>Family</strong></th>
      <th style="text-align:right"><strong>Group</strong></th>
      <th style="text-align:right"><strong>Annotators</strong></th>
      <th style="text-align:right"><strong>Apertium</strong></th>
      <th style="text-align:right"><strong>UniMorph</strong></th>
    </tr>

    {% for language in sorted_langs %}
    <tr>
    <td><a href="https://en.wikipedia.org/wiki/{{ language.name }}_language">{{ language.name }}</a></td>
    <td style="text-align:right">{{ language.family }}</td>
    <td style="text-align:right"><a href="{{ language.group }}">{{ language.group }}</a></td>
    <td style="text-align:right">{{ language.annotators }}</td>
    <td style="text-align:right">{{ language.apertium }}</td>
    <td style="text-align:right">{{ language.unimorph }}</td>
    </tr>
    {% endfor %}

  </table>

</div>

<script src="https://code.jquery.com/jquery-3.1.1.slim.min.js" integrity="sha384-A7FZj7v+d/sdmMqp/nOQwliLvUsJfDHW+k9Omg/a/EheAdgtzNs3hpfag6Ed950n" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/tether/1.4.0/js/tether.min.js" integrity="sha384-DztdAPBWPRXSA/3eYEEUWrWCy7G5KFbe8fFjk5JAIxUYHKkDx6Qin1DkWx51bBrb" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-alpha.6/js/bootstrap.min.js" integrity="sha384-vBWWzlZJ8ea9aCX4pEW3rVHjgjt7zpkNpZk+02D9phzyeVkE+jo0ieGizqPLForn" crossorigin="anonymous"></script>



