import requests
from bs4 import BeautifulSoup

website = "https://www.shopify.com/ca"
response = requests.get(website)
#print(response)
#print(f"{website} : {response}")
#print(website, response)
scrape = BeautifulSoup(response.content, "lxml")
#title = scrape.find_all("h2", {"id": "1"})
title = scrape.find_all("h3", {"class" : "mb-2 text-lg font-medium"})
for t in title:
    print(t.getText())
