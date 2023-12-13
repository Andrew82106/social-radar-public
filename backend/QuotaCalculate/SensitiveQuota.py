import os
from datetime import datetime

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


class SensitiveQuota(BaseInfo):
    def __init__(self):
        super(SensitiveQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliComment, Ins_ZhihuComment, Ins_WangYiNews]
        self.wordBase = {}
        for p in self.platformLst:
            p.load_data()
        self._load_word_base()

    def _load_word_base(self):
        _df = pd.read_excel(os.path.join(self.calculateBase, '敏感词库表统计.xlsx'))
        for i in tqdm.tqdm(range(len(_df)), desc='读取敏感词库'):
            TYPE = _df.iloc[i]['SENSITIVETYPE']
            WORD = _df.iloc[i]['SENSITIVEWORDS']
            if TYPE not in self.wordBase:
                self.wordBase[TYPE] = []
            self.wordBase[TYPE].append(WORD)

    def _find_sensitive_word(self, sentence):
        res = {}
        for TYPE in self.wordBase:
            res[TYPE] = []
            for word in self.wordBase[TYPE]:
                if isinstance(sentence, float):
                    continue
                if str(word) in sentence:
                    res[TYPE].append(word)
            res[TYPE] = list(set(res[TYPE]))
        return res

    def sensitiveDataOverview(self):
        res = {}
        for i in self.wordBase:
            if i not in res:
                res[i] = len(self.wordBase[i])
        return self.packetFormat(res)

    def sensitiveWordCheck(self, sentence):
        return self.packetFormat(self._find_sensitive_word(sentence))

    @cache.cache_result(cache_path='summarySensitiveWord.pkl')
    def summarySensitiveWord(self, eventid, platform):
        res = {}
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        for dataI in tqdm.tqdm(instance.data, desc="计算敏感词汇中"):
            try:
                sentence = dataI[self.CommentInfo_content]
                ID = dataI[self.CommentInfo_IDIndex]
            except:
                sentence = dataI[self.NewsInfo_content]
                ID = dataI[self.NewsInfo_IDIndex]
            if str(ID) != str(eventid):
                continue
            SW = self._find_sensitive_word(sentence)
            for TYPE in SW:
                if TYPE not in res:
                    res[TYPE] = {}
                for word in SW[TYPE]:
                    if word not in res[TYPE]:
                        res[TYPE][word] = 0
                    res[TYPE][word] += 1
        return self.packetFormat(res)

    def calcSensitiveQuota(self, eventid, platform):
        res = {}
        aimDate = self.aimDate
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        for dataI in tqdm.tqdm(instance.data, desc="计算敏感度指标中"):
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
            TIME = self.formatTime(TIME)
            dbscan_result = self._calcMetric(aimDate)
            res[TIME] = dbscan_result
        return self.packetFormat(self.normalize_dict_values(res))

    def calcOverAllSensitiveQuota(self, eventid):
        res = {}
        for i in self.platformLst:
            res1 = self.calcSensitiveQuota(eventid, i.platform)['data']
            for Date in res1:
                if Date not in res:
                    res[Date] = 0
                res[Date] += res1[Date]
        return self.packetFormat(self.normalize_dict_values(res))


if __name__ == '__main__':
    print("今天早上我吃了一碗面条")
