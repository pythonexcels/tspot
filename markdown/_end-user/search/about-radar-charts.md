---
title: [Radar charts; spiderweb charts]

last_updated: tbd
summary: "The Radar (or spiderweb) chart contains both columns and a special type of line chart.
"
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
A Spiderweb chart displays data in the form of a two-dimensional chart of three
or more qualities, represented on axes starting from the same point. This is a
good chart to use when you have asked users to rank an experience
or product. You can use a spiderweb chart to examine the relative values for a
single data point. You can also use it to locate outliers.

When you build a Spiderweb chart you must provide at least 3 (three)
attributes and one measure. The measure values move from smallest to the outer
edge of the web. Each spoke of the web is reserved for one of the variables. The
points where each value lies on the web are connected.

![]({{ site.baseurl }}/images/Spiderweb.png "Spiderweb chart example")

The [Austin Animal Center Outcomes]({{ site.baseurl}}/downloads/Austin_Animal_Center_Outcomes.csv) data shows the
outcome of processing. The measure is the count of total animals. By clicking on
a spoke, you can see the total animals in any flow. The number of animals that
were disposed of, meaning they were (sadly) already deceased on arrival is very
small.
