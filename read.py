from glob import glob
from io import StringIO
from html.parser import HTMLParser
import warc
import re
from bs4 import BeautifulSoup

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

# List any of the WARC files found in the data folder
warc_files = glob('data/*.warc.gz')

# Process each of the WARC files we found
files_processed = 0
for fn in warc_files:
  f = warc.open(fn)
  for record in f:
    url = record.header.get('warc-target-uri', None)
    if not url:
      continue
    html = record.payload.read()
    #


    text = re.sub(r'<.+?>', '', strip_tags(str(html)))
    
    soup = BeautifulSoup(html, 'html.parser')
      
    #finding the div with the id
    #div_bs4 = soup.find('div', {"data-testid": "comment"})
      
  #  print(str(div_bs4))
    files_processed += 1
    print(files_processed)


    text_file = open("data/warcout%d.txt" % files_processed, "w")
    n = text_file.write(str(text))
    text_file.close()



