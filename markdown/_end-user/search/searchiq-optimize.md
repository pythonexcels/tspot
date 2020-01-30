---
title: ["Optimize SearchIQ"]
last_updated: 09/23/2019
summary: "For SearchIQ to work well, you must enable, optimize, and enable it on the data source."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

SearchIQ is a search experience that understands a more natural, speech-like search language. Contrast it with the [original ThoughtSpot search]({{ site.baseurl }}/end-user/search/about-starting-a-new-search.html). For example, you can search for _`What was my top selling product last month?`_, instead of typing _`top 1 product by sales last month`_. You can also speak your search using the voice-to-text capability of your operating system.

Data source owners must enable SearchIQ for their data sources, and then optimize the data source so users get better results. These are the primary steps for enabling and optimizing SearchIQ:

1. [Enable columns for SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-columns.html)
2. [Add Experts for SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-experts.html)
3. [Train SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-train.html)

<!--There are a few ways for Administrators to optimize how SearchIQ interprets natural language questions. Taking the time to do this early leads to better results from SearchIQ, and to better adoption of the product by end users.-->


## Prerequisites ##

- SearchIQ is turned off by default; ask your administrator to enable it.
- You must be a member of a group that has the **Can use experimental features** permission.

## Enable Columns ##

See [Enable Columns for SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-columns.html).

## Add Experts ##

See [Add Experts for SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-experts.html).

## Train SearchIQ ##
See [Train SearchIQ]({{ site.baseurl }}/end-user/search/searchiq-optimize-train.html).

## Mark the source as optimized for SearchIQ ##

After you finish training SearchIQ on your data source, click the **Data** tab, navigate to the data source, select its  **SearchIQ** tab, scroll to the bottom left corner, and finally turn on the setting for **SearchIQ Optimized**.

![]({{ site.baseurl }}/images/worksheet-searchiq-optimized.png "Confirm datasource is optimized for SearchIQ")

## How does SearchIQ work for end Users ##

After you finish training SearchIQ on the Dataset, we recommend that you share with the users a list of the questions you used for training SearchIQ, the names of columns and their descriptions, common synonyms, and some guidance on how to ask a question.

Remember that users who experience SearchIQ see only the columns that SearchIQ knows.

## Related information ##

-   [About SearchIQ]({{ site.baseurl }}/end-user/search/about-searchiq.html)
-   [Use SearchIQ]({{ site.baseurl }}/end-user/search/use-searchiq.html)
-   [Teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html)
