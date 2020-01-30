---
title: [Change result display options]
last_updated: 1/16/2020
summary: "You can change how your search results (Answers) appear."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Your search results, or Answers, have various display options. You can change the
visualization used to display your results, their sort order, how ThoughtSpot groups the data, and what data ThoughtSpot includes.

## Change the view

You can change the view of your answer so it appears as either a table or a chart. To
change the view of your answer:

1. View your answer.
2. Toggle between either a table or a chart type.

    ![Select table or chart]({{ site.baseurl }}/images/toggle_between_views.png "Select table or chart")
    <!--{% include image.html file="toggle_between_views.png" title="Select table or chart" alt="You can toggle between displaying your results as a table or as a chart." caption="Select table or chart" %}-->

When you display your data as a chart, ThoughtSpot automatically selects the type of chart that works best for your data. If you want to use another type, click the change visualization icon ![]({{ site.baseurl }}/images/icon-chart-type-20px.png){: .inline} and select the type of chart you want. Refer to [understand charts]({{ site.baseurl }}/end-user/search/about-charts.html).

## Sort your search

Sorting your search allows you to order your answer, making it easier to read.
To sort your search:

* If you are in the data (table) view, click the column header you would like to sort on.

   By default, sorting applies in descending order. For example, if the column has numerical values, it would start at the highest number and decrease. Click the column header again to sort in ascending order.

   {% include tip.html content="Hold shift and click another column to add a secondary sort. You can even add tertiary sorting and so on by continuing to use this trick." %}

* If you are in the chart view, click the axis label of your chart that you would like to sort and select **Sort**. You can choose to sort in ascending or descending order.


## Change the date bucketing (grouping)

You can change the date _bucketing_ on tables and charts for columns with date
values.  Bucketing is a method for grouping a column in your data. For example,
if you have a column of orders, you can use the date of each order
(**NO_BUCKET**).

![]({{ site.baseurl }}/images/bucket_none.png "Date bucketing chooser")

Alternatively, you can group these **MONTHLY**:

![]({{ site.baseurl }}/images/bucket_monthly.png "Date bucketing chooser")

ThoughtSpot chooses a default date bucket for you when you search. This default
takes the entire search result into account. For example, if your search
includes last month, dates are bucketed daily instead of monthly.

* In a table view, use the date bucket drop-down, under the column header.
* On a chart, you can change the change the axis label.

![]({{ site.baseurl }}/images/bucket_change.png "Chooser location")


The bucket values are a subset of date and time-period keywords. To change the date bucketing, follow these steps:

1. Go to the table or chart you want to change.
2. Locate the column or axis value with the date value you want to change.
3. Click the column's bucket menu.
4. Select a date bucket.


## Exclude and include row values

You can include or exclude row values from your answer.

To exclude or include row values:

1. Right-click the visualization or table cell of interest.
2. Select **Exclude "value"** or **Only Include "value"** if available.

     ![]({{ site.baseurl }}/images/exclude.png "Exclude value option")
