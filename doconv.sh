
# Convert all Markdown files in this hierarchy
# to Docbook 5 XML
for f in `find markdown -name '*md'`
do
  d=`dirname $f`
  md=`basename $f`
  xml=`echo $md | sed s/\.md/\.xml/`
  dita=`echo $xml | sed s/markdown/topics/`
  echo "Running pandoc on ${f} ..."
  # cd ${d}
  pandoc -f gfm -t docbook5 -s -o "${d}/${xml}" "${d}/${md}"
done
