---
title: [Filtered aggregation functions]


last_updated: tbd
toc: true
summary: "You can create a filtered aggregation in the search bar."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

Filters are useful for queries where the results should reflect a new, filtered
value. On this page you learn about comparative versus derivative filters, and
the functions, and the keywords that you can use with them.

## Comparative and derivative filters

Comparative filters compare two segments of some whole against each in the
**Search** bar. For example, a company that has locations across the United
States, may want to compare total revenue in the West to the East segment. In a
comparative filter, one of the segments you are comparing is filtered.

An example of a comparative filter is comparing west revenue with total revenue.
In these cases, one measure is a _filtered measure_, for example, `revenue
region = west` is a filtered measure.

Derivative filters add a column to your results which is derived from other
columns in the same results. For example, you search for revenue and cost and
want to calculate profit in your result.

Some examples of comparative and derivative filters in the real world are:

* revenue of this_soap versus all_soaps (Comparative filter)
* tax as a percentage of revenue (derivative)
* count revenue as a percentage of state revenue (comparative with a derivative)

If you plan to create these types of filters, you need to understand how to
create filter functions.

## Use filter functions

Filter functions take two arguments, the column ( measure or attribute) to
aggregate and the filter condition:

```
FUNCTION_NAME(condition, <column name>)
```

ThoughtSpot functional library will include the following functions:

* `sum_if`
* `average_if`
* `count_if`
* `unique_count_if`
* `max_if`
* `min_if`
* `stddev_if`
* `variance_if`
* `vs`
* `all`

The following table illustrates some examples of these functions in use:

<table>
   <colgroup>
      <col style="width:30%" />
      <col style="width:70%" />
   </colgroup>
   <thead class="thead" style="text-align:left;">
      <tr>
         <th>Function</th>
         <th>Examples</th>
      </tr>
   </thead>
  <tr>
    <td><code>sum_if(region=’west’, revenue)</code></td>
    <td>Only aggregate the revenue for the values corresponding to west region.</td>
  </tr>
  <tr>
    <td><code>count_if(region =’west’, region)</code></td>
    <td>Only aggregate the region for the values corresponding to west region.</td>
  </tr>
  <tr>
    <td><code>count_if(revenue > 100, red)</code></td>
    <td>Count the number of times red appears when revenue was greater than 100 (row level revenue data, not aggregated).</td>
  </tr>
</table>

A condition can have multiple filters like `sales region = west OR region = east`. You
can also just type a value such as `east` as in `sales east` as a filter. If
there are no rows matching the criteria, the condition returns a 0 (zero). A 0
can result in situations where there are logic errors in the formula, so be sure
to double-check your work.

![]({{ site.baseurl }}/images/filtered-agg-forms.png "Filter Aggregation")

After you have aggregated with a filter, you can do further comparisons with the `vs` and `all` keywords.

## Using the vs and all keywords

You can use the `vs` and `all` keywords to expand the usefulness of your
comparison filters. It compares a measure across different sets of filters and
or groupings. The basic format of a comparison search is:

`<common search tokens> (A` **vs** `B) <common search tokens>`

For example:

`revenue region last 10 years vs all`

Try this syntax on using the
[Superstore]({{site.baseurl}}/downloads/Superstore.csv) example data. The first
`vs` example compares two segments with a single search token:

![]({{ site.baseurl }}/images/vs-ex-1.png)

The system automatically applies the `sales` token to both sides and groups each
segment. You can use the `all` keyword to break out the segments and avoid
grouping.

![]({{ site.baseurl }}/images/vs-ex-2.png)

You can also provide multiple `vs` instances:

![]({{ site.baseurl }}/images/vs-ex-3.png)

Of course, you can compare across different columns as well:

![]({{ site.baseurl }}/images/vs-ex-4.png)

Other supported formats you can try:

* `sales accessory6 accessory12 vs all`
* `sales monthly accessory6 vs last year`
* `sales staples file caddy vs all monthly` answers what the share of sales belonging to the file caddy by month
* `sales (germany ariel vs laundry) july 2017 time` answers what is the category share of Germany Ariel for July 17?
