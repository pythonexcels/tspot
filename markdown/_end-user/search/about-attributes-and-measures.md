---
title: [Search results and column types]
last_updated: tbd
summary: "Searches in ThoughtSpot use columns that are defined as either attributes or measures."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

ThoughtSpot identifies search columns (`sales`, `customer_name`, `total_sale`) as either attributes or measures. The columns you choose impact your search results.  That's because several chart types expect that your search contains a certain number of attributes and a certain number of measures.

## Attributes

Attribute are primarily text or date values. Attributes make up the x-axis of your chart most of time. Some examples of attributes in terms of a person include name, eye color, occupation, social security number, address, employee ID, and phone number.

## Measures

Measures are numeric values you can do math on, with meaningful results. You will most likely find your measures on the y-axis of your chart. Some examples of measures in terms of a person are age, height, and weight.

## Query details

After, or while completing a search, you can see how ThoughtSpot displayed the
answer. Click the **Query details** button on the right-hand side of the screen
to open the **Query details** panel.

![]({{ site.baseurl }}/images/what_am_i_looking_at.png "Query details")

This panel shows the measures that ThoughtSpot computed, for each combination of
attributes. Choose **Query visualizer** to see search filters and how the tables
were linked and used.
