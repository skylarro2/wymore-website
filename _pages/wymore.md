---
title: "Wymore Lab - Team"
layout: gridlay
excerpt: "Wymore Lab: Team members"
sitemap: false
permalink: /wymore/
---
<div id="bannerid">
<img src="{{ site.url }}{{ site.baseurl }}/images/U-M_2color-HorizontalReversed.png" width="70%" />
</div>

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}
{% if member.name == "Dr. Troy Wymore" %}
<div class="row">

<div class="col-sm-10 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="30%" style="float: left" />
  <h4 class="bold">{{ member.name }}</h4>

  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% endif %}

  <ul style="overflow: hidden;list-style-type: none;padding:0;">

  {% if member.education4 %}
  <li>
    <div class="bold col-sm-2">{{ member.education1.date }}</div>
    <div class="col-sm-10">{{ member.education1.info }}</div>
  </li>
  {% endif %}

  {% if member.education2 %}
  <li>
    <div class="bold col-sm-2">{{ member.education2.date }}</div>
    <div class="col-sm-10">{{ member.education2.info }}</div>
  </li>
  {% endif %}

  {% if member.education3 %}
  <li>
    <div class="bold col-sm-2">{{ member.education3.date }}</div>
    <div class="col-sm-10">{{ member.education3.info }}</div>
  </li>
  {% endif %}

  {% if member.education4 %}
  <li>
    <div class="bold col-sm-2">{{ member.education4.date }}</div>
    <div class="col-sm-10">{{ member.education4.info }}</div>
  </li>
  {% endif %}

  {% if member.education5 %}
  <li>
    <div class="bold col-sm-2">{{ member.education5.date }}</div>
    <div class="col-sm-10">{{ member.education5.info }}</div>
  </li>
  {% endif %}

  </ul>
</div>

</div>
{% endif %}

{% endfor %}
