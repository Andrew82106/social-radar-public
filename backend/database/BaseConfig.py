from datetime import datetime
import os


class BaseConfig:
    def __init__(self):
        self.info = {
            "time": str(datetime.now().strftime("%Y %D %H:%M:%S"))
        }
        self.ID_Index = "IDIndex"
        self.dateRange = {}

        self.data = None
        self.platform = ""
        self.platform_index = "platform"
        self.ID_UserName = 'username'
        self.ID_Time = 'time'
        self.ID_Like = 'like'
        self.ID_Comment = 'comment'

        self.UserInfo_UserName = 'Username'
        self.UserInfo_RegisterTime = 'register time'
        self.UserInfo_RelatedEvent = 'relatedEvent'
        self.UserInfo_IPLocation = 'IP location'
        self.UserInfo_Level = "Level"
        self.UserInfo_platform = "platform"
        self.UserInfo_ID = "IDIndex"
        self.UserInfo_quota = "quota"

        self.CommentInfo_UserName = 'Username'
        self.CommentInfo_UserID = 'UserID'
        self.CommentInfo_like = 'like'
        self.CommentInfo_time = 'time'
        self.CommentInfo_type = "type"
        self.CommentInfo_content = "comment"
        self.CommentInfo_IDIndex = "IDIndex"
        self.CommentInfo_platform = "platform"

        self.NewsInfo_location = 'Location'
        self.NewsInfo_UserID = 'UserID'
        self.NewsInfo_source = 'source'
        self.NewsInfo_read = "read"
        self.NewsInfo_Title = "Title"
        self.NewsInfo_Time = "time"
        self.NewsInfo_content = "Content"
        self.NewsInfo_IDIndex = "IDIndex"
        self.NewsInfo_platform = "platform"
        """
        这里规定从数据库读进来的数据的键的内容
        """

        self.projectName = 'social-radar'
        self.projectRoute = os.path.dirname(os.path.realpath(__file__))
        while not self.projectRoute.endswith(self.projectName):
            self.projectRoute = os.path.dirname(self.projectRoute)
        self.cacheName = os.path.join(self.projectRoute, "backend/cache")
        self.calculateBase = os.path.join(self.projectRoute, "backend/QuotaCalculate/data")
        self.AllDataRoute = os.path.join(self.projectRoute,
                                         "backend/database/example_data/allNews.xlsx")
        self.ExampleDataRoute = os.path.join(self.projectRoute,
                                             "backend/database/example_data/巴以冲突B站视频500条详细评论清洗版.csv")
        self.ExampleDataRoute_Ali = os.path.join(self.projectRoute,
                                                 "backend/database/example_data/阿里车祸.xlsx")
        self.ExampleDataRoute_Ali2 = os.path.join(self.projectRoute,
                                                  "backend/database/example_data/血槽姐网易.csv")
        self.ExampleDataRoute_Ali3 = os.path.join(self.projectRoute,
                                                  "backend/database/example_data/血槽姐知乎.csv")
        self.baYiNewsWangyi = os.path.join(self.projectRoute,
                                           "backend/database/example_data/巴以网易.csv")
        self.baYiNewsWangyi1 = os.path.join(self.projectRoute,
                                            "backend/database/example_data/巴以网易1.csv")
        self.BilibiliUserData = os.path.join(self.projectRoute,
                                             "backend/database/example_data/BilibiliUserData.xlsx")
        self.WangyiUserData = os.path.join(self.projectRoute,
                                           "backend/database/example_data/WangyiUserData.xlsx")
        self.ZhihuUserData = os.path.join(self.projectRoute,
                                          "backend/database/example_data/ZhiHuUserData.xlsx")
        self.BaYiZhihu = os.path.join(self.projectRoute,
                                      "backend/database/example_data/巴以冲突知乎数据.xlsx")
        self.BZhanXueCao = os.path.join(self.projectRoute,
                                        "backend/database/example_data/B站血槽姐.csv")

        self.newsTableRoute = [
            self.baYiNewsWangyi,
            self.baYiNewsWangyi1,
            self.ExampleDataRoute_Ali2,
        ]
        self.CommentTableRoute = [
            self.AllDataRoute,
            self.ExampleDataRoute_Ali3,
            self.BaYiZhihu,
            self.BZhanXueCao
        ]
        self.UserTableRoute = [
            self.BilibiliUserData,
            self.WangyiUserData,
            self.ZhihuUserData
        ]

    def __len__(self):
        if self.data is None:
            return 0
        return len(self.data)

    @staticmethod
    def formatTime(Time: str):
        try:
            return datetime.strftime(datetime.strptime(Time.split(" ")[0].replace("/", "-"), "%Y-%m-%d"), "%Y-%m-%d")
        except:
            return Time


if __name__ == '__main__':
    x = BaseConfig()
    print(x.projectRoute)
    print(os.path.dirname(x.projectRoute))
    print(str(x.projectRoute).endswith('/database'))
    print(x.ExampleDataRoute)
    print(x.cacheName)
