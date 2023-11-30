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


class SupportedPlatform(BaseInfo):
    def __init__(self):
        super(SupportedPlatform, self).__init__()

    def load_data(self):
        self.data = {
            "评论类平台": [i.platform for i in commentList],
            "新闻类平台": [i.platform for i in newsList],
            "用户信息平台": [i.platform for i in userList]
        }
