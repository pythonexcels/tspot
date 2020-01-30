---
title: ["Teach SearchIQ your language"]
last_updated: 09/23/2019
summary: "You can teach SearchIQ your language, to make its results more accurate."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

Sometimes the results from SearchIQ won't be quite what you were expecting. You can easily teach SearchIQ your language as you use it. Over time, it gets smarter about how to interpret terms that don’t come directly from keywords, column names, or data values.

## Teach SearchIQ your Language

To teach SearchIQ your language:

1. After receiving a search result from SearchIQ, notice a section under the search bar that shows the SearchIQ interpretation of what you typed or spoke. If you do not see this, click **Refine your query**.

   Wherever you see **- -**, those terms were ignored. Where you see a word or words, those are the keywords, column names, or data values as understood by SearchIQ.

   Clicking on any term brings up the menu where you can change how ThoughtSpot understands that term.

2. Click any term you want SearchIQ to ignore in the future, and choose **Ignore**.

3. Click any term you wish SearchIQ had interpreted differently, and choose **Teach**.

   ![]({{ site.baseurl }}/images/searchiq_teach.png "Teach SearchIQ")

4. When you see the teaching dialog box, 1) use the handles on the search diagram to select a term for which you want to change the mapping. Then 2) select a column name to map it to, or type your mapping in the search bar below the diagram. 3) You may need to select what you mean from the search suggestions.

   ![]({{ site.baseurl }}/images/searchiq_teach_mapper.png "Teach SearchIQ mapper")

5. Choose **CONFIRM** to see the new search result.

   ![]({{ site.baseurl }}/images/searchiq_after_mapping.png "]SearchIQ after mapping")

6. Repeat these steps until SearchIQ understands how to interpret your search.

   SearchIQ will remember what you taught it, and use that to understand your searches in the future.

## What are some best practices when teaching SearchIQ?

Searchiq learns the meanings of words and phrases as exact matches. Because of this, it is recommended to include the context in the phrase being mapped to improve the accuracy of the mappings.

For example, consider the following search:

“How many travellers are travelling from New York to San Francisco ?”.

You can train SearchIQ to map this natural language search to the keyword search “unique count traveler name source city = ‘new york’ destination name = ‘san francisco’”. However, SearchIQ will not be able to understand whether "new york" is to be considered a match for "new york" as the source city or destination city.

To make the mapping more specific, you should map “from New York” to “source city = ‘New York`” and “to San Francisco” to “destination city = ‘San Francisco`”. This will help SearchIQ match a city to the source city or destination city based on the preceding preposition (to or from).

## What if I teach SearchIQ a different language from somebody else?

SearchIQ learns the language you teach it, and your efforts are useful to everyone else who uses SearchIQ in the future. If SearchIQ learns different search term mappings from different users, these are applied to new searches in a hierarchical fashion, with the top learnings carrying more weight than those further down the list.

The hierarchy of SearchIQ language learning is set up like this:

1. Language mappings the user taught SearchIQ
2. Language mappings the user's [Group members]({{ site.baseurl }}/admin/users-groups/about-users-groups.html) taught SearchIQ
3. [Language mappings set by the administrator]({{ site.baseurl }}/admin/data-modeling/searchiq-mappings.html)

In this way, SearchIQ provides the best and most customized search experience possible for all users, and your efforts to teach it are valuable to as many people as possible.

## Related information

-   [About SearchIQ]({{ site.baseurl }}/end-user/search/about-searchiq.html)
-   [Use SearchIQ]({{ site.baseurl }}/end-user/search/use-searchiq.html)
-   [Modify SearchIQ mappings]({{ site.baseurl }}/admin/data-modeling/searchiq-mappings.html)
