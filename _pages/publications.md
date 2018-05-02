---
title: "Wymore Lab - Publications"
layout: gridlay
excerpt: "Wymore Lab -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

See [Google Scholar](https://scholar.google.com/citations?user=gJa4WDcAAAAJ&hl=en){:target="_blank"}

{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% if publi.highlight == 1 %}
<div class="row">
<div class="col-sm-12 clearfix" id="normalid">
 <div class="well" style="display:inline-block;width:100%">
   <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: right;margin-top:0;" />
  <p>{{ publi.title }}</p>
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.link.url }}" target="_blank">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>
</div>
{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>


## Full List

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em><br /><a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}
