# tspot
Experimental Markdown to DITA Conversion

## Overview

This repository takes a small sample of the Markdown documentation from
https://github.com/thoughtspot/thoughtspot.github.io/tree/6.0/_end-user and
performs an experimental conversion to DITA topics.

## Prerequisites

* Pandoc for conversion of Markdown to XML
* Python 2.7 for cleanup of XML and conversion to DITA topic files

## Running on Individual Files

Use the following two commands to perform the conversion on each Markdown file

$ pandoc -f gfm -t docbook5 -s -o file.xml file.md
$ python2 file.xml file.dita

## Running on All Files

```
#!/bin/bash

# Convert all Markdown files in this hierarchy
# to Docbook 5 XML. Next, convert the Docbook 5
# XML file to DITA using a Python script
for md in `find markdown -name '*md' `
do
  xml=`echo $md | sed s/\.md/\.xml/`
  dita=`echo $md | sed s/markdown/dita/ | sed s/\.md/.dita/`
  echo "Running pandoc on ${md} ..."
  # echo "pandoc -f gfm -t docbook5 -s -o ${xml} ${md}"
  # echo "C:/Python27/python.exe xml2dita.py ${xml} ${dita}"
  pandoc -f gfm -t docbook5 -s -o "${xml}" "${md}"
  python2 xml2dita.py "${xml}" "${dita}"
done
```

The script writes out the following output to show progress:

```
Running pandoc on markdown/_complex-search/aggregation-formulas.md ...
XML2DITA wrote dita/_complex-search/aggregation-formulas.dita
Running pandoc on markdown/_complex-search/about-nested-formulas.md ...
XML2DITA wrote dita/_complex-search/about-nested-formulas.dita
...
```
