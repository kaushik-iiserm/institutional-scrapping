import urllib3
urllib3.disable_warnings()
import bs4
import pickle

import requests
from bs4 import BeautifulSoup
import sqlite3
from rake_nltk import Rake


### proxy information
proxy_host = '172.16.2.252'
proxy_port = '3128'

### Maintaining the first database
db = sqlite3.connect("iiserm.db")
cur = db.cursor()

cur.execute(" CREATE TABLE IISERM( NAME, Research_area , Research_focus )")

# Create a dictionary with the proxy settings
proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_host}:{proxy_port}',
}

#request for scrapping
url = 'https://www.iisermohali.ac.in/faculty/people/faculty'

# Send an HTTP GET request to the URL
response = requests.get(url,proxies=proxies,verify=False)
# response = requests.get(url,verify=False)

#web parsering
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml

# print(soup.prettify())
all_tags = soup.find_all('a')
# print(all_tags[60])


index = 0
for tag in all_tags[118:225]: #[118:225] the correct one!!

    index = index+1
    # print(index)
    if index != 27: #exclude the 503 undispencreries.
    
        from lxml import html

        input_string = str(tag)
        
        # Parse the input string as HTML
        tree = html.fromstring(input_string)

        # Extract the href attribute value
        href_value = tree.xpath('//a/@href')  #getting the seperate link for each faculties

        # Check if an href attribute was found
        if href_value:
            # print('https://www.iisermohali.ac.in' + str(href_value[0]))
            faculty_url = 'https://www.iisermohali.ac.in' + str(href_value[0])
            
            faculty_response = requests.get(faculty_url,proxies=proxies,verify=False) #scrapping each faculty data.
            soup = BeautifulSoup(faculty_response.text,'lxml') #parsering it
            text = soup.text
            
            ## Name of the professor with Designation
            start_word = "Dr."
            end_word = "- IISER Mohali"
            # Find the index of the start and end words in the text
            start_index = text.find(start_word)
            end_index = text.find(end_word)

            if start_index != -1 and end_index != -1:
                # Extract the text between the start and end words
                extracted_text = text[start_index + len(start_word):end_index]
                name = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace

            else:
                print("Start or end word not found in the text_name.")
            
            ## Research Area
            start_word = "Research Area"
            end_word = "Research Focus"
            # Find the index of the start and end words in the text
            start_index = text.find(start_word)
            end_index = text.find(end_word)

            if start_index != -1 and end_index != -1:
                # Extract the text between the start and end words
                extracted_text = text[start_index + len(start_word):end_index]
                research_area = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace
                # print(research_area)
            else:
                print("Start or end word not found in the text_area.")
                research_area = ''        
            
            ## Research Focus
            start_word = "Research Focus"
            end_word = "Selected Publications"
            # Find the index of the start and end words in the text
            start_index = text.find(start_word)
            end_index = text.find(end_word)

            if start_index != -1 and end_index != -1:
                # Extract the text between the start and end words
                extracted_text = text[start_index + len(start_word):end_index]
                research_focus = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace
                # print(research_focus)
            else:
                print("Start or end word not found in the text_area.")
                research_focus = ''
            
            
        else:
            print("No href attribute found.")
        ### table is created, just create the instance for the (name, research_focus, ...) into the sqlite3
        faculty_detail = (name,research_area,research_focus)
        cur.execute("INSERT INTO IISERM  VALUES (?, ?, ?)", faculty_detail)

db.commit() #saving it the table

#fetching the data from sqlite3 for analysis
cur.execute("SELECT * FROM IISERM") #we need to delete the table data and run the code once when the code is bug-free!!
rows = cur.fetchall()

st = ''' '''
list_ex = []

## We create the instances of Rake and put our combined string for keyword extractions.


## Research focus
r = Rake(min_length=5, max_length=15)

for row in rows:
    # print(row)
    st = st + ' ' + str(row[2])
    list_ex.append(str(row[2]))


frequency = []
keywords = []
experience_string = list_ex
r.extract_keywords_from_text(st)
for freq ,keyword in r.get_ranked_phrases_with_scores():
    if freq > 10:
        # print(freq,keyword)
        frequency.append(freq)
        keywords.append(keyword)

## Research area
r = Rake(min_length=5, max_length=15)

st = ''' '''
list_tag= []
for row in rows:
    # print(row)
    st = st + ' ' + str(row[1])
    list_tag.append(str(row[1]))
    
frequency_tagline = []
keywords_tagline = []
tagline_string = r.extract_keywords_from_text(st)
for freq ,keyword in r.get_ranked_phrases_with_scores():
    if freq > 10:
        # print(freq,keyword)
        frequency_tagline.append(freq)
        keywords_tagline.append(keyword)

## After this keywords are manually extracted ans we also create a pickle file to share it among each other.


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

print('Done!')