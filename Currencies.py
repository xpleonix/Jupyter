
import requests
import xmltodict

url = "http://www.cbr.ru/scripts/XML_val.asp"
response = requests.get(url)
data = xmltodict.parse(response.content)
print(data)

curr_array = []
for item in data['Valuta']['Item']:
    curr_set = [item['Name'], item['EngName'], item['Nominal'], item['ParentCode']]
    curr_array.append(curr_set)
    print(curr_set)
    
    
