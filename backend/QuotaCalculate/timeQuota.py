import tqdm
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


class TimeQuota(BaseInfo):
    def __init__(self):
        super(TimeQuota, self).__init__()
        self.q = {}
        self.platformLst = [Ins_BilibiliComment, Ins_ZhihuComment, Ins_WangYiNews]
        for p in self.platformLst:
            p.load_data()

    def updateLatestData(self, eventID, databaseLoc=None):
        """
        批量从csv中或其他渠道读取数据
        :param databaseLoc: 输入csv或者excel的位置，如果输入api则启用sql
        :param eventID: 和读取数据相关的事件的ID
        :return AimData: 读取到的每个平台的和当前eventID匹配的数据
        """
        AimData = {}
        for p in self.platformLst:
            if databaseLoc is not None:
                p.load_data(databaseLoc)
            AimData[p.platform] = p.fetch_associate_event_with_ID(eventID)
        return AimData

    def getDateList(self, platformName: str, eventID, mode='date'):
        DateList = {}
        for instance in self.platformLst:
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

    def getDateListofAllPlatform(self, eventID, mode):
        DateList = {}
        for instance in self.platformLst:
            DateList[instance.platform] = self.getDateList(instance.platform, eventID, mode)
        self.data = DateList

    def getDateListofAllPlatformDetail(self, eventID, platform):
        DateList = {}
        for instance in self.platformLst:
            if instance.platform != platform:
                continue
            DateList[instance.platform] = self.getDateList(instance.platform, eventID)
        self.data = DateList

    def updateQuota(self, databaseLoc, eventID):
        """
        计算事件eventID的指标
        :param databaseLoc: 输入csv或者excel的位置，如果输入api则启用sql
        :param eventID: 和读取数据相关的事件的ID
        :return:
        """
        DataLst_ = self.updateLatestData(databaseLoc, eventID)
        DataLst = []
        for instance in DataLst_:
            for i in DataLst_[instance]:
                DataLst.append(i)
        # 有可能DataLst是空的
        if len(DataLst) == 0:
            self.q[eventID] = 0
            print("debug--time quota of event {}: proximity:0, concentration:0".format(eventID))
            return
        dateList = []
        for ii in DataLst:
            dateList.append(ii[self.ID_Time])

        date_objects = []
        for date in dateList:
            # print(date)
            date_objects.append(datetime.strptime(date, '%Y-%m-%d %H:%M') if (
                        10 < len(date) <= 16) else (datetime.strptime(date, '%Y-%m-%d') if 10 >= len(date) else datetime.strptime(date, '%Y-%m-%d %H:%M:%S')))

        # 计算与当前日期的接近度
        current_date = datetime.now()
        proximity = sum(abs((current_date - date_obj).total_seconds()) for date_obj in date_objects)/(len(date_objects)*86400)

        # 计算集中度指标
        date_counts = Counter([date_obj.date() for date_obj in date_objects])
        concentration = np.std(list(date_counts.values()))

        print("debug--time quota of event {}: proximity:{}, concentration:{}".format(eventID, proximity, concentration))

        q = concentration/proximity
        self.q[eventID] = q

    def update_all_quota(self, databaseLoc):
        """
        将所有事件的时间指标都计算出来放在类中
        :param databaseLoc:
        :return:
        """
        EventList = EventLst()
        Lst = EventList.getEventIDList()
        for i in Lst:
            self.updateQuota(databaseLoc, i)


if __name__ == '__main__':
    x = TimeQuota()
    x.update_all_quota(
        databaseLoc="/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/database/example_data/巴以冲突B站视频500条详细评论清洗版.csv",
    )
    print("end")