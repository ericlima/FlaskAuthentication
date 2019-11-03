import requests
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from datetime import datetime


API_ENDPOINT = "https://www.cp.pt/sites/passageiros/pt/consultar-horarios/horarios-resultado"

depart = 'Porto - Campanha'
arrival = 'Lisboa - Oriente'
depart_date = datetime.today().strftime('%Y-%m-%d')

data = {
    "depart": depart,
    "arrival": arrival,
    "departDate": depart_date
}

r = requests.post(url = API_ENDPOINT, data = data)

html = r.content.decode()

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()

parser.feed(html)

parser.handle_starttag('tbody','')
parser.handle_endtag('tbody')

tbody = parser.CDATA_CONTENT_ELEMENTS

#root = ET.fromstring(html)

'''
# to parse from file use ET.parse('country_data.xml')

b = {}
for child in root:
    b.update({child[0].text: [child[i].text for i in range(1, len(child) - 2)]})
    b[child[0].text].extend(value for neighbor in child.iter('neighbor') for k, value in neighbor.items())

print(b)

'''


