---
title: [SearchIQ data collection]
last_updated: 09/23/2019
summary: "Learn what data SearchIQ collects about usage and language mappings."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
**SearchIQ is in Beta.**

{% include note.html content="SearchIQ is turned off by default, you can have ThoughtSpot Support enable it for you. SearchIQ is only available in English." %}

SearchIQ collects data to improve its interpretation of natural language search.

Here are some FAQs (frequently asked questions) about data collection in SearchIQ:

**Why does SearchIQ collect data?**

SearchIQ collects data to improve the accuracy of the Natural Language engine in ThoughtSpot. By learning from the  ways in which users express queries, we continuously improve our system.

NOTE: The Web Speech API provided by the user’s browser converts the voice input to text. Each browser implements the Web Speech API differently, so please check the documentation for your browser if you want more information about voice to text.

**What data does SearchIQ collect?**

SearchIQ collects the search query, how it was interpreted by the system, any user interactions with the search result along with the global unique identifier (GUID) for that user. The content of the answer returned by SearchIQ is NOT logged.

SearchIQ does not collect or use voice data.

**What are some examples of data SearchIQ collects?**

Let’s say there is a retail sales worksheet titled RETAIL SALES WORKSHEET, and a user asks the following question using natural language:

“Tell me sales for Nike jackets in 2018”

ThoughtSpot will collect and store the following data:

- The name of the data source on which question was asked (worksheet or tablet, etc): RETAIL SALES WORKSHEET
- The natural language question “Tell me sales for Nike jackets in 2018”.
- How the question was interpreted:

  “tell me” -> --- ,

  “sales” -> “REVENUE”,

  “nike jackets” -> ‘nike jacket sku 3445’ in PRODUCT NAME,

  “in” -> ---, “2018” -> ‘2018’ in SALE DATE.

  Here, “tell me”, “for” and “in” were ignored, “sales” was interpreted as the column name “REVENUE”, “nike jackets” was interpreted as a specific nike jacket in the PRODUCT NAME column, and “2018” was interpreted as a filter on the SALE DATE column.
- The GUID (global unique identifier) of the user

SearchIQ will NOT log the content of the returned answer - i.e. the sale number returned for this question.

**Do any third parties have access to this data?**

Yes, we use a third party service provider, Mixpanel (https://mixpanel.com ), to store and analyze the data we collect.

**Where is this data stored?**

- The data is stored locally on the customer cluster and is accessible only by customer admins and ThoughtSpot employees authorized by the customer.

- The date is stored on Mixpanel servers.

**How is this data secured?**

Mixpanel secures the data in these ways:

Security Overview: https://mixpanel.com/legal/security-overview/

Mixpanel uses TLS to secure data in transit and encrypts data at rest.

Please review the following material regarding the Mixpanel Architecture: https://mixpanel.com/wp-content/uploads/2018/06/System-architecture_June2018.pdf

**What is the retention policy of this data?**
**What happens to the data when it is no longer needed?**

Data can be retained for 5+ years. It is deleted after it is no longer needed.

**Who has access to this data?**

Select ThoughtSpot employees who need to access this data in order to improve the product.

**May I opt out of this data collection?**

Your ThoughtSpot administrator may ask ThoughtSpot to disable SearchIQ data logging for all users in the cluster. Please note that this will impact the accuracy of natural language question interpretation by the system.

## Related information

-   [About SearchIQ]({{ site.baseurl }}/end-user/search/about-searchiq.html)
-   [Use SearchIQ]({{ site.baseurl }}/end-user/search/use-searchiq.html)
-   [Teach SearchIQ your language]({{ site.baseurl }}/end-user/search/teach-searchiq.html)
