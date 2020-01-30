---
title: [Overview of sharing]
last_updated: 12/10/2019
toc: false
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

Whenever you are working in ThoughtSpot, you are in your own private environment until you share your work with others. Sharing applies to searches, pinboards, and any data you upload. You share by clicking the **Share** button from within the object you want to share and specifying the users or groups with whom you want to share. An email notification goes out to those users or groups when you click **Share**.

## What you can share

This is a list of objects a regular, non-administrator user can share. Administrators have more granular control over data security.

You can share with groups and with individual people. You can share several different types of objects:

|Object type|Description|Default security model|
|-----------|-----------|----------------------|
|Uploaded data|Data you upload using a Web browser.|Only the user who uploaded the data (and any user with administrator privileges) has access to it by default. They can share a table (or selected columns) with other people or groups. See [Share uploaded data](share-user-imported-data.html#).|
|Pinboards|A pinboard of saved search results.|Anyone who can view a pinboard can share it. See [share a pinboard]({{ site.baseurl }}/end-user/pinboards/share-pinboards.html#).|
|Answers|The result of a single search.|Anyone who can view an answer can share it. See [share answers]({{ site.baseurl }}/end-user/pinboards/share-answers.html).|

## Who can share and to whom

You do not have to be an administrator or the owner of an object to share saved answers or pinboards. Any user can share them, based on the access levels the user has.

If you upload a spreadsheet, you can share **Can View** or **Can Edit** privileges with other people, who can further share them with others.  This last point is important. Like sharing a secret, sharing an object or your data can quickly spread in ths way to people you do not intend it to. So, if your data or work is sensitive to your business be thoughtful in how you share it.

Finally, you can revoke access to an object (table, worksheet, or pinboard) that you have previously shared. Unsharing an object is very similar to sharing it.
