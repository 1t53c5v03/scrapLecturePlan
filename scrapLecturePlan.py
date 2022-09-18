import requests, bs4
from datetime import datetime, date, time
from ics import Event, Calendar
from lecture import Lecture

eventTableUrl = 'https://vorlesungsplaene.th-luebeck.de/schedulesCohorten/curSem/online/online_cohort_ITS3_WiSe_2021_22.html'
res = requests.get(eventTableUrl)
html = res.text

#print(html)
soup = bs4.BeautifulSoup(html, features='lxml')
lecturePlan = soup.select('.w1')[0].getText()
print('Plan:', lecturePlan)

rows = soup.select('table.tbl > tr')

calendar = Calendar()

for i in range(2, len(rows), 3):
    lecture = Lecture(rows[i], rows[i+1].select('td')[5].getText())
    lectureEvent = Event()
    lectureEvent.name = lecture.title
    lectureEvent.description = f'Tutor*in: {lecture.lecturer}, {lecture.eventType}, {lecture.mandatory}, Weitere Termin(e): {lecture.eventDates}'
    
    lDate = date(int(lecture.date[2][:4]), int(lecture.date[1]), int(lecture.date[0]))
    lStartTime = time(int(lecture.startTime[0]), int(lecture.startTime[1]))
    lectureEvent.begin = datetime.combine(lDate, lStartTime)
    lEndTime = time(int(lecture.endTime[0]), int(lecture.endTime[1]))
    lectureEvent.end = datetime.combine(lDate, lEndTime)
    lectureEvent.location = lecture.place

    calendar.events.add(lectureEvent)
#print(calendar)

with open(f'{lecturePlan}.ics', 'w') as file:
    file.write(calendar.serialize())