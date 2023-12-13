import tqdm
import math

try:
    from database import BilibiliComment, WangYiNews, ZhihuComment
    from database.EventList import EventLst
    from database.BaseInfo import BaseInfo
    from database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
    from database.AutoCache import Cache
except:
    from ..database import BilibiliComment, WangYiNews, ZhihuComment
    from ..database.EventList import EventLst
    from ..database.BaseInfo import BaseInfo
    from ..database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
    from ..database.AutoCache import Cache
cache = Cache()


class OpinionQuota(BaseInfo):
    def __init__(self):
        super(OpinionQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliComment, Ins_ZhihuComment, Ins_WangYiNews]
        for p in self.platformLst:
            p.load_data()

    def _calc_opinion_cluster(self, aimDate, nowDate):
        diff = self._calculate_date_difference(nowDate, aimDate)
        return int(self._map_to_range(diff))

    def _calc_opinion_clusterByDate(self, nowDate):
        res = []
        for instance in self.platformLst:
            if self.formatTime(nowDate) in instance.TimeRecord:
                cont = instance.TimeRecord[self.formatTime(nowDate)]
            else:
                cont = 0
            res.append(cont * (int(0.2 * cont) % 8))
        return sum(res)/len(res)

    def calcOpinionQuota(self, eventid, platform):
        res = {}
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        for dataI in tqdm.tqdm(instance.data, desc="计算聚类指标中"):
            try:
                ID = dataI[self.CommentInfo_IDIndex]
                TIME = dataI[self.CommentInfo_time]
            except:
                ID = dataI[self.NewsInfo_IDIndex]
                TIME = dataI[self.CommentInfo_time]
            if str(ID) != str(eventid):
                continue
            TIME = self.formatTime(TIME)
            dbscan_result = self._calc_opinion_clusterByDate(TIME)
            res[TIME] = dbscan_result
        return self.packetFormat(self.normalize_dict_values(res))

    def calcOPQuotaOverall(self, eventid):
        res = {}
        for i in self.platformLst:
            res1 = self.calcOpinionQuota(eventid, i.platform)['data']
            print(res1)
            for Date in res1:
                if Date not in res:
                    res[Date] = 0
                res[Date] += res1[Date]
        return self.packetFormat(self.normalize_dict_values(res))


if __name__ == '__main__':
    print("今天早上我吃了一碗面条")
