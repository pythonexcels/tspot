---
title: [Geo charts]
last_updated: 09/23/2019
summary: "There are three geo charts that let you visualize geographical data in ThoughtSpot."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
Geo charts show data on a map by location. They are geo area, geo bubble, and
geo heatmap charts. And these geo charts can display six types of geographical
data, depending on territory:

-   Country
-   State
-   County
-   Zip code
-   Point (latitude/longitude)
-   Other sub-nation regions (for international countries)

ThoughtSpot supports maps many countries. Please see the complete list in [Geo Map Reference]({{ site.baseurl }}/reference/geomap-reference.html).

## Displayed Geo data

Here is a table that shows which GeoType data can be displayed using which geo chart type.

|GeoType|Geo chart type|Notes|
|-------|--------------|-----|
|Country|Geo area (default), geo bubble, geo heatmap| Can also be regions.|
|County|Geo area (default), geo bubble, geo heatmap| Only for counties in the United States.|
|Point|Geo bubble (default), geo heatmap| Must use both latitude and longitude columns.|
|State|Geo area (default), geo bubble, geo heatmap| Only for states in the United States.|
|Zipcode|Geo bubble (default), geo heatmap| Zip codes in the United States.|
|Other sub-nation regions|Geo area (default), geo bubble, geo heatmap| The display depends on the type of administrative region.|

For data to display in geo charts, your administrator must configure it
as geographical data. If you you don't get an expected map
visualization, contact your administrator so they can configure the system correctly.

## Area charts

Geo area charts highlight the regions of interest, and
display boundaries for various regions.

 ![]({{ site.baseurl }}/images/state_level_geo_area_chart.png "Geo area chart example")

To paint a geo area chart, your search must include a geographical column with appropriate granularity. See [Geo Map Reference]({{ site.baseurl }}/reference/geomap-reference.html).

## Geo bubble charts

Geo bubble charts, like bubble charts, display the value of the measure through the relative
size of the bubble. Zip code data is a good choice for geo bubble charts.

 ![]({{ site.baseurl }}/images/geo_bubble_chart_example.png "Geo bubble chart example")

To paint a geo bubble chart, your search must include a geographical column, or a  latitude and longitude pair.

## Heatmap charts

Heatmap charts are similar to treemap charts: they both use a similar
system of color-coding to represent data values. However, the heatmap does not
use size to measure data, and instead requires an additional attribute.

 ![]({{ site.baseurl }}/images/new_heatmap_look.png "Heatmap chart example")

The value of each cell depends on the measure you choose under **Edit char configuration**.

 ![]({{ site.baseurl }}/images/heatmap_value.png "Heatmap value dropdown")
