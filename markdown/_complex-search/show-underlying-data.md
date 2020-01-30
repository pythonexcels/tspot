---
title: [Show underlying data]

last_updated: tbd
summary: "Viewing the underlying data of your answer gives you an un-aggregated view of the underlying data."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
You can see the most granular details of a given result set, i.e. it shows the
un-aggregated view. This feature lets you understand what an answer consists of.
For example, if you search for `customer region revenue`, the answer shows the
aggregate revenue value for each customer region. Then, you can right-click any row
and then click **Show underlying data**, to see each value which constitutes `revenue`
for any given region.

Only the first 1,000 rows appear when viewing the underlying data. You can
even download the results shown when you choose **Show underlying data** from a
chart. The download file limit is a million rows.

{% include note.html content="Viewing underlying data does not work for answers
that are derived from chasm trap searches. Nor does this feature work for pivot
tables." %}

To show underlying data:

1. Right-click the visualization or table cell of interest
2. Select **Show underlying data**.

   ![]({{ site.baseurl }}/images/show_underlying_data.png "Show underlying data option")

    A new window opens that displays a summary and the underlying data.

3. Optionally, choose to **+ ADD COLUMNS** to add additional data.

   ![]({{ site.baseurl }}/images/add_columns_underlying_data.png "Add columns to underlying data")

4. Click **CONFIRM CHANGES**.

5. Click **DOWNLOAD** to download a CSV file of the data.

   ![]({{ site.baseurl }}/images/showing_underlying_data.png "Download underlying data")
