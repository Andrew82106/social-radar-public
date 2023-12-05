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

    def SearchContentInDetail(self, keyWord, platform, EventID):
        commentRes = {}
        for instance in commentList:
            if instance.platform != platform:
                continue
            userLst = instance.fetch()
            # print(userLst)
            commentRes[instance.platform] = []
            # print(userLst['data'])
            for userInfo in userLst['data']:
                print(userInfo)
                # if count is not None and len(commentRes[instance.platform]) >= int(count):
                #     break
                # print(keyWord, self.CommentInfo_content, userInfo)
                try:
                    if str(userInfo[self.CommentInfo_IDIndex]) != str(EventID):
                        print(str(userInfo[self.CommentInfo_IDIndex]), str(EventID))
                        continue
                    if keyWord in userInfo[self.CommentInfo_content]:
                        commentRes[instance.platform].append(userInfo)
                except:
                    pass

        newsRes = {}
        for instance in newsList:
            if instance.platform != platform:
                continue
            userLst = instance.fetch()
            newsRes[instance.platform] = []
            for userInfo in userLst['data']:
                # if count is not None and len(newsRes[instance.platform]) >= count:
                #     break
                if str(userInfo[self.NewsInfo_IDIndex]) != str(EventID):
                    continue
                if keyWord in userInfo[self.NewsInfo_content]:
                    newsRes[instance.platform].append(userInfo)

        if len(newsRes):
            self.data = newsRes
        else:
            self.data = commentRes
        for i in self.data:
            if len(self.data[i]):
                self.data = self.data[i]
        # return self.fetch()