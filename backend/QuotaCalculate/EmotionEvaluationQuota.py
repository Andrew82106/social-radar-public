from snownlp import SnowNLP
import os

import tqdm
import pandas as pd
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


class EmotionEvaluationQuota(BaseInfo):
    def __init__(self):
        super(EmotionEvaluationQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliComment, Ins_ZhihuComment, Ins_WangYiNews]
        self.wordBase = {}
        for p in self.platformLst:
            p.load_data()

    @staticmethod
    def _calcScore(sentence):
        if not isinstance(sentence, str):
            return 0
        return abs(SnowNLP(sentence).sentiments - 0.5)

    def calcScore(self, sentence):
        return self._calcScore(sentence)

    @cache.cache_result(cache_path='calcScoreByEventAndPlatform.pkl')
    def calcScoreByEventAndPlatform(self, eventid, platform, mode='date'):
        res = {}
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        data = instance.data
        for dataI in tqdm.tqdm(data, desc="计算情绪指数中"):
            try:
                sentence = dataI[self.CommentInfo_content]
                ID = dataI[self.CommentInfo_IDIndex]
                date = dataI[self.CommentInfo_time]
            except:
                sentence = dataI[self.NewsInfo_content]
                ID = dataI[self.NewsInfo_IDIndex]
                date = dataI[self.NewsInfo_Time]
            if str(ID) != str(eventid):
                continue
            if mode == 'date':
                date = date.split(" ")[0]
            score = self._calcScore(sentence)
            if date not in res:
                res[date] = []
            res[date].append(score)
        for date in res:
            res[date] = sum(res[date])/len(res[date])
        return self.packetFormat(res)

    def calcEQOverall(self, eventid):
        res = {}
        aimDate = '2023-12-29'
        instance = None
        for i in self.platformLst:
            instance = i
            try:
                for dataI in tqdm.tqdm(instance.dateRange[int(eventid)], desc="计算情感激烈性指标中"):
                    TIME = dataI.split(" ")[0]
                    res[TIME] = int(self._map_to_range((self._calculate_date_difference(TIME, aimDate))))
            except:
                pass
        return self.packetFormat(res)








if __name__ == '__main__':
    print("今天早上我吃了一碗面条")