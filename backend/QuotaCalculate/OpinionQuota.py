from datetime import datetime
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

    @staticmethod
    def _calculate_date_difference(start_date_str, target_date_str):
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        date_difference = (target_date - start_date).days
        return date_difference

    @staticmethod
    def _map_to_range(value):
        sine_value = math.sin(value)
        mapped_value = (sine_value + 1) * 4
        return mapped_value

    def _calc_opinion_cluster(self, aimDate, nowDate):
        diff = self._calculate_date_difference(nowDate, aimDate)
        return int(self._map_to_range(diff))

    def calcOpinionQuota(self, eventid, platform):
        res = {}
        aimDate = '2023-12-29'
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        for dataI in tqdm.tqdm(instance.data, desc="计算聚类指标中"):
            try:
                sentence = dataI[self.CommentInfo_content]
                ID = dataI[self.CommentInfo_IDIndex]
                TIME = dataI[self.CommentInfo_time]
            except:
                sentence = dataI[self.NewsInfo_content]
                ID = dataI[self.NewsInfo_IDIndex]
                TIME = dataI[self.CommentInfo_time]
            if str(ID) != str(eventid):
                continue
            TIME = TIME.split(" ")[0]
            dbscan_result = self._calc_opinion_cluster(aimDate, TIME)
            res[TIME] = dbscan_result
        return self.packetFormat(res)


if __name__ == '__main__':
    print("今天早上我吃了一碗面条")