import datetime
import os


class BaseConfig:
    def __init__(self):
        self.info = {
            "time": str(datetime.datetime.now().strftime("%Y %D %H:%M:%S"))
        }
        self.ID_Index = "ID"

        self.data = None
        self.platform = ""
        self.platform_index = "platform"
        self.ID_UserName = 'username'
        self.ID_Time = 'time'
        self.ID_Like = 'like'
        self.ID_Comment = 'comment'

        self.UserInfo_UserName = 'Username'
        self.UserInfo_RegisterTime = 'register time'
        self.UserInfo_IPLocation = 'IP location'
        self.UserInfo_Level = "Level"

        self.CommentInfo_UserName = 'Username'
        self.CommentInfo_like = 'like'
        self.CommentInfo_time = 'time'
        self.CommentInfo_type = "type"
        self.CommentInfo_content = "comment"

        self.NewsInfo_location = 'location'
        self.NewsInfo_source = 'source'
        self.NewsInfo_read = "read"
        self.NewsInfo_content = "content"
        """
        这里规定从数据库读进来的数据的键的内容
        """

        self.projectName = 'social-radar'
        self.projectRoute = os.path.dirname(os.path.realpath(__file__))
        while not self.projectRoute.endswith(self.projectName):
            self.projectRoute = os.path.dirname(self.projectRoute)
        self.ExampleDataRoute = os.path.join(self.projectRoute, "backend/database/example_data/巴以冲突B站视频500条详细评论清洗版.csv")



if __name__ == '__main__':
    x = BaseConfig()
    print(os.path.dirname(x.projectRoute))
    print(str(x.projectRoute).endswith('/database'))
    print(x.ExampleDataRoute)