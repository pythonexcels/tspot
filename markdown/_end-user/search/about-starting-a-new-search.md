---
title: ["What are Searches and Answers?"]
last_updated: 09/23/2019
summary: "You use search to answer questions about your data without having to consult a data analyst."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Using ThoughtSpot's relational search is simple, so anyone can use it. In the
search bar, type what you are interested in exploring, for example `revenue
midwest sales rep`. Searches return a set of results in the form of a table or a
chart. ThoughtSpot likes to call this set of results in response to a search an
_answer_.

As you get better with ThoughtSpot's search, you will be able to get more out of
your data by performing more complex searches.  There are a few basic things you
should understand before starting a new ThoughtSpot search.

## How do I search data?

You’ve probably seen one of these before:

 ![]({{ site.baseurl }}/images/search_bar_blank.png "Search bar")

Click in the box and start typing some letters. As soon as you begin typing, ThoughtSpot suggests some search terms Type slowly and use the suggestions to find what you're looking for.

You can see an answer in the form of a chart or a table. If you do not see an answer, press **Enter** on your keyboard.

You should know that search in ThoughtSpot is more like an Amazon search than a conversation. For example. Instead of:

```
Find me all books by Lewis Carroll with the title Alice in Wonderland
```

You'd type:

```
carroll alice
```

Or consider Google. You wouldn’t type in:

```
Find me the largest city by population
```

You’d type:

```
largest city by population
```

or simply:

```
largest city population
```

That’s how search works in ThoughtSpot. You can use some helping words like “by” and “for” but they can also be left out, and the search will return the same answer.

## What kinds of things can I type?

Search is based on the tables that exist in your data. Tables are made of rows and columns, like spreadsheets. So you can search by typing in any of these words:

-   The column name: like revenue, product name, or store
-   Any of the values in the columns: like 20000, kitten chow, or richmond
-   One of the special [keywords]({{ site.baseurl }}/reference/keywords.html#) ThoughtSpot understands: like yesterday, &gt;, or contains

## Save an answer

An answer is the result of a single search. You can save an answer you want to work more on later, or just keep it for your personal use. You can also share an answer with other users.  The **Answers** tab is where you can view and then the your saved search results.

## Related information

-   [Choose a data source]({{ site.baseurl }}/end-user/search/about-choosing-sources.html)  
-   [Search bar features]({{ site.baseurl }}/end-user/search/about-the-search-bar.html)  
-   [Search suggestions]({{ site.baseurl }}/end-user/search/recent-searches.html)  
-   [Search results and column types]({{ site.baseurl }}/end-user/search/about-attributes-and-measures.html)  
-   [Share an answer]({{ site.baseurl }}/end-user/pinboards/share-answers.html)
-   **Beta** [About SearchIQ]({{ site.baseurl }}/end-user/search/about-searchiq.html)
