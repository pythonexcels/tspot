---
title: [How to use Spot]

last_updated: tbd
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

You can’t ask Spot to do tricks until you after you invite him to a channel and
authorize yourself as a Spot trainer.

##  Call Spot and make him do tricks

1. Launch Slack if you haven't already.
2. Go to a channel where you want to invite Spot.
3. Invite <strong>&#64;spot</strong> like you would invite anyone else.  

   Type <strong>&#64;spot</strong> and press <code>RETURN</code>.

   ![]({{ site.baseurl }}/images/slack-1.png "Invite spot")

4. Click invite them to join.
5. Ask him for help.

   If this is the first time you’ve commanded him, Spot tells you:

   ![]({{ site.baseurl }}/images/spot-2.png "Spot speaks")

5. Take the clicking here link.

   Spot takes you out of Slack and to the ThoughtSpot application.

6. Enter your username and password.  

   If you do this successfully, the application tells you:

    ![]({{ site.baseurl }}/images/spot-3.png "Spot sits")

7. Go back to Slack and ask Spot to list what he does by typing
<strong>&#64;spot</strong> help.

   ![]({{ site.baseurl }}/images/spot-4.png "Spot sits")

   Spot can run a query directly that’s the **1. <anything>** command.

8. Try simply listing your subscriptions.

   ![]({{ site.baseurl }}/images/spot-5.png "Spot sits")

   {% include note.html content="Spot only looks for objects with the
   <strong>spot</strong> sticker on them. Work your way from a pinboard to
   asking for a particular chart." %}

9. Work your way from a pinboard to asking for a particular chart.

     ![]({{ site.baseurl }}/images/spot-6.png)

At this point, you should go onto explore your Spot’s talents on your own!

## Frequently Asked Questions

Whenever possible, Spot answers questions for you directly in channel. Here,
though, are some frequent questions owners ask.

### Can I name my Spot whatever I want?

Sure. This is done by your administrator when the integration is created. Um,
I guess the answer is really “ask your parents?”

### Spot isn’t fetching what I want, why?

Spot can only fetch “toys” that are have the spot sticker. Your administrator
should do this when he sets up ThoughtSpot.

### My spot looks different, why is that?

The screenshots in this document were taken on desktop integration of Slack. If
you are using mobile device, your interactions with Spot will look different.

### How does Spot know you?

The first time you message Spot, it will send back a link which you can click to
link your ThoughtSpot account to Slack account. After the accounts are linked, all
charts you query from Spot will be tied to your permissions/authorization.

### How to subscribe to charts posted to a channel?

Any chart retrieved using spot can be subscribed to, and can have any number of
channel/user subscribers.

### How do I get the list of Spot commands?

Messaging `help` to `spot` gives you a list of commands and how to use them.
