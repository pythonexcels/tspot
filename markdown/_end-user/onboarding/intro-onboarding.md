---
title: [Onboarding Users]
last_updated: 10/07/2019
summary: "Guided onboarding simplifies the initial engagement that new users have with ThoughtSpot, and encourages it adoption throughout your organization."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

Onboarding enables users to master the key workflows of ThoughtSpot, and makes them productive and capable users in a very short time.

When you create a new user, we recommend that you add them to a user group immediately. Configure that user group to use a specific data source, choose up to three initial pinboards, and specify the text of the welcome email.

{: id="onboarding-prerequisites"}
## Prerequisites for onboarding ##

{: id="onboarding-valid-email"}
- **Valid emails**  All users must have valid emails.

  To include users in the onboarding process, each user profile must include a valid email address; see [Create a user]({{ site.baseurl }}/admin/users-groups/add-user.html#add-user).  

  To load and validate user information (including email addresses) in bulk, we recommend using Active Directory configuration and sync. See [Configure LDAP for Active Directory]({{ site.baseurl }}/admin/setup/LDAP-config-AD.html).

{: id="onboarding-tscli-configuration"}
- **Onboarding configuration**  Before starting the onboarding process, an administrator must specify the configuration through the [tscli onboarding command]({{ site.baseurl }}/reference/tscli-command-ref.html#tscli-onboarding).

{: id="onboarding-process"}
## Onboarding Process ##

The key workflows that enable successful onboarding include the following:

1. Configure and save a default Pinboard (or Pinboards) for new users. Alternatively, determine what default Pinboards you plan to use for each user group.

   See steps for [creating a pinboard]({{ site.baseurl }}/end-user/pinboards/about-pinboards.html#create-a-pinboard).

2. Create a new user group, or edit an existing user group to which new users belong:
   - specify the group name and its display name
   - set the sharing visibility to visible
   - specify the Privileges
   - select up to 3 default pinboards
   - test and customize the test welcome email.
   See steps for [creating a user group]({{ site.baseurl }}/admin/users-groups/add-group.html#add-group) or [editing a user group]({{ site.baseurl }}/admin/users-groups/add-group.html#edit-group).

3. Create a new user and assign them to the group you are using for onboarding. See steps for [creating a new user]({{ site.baseurl }}/admin/users-groups/add-user.html#add-user). You can also add existing users to the group; see

   In addition to creating a new user directly in ThoughtSpot, you can add users in bulk through [Active Directory]({{ site.baseurl }}/admin/setup/active-directory-based-access.html).

4. When the new user signs in for the first time, the ThoughtSpot onboarding process starts automatically and guides them through a few basic scenarios of using the application.
   See [User onboarding experience]({{ site.baseurl }}/end-user/onboarding/user-onboarding-experience.html).

5. **\[Optional\]** Any user can repeat their onboarding experience at any time. Simply select **Profile** from user icon on the top right corner of the page. Under **Preferences > New user onboarding**, click **Revisit**.  See [Revisit onboarding]({{ site.baseurl }}/end-user/introduction/about-user.html#onboarding).

{: id="data-source-recommendation"}
<!--SCAL-51041-->
## Notes on Data Source recommendation

User groups in ThoughtSpot can be hierarchical, and each user can belong to multiple groups. Because of this, the choice of the Recommended Data Source may be be surprising, both to users and admins.

We determine the default Data Source for **each user** based on these criteria:

* Consider all default Pinboards, across all Groups
* Identify Data Sources associated with these Pinboards
* Rank the Data Sources on frequency of use
* Select the highest ranked Data Source

Admins can preview onboarding flow for any given user, and adjust the selection of default Pinboards.
