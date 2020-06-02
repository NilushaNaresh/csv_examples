from bs4 import BeautifulSoup
import requests

with open('base.html') as html_file:
    soup=BeautifulSoup(html_file,'html5lib')

#print(soup.prettify())
#print(soup.title)
#print(soup.title.text)
#print(soup.find('div',class_='footer'))

article=soup.find('div',class_='article')
#print(article)
summary=article.p.text
#print(summary)
for article in soup.find_all('div',class_='article'):
    headline=article.h2.a.text
    print(headline)
    summary=article.p.text
    print(summary)
    print()  #to make a line for each loop
