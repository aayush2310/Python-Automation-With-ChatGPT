import requests
from bs4 import BeautifulSoup   #Library name for beautiful soup-bs4
import googletrans   #google provides this translate API for free and i can use that in my python scripts to translate whatever i want

#Get the HTML page
url = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'   #url of our blog post
page = requests.get(url)

#Parse the  page
soup = BeautifulSoup(page.content, 'html.parser')    #parsing the whole page with html parser, specifying that it is an html page and storing it in the soup
# Beautiful soup is a library which is a very popular python library for extracting, crawling and basically working with websites, so any time i need to 
# extract information from webpages. It was also suggested for this specific usecase by the API



#Extract all the headers
headers = soup.find_all(['h1','h2','h3','h4','h5','h6'])

#Translate each header to Spanish
translator = googletrans.Translator()      #initiating the translator
spanish_headers = []
for header in headers:
    translated_header = {
        "text" : translator.translate(header.text, dest='es').text , # " translator.translate(header.text, dest='es') " gives the whole translated object
        "name" : header.name
    }

    spanish_headers.append(translated_header)  #adding the translate result to the spanish_headers array.
    #now in that array i dont have only the list of text.So translated_header will create a list of dictionary with text and name attribute with the tramnslated text and header name
#so that is the destination language that it is going to be translated into.
#Then it collects back those translated spanish headers into this spanish headers array.
#In the spanish headers array, i am going to save an object the header text(the translated header text) and the header name



#Create an HTML file with the Spanish headers
with open('spanish_headers.html','w') as f:     #file mode is 'w' as i have used 'w' as file mode in "BlogPost_Translation.py". Also it came up with a good name "spanish_headers.html"
    f.write('<html>\n')                   #HTML opening tag
    for header in spanish_headers:
        f.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>\n')   #it adds each header in the html file.
    f.write('</html>\n')                  #HTML closing tag


#Part to adjust in this code-Since we are using different headers(h1,h2,h3,...) so i should not have only h1 in line 33
#line 23 saves the header text & what type of header it is whether h1 or h2 or h3 ...
#I stored the type of header as well and then used it in line 40
#So changing line 23 from  " spanish_headers.append(translator.translate(header.text,dest='es').text) " to " spanish_headers.append(translator.translate(header.text,dest='es')) " --earlier trial and error with the code

#header["name"] will tell me the type of header.
#This will preserve the hierarchy of headers in the final html file.

#Before running this script i need to install the libraries.


# I run this python script for my header extraction and translation from my blog. 
#After running this python script on terminal, the script ran and created a "spanish_headers.html" file 

#Final step would be to open spanish_headers.html in a browser