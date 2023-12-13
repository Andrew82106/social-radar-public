from datetime import datetime

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
        """
        calc Em Quota
        :param sentence:
        :return:
        """
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
                date = self.formatTime(date)
            score = self._calcScore(sentence)
            if date not in res:
                res[date] = []
            res[date].append(score)
        for date in res:
            res[date] = sum(res[date])/len(res[date])
        return self.packetFormat(self.normalize_dict_values(res))

    @cache.cache_result(cache_path='calcEQOverall.pkl')
    def calcEQOverall(self, eventid):
        res = {}
        for i in self.platformLst:
            res1 = self.calcScoreByEventAndPlatform(eventid, i.platform)['data']
            for Date in res1:
                if Date not in res:
                    res[Date] = 0
                res[Date] += res1[Date]

        return self.packetFormat(self.normalize_dict_values(res))


if __name__ == '__main__':
    print("今天早上我吃了一碗面条")