---
title: ["About SearchIQ"]
last_updated: 09/23/2019
summary: "With SearchIQ, you can search your data through natural language, just like speaking."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

<div class="alert alert-info" role="alert">
 <p><strong><i class="fa fa-info-circle"></i>  Note: SearchIQ is in Beta</strong></p>
 <ul type="square">
  <li>SearchIQ is only available in English.</li>
  <li>The feature is off by default; to enable it, contact <a href="mailto:support@thoughtspot.com?subject=SearchIQ%20Reguest&body=I%20want%20to%20try%20SearchIQ">ThoughtSpot Support</a>.</li>
  <li>You must have the <strong>Can use experimental features</strong> permission.</li>
</ul>
</div>

To understand natural language search, SearchIQ collects data on searches and user-language preferences. Find more information about what SearchIQ collects at [SearchIQ data collection]({{ site.baseurl }}/end-user/search/searchiq-data-collection.html).

SearchIQ is a different search experience that understands more natural, speech-like search language than the [original ThoughtSpot search]({{ site.baseurl }}/end-user/search/about-starting-a-new-search.html). For example, you can search for `What was my top selling product last month?`, instead of typing `top 1 product by sales last month`. You can also speak your search using the voice-to-text capability of your operating system.

## How do I use SearchIQ?


Search IQ collects data to improve accuracy of natural language interpretation. For more details, see [SearchIQ data collection]({{ site.baseurl }}/end-user/search/searchiq-data-collection.html).

Clicking on the search bar on your homepage, or clicking **Search** in the top menu bar takes you to the search screen.

From here, if SearchIQ is enabled for you by your administrator, you can see a **SearchIQ** toggle button to the right of the search bar.

 ![]({{ site.baseurl }}/images/choose_searchiq.png "Search bar")

Switch it to the on position. This puts the search into SearchIQ mode, and you can now type in a search using plain, speech-like language.

If you leave the **SearchIQ** setting in the off position, you have the [original ThoughtSpot search experience]({{ site.baseurl }}/end-user/search/about-starting-a-new-search.html), which uses keywords, column names, and data values.

## What kinds of things can I type?

Like regular search, SearchIQ is based on the tables that exist in your data. Tables are made of rows and columns, like spreadsheets. So you can search by typing in any of these words:

-   The column name: like revenue, product name, or store
-   Any of the values in the columns: like 20000, kitten chow, or richmond
-   One of the special [keywords]({{ site.baseurl }}/reference/keywords.html#) ThoughtSpot understands: like yesterday, &gt;, or contains

What's different about SearchIQ is that the form of your question can be more like natural language. This means that SearchIQ ignores extraneous words like `What was the` or `Can you show me`. If you find that your natural language search doesn't return the results you expect, you can [teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html) easily.

## How do I use voice search with SearchIQ?

The ability to do voice search comes with your computer's operating system and your browser's speech-to-text capabilities. As such, it isn't provided by ThoughtSpot. But you can take advantage of these when searching with SearchIQ.

Make sure your microphone on your computer is enabled and working correctly. If you're unsure, check the documentation for your operating system.

Next, make sure your browser supports the text-to-speech capability by consulting its documentation.

If all is well, you can see a microphone icon it the search bar, when it is in SearchIQ mode. Clicking on the microphone will begin accepting voice input, which is translated to text in the search bar.

{% include note.html content="If the SearchIQ text-to-speech functionality is not working, ensure that you are accessing ThoughtSpot in your browser using HTTPS:// and not HTTP://." %}

## Related information

-   [SearchIQ Data Collection]({{ site.baseurl }}/end-user/search/searchiq-data-collection.html)
-   [Use SearchIQ]({{ site.baseurl }}/end-user/search/use-searchiq.html)
-   [Teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html)
