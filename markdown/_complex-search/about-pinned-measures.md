---
title: [Group aggregation functions]

last_updated: tbd
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
What if you want to aggregate a value by a specific attribute (for example, show
revenue by product)? This is known as a grouped aggregation, but some people
call it a pinned measure or level-based measure. You can do this for any
aggregation using the grouping functions.

Each of the grouping functions accepts a measure and one or more optional
attributes:

```
formula (measure, [attribute, attribute, ...])
```

Only the measure value is required. If you supply both a measure and an
attribute, the function returns the aggregate of the measure grouped by the
attribute(s). You should experiment with only a measure and then with an
attribute to see which output best meets your use case.

## List of group functions

Group aggregation functions have names with formats like `group_<aggregation>`.
The group aggregation functions are the following:

<table>
<colgroup>
   <col style="width:25%" />
   <col style="width:75%" />
</colgroup>
  <thead>
    <tr>
      <th>Function</th>
      <th>Description</th>
    </tr>
  </thead>
  <tr>
    <td><code>group_average</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the average of the measure grouped by the attribute(s).</p>
    <p><code>group_average (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_count</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the count of the measure grouped by the attribute(s).</p>
    <p><code>group_count (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_max</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the maximum of the measure grouped by the attribute(s).</p>
    <p><code>group_max (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_min</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the minimum of the measure grouped by the attribute(s).</p>
    <p><code>group_min (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_stddev</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the standard deviation of the measure grouped by the attribute(s).</p>
    <p><code>group_stddev (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_sum</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the sum of the measure grouped by the attribute(s).</p>
    <p><code>group_sum (revenue, customer region)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_unique_count</code></td>
    <td><p>Takes a column name and one or more attributes. Returns the number of unique values in a column, grouped by the attribute(s).</p>
    <p><code>group_unique_count ( product, supplier)</code></p>
    </td>
  </tr>
  <tr>
    <td><code>group_variance</code></td>
    <td><p>Takes a measure and one or more attributes. Returns the variance of the measure grouped by the attribute(s).</p>
    <p><code>group_variance (revenue, customer region)</code></p>
    </td>
  </tr>
</table>

## Flexible aggregation

The `group_aggregate` function gives you more control over aggregation and filtering.

See [Flexible aggregation](aggregation-flexible.html#) to learn more about specifying `query_groups` with this formula.
