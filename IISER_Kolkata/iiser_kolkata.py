
pip install rake_nltk

import nltk
nltk.download('punkt')

import nltk
nltk.download('stopwords')

"""**Finding all the ' a ' tags for all the faculties**"""

import urllib3
urllib3.disable_warnings()
import bs4
import pickle

import requests
from bs4 import BeautifulSoup
import sqlite3
from rake_nltk import Rake


### proxy information
###proxy_host = '172.16.2.252'
###proxy_port = '3128'

### Maintaining the first database

db = sqlite3.connect("iiserk_bio.db")
cur = db.cursor()

cur.execute(" CREATE TABLE IISERK_bio( NAME, Research_interest)")

# Create a dictionary with the proxy settings
###proxies = {
###    'http': f'http://{proxy_host}:{proxy_port}',
  ###  'https': f'http://{proxy_host}:{proxy_port}',
###}

#request for scrapping
url = 'https://www.iiserkol.ac.in/web/en/people/faculty/dbs/#gsc.tab=0'

# Send an HTTP GET request to the URL
response = requests.get(url,verify=False)
# response = requests.get(url,verify=False)

#web parsering
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml

# print(soup.prettify())
all_tags = soup.find_all('a')
print((all_tags[76:129])) ###the correct ones

"""**Getting the seperate link for each faculties**"""

import urllib3
urllib3.disable_warnings()
import bs4
import pickle

import requests
from bs4 import BeautifulSoup
import sqlite3
from rake_nltk import Rake

db = sqlite3.connect("iiserk_bio.db")
cur = db.cursor()

cur.execute(" CREATE TABLE IISERK_bio( NAME , Research_focus )")

# Create a dictionary with the proxy settings
#proxies = {
 #   'http': f'http://{proxy_host}:{proxy_port}',
#    'https': f'http://{proxy_host}:{proxy_port}',
#}

#request for scrapping
url = 'https://www.iiserkol.ac.in/web/en/people/faculty/dbs/#gsc.tab=0'


# Send an HTTP GET request to the URL
response = requests.get(url,verify=False)
# response = requests.get(url,verify=False)

#web parsering
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml

# print(soup.prettify())
all_tags = soup.find_all('a')

index = 0
all_tags = all_tags[76:129]
all_tags = all_tags[1::2]

for tag in all_tags: #[76:129] the correct one!!
    index = index+1
    # print(index)
    from lxml import html
    input_string = str(tag)
       # Parse the input string as HTML
    tree = html.fromstring(input_string)
    # Extract the href attribute value
    href_value = tree.xpath('//a/@href')  #getting the seperate link for each faculties
    print(href_value)

"""**Getting all the text on a particular faculty's page**"""

import urllib3
urllib3.disable_warnings()
import bs4
import pickle

import requests
from bs4 import BeautifulSoup
import sqlite3
from rake_nltk import Rake

db = sqlite3.connect("iiserk_bio.db")
cur = db.cursor()

cur.execute(" CREATE TABLE IISERK_bio( NAME , Research_focus )")

# Create a dictionary with the proxy settings
#proxies = {
 #   'http': f'http://{proxy_host}:{proxy_port}',
#    'https': f'http://{proxy_host}:{proxy_port}',
#}

#request for scrapping
url = 'https://www.iiserkol.ac.in/web/en/people/faculty/dbs/#gsc.tab=0'


# Send an HTTP GET request to the URL
response = requests.get(url,verify=False)
# response = requests.get(url,verify=False)

#web parsering
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml

# print(soup.prettify())
all_tags = soup.find_all('a')

index = 0
all_tags = all_tags[76:129]
all_tags = all_tags[1::2]

for tag in all_tags: #[76:129] the correct one!!
    index = index+1
    # print(index)
    from lxml import html
    input_string = str(tag)
    # Parse the input string as HTML
    tree = html.fromstring(input_string)
    # Extract the href attribute value
    href_value = tree.xpath('//a/@href')  #getting the seperate link for each faculties
    #print(href_value)

    # Check if an href attribute was found

    if href_value:
      faculty_url = 'https://www.iiserkol.ac.in' + str(href_value[0])
      faculty_response = requests.get(faculty_url,verify=False) #scrapping each faculty data.
      soup = BeautifulSoup(faculty_response.text,'lxml') #parsering it
      text = soup.text
      print(text)

    else:
      print("No href attribute found.")

"""**Extracting Research Area and Academic Background**"""

import urllib3
urllib3.disable_warnings()
import bs4
import pickle

import requests
from bs4 import BeautifulSoup
import sqlite3
from rake_nltk import Rake

db = sqlite3.connect("iiserk_bio.db")
cur = db.cursor()

cur.execute(" CREATE TABLE IISERK_bio( NAME , Research_focus )")

# Create a dictionary with the proxy settings
#proxies = {
 #   'http': f'http://{proxy_host}:{proxy_port}',
#    'https': f'http://{proxy_host}:{proxy_port}',
#}

#request for scrapping
url = 'https://www.iiserkol.ac.in/web/en/people/faculty/dbs/#gsc.tab=0'


# Send an HTTP GET request to the URL
response = requests.get(url,verify=False)
# response = requests.get(url,verify=False)

#web parsering
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml

# print(soup.prettify())
all_tags = soup.find_all('a')

index = 0
all_tags = all_tags[76:129]
all_tags = all_tags[1::2]

for tag in all_tags: #[76:129] the correct one!!
    index = index+1
    # print(index)
    from lxml import html
    input_string = str(tag)
    # Parse the input string as HTML
    tree = html.fromstring(input_string)
    # Extract the href attribute value
    href_value = tree.xpath('//a/@href')  #getting the seperate link for each faculties
    #print(href_value)

    # Check if an href attribute was found

    if href_value:
      faculty_url = 'https://www.iiserkol.ac.in' + str(href_value[0])
      faculty_response = requests.get(faculty_url,verify=False) #scrapping each faculty data.
      soup = BeautifulSoup(faculty_response.text,'lxml') #parsering it
      text = soup.text
      #print(text)

      ## Research Interest

      start_word = "Research Interest:"
      end_word = "Academic Background:"
      # Find the index of the start and end words in the text
      start_index = text.find(start_word)
      end_index = text.find(end_word)

      if start_index != -1 and end_index != -1:
        extracted_text = text[start_index + len(start_word):end_index]
        research = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace
        print(research)
        # name = name.splitlines()[0]

      else:
        print("Start or end word not found in the text_name.")


      #background
      start_word = "Academic Background:"
      end_word = "Positions:"

      # Find the index of the start and end words in the text
      start_index = text.find(start_word)
      end_index = text.find(end_word)

      if start_index != -1 and end_index != -1:
        extracted_text = text[start_index + len(start_word) :end_index]
        background_ = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace
        print(background_)

      else:
        print("Start or end word not found in the text_area.")

    else:
      print("No href attribute found.")


    faculty_detail = (research, background_)
    cur.execute("INSERT INTO IISERK_bio VALUES (?, ?)", faculty_detail)


db.commit() #saving it the table

"""**Fetching and saving in Pickle format**"""

#fetching

cur.execute("SELECT * FROM IISERK_bio")
rows = cur.fetchall()

if rows:  # Check if there are rows fetched from the database
    st = ''
    r = Rake()

    for row in rows:
        print(row)
        if len(row) > 2:  # Check if the row has the necessary column (index 2)
            st = st + ' ' + str(row[2])
        else:
            print("Column index 2 is out of range for some rows.")

    print(st)
else:
    print("No data found in the table IISERK_bio.")

frequency = []
keywords = []
experience_string = st
r.extract_keywords_from_text(st)
for freq ,keyword in r.get_ranked_phrases_with_scores():
    if freq > 10:
        print(freq,keyword)
        frequency.append(freq)
        keywords.append(keyword)



st = ''' '''
for row in rows:
  print(row)
  st = st + ' ' + str(row[1])

frequency_tagline = []
keywords_tagline = []
tagline_string = r.extract_keywords_from_text(st)
for freq ,keyword in r.get_ranked_phrases_with_scores():
    if freq > 10:
        print(freq,keyword)
        frequency_tagline.append(freq)
        keywords_tagline.append(keyword)



### pickling the data!!
data = {"frequency": frequency,
    "keyword": keywords,
    "frequency_tagline": frequency_tagline,
    "keyword_tagline": keywords_tagline,
    "experience_string" : experience_string,
    "tagline_string" : tagline_string
}
with open('analysis.pkl','wb') as file:
    pickle.dump(data, file)
db.close()
#### saving the important analysis using pickle
