---
title: [Change axis options]
last_updated: 11/06/2019
summary: "In ThoughtSpot, you can start changing all axes options by clicking on the axis, directly in the chart."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
To change axis, you can click the axis itself.

Here, we demonstrate the various options for axis configuration using a visualization "Sales by Department"

![Change axis]({{ site.baseurl }}/images/edit-axis.png "Change Axis for Total Sales")

This opens the detail axis customization menu in the chart.

![Change axis detail]({{ site.baseurl }}/images/edit-axis-detail.png "Options for changing the axis")

You can make the following changes to the axis:

* [Aggregate](#aggregate)
* [Filter](#filter)
* [Conditional formatting](#conditional-formatting)
* [Sort](#sort)
* [Grouping](#grouping)
* [Position](#position)
* [Rename](#rename)
* Edit
* Remove

{: id="aggregate"}
## Change the axis aggregate

To change the axis aggregate, click the **Aggregate** option in the axis menu, and select an alternative from the list of options.

Depending on the type of data type and other settings, the aggregation options include _Total_, _Avg_, _Min_, _Max_, _Total Count_, _Unique Count_, _Std Deviation_, and _Variance_.

![Change axis aggregate]({{ site.baseurl }}/images/edit-axis-aggregate.png "Change axis aggregate")

{: id="filter"}
## Add, Change, and Remove Filters

To manage the filters applied to the axis (in this example, _Total Sales_), follow these steps:

1. Click the **Filters** option in the axis menu.

   ![Change axis filter]({{ site.baseurl }}/images/edit-axis-filter.png "Change axis filter")

2. In the window modal, click **+ add a condition**.

   ![Add a condition to axis]({{ site.baseurl }}/images/edit-axis-filter-1.png "Add a condition axis")

3. Select the comparison option.  

   Here, the options include _is greater than_, _is greater than or equal to_, _is less than_, _is less than or equal to_, _is between_, _is in_, and _is not in_.

   In this example, select _is greater than or equal to_.

   ![Set filter comparison operation]({{ site.baseurl }}/images/edit-axis-filter-2.png "Set filter comparison operation")

4. Set the relevant numerical limits.

    Here, enter the maximum of `1000000`.

    ![Set filter numerical limit]({{ site.baseurl }}/images/edit-axis-filter-3.png "Set filter numerical limit")

    Note that if you select the _is between_ comparison operator, you must set two limits: minimum and maximum. Similarly, _is in_ and _is not in_ operators require a list of values separated by ";".

5.  To add another filter condition, click **+add another**.

    ![Add another filter condition]({{ site.baseurl }}/images/edit-axis-filter-4.png "Add another filter condition")

7.  To remove a filter condition, click the delete icon (**x**) next to its definition.

    ![Remove filter condition]({{ site.baseurl }}/images/edit-axis-filter-5.png "Remove filter condition")


6.  Click **Done**.

    ![Complete filter on axis]({{ site.baseurl }}/images/edit-axis-filter-6.png "Complete filter on axis")

Here, you can see differences between the original chart and the one with the filter applied: Three (3) of the departments had sales under $1,000,000, and they don't appear on the newer chart.    

![Chart with filter applied]({{ site.baseurl }}/images/edit-axis-filter-applied.png "Chart with filter applied. Only shows 10 out of 13 departments.")

To remove a filter from the chart, click the **x** icon on the filter tile.

![Remove filter from a chart]({{ site.baseurl }}/images/edit-axis-filter-remove.png "Remove filter from a chart")

{: id="conditional-formatting"}
## Apply conditional formatting

To apply conditional formatting to the axis (in this example, _Total Sales_), follow these steps:

1. Click the **Conditional formatting** option in the axis menu.

   ![Add conditional formatting]({{ site.baseurl }}/images/edit-axis-conditional-formatting.png "Add conditional formatting")

2. The **Conditional formatting** window modal appears.

   ![Conditional formatting interface]({{ site.baseurl }}/images/edit-axis-conditional-formatting-1.png "Conditional formatting interface")  

3. In the window modal, click **+ add formatting**.

   ![Add a format]({{ site.baseurl }}/images/edit-axis-conditional-formatting-2.png "Add a format")  

4. Select the conditional range.

   The text area on the left specifies the lower limit of the condition, so the condition applies to all values that are greater or equal to it.
   And the text area on the right specifies the upper limit of the condition, so the condition applies to all lower values.

   * To show show values with a lower limit, enter a value in the left text box.

   * To show values with an upper limit, enter a value in the right text box.

   * To show values in a specified range, enter the appropriate values in both text boxes.

   Here, we apply conditional formatting to values between `5,500,000` and `8,000,000`.

   ![Add conditional format range]({{ site.baseurl }}/images/edit-axis-conditional-formatting-3.png "Add conditional format range")

5. To specify a different color of the conditional format, select the new color from the color selector.

   This option draws upper and lower limit lines on the chart, and colors the chart elements that meet the conditional requirements.

   ![Change conditional format color]({{ site.baseurl }}/images/edit-axis-conditional-formatting-4.png "Change conditional format color")

   Alternatively, you can place a range band on the chart. Select the **Fill chart** option.

   ![Add conditional format band]({{ site.baseurl }}/images/edit-axis-conditional-formatting-8.png "Add conditional format band")

6. To add another condition, click **+add formatting**.

    ![Add another conditional format]({{ site.baseurl }}/images/edit-axis-conditional-formatting-5.png "Add another condition")

7.  To remove a defined conditional format, click the delete icon (**x**) next to its definition.

    ![Remove conditional format]({{ site.baseurl }}/images/edit-axis-conditional-formatting-6.png "Remove conditional format")

8.  Click **Done**.

    ![Complete conditional format]({{ site.baseurl }}/images/edit-axis-conditional-formatting-7.png "Complete conditional format")

Here, you can see a chart that highlights elements with conditional  formatting on some elements. You can also see how the same chart appears with a background chart band.    

![Conditional formatting applied, two options]({{ site.baseurl }}/images/edit-axis-conditional-formatting-applied-comparison.png "Conditional formatting applied, two options")

{: id="sort"}
## Change the Sort

To change the sorting of a measurement on an axis, click the **Sort** option in the axis menu, and select an alternative from the list of options: _Ascending_ or _Descending_.

![Change axis sort]({{ site.baseurl }}/images/edit-axis-sort.png "Change axis sort")

Here, you can compare the original chart that was not sorted on the _Total Sales_ axis with the chart that uses descending sort.

![Compare unsorted chart and chart sorted in Descending order]({{ site.baseurl }}/images/edit-axis-sort-applied.png "Compare unsorted chart and chart sorted in Descending order")

{: id="position"}
## Change the Postion of the axis

It is generally easier to interpret a chart if axes that use the same units of measurement or scale appear on the same side of the chart. In our example, we can best visualize _Item Cost_ and _Item Price_ on the same side of chart.

To change the position of an axis, select the **Position** option in the axis menu, and then select an alternative from the list of options: _Left_ or _Right_.

Here, we move the _Item Price_ axis from the right side of the chart to the left side.

![Change axis position]({{ site.baseurl }}/images/edit-axis-position.png "Change axis position")

You can compare the original chart with the one where the _Total Sales_ axis is on the right, while _Item Cost_ and _Item Price_ both appear on the left.

![Compare charts with different position assignments]({{ site.baseurl }}/images/edit-axis-position-applied.png "Compare charts with different position assignments")

{: id="grouping"}
## Change the Grouping

When two axis use the same unit of measure and a similar scale, we can group them together.

To change the grouping on an axis, click the **Group** option in the axis menu, and select an alternative from the list of options, which are the measurements on the other axes.

Here, we change the _Item Price_ axis by grouping it with _Item Cost_.

![Group two axes]({{ site.baseurl }}/images/edit-axis-group.png "Group two axes")

Compare the original chart with one that groups _Item Price_ and _Item Cost_ as _Item Price & Item Cost_. The chart looks cleaner, and clearly communicates the distinct information on each of the two measurements.

![Compare ungrouped chart and chart that groups similar measures]({{ site.baseurl }}/images/edit-axis-group-applied.png "Compare ungrouped chart and chart that groups similar measures")

Notice that the **Customize** menu shows a linkage between the two grouped axes.

![Grouped axes]({{ site.baseurl }}/images/edit-axis-group-menu.png "Grouped axes")

{: id="rename"}
## Rename an axis

You can always rename an axis for clarity, brevity, format, and so on.

In our example, it makes sense to rename the axis created from grouping as _Item Price & Item Cost_ to something shorter, like _Item Price and Cost_.

To rename an axis, select the **Rename** option in the axis menu, type the new name, and either click out or hit **Enter/Return** on your keyboard.

![Rename axis]({{ site.baseurl }}/images/edit-axis-rename.png "Rename axis")
