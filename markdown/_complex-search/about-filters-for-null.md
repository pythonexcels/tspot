---
title: ["Filter on null, blank, or empty values"]


last_updated: tbd
summary: "Filtering on NULL and empty values is a special case. "
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Filtering on null, blank, or empty values can be tricky if your data contains both of these. You can use this method to see what's really going on with these types of values, and to get the filtering behavior you want.

## How NULL and blank values are displayed

When you view a table or chart, you may see values that appear as **\{blank\}**. These can actually be one of two types of values:

-   NULL values, which are essentially missing values.
-   blank or empty values, like an empty string of text or a string containing only whitespace (spaces, tabs).

Both of these types of values are represented as **\{blank\}**, but if you filter on **\{blank\}**, the filter will apply to only the NULL values. That is, only the NULL values will be included in your result. It can be hard to tell what's going on if you have a data source that contains both NULL and blank/empty values.

## To show NULL and blank values differently

If you need to differentiate between NULL and blank values, you can [Add a formula](how-to-add-formula.html#) to make them appear differently in charts and tables. In this example, we'll use `<text_column>` to refer to the text column which contains both NULL and blank values:

```
if ( strlen ( <text_column> ) = 0 ) then if ( isnull ( <text_column> ) ) then 'null' else 'empty' else <text_column>
```

This formula will show "null" where the value contained in the column is actually NULL. When the value is blank or empty, it will show up as "empty".

## To allow filtering on both NULL and blank values

If you want to keep the same display format for NULL and blank values, but be able to filter on both using "\{blank\}", your [formula](how-to-add-formula.html#) will be slightly different. You can use a formula like:

```
if ( strlen ( <text_column> ) = 0 ) then null else <text_column>
```

Use the filter you created instead of the original text column in your search to get the desired result.

## Filtering on your formula

After creating formula for what you want to do, you can filter on the formula column you created in the search bar by typing the value **\{blank\}**, which will act as a filter. Or you can filter by left-clicking on a **\{blank\}** value in your search result table, then right-clicking and selecting **Show only "\{Blank\}"**.

 ![]({{ site.baseurl }}/images/formula_null_empty_merge.png "Show only NULL and blank values")
