try:
    from database import BilibiliComment, WangYiNews, ZhihuComment
    from database.EventList import EventLst
    from database.BaseInfo import BaseInfo
    from database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
except:
    from ..database import BilibiliComment, WangYiNews, ZhihuComment
    from ..database.EventList import EventLst
    from ..database.BaseInfo import BaseInfo
    from ..database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
from datetime import datetime
from collections import Counter
import numpy as np
import math
import tqdm


class SummaryQuota(BaseInfo):
    def __init__(self):
        super(SummaryQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliComment, Ins_ZhihuComment, Ins_WangYiNews]
        for p in self.platformLst:
            p.load_data()

    def calc_summary_q(self, eventID, platform):
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        res = {}
        try:
            for date in instance.dateRange[int(eventID)]:
                date = str(date).split(" ")[0]
                print(date, end='  ')
                res[date] = self._map_to_range(self._calculate_date_difference(date, self.aimDate))
        except Exception as e:
            print(e)
        return self.packetFormat(self.normalize_dict_values(res))

    def calcSQOverall(self, eventid):
        res = {}
        aimDate = '2023-12-29'
        instance = None
        for i in self.platformLst:
            instance = i
            try:
                for dataI in tqdm.tqdm(instance.dateRange[int(eventid)], desc="final"):
                    TIME = dataI.split(" ")[0].replace("/", "-")
                    TIME = datetime.strftime(datetime.strptime(TIME, "%Y-%m-%d"), "%Y-%m-%d")
                    res[TIME] = int(self._map_to_range((self._calculate_date_difference(TIME, aimDate))))
            except:
                pass
        return self.packetFormat(self.normalize_dict_values(res))


if __name__ == '__main__':
    print("end")