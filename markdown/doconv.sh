
# Convert all Markdown files in this hierarchy
# to Docbook 5 XML
for f in `find $PWD -name '*md'`
do
  d=`dirname $f`
  md=`basename $f`
  xml=`echo $md | sed s/\.md/\.xml/`
  echo "Running pandoc on ${f} ..."
  cd ${d}
  pandoc -f gfm -t docbook5 -s -o "${xml}" "${md}"
done
