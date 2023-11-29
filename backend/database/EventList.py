from datetime import datetime, timedelta
from database.BaseInfo import BaseInfo

EventList = {
    'maximum ID': 5,
    'finished': {1: ["华为Mate60", 'mate60', '雷蒙多'],
                 2: ["巴以冲突", '巴以'],
                 3: ['俄乌冲突', '俄乌']},
    'processing': {
        4:
            {
                'keyword': ['流感', '甲流'],
                'start time': (datetime.now() - timedelta(hours=3)).strftime("%Y %D %H:%M:%S"),
                'schedule': 0.55
            },
        5:
            {
                'keyword': ['旧金山访问', '亚太会议'],
                'start time': (datetime.now() - timedelta(hours=6)).strftime("%Y %D %H:%M:%S"),
                'schedule': 0.55
            }
    },
    'trash': []
}

"""
EventList存放所有的事件信息

maximum ID存放当前使用到的事件数

finished 存放已经爬取好的事件

processing 存放正在处理的事件

trash 存放已经丢弃的事件
"""


class EventLst(BaseInfo):
    def __init__(self):
        super(EventLst, self).__init__()

    def load_data(self):
        self.data = EventList
        self.maxID = self.data['maximum ID']

    def getEventID(self, description):
        for i in self.data['finished']:
            for word in self.data['finished'][i]:
                if description in word:
                    return i

    def getEventDetail(self, EventID):
        return self.data['finished'][EventID]

    def getEventIDList(self):
        res = [i for i in range(1, self.EventList['maximum ID'] + 1, 1)]
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

