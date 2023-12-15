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
        for dataI in tqdm.tqdm(instance.dateRange[int(eventid)], desc="计算用户指标中"):
            TIME = dataI.split(" ")[0]
            res[TIME] = int(self._map_to_range((self._calculate_date_difference(TIME, aimDate))))
        return self.packetFormat(self.normalize_dict_values(res))

    def getDateList(self, platformName: str, eventID, mode='date'):
        DateList = {}
        for instance in self.platformLst1:
            if instance.platform != platformName:
                continue
            for ii in instance.fetch_associate_event_with_ID(eventID):
                if mode == 'date':
                    T = ii[self.ID_Time].split(" ")[0]
                else:
                    T = ii[self.ID_Time]
                if T not in DateList:
                    DateList[T] = 0
                DateList[T] += 1
        return DateList

    def calcUserQuotaOverall(self, eventid):
        DateList = {}
        for instance in self.platformLst1:
            DateList0 = self.getDateList(instance.platform, eventid)
            for i in DateList0:
                i1 = self.formatTime(i)
                if i1 not in DateList:
                    DateList[i1] = 0
                DateList[i1] += DateList0[i]

        DateList = self._averageAt(DateList)
        self.data = self.normalize_dict_values(DateList)
        return self.packetFormat(self.data)


if __name__ == '__main__':
    print("end")