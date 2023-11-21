Event = {
    "巴以冲突": 1
}


def getEventID(description):
    for i in Event:
        if description in i:
            return Event[i]


def getEventDetail(EventID):
    for i in Event:
        if Event[i] == EventID:
            return Event[i]


def getEventIDList():
    res = []
    for i in Event:
        res.append(Event[i])
    return res


def getEventDetailList():
    res = []
    for i in Event:
        res.append(i)
    return res