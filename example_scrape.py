import csv

from bs4 import BeautifulSoup
import requests

source_code=requests.get('https://coreyms.com/').text
soup=BeautifulSoup(source_code,'html5lib')

csv_file=open('csv_holder.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])


for article in soup.find_all('article'):
#print(article)
    head=article.h2.a.text
    print(head)
    summary=article.find('div',class_='entry-content').p.text
    print(summary)
#print(soup.title)
    try:
        vid_src=article.find('iframe',class_='youtube-player')['src']
    #print(vid_src)

        vid_id=vid_src.split('/')[4]
        vid_id=vid_src.split('?')[0]

    except:
        vid_id=None

    print(vid_id)

    print()

    csv_writer.writerow([head,summary,vid_id])

csv_file.close()