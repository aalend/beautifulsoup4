import requests
from bs4 import BeautifulSoup
import re
from csv import writer

response = requests.get('https://dev.to/t/python')

soup = BeautifulSoup(response.text, 'html.parser')

posts = soup.find_all(class_='crayons-story__body')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Link', 'Date']
    csv_writer.writerow(headers)

    for post in posts:
        title = post.find(
            class_='crayons-story__title').get_text().replace('\n', '')
        link = post.find('a', id=re.compile('^article-link-'))
        date = post.find('time').get_text()
        csv_writer.writerow([title, link, date])
