---
title: [Understand filters]


last_updated: tbd
summary: "Filters narrow down the search result to only include the data you want to see."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
When you add a value to your search, it becomes a filter. You can define filters on tables, views and worksheets. When you add a filter, it is applied to the table, view, or worksheet, so the result set only shows rows that satisfy a set of parameters specified in the filter. You can also set filters that are automatically used in every search you perform using a particular data source. For example, you can exclude inactive customers records from your search result set. To avoid typing `status = inactive` with every search you perform, you can use a filter. The complex the filter is, the more useful it is to set on the data sources (e.g. `status = inactive year = 2017 rating > 0`).

To add a filter from the search bar:

1. Click in the search bar and type the values you want to include in the search.

    Typing a value in the search bar acts as a filter.

    ![]({{ site.baseurl }}/images/filter_from_the_search_bar.png "Filter from the search bar")

    You can also use keywords like `yesterday`, `after`, and `next month` to
    filter your search. To see more keywords, refer to the [keyword
    reference]({{ site.baseurl }}/reference/keywords.html#).

2. Click outside of the search bar or push enter to apply your filter.

Simple filters can be applied to an answer, while pinboard filters can be
applied to all visualizations of a pinboard. You can find out more about
[pinboard filters in the pinboards section]({{ site.baseurl
}}/complex-search/pinboard-filters.html#).


## Where filters appear in ThoughtSpot

As you have seen with search, filters appear in grey boxes in the search bar.

 ![]({{ site.baseurl }}/images/search_bar_with_phrases_boxed.png "Search bar with filters")

In an answer or a pinboard, filters appear just under the title. For pinboards,
your filters apply to all worksheet-based visualizations in the pinboard.

 ![]({{ site.baseurl }}/images/filter_appears.png "Pinboard filters")

If you ever find that your search or pinboard does not appear to contain all the
data you want to see, check for any existing filters and remove them by clicking
the **X** to see all the data.

{% include note.html content="Filtering on NULL and empty values is a special
case. You can find out more about how these values are represented and how to
filter for them in [About filtering on null, blank, or empty
values](about-filters-for-null.html#)." %}

## Simple filters

Simple filters can be applied to searches in a few different ways. You can use
the search bar or choose **Filter** from the column header or axis label.
You can apply simple filters to your search, whether it shows a table or a
chart. Your filters remain part of the search even when you change the
visualization type.

When adding a filter from the ellipses icon
![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline},
in the column header or by clicking on a chart axis, numeric columns and
text columns provide you with the ability to include or exclude values, and
a checkbox selector for the values. If the column contains a date, you can see a
calendar selector when applying a filter. This is also where you can apply bulk filters.

## Bulk filters

If you have a large worksheet or table with thousands or millions of rows, you
may want to create bulk filters. You can paste in a list of filter values to
include or exclude, without having to click the box next to each value in the
filter selector.

Bulk filters can be very useful when you have a very large worksheet or table.
You can use them to filter a large list of values easily. For example, this is
useful if you want to only search on a list of products that your manager sent
to you in an email. You can cut and paste those values into the bulk filter box
to quickly generate a report or chart that includes only those items of
interest.

You can [create a bulk filter]({{ site.baseurl}}/complex-search/create-bulk-filter.html) by pasting a list of values,
separated by commas, semicolons, new lines, or tabs, into the bulk filter box.
This allows you to easily search a large list of filters repeatedly.

## Cascading filters

If you want to apply a table filter whenever the table has been used (Views, Worksheets, Answers, and Pinboards), use Cascading filters.
When columns from that table are applied in a search, the table filter is implicitly applied to the search. All worksheet filters are accessible from the query visualizer.

Consider a table with a filter that is used in a worksheet. When a search uses that worksheet, the filters are automatically applied as a part of the search.

## Worksheet filters

A worksheet filter gets applied every time that worksheet is used. This means that for any search involving a filtered worksheet, all worksheet filters are applied before the search is submitted. So results are always filtered, even if the specific terms searched do not include the column(s) that are filtered.
