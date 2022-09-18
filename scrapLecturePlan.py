import requests, bs4, icalendar
from lecture import *

eventTableUrl = 'https://vorlesungsplaene.th-luebeck.de/schedulesCohorten/curSem/online/online_cohort_ITS3_WiSe_2021_22.html'
res = requests.get(eventTableUrl)
html = res.text

#print(html)
soup = bs4.BeautifulSoup(html, features='lxml')
print('Plan:', soup.select('.w1')[0].getText())

rows = soup.select('table.tbl > tr')
for i in range(2, len(rows), 3):
    newEvent = Lecture(rows[i], rows[i+1].select('td')[5].getText())
    #print(newEvent)