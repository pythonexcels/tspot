---
title: [Following pinboards]
last_updated: 1/17/2020
summary: "In ThoughtSpot, you can follow Pinboards and schedule email notifications to regularly review the visuals that represent dynamic data."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
When you follow a pinboard, ThoughtSpot sends you regular emails that contain the snapshot of the pinboard. You can change the scheduling of this email to suit your business needs.

{: id="pinboard-follow"}
## Follow Pinboards

Complete the following steps to follow a Pinboard:

1. Click **Pinboards** on the top navigation bar.

     ![]({{ site.baseurl }}/images/click-pinboards.png "Pinboards")

2. On the Pinboard list page, select a Pinboard by clicking on it.

3. Click **Follow** at the top right corner of the Pinboard.

   ![Follow Pinboard]({{ site.baseurl }}/images/follow-pinboard.png "Follow Pinboard")

   This action opens the scheduler.  See [Schedule Pinboard reports](#pinboard-follow-schedule).

Notice that after you configure the schedule, the Pinboard appears as **Following**.

![Followed Pinboard]({{ site.baseurl }}/images/followed-pinboard.png "Followed Pinboard")

{: id="pinboard-follow-schedule"}
## Schedule Pinboard reports  

In the **Follow** scheduler, specify the email schedule by marking the appropriate options in the pulldown menus. The default schedule is weekly, on the day and time when you configure the schedule.

<!--![Schedule the notifications]({{ site.baseurl }}/images/follow-schedule.png "Schedule the notifications")-->

<!--![Schedule the notifications]({{ site.baseurl }}/images/pinboard-follow-schedule.png "Schedule the notifications")-->

{% include content/schedule-details.md %}

![Schedule weekly Pinboard notifications]({{ site.baseurl }}/images/pinboard-follow-schedule-weekly.png "Schedule weekly Pinboard notifications")

![Schedule daily Pinboard notifications]({{ site.baseurl }}/images/pinboard-follow-schedule-daily.png "Schedule daily Pinboard notifications")

![Schedule monthly Pinboard notifications]({{ site.baseurl }}/images/pinboard-follow-schedule-monthly.png "Schedule monthly Pinboard notifications")

Click **Save**.

If the user account is not configured with an email, you must supply one at this time.

{: id="schedule-change"}
## Change the schedule

To change the existing time interval and the timing of notifications, click **Following** in the top right corner of the Pinboard.

When the scheduling interface appears, make the necessary changes, and click **Save**.

{: id="pinboard-unfollow"}
## Unfollow Pinboard

To stop following a Pinboard, click **Following** in the top right corner.

When the scheduling interface appears, click **Unfollow**.

![Unfollow Pinboard]({{ site.baseurl }}/images/pinboard-unfollow.png "Unfollow Pinboard")
