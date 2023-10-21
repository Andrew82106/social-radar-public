from BaseInfo import BaseInfo


class SupportedPlatform(BaseInfo):
    def __init__(self):
        super(SupportedPlatform, self).__init__()

    def load_data(self):
        self.data = {
            "评论类平台": [i.platform for i in commentList],
            "新闻类平台": [i.platform for i in newsList],
            "用户信息平台": [i.platform for i in userList]
        }