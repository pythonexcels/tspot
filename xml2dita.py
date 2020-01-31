

############################################################
# xml2dita : Convert XML output from Pandoc into DITA
#            for some very specific cases
############################################################

from lxml import etree
from xml.sax.saxutils import escape
from PIL import Image
import os
import pdb
import re
import sys
import time


def exampleBlock(lines):
    data = lines.splitlines()
    data.remove('')
    return data

def run():
    # sys.argv = ['translate.py','markdown/_complex-search/period-searches.xml','topics/_complex-search/period-searches.dita']
    if len(sys.argv) != 3:
        print ("Command is translate.py input.xml output.xml")
        sys.exit(1)

    if (sys.version_info > (3, 0)):
        print ("Error: this script only works for Python 2, you are running Python 3")
        sys.exit(1)

    time_now = int(time.time())
    fp = open(sys.argv[1])
    fpout = open(sys.argv[2],'w')
    lines = fp.readlines()
    base = os.path.basename(sys.argv[1])
    base = re.sub(r'\.','_',base)
    section_count = 1
    for cnt,line in enumerate(lines):
        if line.startswith('<section'):
            lines[cnt] = '<section id="%s-%d">'%(base,section_count)
            section_count += 1
            continue
        if '<!DOCTYPE' in line:
            lines[cnt] = '<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n'
            continue

    # data = fp.read()
    data = ''.join(lines)
    data = re.sub(r'(?s)<article.*?>','<article>',data)
    data = re.sub(r'xlink:href','href',data)
    data = re.sub(r'<br>','',data)
    data = re.sub(r'xml:id','id',data)
    data = re.sub(r'<em>Resolved</span>','<em>Resolved</em>',data)
    data = re.sub(r'<anything></emphasis>','anything</emphasis>',data)
    root = etree.XML(data)

    #delete the 'article' root tag by setting 'section' as root tag
    # section = list(etree.fromstring(data))[1]
    # root = section

    #delete notes for markdown section
    # for elem in root.xpath("//section/section"):
    #     if elem.get('{http://www.w3.org/XML/1998/namespace}id') == 'notes-for-markdown-to-xml-methodology':
    #         elem.getparent().remove(elem)

    # root = list(etree.fromstring(data))[1]

    def refresh_root(xml_root):
        rawxml = etree.tostring(xml_root,xml_declaration=False,pretty_print=False,method='xml',encoding='UTF-8')
        return etree.fromstring(rawxml)

    # Try to extract the title for the document
    title = ''
    first_section_title = root.xpath('//section/title')[0].text
    s = re.search(r'\[(.*?)\]',first_section_title)
    first_paragraph = root.xpath('//para')[0]
    first_paragraph_contents = first_paragraph.text
    spara = re.search(r'(?s)^\s*title:\s*\[(.*?)\]\s*',first_paragraph_contents)

    if s:
        title = s.group(1)
        root.xpath('//section/title')[0].text = title
    elif spara:
        title = spara.group(1)
        root.xpath('//section/title')[0].text = title
        first_paragraph.getparent().remove(first_paragraph)
        root = refresh_root(root)

    # Remove <info>
    info_elements = root.xpath('//info')
    if info_elements:
        info_elements[0].getparent().remove(info_elements[0])
    root = refresh_root(root)

   # Unordered list
   # <itemizedlist spacing="compact">
   #   <listitem>
   #     <para>
   #       <link linkend="aggregate">Aggregate</link>
   #     </para>
   #   </listitem>
    for elem in root.iter():
        # Article -> body
        if elem.tag == 'article':
            elem.tag = 'body'
            continue

        if elem.tag == 'para':
            elem.tag = 'p'
            continue

        if elem.tag == 'emphasis' or elem.tag == 'em':
            elem.tag = 'i'
            elem.attrib.clear()
            continue

        if elem.tag == 'literal':
            elem.tag = 'codeph'
            continue

        # if elem.tag == 'link':
        #     elem.tag = 'xref'
# <xref keyref="genus" format="dita">
#     <link xlink:href="how-to-add-formula.html#">Add a formula</link> to

        if elem.tag == 'itemizedlist' and 'type' in elem.attrib and elem.attrib['type'] == 'Unordered':
            elem.tag = 'ul'
            elem.attrib.clear()
            continue

        if elem.tag == 'itemizedlist':
            elem.tag = 'ul'
            elem.attrib.clear()
            continue

        #change listitem -> item
        if elem.tag == 'listitem':
            elem.tag = 'li'
            continue

        #change itemized list to list w/ attrib unordered
        if elem.tag == 'itemizedlist':
            elem.tag = 'list'
            elem.set('type','Unordered')
            continue

        #change orderedlist to list w/ attrib ordered
        if elem.tag == 'orderedlist':
            elem.tag='ol'
            continue

        if elem.tag == 'link' and elem.attrib and 'linkend' in elem.attrib:
            this_link = elem.attrib['linkend']
            del(elem.attrib['linkend'])
            elem.attrib['keyref'] = this_link
            elem.tag = 'xref'
            continue

        #clear attributes for section tag
        # if elem.tag == 'section':
        #     elem.attrib.clear()

        #change para -> body
        # if elem.tag == 'para':
        #     elem.tag = 'body'

        #change literal -> code
        # if elem.tag == 'literal':
        #     elem.tag = 'code'

        #change programlisting -> example-block
        # if elem.tag == 'programlisting':
        #     lines = elem.text
        #     elem.attrib.clear()
        #     elem.text = None
        #     elem.tag = 'example-block'
        #     data = exampleBlock(lines)
        #     for line in data:
        #         ex = etree.SubElement(elem, 'example-line')
        #         ex.text = escape(line)

    fig_count = 1
    while True:
        clean = True
        for elem in root.xpath("//p"):
            ptext = elem.text
            # if 'Change axis filter' in ptext:
            #     pdb.set_trace()
            s = re.search(r'(?s)\s*!\[(.*?)\]\({{\s+site.baseurl\s+}}(/images/.*?) "(.*?)"\)\s*',ptext)
            if s:
                elem.tag = 'fig'
                elem.attrib['id'] = 'fig_%d_%d'%(time_now,fig_count)
                figure_title = etree.SubElement(elem,'title')
                figure_title.text = ' '.join(s.group(3).split())
                figure_image = etree.SubElement(elem,'image')
                # figure_image['href'] = 'https://docs.thoughtspot.com/6.0'+s.group(2)'
                figure_image.set('href','https://docs.thoughtspot.com/6.0'+s.group(2).split()[0])
                # figure_image['id'] = 'image_%d_%d'%(time_now,fig_count)'
                figure_image.set('id','image_%d_%d'%(time_now,fig_count))
                figure_image.set('scope','external')
                elem.text = ''
                clean = False
                root = refresh_root(root)
                fig_count += 1
                break
            if re.match(r'(?s)^\s*{:\s+id=".*?"}\s*$',ptext):
                elem.getparent().remove(elem)
                clean = False
                root = refresh_root(root)
                break
        if clean:
            break

   # ![Change axis]({{ site.baseurl }}/images/edit-axis.png "Change
   #  Axis for Total Sales")

    bodytext = etree.tostring(root,xml_declaration=False,pretty_print=True,method='xml',encoding='UTF-8')
    topictext = '<topic id="%s"><title>%s</title>%s\n</topic>'%(base,title,bodytext)

    newroot = etree.fromstring(topictext)

    xmltext = etree.tostring(newroot,xml_declaration=True,pretty_print=True,method='xml',encoding='UTF-8')
    xmltext = re.sub(r'<topic','<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n<topic',xmltext)
    fpout.write(xmltext)
    fp.close()
    fpout.close()
    print ("XML2DITA wrote %s"%sys.argv[-1])

if __name__ == '__main__':
    run()
