---
title: "Wymore - Team"
layout: gridlay
excerpt: "Wymore: Team members"
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

<div class="col-sm-12 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="30%" style="float: left" />
  <h2 class="bold">{{ member.name }}</h2>

  {% if member.email %}
  <i>{{ member.info }}<br>email: <{{ member.email }}></i>
  {% endif %}

  <ul style="overflow: hidden;list-style-type: none;padding:0;">

  <b style="font-size:200%;padding-top:15px;display:inline-block;">Education: </b>
  {% if member.education1 %}
  <li>
    <div class="bold col-sm-3">{{ member.education1.date }}</div>
    <div class="col-sm-9">{{ member.education1.info }}</div>
  </li>
  {% endif %}

  {% if member.education2 %}
  <li>
    <div class="bold col-sm-3">{{ member.education2.date }}</div>
    <div class="col-sm-9">{{ member.education2.info }}</div>
  </li>
  {% endif %}

  {% if member.education3 %}
  <li>
    <div class="bold col-sm-3">{{ member.education3.date }}</div>
    <div class="col-sm-9">{{ member.education3.info }}</div>
  </li>
  {% endif %}

  <br>

  <b style="font-size:200%;padding-top:15px;display:inline-block;">Positions: </b>
  {% for position in member.positions %}
    <li>
      <div class="bold col-sm-3">{{position.date}}</div>
      <div class="col-sm-9">{{position.info}}</div>
    </li>
  {% endfor %}

  <b style="font-size:200%;padding-top:15px;display:inline-block;">Service: </b>
  {% for service in member.services %}
    <li>
      <div class="bold col-sm-3">{{service.date}}</div>
      <div class="col-sm-9">{{service.info}}</div>
    </li>
    <br>
  {% endfor %}

  </ul>
</div>



</div>
{% endif %}

{% endfor %}
