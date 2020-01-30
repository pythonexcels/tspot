---
title: [Download a pinboard as PDF]
last_updated: 10/07/2019
summary: "In ThoughtSpot, you can download the entire pinboard in PDF format, so you can share it with people inside and outside your organization. You have options for adding branding, composing the report of the entire Pinboard or only some of its Visualizations, truncating tables, and many others."
sidebar: mydoc_sidebar
permalink: /:collection/:path.html
---
You can download a Pinboard in PDF format, without downloading each visualization separately. Follow these steps:

1. Click **Pinboards** on the top navigation bar.

     ![]({{ site.baseurl }}/images/click-pinboards.png "Pinboards")

2. Select a Pinboard from the list of Pinboards by clicking on its title.

3. In the open Pinboard, click the **More Options** menu ![more options menu icon]({{ site.baseurl }}/images/icon-ellipses.png){: .inline} (ellipses icon), and select **Download as PDF**.

     ![Download Pinboard as PDF]({{ site.baseurl }}/images/pinboard-download-pdf.png "Download a Pinboard as PDF")

4. In the **Download** window modal, you have two main _Format_ output options:
  * Select **[Pinboard](#pdf-pinboard)** to generate a PDF that combines several visual answers on the same page, just like they appear on the Pinboard.
  * Select  **[Visualizations](#pdf-visualizations)** to print each visualization on its own page of the PDF file.

   ![Choose PDF format: Pinboard or Visualizations]({{ site.baseurl }}/images/pinboard-formats.png "Choose PDF format: Pinboard or Visualizations")

{: id="pdf-pinboard"}
## Download PDG as Pinboard

The Pinboard mode produces a PDF file that looks very similar to the Pinboard inside ThoughtSpot. The highlights and insights appear at the top, and the rest of the Pinboard is on a rectangular grid, with natural page breaks.

Follow these steps to specify additional options:

1. Under **Layout**, select either the _Landscape_ or _Portrait_ page orientation.

2. Click the **More Settings** option.

   Under **Branding**, specify if you want to add a _Footer logo_, _Include page number_, or add _Footer text_.

3. Click **Download**.

![PDF export as Pinboard]({{ site.baseurl }}/images/pinboard-export.png "Export a Pinboard as PDF, either combined, or one visualization to a page")

{: id="pdf-visualizations"}
## Download PDF as Visualizations

When you select **Visualizations**, you now have a choice to print all, or some, of the visualizations in the Pinboard. The highlights and insights appear at the top, and the rest of the visualizations get their own page.

Follow these steps to specify additional options:

1. Under **Layout**, select either the _Landscape_ or _Portrait_ page orientation.

2. Click the **More Settings** option.

    Under **Content**, specify if you want the table visuals to end after filling the whole page by selecting the _Truncate Tables_ option.

3. Add **Branding** details through the _Footer logo_, _Include page number_, or _Footer text_ options.

4. In the list of **Visualizations**, select the visualizations you want in the PDF. Deselect the visualization you don't want.

8. Click **Download**.

![PDF export as Visualizations]({{ site.baseurl }}/images/pinboard-viz-export.png "Export a Pinboard to PDF as Visualizations")


{: id="pdf-examine"}
## Examine the PDF

After the download completes, examine your PDF.

Notice that the PDF produced in **Pinboard** mode combines the visuals on the page in the same manner as the original Pinboard. Contrast this with the PDF produced in **Visualizations** mode: this PDF combines the small adjacent indicator and KPI visuals at the top, and all other visuals and tables appear on their own page.

![Comparing Pinboard PDFs]({{ site.baseurl }}/images/pinboard-pdfs.png "Comparing Pinboard PDFs")
