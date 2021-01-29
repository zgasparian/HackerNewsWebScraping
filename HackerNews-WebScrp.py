from bs4 import BeautifulSoup
import requests
import csv
import time

start = time.time()
source= requests.get('https://news.ycombinator.com/').text
soup = BeautifulSoup(source,'lxml')
body = soup.find('body')
# print(body.prettify())
csv_file=open('outrput1.csv','w')
csv_writer= csv.writer(csv_file)
csv_writer.writerow(['ITEM','LINK','POINTS'])
# article = body.find('table',class_='itemlist')
for article in body.find_all('tr', class_='athing'):
    # print(article)

    text= article.find('a',class_='storylink').text
    print(text)
    link = article.find('a',class_='storylink')['href']
    print(link)

    try:
        vote = article.next_sibling.find('span', class_='score').text
        # print(vote.text)
    except Exception as e:
        vote = None

    print(vote)
    print()
    csv_writer.writerow([article.text,link,vote])
csv_file.close()
end=time.time()
print(f'{end - start} Seconds took to run the script')
