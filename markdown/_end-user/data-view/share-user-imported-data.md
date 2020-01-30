---
title: [Share uploaded data]
last_updated: 1/17/2020
summary: When you upload data to ThoughtSpot, you can share it with others.
toc: false
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
![Share data]({{ site.baseurl }}/images/sharing-data.gif "Share data")
<!--{% include image.html file="sharing-data.gif" title="Share data" alt="Learn how to share data." caption="Share data" %}-->

If you upload a spreadsheet, you can share **Can View** or **Can Edit**
privileges with other people, who can further share them with others.

## Understand data sharing

Data that you upload from a Web browser is only visible to you and to the
administrator. You can share the entire uploaded table, or only some of its
columns.

By default, if you share only some table columns, users with access to those
columns cannot see the other columns' data in their searches. However, the data
can become visible if a worksheet or pinboard that _also contains_ those columns
is shared with these users.

If you want to prevent other users from revealing your excluded columns,
you can ask your administrator to enable a stricter behavior.

You can share data [from the **Data** tab]({{ site.baseurl }}#share-datatab), or [from within the table, worksheet, or view]({{ site.baseurl }}#share-dataset) that you want to share.

{: id="share-datatab"}
## Share from the Data tab
To share uploaded data from the **Data** tab, follow these steps.

1. Click **Data** on the top navigation bar.

2. Hover over the uploaded data you want to share and select it by clicking the empty checkbox that appears.

3. Click **Share**.

    ![Share the data]({{ site.baseurl }}/images/sharing-data.png "Share the data")
    <!--{% include image.html file="sharing-data.png" title="Share the data" alt="Select the data you want to share and click the share icon." caption="Share the data" %}-->

4. Select **Entire Table** or **Specific Columns**.

    ![Specify sharing type]({{ site.baseurl }}/images/sharing-datacolumns.png "Specify sharing type")
    <!--{% include image.html file="sharing-datacolumns.png" title="Specify sharing type" alt="Select either entire table or specific columns." caption="Specify sharing type" %}-->

5. If you select **Specific Columns**, select the column(s) you want to share. If you select **Entire Table**, skip to step 6.

    {% include note.html content="You cannot click multiple columns at once. You must input the users or groups with whom you want to share for each column." %}

6. Click **+ Add users or groups** and select the users and groups with whom you want to share.

    ![Add users or groups]({{ site.baseurl }}/images/sharing-data-addusers.png "Add users or groups")
    <!--{% include image.html file="sharing-data-addusers.png" title="Add users or groups" alt="Add the users and groups you want to have access to the dataset." caption="Add users or groups" %}-->

7. [Specify permissions]({{ site.baseurl }}#specify-permissions).

{: id="share-dataset"}
## Share from within the dataset
To share data from within the dataset, follow these steps.
1. Navigate to the dataset you want to share.

2. Click the ellipsis icon ![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline}, and then click **Share**.

    ![Share the data]({{ site.baseurl }}/images/sharing-data-in-dataset.png "Share the data")
    <!--{% include image.html file="sharing-data-in-dataset.png" title="Share the data" alt="Click the three-dot ellipsis icon and then click Share." caption="Share the data" %}-->

3. Select the users or groups with whom you want to share.<br>
    You can only share the entire table, worksheet, or view. You cannot share individual columns. To share individual columns, share [from the **Data** tab]({{site.baseurl }}#share-datatab).

4. [Specify permissions]({{ site.baseurl }}#specify-permissions).

{: id="specify-permissions"}
## Specify permissions
7. Configure the level of access by selecting from the dropdown list. You can select:
    -   **Can View** to provide read-only access. This enables viewing the table or other data source's data, as well as defining worksheets based on that data.
    -   **Can Edit** to allow modification. This enables renaming, modifying, or deleting the entire table or other data source and adding or removing its columns.

    ![Specify permissions]({{ site.baseurl }}/images/sharing-data-privileges.png "Specify permissions")
    <!--{% include image.html file="sharing-data-privileges.png" title="Specify permissions" alt="Configure the user or group's level of access by selecting 'can view' or 'can edit.'" caption="Specify permissions" %}-->

8. Click **Add**.

9. Click **Done**.

10. The **Share settings updated** notification appears on the bottom of your screen.

    ![Share settings updated]({{ site.baseurl }}/images/sharing-settingsupdated.png "Share settings updated")
    <!--{% include image.html file="sharing-settingsupdated.png" title="Share settings updated" alt="After you click Done, the 'Share settings updated' notification appears." caption="Share settings updated" %}-->
