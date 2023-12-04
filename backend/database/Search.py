try:
    from database.globalConfig import Ins_BilibiliComment
    from database.globalConfig import Ins_ZhihuComment
    from database.globalConfig import Ins_WangYiNews
    from database.globalConfig import Ins_BilibiliUserInfo
    from database.globalConfig import Ins_ZhihuUserInfo
    from database.globalConfig import Ins_WangYiNewsUserInfo
    from database.globalConfig import userList, commentList, newsList
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from globalConfig import Ins_BilibiliComment
    from globalConfig import Ins_ZhihuComment
    from globalConfig import Ins_WangYiNews
    from globalConfig import Ins_BilibiliUserInfo
    from globalConfig import Ins_ZhihuUserInfo
    from globalConfig import Ins_WangYiNewsUserInfo
    from globalConfig import userList, commentList, newsList
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class Search(BaseInfo, DB_Data):
    def __init__(self):
        super().__init__()

    def SearchUserName(self, keyWord):
        res = {}
        for instance in userList:
            userLst = instance.fetch()
            res[instance.platform] = []
            for userInfo in userLst['data']:
                if keyWord in userInfo[self.UserInfo_UserName]:
                    res[instance.platform].append(userInfo)

        self.data = res
        return self.fetch()

    def SearchContent(self, keyWord):
        commentRes = {}
        for instance in commentList:
            userLst = instance.fetch()
            commentRes[instance.platform] = []
            # print(userLst['data'])
            for userInfo in userLst['data']:
                # print(userInfo)
                # print(keyWord, self.CommentInfo_content, userInfo)
                try:
                    if keyWord in userInfo[self.CommentInfo_content]:
                        commentRes[instance.platform].append(userInfo)
                except:
                    pass

        newsRes = {}
        for instance in newsList:
            userLst = instance.fetch()
            newsRes[instance.platform] = []
            for userInfo in userLst['data']:
                if keyWord in userInfo[self.NewsInfo_content]:
                    newsRes[instance.platform].append(userInfo)

        self.data = {"comment": commentRes, "news": newsRes}
        return self.fetch()
