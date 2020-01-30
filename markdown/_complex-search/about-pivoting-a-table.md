---
title: [Pivot table]


last_updated: tbd
summary: "A pivot table is a chart type."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Creating a pivot table enables exploring alternate visualization of data in a
wide table. It is useful especially when improve data display when some data is
best viewed horizontally, while others, vertically. Pivot tables are a chart
time table that use a drag-and-drop interface.  

 ![]({{ site.baseurl }}/images/pivot_chart_example.png "Pivot table chart type")

If a **Pivot Table** is available for your answer, you see this type of
visualization as an option under the visualization. Add rows, measures, and
columns to the search bar:

 ![]({{ site.baseurl }}/images/pivot_table_rows_measures_columns.png "Chart axes: rows, measures, columns")


You can restructure your pivot table by moving these values under **Configure
Chart** or by dragging and dropping column headings on the table itself. If you
right-click a row heading, the system displays a contextual sort menu:

![]({{ site.baseurl }}/images/pivot-context-menu.png)


## Expanding or contract columns and rows

Click a column or row to expand it. Additionally, you can expand or collapse all
by right clicking the arrow on the top left of a cell.

![]({{ site.baseurl }}/images/pivot_table_expand_collapse_all.png "Expand or collapse all option")

When you pin a pivot table to a pinboard, it will retain your expansion settings.

## Display totals

You can show **% Row Grand Total** and, **% of Column Grand Total**, or **% of
Grand Total** on pivot tables. Grand  totals aggregate data of the entire pivot
grid. They show values summarized across all available data.

![]({{ site.baseurl }}/images/pivot-grand-total.png)

You only see 100% value when grand total rows is enabled. This is because when
it is disabled, the rows and columns they have no parental total column and the
percentage cannot be calculated. All intermediate total (columns or rows)
display the percentage values calculated with respect to their parent. For each
inner summary (column or row) the parental total values are assumed to be 100%
internally.

To see the total column make sure you also have **Pivot Summaries** checked.

![]({{ site.baseurl }}/images/pivot-summaries.png)

## Format row headers

For row headers, you can switch between the default view and a more compact
(tree) layout:

![]({{ site.baseurl }}/images/pivot_table_rows_measures_columns.png)

From the header menu users, change the type of total shown for an aggregated
measure:

![]({{ site.baseurl }}/images/pivot-table-agg-totals.png )

You can also **Remove** a headline.

## Heatmap of large contributors

The heatmap functionality allows you to see which measures contribute more than
others (heat) within the table.

![]({{ site.baseurl }}/images/pivot_table_heatmap_mode.png "Heatmap mode enabled")

Toggle on the **Heatmap mode** found under **Configuration Options** to add
color coordination to your data.

## Pivot table limitations

The pivot table chart type has these limitations:

- Only the first 10,000 data values are used. If you would like to increase this limit, please contact ThoughtSpot Support.
- Pivot table is not available if the dataset contains more than 100,000 rows.
- Cardinality is not configurable.
- Show underlying data menu is unavailable.
- Conditional formatting is not functional.
