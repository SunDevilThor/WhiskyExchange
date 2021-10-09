# OFFLINE file for WhiskeyExchange Scraper

from bs4 import BeautifulSoup

file1 = open('WhiskyExchange.html')

file2 = open('WhiskyExchangeProduct.html')

soup1 = BeautifulSoup(file1, 'html.parser')
soup2 = BeautifulSoup(file2, 'html.parser')

print(soup1.title.text)
print(soup2.title.text)
