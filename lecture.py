class Lecture:
    def __init__(self, row, eventDates): 
        #print(row)
        # row-id
        self.id = row.get('id')
        
        # cell: date
        self.date = row.select('td')[0].getText()
        
        # cell: start
        self.startTime = row.select('td')[2].getText().strip('-').strip()
        
        # cell: end
        self.endTime = row.select('td')[3].getText()
        
        # cell: title
        titleRowList = row.select('td')[5].getText().split('(', 1)
        self.mandatory = titleRowList[1].strip(')')
        rowType, eventTitle = titleRowList[0].split(" ", 1)
        self.title = eventTitle
        
        if rowType == 'PfPr':
            eventType = 'Pflichtpraktikum'
        elif rowType == 'FPr':
            eventType = 'Freiwilliges Praktikum'
        else:
            eventType = f'unbekannter Typ: {rowType}'
        self.eventType = eventType
        
        # cell: lecturer
        self.lecturer = row.select('td')[7].getText()
        
        # cell: place
        self.place = row.select('td')[9].getText()
        
        # cell: duration
        self.duration = row.select('td')[11].getText()
        hours, minutes = self.duration.split(':')
        self.durationMin = int(hours)*60 + int(minutes)
        
        # cell: other event dates
        self.eventDates = eventDates.strip('Termin: ').strip('Termine: ').split('/ ')    
    
    def __str__(self):
        objStr = f'Event: {self.id}\nTitle: {self.title}\nDate: {self.date}\nBegin: {self.startTime}\nEnde: {self.endTime}\nDauer: {self.duration} ({self.durationMin} Minuten)\nTutor*in: {self.lecturer}\nOrt/Raum: {self.place}\nPflicht: {self.mandatory}\nEvent-Typ: {self.eventType}\nWeitere Termine des Moduls: {self.eventDates}\n'
        return objStr

    def getAsIcsFile(self):
        # icsFile = 
        # return icsFile