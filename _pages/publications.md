---
title: "Wymore - Publications"
layout: gridlay
excerpt: "Wymore -- Publications."
sitemap: false
permalink: /publications/
---


# Publications

See [Google Scholar](https://scholar.google.com/citations?user=gJa4WDcAAAAJ&hl=en){:target="_blank"}

{% for publi in site.data.publist %}

{% if publi.highlight == 1 %}
<div class="row">
<div class="col-sm-12 clearfix" id="normalid">
 <div class="well" style="display:inline-block;width:100%">
   <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: right;margin-top:0;" />
  <p>{{ publi.title }}</p>
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p>{% if publi.type %}<b>{{publi.type}}</b>, {% endif %} <i>{{ publi.journal}}</i>, <b>{{ publi.year }}</b>, {{ publi.location }}.</p>
  <p><strong><a href="{{ publi.link.url }}" target="_blank">{{ publi.link.display }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
 </div>
</div>
</div>
{% endif %}
{% endfor %}

<p> &nbsp; </p>

## Full List

{% for publi in site.data.publist %}

  {{ publi.title }} <br />
  <em>{{ publi.authors }} </em> <br />
  {% if publi.type %}<b>{{publi.type}}</b>, {% endif %}<i>{{ publi.journal}}</i>, <b>{{ publi.year }}</b>, {{ publi.location }}. <br />
  <a href="{{ publi.link.url }}">{{ publi.link.display }}</a>

{% endfor %}
