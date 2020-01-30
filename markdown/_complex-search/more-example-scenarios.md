---
title: [View example scenarios]

last_updated: 11/2/2018
summary: "It's not always easy to know when you need to use a view, but these are some common scenarios."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Here are three common examples of when you would want to use a view.

## Example 1

Search a filtered subset

Let's say you have a table with all the sales transactions for each customer. You want to find high value customers (those who have spent a certain amount of money in the last year). Then you want to do some further analysis on these high value customers, like the count by region. Here you essentially need to sum up the sales per customer, filter by that sum to get the top customers, and then do a count, making it two levels of aggregation. A single search can do only one level of aggregation.

However, a search can calculate the initial sum and filter within it to get the highest value customers. Then you can save that result as a view. Joining the view to some other tables, like the customer dimension, allows you to do the count and other similar analyses using the view along with the other tables.

## Example 2

Cohort analysis

This example is similar to the previous example, except that it involves a more complex filter, called a cohort. You might create a search to find customers who bought product A, but did not buy product B.

First, you would have to perform searches for total sales by customer for both A and B, and create views for both. Then join these two views back in an outer join looking for conditions where the A and B join values are null.

This example could also be solved in a single search by using [conditional formulas]({{ site.baseurl }}/advanced-search/formulas/conditional-sum.html#) to determine the desired group (or cohort) of customers as defined by their buying behavior, and then doing the analysis on this group. But the performance will be better if you do this using a view, and then [materialize the view]({{ site.baseurl }}/admin/loading/materialized-views.html#).

## Example 3

Combining aggregated sources

If you do a lot of your analysis in the aggregate, like at the quarterly level, you may be challenged when trying to combine this aggregated data from different sources. For example, you may want to combine three different quarterly views from SalesForce - Pipeline, Bookings, and Sales Activity to create a comprehensive analysis of each region's performance. Joining the quarterly views together in a worksheet enables you to do this type of analysis easily.

## Example 4

Lightweight data transformation

You may have a table with separate columns for people's first name and last name. You could use a concat formula to create a single column with first name, a space, and last name. But using this formula could make performance slow, since that column would always be calculated on the fly when searching. In this case, creating a view using the concatenate formula and materializing it will improve performance when searching this data.
