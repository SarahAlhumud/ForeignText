import requests
from bs4 import BeautifulSoup
import re


url = 'http://freeread.com.au/@RGLibrary/ArthurConanDoyle/SherlockHolmes/RETU.html'
res = requests.get(url)
html_page = res.content

# print(html_page)

soup = BeautifulSoup(html_page, 'html.parser')

# print(soup)

text = soup.find_all(text=True)

set([t.parent.name for t in text])

output = ''
blacklist = [
    'i', 'h2', 'h3', 'p', 'body', 'div', '[document]', 'sup', 'li', 'head', 'h1', 'ol', 'html', 'b', 'title', 'a'

]

for t in text:
    if t.parent.name in blacklist:
        output += '{} '.format(t)

# print(output)
# each story start with roman numerals
stories = re.split(r' \s\s[MDCLXVI]+\. ', output, flags=re.IGNORECASE)
# print(stories)


for i, story in enumerate(stories):
    print('###'*30)
    print(i)
    print(story)
    f = open('Stories/'+str(i) +'.txt', 'w')
    f.write(story)
    f.close()

