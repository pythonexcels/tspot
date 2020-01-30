---
title: [Overview of aggregate formulas]


last_updated: tbd
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
When working with formulas, it is useful to understand the difference between
regular (or row-wise) formulas and aggregation formulas.

## Standard and aggregation formulas

Formulas can be broken down into two types standard and aggregation formulas.
Standard formulas act on individual rows and returns one result per row.
Standard formulas use functions like:

* `add`
* `subtract`
* `multiply`
* `divide`
* `contains`
* `if...then...else`

Aggregation formulas combine rows together and returns a single result for a
group of rows. Aggregation formulas use functions, some examples of functions
you find in aggregation formulas are:

* `average`
* `cumulative_sum`
* `moving_average`
* `stddev` (standard deviation)

You can tell which formulas are aggregation formulas by looking at the function
list in the **Formula Assistant**. Aggregation functions have their own section.

 ![]({{ site.baseurl }}/images/formula_asst_aggregate.png "Aggregation formulas in the Formula Assistant")

## Advanced aggregation functions

Some more advanced aggregation functions are widely used in business
intelligence, since they provide better insight into data. Some of the more
advanced aggregation functions are:

- [Group aggregation functions](about-pinned-measures.html#) apply a specific aggregate to a value, and group the results by an attribute in the data.

- [Cumulative functions](about-cumulative-formulas.html#) measure from the start of your data to the current point. They're often applied on time-based data.

-  [Moving formulas](about-moving-formulas.html#) measure within a window (usually time-based) that you define.

Data from any rows that are not included in the search result will not be incorporated, and you cannot create a filter on aggregated data.

## Flexible aggregation

The `group_aggregate` function makes it possible to aggregate measures at granularities that are
different from the dimensions or column groupings used in the search.

See [Flexible aggregation](aggregation-flexible.html#) to learn more about working with this formula.

## Using division with aggregation in a search

Whenever your search result combines rows, your formula will get aggregated
automatically. For example, if your search contains words like "region",
"monthly", or "department", the results will be grouped (aggregated) by that
category. The administrator can change the default aggregation that gets applied
through a configuration, and you can also change it using the dropdown list in
the column header of the search result.

For example, this search would typically return a sum of total sales by department:

```
sum sales department
```

This search would return an average of sales by month:

```
average sales monthly
```

When you're using division in your formula, and the search is aggregated like
this, you may have to change the order of operations to get the result you
expect. This is best understood by using a real world example.

Suppose you want to calculate the gross margin by department for a grocery
store. The formula for gross margin is:

```
profit / sales
```

But if you use that as your formula, you won't get the expected calculation.
Why? It's because the formula will be evaluated in this order: For each row,
divide profit by sales and then total up all the results. As you can see, the
results do not look like gross margin values, which should be between 0 and 1.

 ![]({{ site.baseurl }}/images/formula_gross_margin_no_sum.png "Aggregated search with a division formula")

Instead, you'd need to use a formula that uses the order of operations you want:

```
sum (profit) / sum (sales)
```

Now the result is as expected, because the formula totals the profits for all
rows, and then divides that by the total of sales for all rows, returning an
average gross margin:

 ![]({{ site.baseurl }}/images/formula_gross_margin_sum.png "Aggregated search with a corrected division formula")
