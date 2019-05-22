#requests is a built in module. To check the available python modules,
#just go to python3, then do help, then type "modules" and hit enter
#requests allows us to download content of a website as HTML
url1 = "https://www.dailymail.co.uk/home/index.html"
url2 = "https://www.nytimes.com/"
import requests
r = requests.get(url1)

r_html = r.text
# .text property allows us to format the HTML code as text

from bs4 import BeautifulSoup
soup = BeautifulSoup(r_html, "html.parser")

headlines = []
for h in soup.find_all('h2'):
    a = h.get_text()
    headlines.append(a)

for item in headlines:
    print(item)
