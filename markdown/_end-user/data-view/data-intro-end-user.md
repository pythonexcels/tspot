---
title: ["Understand data sources"]
last_updated: tbd
summary: "Use the Data tab to manage data sources."
toc: false
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
The **Data** tab lists all of the tables and data sources available to you. There are three types of data sources that you may see in the data list. They are tables, worksheets, and user uploaded data. You usually see only worksheets and user-uploaded sources. These are the most commonly used data sources for searching.

| Name             | Icon           | Definition                                                       | Created by                |
| ---------------- | -------------- | -----------------------------------                              | ------------------------- |
| Table            |                | Raw table loaded by an Administrator                             | Administrators            |
| Worksheet        |                | Collection of related tables optimized for searching (like standard concept of a _view_) | Anyone |
| User Imported    |                | Table uploaded by a user through the web browser (e.g. as a `.csv` file) | Anyone |
| View             |                | Table saved as a [materialized view]({{ site.baseurl }}/complex-search/about-query-on-query.html) by a user through the web browser through **Save as view** option on a search | Anyone |


![]({{ site.baseurl }}/images/types_of_data_sources_table.png "Types of Data Sources")

Clicking on the name of a table or data source shows you detailed information
about it. You won't be able to change these settings or edit the table unless it
was shared with you with the **Edit** privilege. To see how to edit a data
source, refer to the _ThoughtSpot Administrator Guide_.

Use the filters at the top of the page to find the data you are interested in.
From the **Data** tab, you can also delete or apply stickers to tables and data
sources in bulk by selecting them and clicking the appropriate action button.

![]({{ site.baseurl }}/images/manage_data_page.png "Data page")


## Related information

-   [View your data profile]({{ site.baseurl }}/admin/loading/view-your-data-profile.html)  
Basic column data profile information is available under Profile on the Data page.
-   [About sharing]({{ site.baseurl }}/end-user/data-view/sharing-for-end-users.html)  
Whenever you are working in ThoughtSpot, you are in your own private environment
until you share your work with others. This applies to searches, pinboards, and
any data you upload.
- [Overview of data modeling settings]({{ site.baseurl }}/admin/data-modeling/data-modeling-settings.html)
