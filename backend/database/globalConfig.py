try:
    from database.BaseInfo import BaseInfo
    from database.BilibiliUserInfo import BilibiliUserInfo
    from database.BilibiliComment import BilibiliComment
    from database.ZhihuUserInfo import ZhihuUserInfo
    from database.ZhihuComment import ZhihuComment
    from database.WangYiNewsUserInfo import WangYiNewsUserInfo
    from database.WangYiNews import WangYiNews
except:
    from BaseInfo import BaseInfo
    from BilibiliUserInfo import BilibiliUserInfo
    from BilibiliComment import BilibiliComment
    from ZhihuUserInfo import ZhihuUserInfo
    from ZhihuComment import ZhihuComment
    from WangYiNewsUserInfo import WangYiNewsUserInfo
    from WangYiNews import WangYiNews


Ins_BilibiliComment = BilibiliComment()
Ins_ZhihuComment = ZhihuComment()
Ins_WangYiNews = WangYiNews()
Ins_BilibiliUserInfo = BilibiliUserInfo()
Ins_ZhihuUserInfo = ZhihuUserInfo()
Ins_WangYiNewsUserInfo = WangYiNewsUserInfo()


"""
把所有的信息类都实例化在这里，方便后续的调用！
"""


commentList = [
    Ins_BilibiliComment,
    Ins_ZhihuComment
]

newsList = [
    Ins_WangYiNews
]

userList = [
    Ins_BilibiliUserInfo,
    Ins_ZhihuUserInfo,
    Ins_WangYiNewsUserInfo
]


platformNames = {
    "Bilibili": Ins_BilibiliUserInfo.platform,
    'zhihu': Ins_ZhihuUserInfo.platform,
    'wangyi': Ins_WangYiNewsUserInfo.platform
}


PLATFORM = {
            "评论类平台": [i.platform for i in commentList],
            "新闻类平台": [i.platform for i in newsList],
            "用户信息平台": [i.platform for i in userList]
        }


class SupportedPlatform(BaseInfo):
    def __init__(self):
        super(SupportedPlatform, self).__init__()

    def load_data(self):
        self.data = PLATFORM

    def addPlatform(self, platformType, platformName):
        if self.data is None:
            self.load_data()
        assert platformType in self.data, '输入平台类型非法'
        if platformName not in self.data[platformType]:
            self.data[platformType].append(platformName)

    def delPlatform(self, platformName):
        if self.data is None:
            self.load_data()
        for platformType in self.data:
            if platformName in self.data[platformType]:
                self.data[platformType].remove(platformName)

    def summaryEventByPlatform(self):
        data = {

        }
        for instance in commentList:
            if instance.platform not in data:
                data[instance.platform] = []
            instance.load_data()
            for dataItem in instance.data:
                if dataItem[self.CommentInfo_IDIndex] not in data[instance.platform]:
                    data[instance.platform].append(dataItem[self.CommentInfo_IDIndex])

        for instance in newsList:
            if instance.platform not in data:
                data[instance.platform] = []
            instance.load_data()
            for dataItem in instance.data:
                if dataItem[self.NewsInfo_IDIndex] not in data[instance.platform]:
                    data[instance.platform].append(dataItem[self.NewsInfo_IDIndex])

        return self.packetFormat(data)

    def summaryPlatformByEvent(self):
        data = {

        }
        for instance in commentList:
            instance.load_data()
            for dataItem in instance.data:
                ID = dataItem[self.CommentInfo_IDIndex]
                platform = instance.platform
                if ID not in data:
                    data[ID] = []
                if platform not in data[ID]:
                    data[ID].append(platform)

        for instance in newsList:
            instance.load_data()
            for dataItem in instance.data:
                ID = dataItem[self.NewsInfo_IDIndex]
                platform = instance.platform
                if ID not in data:
                    data[ID] = []
                if platform not in data[ID]:
                    data[ID].append(platform)

        return self.packetFormat(data)


if __name__ == '__main__':
    x = SupportedPlatform()
    print(x.summaryEventByPlatform())
    print(x.summaryPlatformByEvent())