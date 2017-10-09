---
layout: page
permalink: /publications/
title: Publications
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


The following publications have made use of UniMorph data. (TEST)

<!--
  <div>
  <link rel="stylesheet" href="css/bib-publication-list.css"/>
  <style>
    #bibtex { display: block;}
  </style>
  
  <table id="pubTable" class="display"></table>
  
  <pre id="bibtex" style="display:none;">

    
  </pre>
  </div>
  	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
		<script type="text/javascript" src="build/bib-list.js"></script>
		<script type="text/javascript">
		    $(document).ready(function() {
        	bibtexify("#bibtex", "pubTable", {'tweet': 'vkaravir'});
    		});
		</script>
-->
