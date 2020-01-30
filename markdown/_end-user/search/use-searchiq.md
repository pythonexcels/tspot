---
title: ["Use SearchIQ"]
last_updated: 09/23/2019
summary: "Use SearchIQ to do a natural language search."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

To search using SearchIQ, follow these steps:

1. Click the ThoughtSpot search bar on the homepage or select **Search** from the top menu.

   ![]({{ site.baseurl }}/images/top_navigation_bar.png "Menu bar")

2. Click the SearchIQ toggle button to go into SearchIQ mode.

   ![]({{ site.baseurl }}/images/choose_searchiq_on.png "SearchIQ toggle button")

   If you later decide to go back to the classic search mode, you can click the SearchIQ toggle button to turn it off again.

3. Choose the data you want to search using the selector in the left panel.

   ![]({{ site.baseurl }}/images/searchiq_select_data_source.png "SearchIQ data selector")

4. Type your search in the search bar using plain language.

   If you see a microphone icon in the search bar, that means your operating system and browser are enabled for speech-to-text. In this case, you can click the microphone and speak your search instead of typing.

5. Press the **Enter** key when your search is complete.

6. When your answer appears, you may also see one or more of these messages:

   * Interpretation: You can see how different words you typed were understood.

     ![]({{ site.baseurl }}/images/searchiq_interpreted.png "SearchIQ interpretation")

   * Ignored words: These words were not needed in order to create the answer, so they are ignored.

     ![]({{ site.baseurl }}/images/searchiq_ignored_words.png "SearchIQ ignored words message")

   * Ambiguous words: These are words that could have more than one meaning in the context of the search.

     ![]({{ site.baseurl }}/images/searchiq_ambiguous.png "SearchIQ ambiguous words message")   

        You can clarify by choosing what you meant from the possible meanings shown.

        ![]({{ site.baseurl }}/images/searchiq_disambiguate.png "SearchIQ clarify selected words")   

7. If you want to see details of how your search was computed, click the **Details** link to the right of the search terms.

   ![]({{ site.baseurl }}/images/searchiq_details.png "SearchIQ details")   

8. If the answer isn't what you were expecting, you can refine your answer by [teaching SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html).

9. If you need help, use [Ask an expert]({{ site.baseurl }}/end-user/search/ask-an-expert.html).

## Related information

-   [About SearchIQ]({{ site.baseurl }}/end-user/search/about-searchiq.html)
-   [Teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html)
-   [Ask an expert]({{ site.baseurl }}/end-user/search/ask-an-expert.html)
