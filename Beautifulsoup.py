import requests
from bs4 import BeautifulSoup

url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'lxml')
print(soup)

lst = soup.find_all('name')

for item in lst:
    print(item)
    

url = "https://seaborn.pydata.org/examples/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
print(soup)

lst = soup.find_all('p')[:-2]

for item in lst:
    print(item)

print("") 
print("seaborn Examples") 

def clean_item(item):
    position = item.find('</p')
    return item[3:position]

for item in lst:
    print(clean_item(str(item)))

