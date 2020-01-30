---
title: [Moving functions]


last_updated: tbd
summary: "Moving formulas are aggregate formulas that allow you to calculate the average, max, min, or sum of your data over a predetermined interval, or window, with an adjustable range."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Moving formulas can be used to smooth out any irregularities in your data to
easily recognize trends. The larger the interval you set, the more the peaks and
valleys are smoothed out. While the smaller the interval, the closer the moving
averages are to the actual data points.

Each of the moving formula accepts a measure, two integers to define the window,
and one or more optional attributes.

```
formula (measure,integer,integer,[attribute,attribute,...])
```

Only the measure and integer values are required. If you supply both required
and optional values, the formula returns the aggregate of the measure over the
given window. You should experiment with only a measure and integers leaving out
the attribute and then adding it back in. This will help you decide which output
best meets your use case.

The moving formulas are the following:

* `moving_average`, for example `moving_average (revenue, 2, 1, customer region)`

  Takes a measure, two integers to define the window to aggregate over, and one
  or more attributes. Returns the average of the measure over the given window.
  The attributes are the ordering columns used to compute the moving average.
  The window is (`current - Num1...Current + Num2`) with both end points being
  included in the window. For example, `1,1` will have a window size of 3. To
  see periods in the past, use a negative number for the second endpoint, as in
  the example `moving_average(sales, 1, -1, date)`.

* `moving_max`, for example `moving_max (complaints, 1, 2, store name)`

  Takes a measure, two integers to define the window to aggregate over, and one
  or more attributes. Returns the maximum of the measure over the given window.
  The attributes are the ordering columns used to compute the moving maximum.
  The window is (current - Num1...Current + Num2) with both end points being
  included in the window. For example, `1,1` will have a window size of 3. To
  see periods in the past, use a negative number for the second endpoint, as in
  the example `moving_max(sales, 1, -1, date)`.

* `moving_min`, for example `moving_min (defects, 3, 1, product)`

    Takes a measure, two integers to define the window to aggregate over, and
    one or more attributes. Returns the minimum of the measure over the given
    window. The attributes are the ordering columns used to compute the moving
    minimum. The window is (current - Num1...Current + Num2) with both end
    points being included in the window. For example, `1,1` will have a window
    size of 3. To see periods in the past, use a negative number for the second
    endpoint, as in the example `moving_min(sales, 1, -1, date)`.

* `moving_sum`, for example `moving_sum (revenue, 1, 1, order date)`

  Takes a measure, two integers to define the window to aggregate over, and one
  or more attributes. Returns the sum of the measure over the given window. The
  attributes are the ordering columns used to compute the moving sum. The window
  is (current - Num1...Current + Num2) with both end points being included in
  the window. For example, `1,1` will have a window size of 3. To see periods in
  the past, use a negative number for the second endpoint, as in the example
  `moving_sum(sales, 1, -1, date)`.


## Calculate a moving average

This example  demonstrates using the `moving_average` formula. To use the moving function in a search:

1. Start a new search.

   ![]({{ site.baseurl }}/images/aggregation_answer.png "Aggregation Answer example")

2. In the upper-right side of the table, click the ellipses icon ![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline} and select **Add formula**.

   ![]({{ site.baseurl }}/images/create_formula_in_answer.png "Create a new formula in an answer")

3. Enter the moving_average formula, providing a measure, a window, and one or more attributes.

    The example will return the average of revenue, within the commit date window size of 3. The window includes the previous, current, and next rows. The attributes are the ordering columns used to compute the moving average. The window is (current - Num1...Current + Num2) with both end points being included in the window. For example, "1,1" will have a window size of 3. To see periods in the past, use a negative number for the second endpoint, as in the example "moving_average(sales, 1, -1, date)".

    ![]({{ site.baseurl }}/images/moving_average_formula.png "Moving Average Formula")

4. Name the formula by entering a title in the top field, and then click **Save**.

   The formula will appear in the search bar and in the table as its own column.

   ![]({{ site.baseurl }}/images/moving_average_table.png "Moving Average Table")

   A box displaying the moving average within the entire table will appear at the bottom.

5. To use a different aggregation type, click the current aggregation type in the bottom of the box and select another type.
