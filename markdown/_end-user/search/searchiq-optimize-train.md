---
title: ["Train SearchIQ"]
last_updated: 08/22/2019
summary: "Training SearchIQ ensures a good natural language search experience."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

There are two complementary paths for optimizing SearchIQ to understand natural language search, [Data Modeling](#data-modeling) and [Language Modeling](#language). Also, consider the the [Training Examples](#training-examples)

<div id="data-modeling"></div>
## Data modeling settings ##

[Add experts to the data source]({{ site.baseurl }}/admin/data-modeling/add-expert.html) to enable the [Ask an Expert]({{ site.baseurl }}/end-user/search/ask-an-expert.html) workflow. This supplies users with another path to getting an answer when they get stuck.

<div id="language-modeling"></div>
## Language modeling ##

We bundle SearchIQ with a set of pre-defined templates that help it understand natural language, and return the best possible answers. You can also add your own templates for each data source, and teach it new language interpretations:

<!-- this is not there
#### Teach SearchIQ from the Data Tab ####

   1. Click the **Data** tab.
   2. Click the three dot icon, and choose **Teach**.  

   This takes you to a screen where you can map searches to things in the data.
   For example, you can map the phrase “best movie” to match the search “top movie_title sort by imdb_score”.

    -->

### Teach SearchIQ using a saved SearchIQ answer ###

See [Teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html).

   1. Select a saved answer.
   2. Click one of the drop-down phrases that shows how SearchIQ interprets the search terms, and click **Teach**.

### Use new searches to teach SearchIQ ###

   We recommend that you train SearchIQ by performing at least 50 natural language searches. This teaches SearchIQ how to map common questions to relevant entities. Use points described in [Teach SearchIQ]({{ site.baseurl }}/end-user/search/teach-searchiq.html) for any unexpected answers.

   - For best results, use simple and short queries.
   - Ask questions that contain only exact column names or their synonyms.
   - Use exact values for filtering.
   - Use keywords. See [Keywords]({{ site.baseurl }}/reference/keywords.html).
   - Use stopwords. See [Stop Words]({{ site.baseurl }}/reference/stop-words.html).

   When SearchIQ returns a satisfactory table or chart, remember to click the **Looks Good** button to provide the necessary feedback.

<div id="training-examples"></div>
## Training Examples for SearchIQ ##

**Example 1: where are the best sales**

In this example, the query returned a very good answer, by interpreting _where_ as _Store City_ and _best_ as _sort by Sales_. The chart **Looks Good**, and this is valuable feedback for training SearchIQ.

![]({{ site.baseurl }}/images/worksheet-searchiq-training-example1.png "Click Looks Good on a bar chart")

**Example 2: which state has the lowest volume**

In this example, the query returned a very good answer, by inerpreting _lowest_ as _sort by Quantity_ and _volume_ as _Quantity_. This chart also **Looks Good**, and provides valuable feedback for training SearchIQ.

![]({{ site.baseurl }}/images/worksheet-searchiq-training-example2.png "Click Looks Good on a map")

<!-- comment from vk: As part of this training we would never use Ask an Expert (as data source owner who is training is an expert)

**Example 3: where should i build a new store**

This example was not as successful as the previous ones; it just returned a simple table with Store City and Store Name columns. The question is too sophisticated for SearchIQ, so we **Ask an expert** how to improve the answer.

![]({{ site.baseurl }}/images/worksheet-searchiq-training-example3.png "Click ask an expert")
-->
