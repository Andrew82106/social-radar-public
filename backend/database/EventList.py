from datetime import datetime
try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class EventLst(BaseInfo, DB_Data):
    def __init__(self):
        super(EventLst, self).__init__()

    def load_data(self):
        self.readEventList()

    def getEventID(self, description):
        for i in self.data['finished']:
            for word in self.data['finished'][i]:
                if description in word:
                    return i

    def getEventDetail(self, EventID):
        return self.data['finished'][EventID]

    def getEventIDList(self):
        if self.data is None:
            self.load_data()
        res = [i for i in range(1, self.data['maximum ID'] + 1, 1)]
        return res

    def addEvent(self, wordlist):
        if self.data is None:
            self.load_data()
        for i in self.data['processing']:
            if self.data['processing'][i]['keyword'] == wordlist:
                return
        for i in self.data['finished']:
            if self.data['finished'][i] == wordlist:
                return
        self.maxID += 1
        self.data['maximum ID'] += 1
        self.data['processing'][self.maxID] = {
            'keyword': wordlist,
            'start time': (datetime.now()).strftime("%Y %D %H:%M:%S"),
            'schedule': 0.1
        }

    def delEvent(self, EventID):
        if self.data is None:
            self.load_data()
        if not (1 <= int(EventID) <= self.maxID):
            return
        if EventID in self.data['trash']:
            return
        self.data['trash'].append(EventID)

