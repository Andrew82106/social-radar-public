from database.BaseInfo import BaseInfo
from database.BilibiliUserInfo import BilibiliUserInfo
from database.BilibiliComment import BilibiliComment
from database.ZhihuUserInfo import ZhihuUserInfo
from database.ZhihuComment import ZhihuComment
from database.WangYiNewsUserInfo import WangYiNewsUserInfo
from database.WangYiNews import WangYiNews
from database.EventList import EventList

commentList = [
    BilibiliComment(),
    ZhihuComment()
]

newsList = [
    WangYiNews()
]

userList = [
    BilibiliUserInfo(),
    ZhihuUserInfo(),
    WangYiNewsUserInfo()
]


class SupportedPlatform(BaseInfo):
    def __init__(self):
        super(SupportedPlatform, self).__init__()

    def load_data(self):
        self.data = {
            "评论类平台": [i.platform for i in commentList],
            "新闻类平台": [i.platform for i in newsList],
            "用户信息平台": [i.platform for i in userList]
        }
