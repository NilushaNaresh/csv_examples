import csv

from bs4 import BeautifulSoup
import requests

page=requests.get('https://codingbat.com/java').text
soup=BeautifulSoup(page,'html5lib')

csv_file = open('scrape_file.csv','w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title','content'])

for article in soup.find_all('div',class_='tabin'):
    for head in article.find_all('div',class_='summ'):
        heading=head.a.span.text
        print(heading)
        content=article.table.find('tbody').a.text
        print(content)

        csv_writer.writerow([heading,content])

csv_file.close()

