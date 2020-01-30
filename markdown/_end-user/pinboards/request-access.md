---
title: [Request Access]
last_updated: 1/23/2020
summary: "If you cannot view a Pinboard on ThoughtSpot, you can request access to it."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
## Request view access
If you try to share a Pinboard by copying and pasting a link to it, the person you share it with may have to request access. You can avoid this by sharing [using the sharing icon.]({{ site.baseurl }}/end-user/Pinboards/share-Pinboards.html)

If a user receives a link to a Pinboard for which they have neither view nor edit access, the **Request Access** page appears.

![Request access]({{ site.baseurl }}/images/sharing-requestaccess.png "Request access")
<!--{% include image.html file="sharing-requestaccess.png" title="Request access" alt="If you do not have view access to a Pinboard, you can send an email requesting access to it." caption="Request access" %}-->

The user adds an optional message explaining why they need to view or edit the Pinboard, and clicks **Request access** to send an email to the Pinboard owner. The email also goes to your administrator, and to [ThoughtSpot Support]({{ site.baseurl }}/appliance/contact.html).

A message appears, telling the user who owns the Pinboard:

![Access requested]({{ site.baseurl }}/images/sharing-requested.png "Access requested")
<!--{% include image.html file="sharing-requested.png" title="Access requested" alt="When you send an email requesting access to a Pinboard, ThoughtSpot tells you who owns the Pinboard." caption="Access requested" %}-->

ThoughtSpot sends an email notification, requesting view or edit access, to the Pinboard owner. The email includes the user's optional message. The owner then shares the Pinboard with the user.

## Request edit access
You may have view only access to a Pinboard. If you don't have edit privileges, you cannot save any changes you make to the Pinboard. You cannot pin an Answer to that Pinboard, change the Pinboard layout, or delete a visualization.

 If you have view only access, the locked icon ![]({{ site.baseurl }}/images/icon-lock-24px.png "The locked icon"){: .inline} appears next to the Pinboard name.

If you click on that icon, it tells you to request access to the Pinboard to edit it.

![Request edit access]({{ site.baseurl }}/images/sharing-viewonly.png "Request edit access")
<!--{% include image.html file="sharing-viewonly.png" title="Request edit access" alt="If you have view only access to a Pinboard, you must request edit access or request access to the underlying data source." caption="Request edit access" %}-->

To request edit access to a Pinboard, email the owner of the Pinboard.

## Request data access
If you don't have access to a Pinboard's underlying data source, you cannot use features that involve columns based on data you do not have access to. For example, you cannot filter on the Pinboard, Drill down on the Answers in the Pinboard, or run SpotIQ on those Answers. If you attempt to use these features, a notification appears, telling you to request access to the underlying data source.

![Access required]({{ site.baseurl }}/images/sharing-downloadaccessrequired.png "Access required")
<!--{% include image.html file="sharing-downloadaccessrequired.png" title="Access required" alt="If you attempt to complete an action that you cannot do with view only access, a notification appears, telling you to request access to the underlying data source. Click the locked icon next to the Pinboard title to see the underlying data source." caption="Access required" %}-->

 If you do not have access to the data source, the locked icon ![]({{ site.baseurl }}/images/icon-lock-24px.png "The locked icon"){: .inline} appears next to the Pinboard name.

If you click on that icon, it tells you to request access to the data source to interact with the Pinboard. It specifies which data source you need access to. In the image below, you need access to the **Retail Sales** data source.

![Request data access]({{ site.baseurl }}/images/sharing-nodataaccess.png "Request data access")
<!--{% include image.html file="sharing-viewonly.png" title="Request edit access" alt="If you have view only access to a Pinboard, you must request edit access or request access to the underlying data source." caption="Request edit access" %}-->

To request access to a data source, email your administrator.
