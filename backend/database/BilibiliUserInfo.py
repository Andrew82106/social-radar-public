try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class BilibiliUserInfo(BaseInfo, DB_Data):
    def __init__(self):
        super(BilibiliUserInfo, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.readBiliBiliUserInfo()

    def summary_location(self, EventID):
        if self.data is None:
            self.load_data()
        locationCount = {}
        for instance in self.data:
            location = instance[self.UserInfo_IPLocation]
            relatedEvent = instance[self.UserInfo_RelatedEvent]
            if str(EventID) not in relatedEvent:
                continue
            if location not in locationCount:
                locationCount[location] = 0
            locationCount[location] += 1
        return self.packetFormat(locationCount)


if __name__ == '__main__':
    a = BilibiliUserInfo()
    p = a.platform