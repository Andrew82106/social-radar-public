import tqdm
from database import BilibiliComment
from database.EventList import EventLst
from database.BaseInfo import BaseInfo
from datetime import datetime
from collections import Counter
import numpy as np
import math


class TimeQuota(BaseInfo):
    def __init__(self):
        super(TimeQuota, self).__init__()
        self.q = {}

    @staticmethod
    def updateLatestData(databaseLoc, eventID):
        """
        :param databaseLoc: 输入csv或者excel的位置，如果输入api则启用sql
        :param eventID: 和读取数据相关的事件的ID
        :return:
        """
        EventLst = [eventID]
        bilibili = BilibiliComment.BilibiliComment()
        bilibili.load_data(Location=databaseLoc)
        AimData = []
        for i in EventLst:
            AimData += bilibili.fetch_associate_event_with_ID(i)
        return AimData

    def updateQuota(self, databaseLoc, eventID):
        """
        计算事件eventID的指标
        :param databaseLoc: 输入csv或者excel的位置，如果输入api则启用sql
        :param eventID: 和读取数据相关的事件的ID
        :return:
        """
        DataLst = self.updateLatestData(databaseLoc, eventID)
        dateList = []
        for ii in DataLst:
            dateList.append(ii[self.ID_Time])

        date_objects = [
            datetime.strptime(date, '%Y-%m-%d %H:%M') if len(date) > 10 else datetime.strptime(date, '%Y-%m-%d') for
            date in dateList]

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