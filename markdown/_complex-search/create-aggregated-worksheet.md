---
title: [Save a search as a view]

last_updated: 11/2/2018
summary: "If you want to search on top of another search, try saving your search as a view. Then, you can use the saved view as a data source for a new search."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
This procedure walks you through creating a view from a search. To create a view from a search:

1. Start a new search, or edit an existing visualization from a pinboard.

    Any filters or aggregations created during this search will be reflected in the view.

2. Make any changes to the visualization that you want in your saved view (change aggregation level, filters, etc.)

3. Click the ellipses icon
 ![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline},
and **Save as view**.

     ![]({{ site.baseurl }}/images/save_as_view.png "Save as a View")

4. Give the view a name and save it.

     ![]({{ site.baseurl }}/images/save_view_dialog.png "Name the View")

5. [Link]({{ site.baseurl }}/admin/data-modeling/create-new-relationship.html) your view to any other data source, or [define joins]({{ site.baseurl }}/admin/loading/constraints.html).

At this point the view has been saved, but you may also want to [materialize the view]({{ site.baseurl }}/admin/loading/materialized-views.html), to improve its performance when searching.
