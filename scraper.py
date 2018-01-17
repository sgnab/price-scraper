from bs4 import BeautifulSoup
import requests
import urllib3
import html5lib
import lxml
from time import sleep
cities = ['Toronto', 'Vancouver', 'Halifax']
infos={'city':cities,'make':'honda','model':'civic','minYear':'2000','maxYear':'2018'}
def myFilter(tag):
    return ((tag.name=="span" and tag.parent.name!="span"))
for city in infos['city']:
    try:
        doc = requests.get("https://"+city+".craigslist.ca/search/cta?auto_make_model="+infos['make']+"+"+infos['model']+"&min_auto_year="+infos['minYear']+"&max_auto_year="+infos['maxYear']+"")
        sleep(5)
        soap = BeautifulSoup(doc.content, 'lxml')
        prices = []
        years = []

        for asset in soap.find_all(["a",myFilter],class_=['result-title','result-price']):
            try:
                if asset.string[0] == "$" or type(int(asset.string[1]))==int :
                    if asset.string[0]=="$":
                        prices.append(asset.string[1:])
                    else:
                        years.append(asset.string[0:4])
            except ValueError:
                pass

    except requests.exceptions.ConnectionError:
        requests.status_code = "Connection refused"

    print((prices))
    print((years))
