---
title: [Sankey charts]

last_updated: tbd
summary: "The Sankey chart is a type of chart that contains both columns and a special type of line chart.
"
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Sankey diagrams illustrate a flow through a process or system. Transactional
data is optimal for this type of diagram.  For example, financial transactions
that take place as money moves through accounts or as a product is process. Many
marketing users are familiar with Sankey charts from using Google Analytics to
view sales conversions.

When you build a Sankey chart you need to provide at least 2 (two) attributes
and one measure. Your x-axis attributes can contain at most 13 values, any more
and you cannot view a SanKey chart. ThoughtSpot Sankey charts are read from left
to right. The width of the flow represents the measure, the attributes or "steps"
appear as solid bars:

![]({{ site.baseurl }}/images/sankey.png "Sankey chart example")

The [Austin Animal Center Outcomes]({{ site.baseurl }}/downloads/Austin_Animal_Center_Outcomes.csv)
data shows the outcome of processing for different breeds of animal. The measure
is the count of total animals. Looking at how an animal was classified when they
entered the system, this chart shows the outcome processing that took the animal
out of the system.

By clicking on a flow, you can see the total animals in any flow. Many domestic
short haired cats (over 10k) were transferred to other agencies. While all bats
that came into the system were euthanized. There were a surprising number of
bats processed.
