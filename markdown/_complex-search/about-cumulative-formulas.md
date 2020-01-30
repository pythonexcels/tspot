---
title: [Cumulative functions]


last_updated: tbd
toc: false
summary: "Cumulative formulas are aggregate formulas."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Cumulative formulas that allow you to calculate the average, max, min, or sum or
your data over time. Although we usually talk about cumulative formulas over
time, you can use them over any other sequential data. Each of the cumulative
formulas accepts a measure and one or more optional grouping by an attribute
(like region or department):

```
formula (measure, [attribute, attribute, ...])
```

Only the measure value is required. If you supply both a measure and attributes,
the formula returns the aggregate of the measure accumulated by the attribute(s)
in the order specified. You should experiment with only a measure and then with
an attribute to see which output best meets your use case.


The cumulative formulas are:

<table>
 <colgroup>
    <col style="width:25%" />
    <col style="width:75%" />
 </colgroup>
    <tr>
       <th>Function</th>
       <th>Description</th>
    </tr>
    <tr>
       <td><code>cumulative_average</code></td>
       <td>Takes a measure and one or more attributes. Returns the average of the measure, accumulated by the attribute(s) in the order specified. For example:
       <code>cumulative_average (revenue, order date, state)</code></td>
    </tr>
    <tr>
       <td><code>cumulative_max</code></td>
       <td>Takes a measure and one or more attributes. Returns the maximum of the measure, accumulated by the
    attribute(s) in the order specified. For example: <code>cumulative_max (revenue, state)</code></td>
    </tr>
    <tr>
       <td><code>cumulative_min</code></td>
       <td>Takes a measure and one or more attributes. Returns the minimum of the measure, accumulated by the attribute(s) in the order specified. or example: <code>cumulative_min (revenue, campaign)</code></td>
    </tr>
    <tr>
       <td><code>cumulative_sum</code></td>
       <td>Takes a measure and one or more attributes. Returns the sum of the measure, accumulated by the attribute(s) in the order specified. For example:  <code>cumulative_sum (revenue, order date)</code></td>
    </tr>
</table>

## Calculate a cumulative sum

This example demonstrates using the cumulative_sum formula, also known as a
running total. To use the cumulative function in a search:

1. Start a new search.

   ![]({{ site.baseurl }}/images/aggregation_answer.png "Aggregation Answer example")

2. In the upper-right side of the table, click the ellipses icon ![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline} and select **Add formula**.

   ![]({{ site.baseurl }}/images/create_formula_in_answer.png "Create a new formula in an answer")

3. Enter the cumulative_sum formula, providing a measure and one or more attributes.

   The example will return the sum of revenue, accumulated by the commit date.

     ![]({{ site.baseurl }}/images/cumulative_sum_formula.png "Cumulative Sum Formula")

4. Name the formula by clicking its title and typing a new name.
5. Click **Save**.

   The formula will appear in the search bar and in the table as its own column.

     ![]({{ site.baseurl }}/images/cumulative_sum_table.png "Cumulative Sum Table")

    A headline box displaying the cumulative sum within the entire table will
    appear at the bottom. You can click it to toggle between different
    aggregations.
