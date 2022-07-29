from bs4 import BeautifulSoup
import requests
import urllib
import re
import csv
from selenium import webdriver

driver = webdriver.Chrome('.\\chromedriver.exe')
driver.get('https://golden.com/query/list-of-e-commerce-companies-RN9/results?page=5&per_page=25')
soupdr = BeautifulSoup(driver.page_source, 'lxml')

tablename = soupdr.find('div', role="cell", class_="css-1pnx597") #table body 

# webcell = tablename.find_all('div', class_="css-1ci65ym")
print(tablename)
# for site in webcell:
#     name = site.a.text
#     print(name)
# for website in webcell:
#     websitec = website.find('div', class_ = )
#     print(website)



# outerbin = tablename.find_all('div', class_ = "css-1f18le8" )
# innerbin = outerbin.find_all('div', class_="css-1ci65ym")
# print(innerbin)