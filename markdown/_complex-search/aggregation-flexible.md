---
title: [Flexible aggregation functions]
summary: "Use the group_aggregate function in ThoughtSpot to aggregate measures at different granularities then the dimensions used in the search columns."
last_updated: 11/05/2019
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

## How aggregation formulas work

Typically, the groupings and filters used in a formula use the same fields as columns returned in the search results. The concept of a grouping equates to an attribute column.

For example, in the search `revenue ship mode`, `revenue` is
the measure, and `ship mode` is the attribute, or grouping. The result of this
search shows total revenue for each ship mode:

| revenue | ship mode |
| --- | --- |
| $ _a_ | air |
| $ _r_ | rail |
| $ _t_ | truck |
| $ _s_ | sea transport |

The aggregation formulas are described in [Overview of aggregate formulas](aggregation-formulas.html#).

## About flexible aggregation

ThoughtSpot provides flexible aggregation with the `group_aggregate` function. You can use this formula
to group and filter query results on different dimensions and granularities from the columns already used in the search bar query.

The `group_aggregate` formula uses a sub-query to perform these custom aggregations. If the sub-query
is at a higher detailed level, ThoughtSpot adds the result column to the result of original
query. When the sub-query is at a finer detail level than the original query, ThoughtSpot uses _roll-up_, or _reaggregation_.

This is particularly useful for comparison analysis.

To use the groups and filters, specify them using the `query_groups` and
`query_filters` keywords, respectively. You can also add or exclude groups or filters.

{% include content/flexible-aggregation-best-practices.md %}

## Examples

For a search on `revenue monthly ship mode`, you can add a formula to calculate yearly revenue by ship mode:

```
group_aggregate(sum(revenue), {ship mode, year(commit date)}, {})
```

The same formula can also be written using `query_groups()` and `query_filters()` as following:

```
group_aggregate(sum(revenue), query_groups() - {commit date} + {year(commit date)}, {})
```

This is helpful to include the main query groups that are not known at formula
creation time. You can use `+/-` to modify the set of groups included from
the query.

{% include note.html content="`+/-` is currently supported only for  `query_groups`, not `query_filters`."%}

## When group formula results are finer-grained than the search

With the flexibility of groupings for group formulas, the computed column
created by a formula can be finer or courser grained than the search itself.

For example, you can have a search that shows **total yearly sales** and a
formula that computes total sales _for each month_ (a finer-grained calculation
than the search).

In such cases, if an additional aggregation is specified by the formula, the
results get _reaggregated_.

Reaggregation can be applied in either of these ways:

* You can add an aggregation keyword just before a formula column in a search.
For example, in this search we've added the keyword **min** just before our formula
for `monthly_sales`:

  **sum revenue yearly min monthly_sales**

  where, the `monthly_sales` formula is written as:

    ```
     group_aggregate(sum(revenue), {start_of_month(date)}, {})
    ```

* You can create a separate formula, such as in this search for:

  **sum revenue yearly min_monthly_sales**

  where, the `min_monthly_sales` formula is written as:

  ```
  min(monthly_sales)
  ```

Alternatively, if no aggregation is specified, then the search query also
inherits the formula groupings, as in this search:

**sum revenue yearly monthly_sales**

where, the original query is computed at a monthly grain instead of yearly.

## Reaggregation scenarios

Some scenarios require aggregation on an already aggregated result.

For example, computing minimum monthly sales per ship mode, requires two
aggregations:

* the first aggregation of **sum** to compute total monthly sales per ship
mode.

* the second aggregation of **min** to compute minimum sale that happened
for any given month for that ship mode.

An example of this is this search:

**ship mode min monthly_sales**

where the formula `monthly_sales` is written as:

```
group_aggregate(sum(revenue), query_groups() + {start_of_month(date)}, {})
```
For more extensive examples of using the `group-aggregate` function, we encourage you to see [Reaggreggation scenarios in practice]({{site.baseurl}}/reference/reaggregation-scenarios.html)

## Groups and filters

Flexible group aggregate formulas allow for flexibility in both [groupings](about-pinned-measures.html#)
and [filters](filtered-agg-forms.html#). The formulas give you the ability to
specify only groupings or only filters.

## Related information

* For more examples of flexible aggregation, see the [group_aggregate]({{site.baseurl}}/reference/practice/formula-reference.html#group_aggregate) function in the [Formula function reference]({{site.baseurl}}/reference/formula-reference.html).

* To learn about aggregation formulas in general, see
[Overview of aggregate formulas](aggregation-formulas.html#) and
[Group aggregation functions](about-pinned-measures.html#)

* To learn about how the `group-aggregate` function can be used within your business practice, we encourage you to see [Reaggregation scenarios in practice]({{site.baseurl}}/reference/practice/reaggregation-scenarios.html)
