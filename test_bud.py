import bs4
import re
import requests
from bs4 import BeautifulSoup
import sqlite3

### proxy information
proxy_host = '172.16.2.251'
proxy_port = '3128'

# ### Maintaining the first database

db = sqlite3.connect("iiserm.db")
cur = db.cursor()

# Create a dictionary with the proxy settings
proxies = {
    'http': f'http://{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_host}:{proxy_port}',
}
url = 'https://www.iisermohali.ac.in/faculty/hss/adrene'

# Send an HTTP GET request to the URL
response = requests.get(url,proxies=proxies,verify=False)
soup = BeautifulSoup(response.text,'lxml')  #difference between html and lxml
text = soup.text
start_word = "Dr."
end_word = "- IISER Mohali"
# Find the index of the start and end words in the text
start_index = text.find(start_word)
end_index = text.find(end_word)

if start_index != -1 and end_index != -1:
    # Extract the text between the start and end words
    extracted_text = text[start_index + len(start_word):end_index]
    result = extracted_text.strip()  # Use strip() to remove leading/trailing whitespace
    cur.execute("INSERT INTO IISERM (NAME,FIRST NAME) VALUES (%s,%s)",(result,result))

else:
    print("Start or end word not found in the text.")

# table = """ CREATE TABLE IISERM (
#     NAME text , 
#     FIRST NAME text
#     );"""
# cur.execute("SELECT * FROM IISERM where NAME=? , (result,)")
# cur.fetchall()
# cur.execute(table)
print('ready')
db.commit()
db.close()