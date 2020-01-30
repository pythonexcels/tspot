---
title: [Bar charts]
last_updated: tbd
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
The bar chart is very similar to the column chart. The only difference is that
it is oriented the other way.

Bar charts display your data using horizontal rectangular bars. The length of
the bar is proportional to the data value.

 ![]({{ site.baseurl }}/images/bar_chart_example.png "Bar chart example")

Your search needs at least one attribute and one measure to be represented as a bar chart.

## Stacked bar charts {#stacked-bar-charts}

The stacked bar chart is similar to the bar chart, but with one major difference. It includes a legend, which divides each bar into additional sections by color.

Stacked bar charts are typically used when you want to compare aggregated
data and the data that it includes together. You can toggle the options in
styles to show Detailed Labels (summaries for each section of each bar) and Total Labels (show the sum of the stacks for each bar).

![]({{ site.baseurl }}/images/bar_chart_example_stacked_labels.png "Stacked bar chart example")

It is important to note that stacked bar charts plot the y-axis as a percentage by default. You can choose to toggle **Show Y-Axis as %** on or off in the Configuration Options. This feature is also available for stacked area charts.

![]({{ site.baseurl }}/images/bar_chart_example_stacked_xy.png "Stacked bar chart example")

Your search needs at least two attributes and one measure to be represented as a stacked bar chart.
