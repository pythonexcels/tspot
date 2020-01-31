
from lxml import etree
from xml.sax.saxutils import escape
from PIL import Image
import os
import pdb
import re
import sys
import time
#add spacing under program listing tag
#adjust numbering
#adjust image title and image dimensions
#remove section for notes
#python package pillow
#read the image and get attributes of align, float, file, width, angle, dpi, cropped, position, nsoffset, height
def getImageInfo(filename):
    info = []
    with Image.open(filename) as image:
        width, height = image.size
    widthInches = str(round(width/100))+'in'
    heightInches = str(round(height/100))+'in'
    info.append('aleft') #align
    info.append('0') #float
    info.append(filename) #file
    info.append(widthInches) #width
    info.append('0.000') #angle
    info.append('100') #dpi
    info.append('0') #cropped
    info.append('below') #position
    info.append('0.000in') #nsoffset
    info.append(heightInches) #height
    return info

def exampleBlock(lines):
    data = lines.splitlines()
    data.remove('')
    return data

def run():
    # sys.argv = ['translate.py','c.xml','c.dita']
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


    title = ''
    first_section_title = root.xpath('//section/title')[0].text
    s = re.search(r'\[(.*?)\]',first_section_title)
    if s:
        title = s.group(1)
        root.xpath('//section/title')[0].text = title

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

        if elem.tag == 'emphasis':
            elem.tag = 'i'
            elem.attrib.clear()
            continue

        if elem.tag == 'literal':
            elem.tag = 'codeph'
            continue

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

    # Change <section><title> -> <section><head> by iterating only through
    # those elements
    # for elem in root.xpath("//section/title"):
    #     elem.tag = 'head'

    #change the image markup
    #read the image and get attributes of align, float, file, width, angle, dpi, cropped, position, nsoffset, height
    # for elem in root.xpath("//body/inlinemediaobject"):
    #     imageName = elem[0][0].attrib['fileref']
    #     imageInfo = []
    #     imageInfo = getImageInfo(imageName)
    #     elem.remove(elem[0])
    #     elem.getparent().tag = 'figure'
    #     elem.tag = 'title'
    #     elem.text = 'Image title here'
    #     art = etree.SubElement(elem.getparent(),'art')
    #     art.set('height',imageInfo[9])
    #     art.set('nsoffset',imageInfo[8])
    #     art.set('position',imageInfo[7])
    #     art.set('cropped',imageInfo[6])
    #     art.set('dpi',imageInfo[5])
    #     art.set('angle',imageInfo[4])
    #     art.set('width',imageInfo[3])
    #     art.set('file',imageInfo[2])
    #     art.set('float',imageInfo[1])
    #     art.set('align',imageInfo[0])

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
                figure_image.set('href','https://docs.thoughtspot.com/6.0'+s.group(2))
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
    print ("Wrote %s"%sys.argv[-1])

if __name__ == '__main__':
    run()
