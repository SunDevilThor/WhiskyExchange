# WhiskeyExchange Scraper
# Tutorial from John Watson Rooney YouTube channel

import requests, requests.exceptions
from bs4 import BeautifulSoup
import pandas as pd

baseurl = 'https://www.thewhiskyexchange.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
}

productlinks = []

for x in range(1, 5):
    response = requests.get(f'https://www.thewhiskyexchange.com/c/35/japanese-whisky?pg={x}&psize=24&sort=pasc', headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

# Run this once and comment out once file is created
# with open('WhiskyExchange.html', 'w') as file: 
#    file.write(str(soup))
#    print('Offline file saved')

    productlist = soup.find_all('li', class_='product-grid__item')

    for item in productlist:
        for link in item.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])

whisky_list = []
for link in productlinks: 
    response = requests.get(link, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    name = soup.find('h1', class_= 'product-main__name').text.strip()
    product_info = soup.find('p', class_= 'product-main__data').text.strip()
    price = soup.find('p', class_= 'product-action__price').text.strip()
    availability = soup.find('p', class_= 'product-action__stock-flag').text.strip()

    whisky = {
        'name': name,
        'product_info': product_info,
        'price': price, 
        'availability': availability
    }

    whisky_list.append(whisky)
    print('Saving: ', whisky['name'])

df = pd.DataFrame(whisky_list)
print(df.head())
df.to_csv('Whisky.csv')

