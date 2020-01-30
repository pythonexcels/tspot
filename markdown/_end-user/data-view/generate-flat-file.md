---
title: [Create and load a CSV file]
last_updated: tbd
summary: "The simplest way to load data is to upload a CSV or Excel file from the ThoughtSpot Web interface. "
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---

{% include content/web-load-intro.md %}

## Create a CSV file

{% include content/csv-create.md %}

Large organizations typically have a data administrator or department the builds ETL processes. If the data you want is in another system, speak with your ThoughtSpot administrator about getting CSV files extracted from this system.

## Formatting the CSV

{% include content/csv-format.md %}

## Load the CSV File

{% include content/csv-load.md %}

## Troubleshoot uploads

Boolean data must use `TRUE`/`FALSE` values. Other values such as `Y`/`N` are not supported.
