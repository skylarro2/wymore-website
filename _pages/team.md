---
title: "Wymore - Team"
layout: gridlay
excerpt: "Wymore: Team members"
sitemap: false
permalink: /team/
---
<div id="bannerid">
<img src="{{ site.url }}{{ site.baseurl }}/images/U-M_2color-HorizontalReversed.png" width="70%" />
</div>

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

<div class="row">

<div class="col-sm-10 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="20%" style="float: left" />
  <h4 class="bold">{{ member.name }}</h4>


  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% endif %}

  <ul style="overflow: hidden;list-style-type: none;padding:0;font-size:1.7rem;">

  {% if member.number_educ >= 1 %}
  <li>
    <div class="bold col-sm-2">{{ member.education1.date }}</div>
    <div class="col-sm-10">{{ member.education1.info }}</div>
  </li>
  {% endif %}

  {% if member.number_educ >= 2 %}
  <li>
    <div class="bold col-sm-2">{{ member.education2.date }}</div>
    <div class="col-sm-10">{{ member.education2.info }}</div>
  </li>
  {% endif %}

  {% if member.number_educ >= 3 %}
  <li>
    <div class="bold col-sm-2">{{ member.education3.date }}</div>
    <div class="col-sm-10">{{ member.education3.info }}</div>
  </li>
  {% endif %}

  {% if member.number_educ >= 4 %}
  <li>
    <div class="bold col-sm-2">{{ member.education4.date }}</div>
    <div class="col-sm-10">{{ member.education4.info }}</div>
  </li>
  {% endif %}

  {% if member.number_educ >= 5 %}
  <li>
    <div class="bold col-sm-2">{{ member.education5.date }}</div>
    <div class="col-sm-10">{{ member.education5.info }}</div>
  </li>
  {% endif %}


  {% if member.page %}
  <a href="{{ site.url }}{{ site.baseurl }}/{{ member.page }}">Read more</a>
  {% endif %}

  </ul>
</div>

</div>

{% endfor %}

<!-- ## Administrative Support
<a href="mailto:"></a> is helping us (and other groups) with administration.
-->
