
# Convert all Markdown files in this hierarchy
# to Docbook 5 XML
for md in `find markdown -name '*md'`
do
  xml=`echo $md | sed s/\.md/\.xml/`
  dita=`echo $md | sed s/markdown/topics/ | sed s/\.md/.dita/`
  echo "Running pandoc on ${md} ..."
  # echo "pandoc -f gfm -t docbook5 -s -o ${xml} ${md}"
  # echo "C:/Python27/python.exe xml2dita.py ${xml} ${dita}"
  pandoc -f gfm -t docbook5 -s -o "${xml}" "${md}"
  C:/Python27/python.exe xml2dita.py "${xml}" "${dita}"
done
