---
title: [Nested formulas]


last_updated: tbd
toc: false
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Nested formulas, or formula on formula, allow you to reference a formula within
another formula. This graphic illustrates how you would define a formula and
then reference it from another:

![]({{ site.baseurl }}/images/nested_formulas_example.png "formula1 nested in formula2")

These formulas become columns, and are even suggested within the Formula
Builder. There is no limit to the nesting depth you can create.

ThoughtSpot doesn't allow users to create invalid formulas, such as cyclic
(loops) or inconsistent aggregation formulas. To support this, formulas have
dependency awareness.  For example, you cannot delete a formula that is nested
in another. Also, formula dependency awareness ensures that you do not break any dependent
formulas while editing a formula with dependent formulas. For example, common
cases of invalidating occur when users try to change a data type.  

Nesting enables encapsulation and decomposition of formula logic.  Meaning, you
may have a staff member create some small useful formulas that others can use.
This also minimizes duplication of formulas.
