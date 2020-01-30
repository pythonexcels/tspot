---
title: [Understand formulas in searches]
last_updated: 11/06/2019
summary: "To provide richer insights, you can add a formula to your ThoughtSpot search."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
The Formula Builder includes many types of operators, such as logical (if, then, else), math, date, and text string functions.

You can create a formula from directly within a search. If you have the privilege that allows you to create or edit worksheets, you can also create a formula within a worksheet. Formulas in worksheets act as derived columns, so that anyone who uses the worksheet as a data source will see the formula as just another column.

Adding a formula within a search works much the same way as adding a formula to a worksheet. However, you will be able to edit the formula directly from within the answer. If you add the answer to a pinboard and share it with the **Edit** privilege, other people can see the formula results, too. To make edits to the formula, they also need to have the **Edit** privilege on the underlying data.

-   **[Add a formula to a search]({{ site.baseurl }}/complex-search/how-to-add-formula.html)**  
You can add a formula directly within a search. Some common reasons for using a formula in a search are to perform mathematical functions, check for and replace null values, or add if...then...else logic.
-   **[View or edit a formula in a search]({{ site.baseurl }}/complex-search/edit-formula-in-answer.html)**  
You can always go back and view or edit a formula that has been added to a search. Do this by clicking the edit icon next to its name in the **Columns** listing.
-   **[About aggregate formulas]({{ site.baseurl }}/complex-search/aggregation-formulas.html)**  
When working with formulas, it is useful to understand the difference between regular (or row-wise) formulas and aggregation formulas.
-   **[About conversion formulas]({{ site.baseurl }}/complex-search/conversion-formulas.html)**  
Some formulas require the input to be of a particular data type. If you find that you want to pass a value to the function, but it is of the wrong data type, you can convert it using a conversion formula.
-   **[About date formulas]({{ site.baseurl }}/advanced-search/formulas/date-formulas.html)**  
Date formulas allow you to apply date related functions to your formulas.
-   **[About percent (simple number) calculations]({{ site.baseurl }}/advanced-search/formulas/percent-calculations.html)**  
You can use simple number functions to perform useful percent calculations.
-   **[About conditional formulas (operators)]({{ site.baseurl }}/advanced-search/formulas/conditional-sum.html)**  
Conditional formulas, or operators, allow you to apply `if`/`then`/`else` conditions in your formulas.
-   **[About nested formulas]({{ site.baseurl }}/complex-search/about-nested-formulas.html)**  
Nested formulas, or formula on formula, allow you to reference a formula within another formula.
-   **[About formula support for chasm trap schemas]({{ site.baseurl }}/complex-search/about-formula-support-for-chasm-trap-schemas.html)**  
You can create a formula that involves aggregated measures coming from multiple fact tables of a chasm trap.

Text formulas are also available. These are covered in the comprehensive
**[Formula function reference]({{ site.baseurl }}/reference/formula-reference.html)**,
which provides brief descriptions and examples for all types of formulas. The above topics explain concepts and give step-by-step instructions of how to work with formulas, whereas the reference is a quick cheat sheet.
