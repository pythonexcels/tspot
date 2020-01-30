
from lxml import etree
from xml.sax.saxutils import escape
from PIL import Image
import sys
import re
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
    if len(sys.argv) != 3:
        print ("Command is translate.py input.xml output.xml")
        sys.exit(1)

    if (sys.version_info > (3, 0)):
        print ("Error: this script only works for Python 2, you are running Python 3")
        sys.exit(1)

    fp = open(sys.argv[1])
    fpout = open(sys.argv[2],'w')
    data = fp.read()
    data = re.sub(r'(?s)<article.*?>','<article>',data)

    #delete the 'article' root tag by setting 'section' as root tag
    section = list(etree.fromstring(data))[1]
    root = section
    #root = etree.XML(data)

    #try setting root to section tag

    #image for svg 6w4h

    #delete notes for markdown section
    for elem in root.xpath("//section/section"):
        if elem.get('{http://www.w3.org/XML/1998/namespace}id') == 'notes-for-markdown-to-xml-methodology':
            elem.getparent().remove(elem)

    for elem in root.iter():

        #clear attributes for section tag
        if elem.tag == 'section':
            elem.attrib.clear()

        #change listitem -> item
        if elem.tag == 'listitem':
            elem.tag = 'item'

        #change itemized list to list w/ attrib unordered
        if elem.tag == 'itemizedlist':
            elem.tag = 'list'
            elem.set('type','Unordered')

        #change orderedlist to list w/ attrib ordered
        if elem.tag == 'orderedlist':
            elem.tag='list'
            elem.set('type','Ordered')

        #change para -> body
        if elem.tag == 'para':
            elem.tag = 'body'

        #change literal -> code
        if elem.tag == 'literal':
            elem.tag = 'code'

        #change programlisting -> example-block
        if elem.tag == 'programlisting':
            lines = elem.text
            elem.attrib.clear()
            elem.text = None
            elem.tag = 'example-block'
            data = exampleBlock(lines)
            for line in data:
                ex = etree.SubElement(elem, 'example-line')
                ex.text = escape(line)

    # Change <section><title> -> <section><head> by iterating only through
    # those elements
    for elem in root.xpath("//section/title"):
        elem.tag = 'head'

    #change the image markup
    #read the image and get attributes of align, float, file, width, angle, dpi, cropped, position, nsoffset, height
    for elem in root.xpath("//body/inlinemediaobject"):
        imageName = elem[0][0].attrib['fileref']
        imageInfo = []
        imageInfo = getImageInfo(imageName)
        elem.remove(elem[0])
        elem.getparent().tag = 'figure'
        elem.tag = 'title'
        elem.text = 'Image title here'
        art = etree.SubElement(elem.getparent(),'art')
        art.set('height',imageInfo[9])
        art.set('nsoffset',imageInfo[8])
        art.set('position',imageInfo[7])
        art.set('cropped',imageInfo[6])
        art.set('dpi',imageInfo[5])
        art.set('angle',imageInfo[4])
        art.set('width',imageInfo[3])
        art.set('file',imageInfo[2])
        art.set('float',imageInfo[1])
        art.set('align',imageInfo[0])

    fpout.write(etree.tostring(root,xml_declaration=True,pretty_print=True,method='xml',encoding='UTF-8'))
    fp.close()
    fpout.close()
    print ("Wrote %s"%sys.argv[-1])

if __name__ == '__main__':
    run()
