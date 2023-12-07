try:
    from database import BilibiliComment, WangYiNews, ZhihuComment
    from database.EventList import EventLst
    from database.BaseInfo import BaseInfo
    from database.globalConfig import Ins_BilibiliUserInfo, Ins_ZhihuUserInfo, Ins_WangYiNewsUserInfo
    from database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
except:
    from ..database import BilibiliComment, WangYiNews, ZhihuComment
    from ..database.EventList import EventLst
    from ..database.BaseInfo import BaseInfo
    from ..database.globalConfig import Ins_BilibiliUserInfo, Ins_ZhihuUserInfo, Ins_WangYiNewsUserInfo
    from ..database.globalConfig import Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment
from datetime import datetime
from collections import Counter
import numpy as np
import random
import math
import tqdm


class UserBQuota(BaseInfo):
    def __init__(self):
        super(UserBQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliUserInfo, Ins_ZhihuUserInfo, Ins_WangYiNewsUserInfo]
        self.platformLst1 = [Ins_WangYiNews, Ins_ZhihuComment, Ins_BilibiliComment]
        for p in self.platformLst:
            p.load_data()

    def fetch_user_quota(self, userName, platform):
        instance = None
        for i in self.platformLst:
            if i.platform == platform:
                instance = i
                break
        data = instance.data
        for dataI in data:
            Name = dataI[self.UserInfo_UserName]
            if Name != userName:
                continue
            metric = self._calcMetric(Name)
            res = dataI
            res[self.UserInfo_quota] = metric
            return self.packetFormat(res)
        return self.packetFormat("无该用户")

    def calcUserQuota(self, eventid, platform):
        res = {}
        aimDate = '2023-12-29'
        instance = None
        for i in self.platformLst1:
            if i.platform == platform:
                instance = i
                break
        assert instance is not None, f"instance is None! para: eventid:{eventid} platform:{platform}"
        for dataI in tqdm.tqdm(instance.dateRange, desc="计算用户指标中"):
            TIME = dataI.split(" ")[0]
            res[TIME] = int(self._map_to_range((self._calculate_date_difference(TIME, aimDate))))
        return self.packetFormat(res)


if __name__ == '__main__':
    print("end")