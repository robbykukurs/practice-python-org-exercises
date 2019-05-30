#requests is a built in module. To check the available python modules,
#just go to python3, then do help, then type "modules" and hit enter
#requests allows us to download content of a website as HTML
url1 = "https://www.dailymail.co.uk/home/index.html"
url2 = "https://www.nytimes.com/"
import requests
r = requests.get(url1)

r_html = r.text
# .text property allows us to format the HTML code as text

#BeautifulSoup allows us to sort website code by tags
from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, "html.parser")

#here we're sorting all the headlines and getting only the text part out of them
headlines = []
for h in soup.find_all('h2'):
    a = h.get_text()
    headlines.append(a)

#you have to join the output or else you won't be able to provide it as input for the file below
final = " ".join(headlines)

#the below creates a new file in this python file directory as 'w'write only
with open('latest_dailymail_headlines', 'w') as open_file:
    open_file.write(final)
