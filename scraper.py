from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

from time import sleep
from random import randint

# import csv
# with open('https://dirtbikeplanet.com') as html_file:
#     soup = BeautifulSoup(html_file, 'lxml')

# article = soup.find_all('div', class_='copy-container')

# headline = article.header.p.a.text
titles = []
urls = []

pages = np.arange(1, 37, 1)

for page in pages:
    source = requests.get('https://dirtbikeplanet.com/?page_num=' + str(page)).text
    soup = BeautifulSoup(source, 'lxml')

    sleep(randint(2,10))

    for article in soup.find_all('div', class_='copy-container'):

        headline = article.header.p.a.text
        titles.append(headline)

        link = article.header.p.a['href']
        urls.append(link)


content_titles = pd.DataFrame({
'Title' :titles,
'Link': urls
})

print(content_titles)
print(content_titles.dtypes)
content_titles.to_csv('cms_scrape.csv')


# csv_file = open('cms_scrape.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Title', 'URL'] )
# csv_writer.writerow([titles, urls])

# csv_file.close()
