---
title: ["Enable Columns for SearchIQ"]
last_updated: 09/23/2019
summary: "Let us discuss how to enable SearchIQ for the columns of the data source."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

Before enabling columns, keep in mind these points, and other in-product guidelines:
- Enable no more than fifteen (15) columns for SearchIQ.
- Enable at most one (1) date column.
- Column names should not contain more than 3 words.
- Name the columns well, by optimizing for business users. For example, use _Opportunity Cost_ and avoid `opp_cst`.   
- Avoid indexing descriptive columns, ones that contain more than seven (7) words, or contain values with stop words, such as _is_, _are_, _the_, _what_, and so on). See the [Stop Words]({{ site.baseurl }}/reference/stop-words.html) reference for the full list of stop words.
- For columns that represent formulas with categorical values, set the **Indexing Type** to `PREFIX_AND_SUBSTRING`.

To enable columns in a worksheet for SearchIQ, follow these steps:
1.  Click **Data** on top navigation bar.
2.  Click **Tables**.
3.  Click **Worksheets**.
4.  Select and open the worksheet you want to enable for SearchIQ.
5.  Scroll to the far right, until you see the **SearchIQ Enabled** attribute.  
    Set it to _Yes_ for each column enabled for SearchIQ.   

    ![]({{ site.baseurl }}/images/worksheet-column-enable-searchiq.png "Enable SearchIQ on columns")

6.  Change the **Entity Category** for the columns you marked **SearchIQ Enabled**, from _default_ to one that accurately describes the column.  

    See [Set Entity Categories]({{ site.baseurl }}/admin/data-modeling/set-entity-category.html). The category options are <em>default</em>, <em>person</em>, <em>replace</em>, <em>time</em>, <em>money</em>, <em>product</em>, <em>zip_code</em>, <em>lat_long</em>, <em>company_org</em>, and <em>num_types</em>.

    ![]({{ site.baseurl }}/images/worksheet-column-entity-categories-searchiq.png "Specify entity categories for columns")

7.  Add **Synonyms** for all columns you marked **SearchIQ Enabled**, simply by typing them in the appropriate cell.  See [Add common synonyms]({{ site.baseurl }}/admin/data-modeling/change-visibility-synonym.html) for more information.  

    ![]({{ site.baseurl }}/images/worksheet-column-synonyms-searchiq.png "Specify synonyms")

8.  Change the **Index Type** to `DONT_INDEX` for columns when they must be excluded from indexing. We recommend excluding a column when it is descriptive in nature, =contains a large amount of text, has [stop words]({{ site.baseurl }}/reference/stop-words.html), or for a variety of similar reason.  See [Turn off indexing]({{ site.baseurl }}/admin/data-modeling/change-index.html).  

     ![]({{ site.baseurl }}/images/data-modeling-columns-indextype-dont-index.png "Don't index")

     This prevents SearchIQ from scanning through large amounts of text to understand what user asked. Note that searches on text fields that use the `contains` keyword still work.  

     ![]({{ site.baseurl }}/images/worksheet-column-do-not-index-searchiq.png "Change Index Type to DONT_INDEX")

9.  Change the **Index Type** for columns that represent formulas with categorical values to `PREFIX_AND_SUBSTRING`. See [Turn off indexing]({{ site.baseurl }}/admin/data-modeling/change-index.html).

     ![]({{ site.baseurl }}/images/data-modeling-columns-indextype-prefix-substring.png "Index type for formulas with categorical values")

     ![]({{ site.baseurl }}/images/worksheet-column-prefix-and-substring-searchiq.png "Change Index Type to PREFIX_AND_SUBSTRING")

10. Rename the columns to have names that are shorter (maximum three words), and easier for business users to understand.  

      ![]({{ site.baseurl }}/images/worksheet-column-rename.png "Rename a column")

11. Click **Save Changes**.
