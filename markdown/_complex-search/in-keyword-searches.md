---
title: [Using the in keyword for nested searches]


last_updated: tbd
summary: "You can use the in keyword to do a search on the result of another search."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Beginning with version 5.2 of ThoughtSpot, you no longer need a View when you want to do a search on top of another search. You can use the "in" keyword instead.

![]({{ site.baseurl }}/images/in_search_bar_example.png "In search example")

Suppose you wanted to narrow down a result set based on criteria defined using a search. For example:

Find the top 5 stores by sales in the bakery department

Then you want to see all sales across all departments for those five stores.

In past versions,  you'd have two options:

1. Do your first search to find top 5 stores by bakery sales and save it as a View. Then join the view to your worksheet and search both together to get your answer.

   This approach gives a dynamic result that's computed on the fly each time, but it require the Can Manage Data privilege and requires multiple steps.

2. Save the names of the five stores with the most bakery sales and use them as a filter in a new search.

   This approach is easy to accomplish for ad hoc searches, but doesn't compute dynamically.

Now you can do this analysis in a single search using the "in" keyword. This provides the benefit of computing the answer dynamically without the extra steps required when using a view.

## The "in" keyword

{% include content/keywords-in.md %}

##  Create an in search

1. Start a new search.

2. Do the search you plan to use for the in clause. That is, the first level search.

   Check that the result is what you're looking for.

   ![]({{ site.baseurl }}/images/in_search_first_step.png "In search example")

3. Copy that search, and paste it into your new search as the in clause.

   ![]({{ site.baseurl }}/images/in_search_example.png "In search example")
