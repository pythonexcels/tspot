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
for f in `find $PWD -name '*md'|head -2`
 do d=`dirname $f`
 md=`basename $f`
 xml=`echo $md | sed s/\.md/\.xml/`
 echo "Running pandoc on $f ..."
 pandoc -f gfm -t docbook5 -s -o $xml $md
done
```
