

##############################################################
# toc2ditamap : Create a ditamap based on an HTML  TOC snippet
##############################################################

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
    # sys.argv = ['toc2ditamap.py', 'toc.html', 'tspot.ditamap']
    if len(sys.argv) != 3:
        print ("Command is toc2ditamap.py input.html output.ditamap")
        sys.exit(1)

    if (sys.version_info > (3, 0)):
        print ("Error: this script only works for Python 2, you are running Python 3")
        sys.exit(1)

    time_now = int(time.time())
    fp = open(sys.argv[1])
    fpout = open(sys.argv[2],'w')
    data = fp.read()
    # data = re.sub(r'(?s)<article.*?>','<article>',data)
    # data = re.sub(r'xlink:href','href',data)
    # data = re.sub(r'<br>','',data)
    # data = re.sub(r'xml:id','id',data)
    # data = re.sub(r'<em>Resolved</span>','<em>Resolved</em>',data)
    # data = re.sub(r'<anything></emphasis>','anything</emphasis>',data)
    htmlroot = etree.XML(data)
    root = etree.Element('map')
    title = etree.SubElement(root,'title')
    title.text = 'TSpot Online Help'
    def refresh_root(xml_root):
        rawxml = etree.tostring(xml_root,xml_declaration=False,pretty_print=False,method='xml',encoding='UTF-8')
        return etree.fromstring(rawxml)

    def refresh_htmlroot(html_root):
        rawhtml = etree.tostring(html_root,xml_declaration=False,pretty_print=False,method='html',encoding='UTF-8')
        return etree.fromstring(rawhtml)

    while True:
        clean = True
        for elem in htmlroot.iter():
            # Article -> body
            if elem.tag == 'ul':
                elem.tag = 'topicref'
                elem.attrib.clear()
                continue

            if elem.tag == 'li':
                elem.attrib.clear()
                elem.tag = 'topicref'
                arefs = elem.xpath("./a")
                if not arefs:
                    continue
                aref = arefs[0]
                # if aref.attrib['href'] == '#':
                #     aref.getparent().remove(aref)
                #     elem.getparent().remove(elem)
                #     clean = False
                #     break

                linkref = aref.attrib['href'].replace('/6.0/','topics/').replace('.html','.dita')
                elem.set('href',linkref)
                aref.getparent().remove(aref)
                htmlroot = refresh_htmlroot(htmlroot)
                clean = False
                break

        if clean:
            break

    final = '<?xml version="1.0" encoding="UTF-8"?>\n<!DOCTYPE map PUBLIC "-//OASIS//DTD DITA Map//EN" "map.dtd">\n<map>\n'
    # final += etree.tostring(htmlroot,pretty_print=True)
    core = etree.tostring(htmlroot,xml_declaration=False,pretty_print=True,method='html',encoding='UTF-8').replace(' href="#"','')
    core = re.sub(r'<a>.*?</a>','',core)
    final += core
    final += '\n</map>\n'
    fpout.write(final)
    fpout.close()
    print ("TOC2DITAMAP wrote %s"%sys.argv[-1])
    # bodytext = etree.tostring(root,xml_declaration=False,pretty_print=True,method='xml',encoding='UTF-8')
    # topictext = '<topic id="%s"><title>%s</title>%s\n</topic>'%(base,title,bodytext)

    # newroot = etree.fromstring(topictext)

    # xmltext = etree.tostring(newroot,xml_declaration=True,pretty_print=True,method='xml',encoding='UTF-8')
    # xmltext = re.sub(r'<topic','<!DOCTYPE topic PUBLIC "-//OASIS//DTD DITA Topic//EN" "topic.dtd">\n<topic',xmltext)
    # fpout.write(xmltext)
    # fp.close()
    # fpout.close()

if __name__ == '__main__':
    run()
