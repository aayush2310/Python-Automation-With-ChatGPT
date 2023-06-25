#This file is generated when i execute BlogPost_Translation.py
#This is the code which i got as a response from the API
.

#Import libraries
import requests
from bs4 import BeautifulSoup
from googletrans import Translator

#Get the HTML page
url = '<url>'
page = requests.get(url)

#Parse the HTML page
soup = BeautifulSoup(page.text, 'html.parser')

#Extract all the headers
headers = soup.find_all(['h1','h2','h3','h4','h5','h6'])

#Translate each header to Spanish
translator = googletrans.Translator()
spanish_headers = []
for header in headers:
    spanish_headers.append(translator.translate(header.text,dest='es').text)


#Create an HTML file with the Spanish headers
with open('spanish_headers.html','w') as f:
    f.write('<html>\n')
    for header in spanish_headers:
        f.write(f'<h1>{header}</h1>\n')
    f.write('</html>\n')
                         
#Now I will make adjustments in this code(if needed) and then i will test this program with my blog article.