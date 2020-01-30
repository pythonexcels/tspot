---
title: [Set the y-axis range]

last_updated: tbd
summary: "On charts, you can manually configure the y-axis range to be different from the search default. You can have multiple measures on the y-axis of many charts."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
You can manually set the y-axis range by using the **Edit chart styles** icon.

## Setting the y-axis range

The style  panel includes the option to manually set the y-axis range. To set
the y-axis range:

1. While viewing your answer as a chart, click **Edit chart styles**.

   ![]({{ site.baseurl }}/images/y_axis_range_select_styles.png "Edit chart styles icon")

2. Under **Y-Axis Range** enter your preferred start and end values.

    In this example, our original chart is showing sales values by department
    from 0 to over $10M. We can enter a y-axis range of `5000000` to `9000000` to
    show only sales between $5M and $10M.

    The chart will reorganize itself to reflect the new y-axis range.

    ![]({{ site.baseurl }}/images/y_axis_range.png "Y-Axis Range details")

## Create charts with multiple measures on the y-axis

You can have multiple measures on the y-axis of most (but not all) chart types.
You can configure this on the chart styles panel. To learn more, see these topics:

* [Configure columns for X and Y axis]({{ site.baseurl }}/end-user/search/show-data-labels.html#stack-multiple-measures-on-the-y-axis)

* [Charts with multiple measures on the y-axis]({{ site.baseurl }}/end-user/search/about-charts.html#charts-with-multiple-measures-on-the-y-axis)
