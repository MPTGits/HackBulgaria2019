import requests
from bs4 import BeautifulSoup

r = requests.get("http://register.start.bg/")
#print(r.text)
soup = BeautifulSoup(r.text, 'lxml')

all_links=soup.findAll('a',href=True)

for link in all_links:
    print(link.attrs['href'])


#for element in soup:
 #   print(element)
    #print("ENDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")