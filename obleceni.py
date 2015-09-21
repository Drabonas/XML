__author__ = 'Drab'
import xml.sax
pole_catalog=[]

class XMLContextHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.element = None
        self.user_name = None
        self.user_group = None
        self.price = None

    def startElement(self, name, attrs):
        self.element = name

    def endElement(self, name):
        self.element = None
        if name =='catalog_item':
            self.pole_array=[self.user_name,self.user_group,self.price]
            pole_catalog.append(self.pole_array)

    def characters(self, content):
        if self.element == 'item_number':
            self.user_name = content
        if self.element == 'color_swatch':
            self.user_group = content
        if self.element == 'price':
            self.price = content


f = open("text.xml", "r")
xml.sax.parse(f, XMLContextHandler())
f.close()
suma = 0
print pole_catalog
for i in range(len(pole_catalog)):
    suma = suma + float(pole_catalog[i][2])
print 'Cena celkem :' + str(suma + len(pole_catalog)-2)
