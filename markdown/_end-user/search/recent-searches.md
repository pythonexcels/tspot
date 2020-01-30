---
title: [Search suggestions]

last_updated: tbd
summary: "How ThoughtSpot learns from your searches and helps you."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Search suggestions include complete recent searches that are similar to the search you are constructing.

 ![]({{ site.baseurl }}/images/search_history.png "Search suggestions example")

## Usage-based ranking (UBR)

Search suggestions are relevant to the data and personalized to your search
behavior. ThoughtSpot learns over time what columns are most important to you
and to your company as a whole. Then, it uses this knowledge to rank the search terms
it offers. The term for this is usage-based ranking (UBR).

ThoughtSpot keeps usage statistics on frequency of search terms in its local
cache. If you frequently use type terms related to finance or to a particular
product, ThoughtSpot provides you with related suggestions more frequently.
Using this information, frequently used terms and phrases are offered in search
suggestions more often than those that are not commonly used.

UBR based on search patterns makes ThoughtSpot more valuable over time. Search
suggestions become more helpful the more searches you complete.

## Recent searches

As you type in the search bar, you are given search suggestions that include
recent searches. This makes it easier to learn what you can do with ThoughtSpot.
In addition to displaying your own recent searches, the search bar also learns
from searches made by other people. This should provide you with interesting
searches that you may not have been aware of. You can see recent searches in a
separate section of search suggestions, as recent searches appear higher in
suggestions than other terms.

## Auto-disambiguation in search

When there are more than one possible meaning for a search term, you can provide
disambiguation by selecting from a list of choices. Now, your choice is sticky.
That means you won’t have to select it again, in the scope of the current
search.

 ![]({{ site.baseurl }}/images/disambiguation.png "Auto-disambiguation example")

## Out of scope columns

Search suggestions are not limited in scope to the columns that you select as
the data sources. Suggestions can include columns that are out of scope, too. If
you choose one of these suggestions, the columns will be added to the data
sources scope for you.

## Object searches

Search suggestions also include relevant pinboards that have already been
created. This means that if a pinboard that is similar to the search you're
trying to do already exists, it will appear in search suggestions.
