try:
    from database import globalConfig
    from database.globalConfig import userList, commentList, newsList, BaseInfo
except:
    import globalConfig
    from globalConfig import userList, commentList, newsList, BaseInfo


class SummaryData(BaseInfo):
    def __init__(self):
        super().__init__()

    def load_data(self):
        self.data = {
            "用户信息": {},
            "评论信息": {},
            '细节数据': {

            }
        }
        for instance in userList:
            Data = instance.fetch()
            data = Data['data']
            platform = Data['platform']
            self.data['用户信息'][platform] = len(data)

        for instance in newsList:
            Data = instance.fetch()
            data = Data['data']
            platform = Data['platform']
            self.data['评论信息'][platform] = len(data)
            for i in data:
                eventID = i[self.NewsInfo_IDIndex]
                if eventID not in self.data['细节数据']:
                    self.data['细节数据'][eventID] = {}
                if platform not in self.data['细节数据'][eventID]:
                    self.data['细节数据'][eventID][platform] = 0
                self.data['细节数据'][eventID][platform] += 1

        for instance in commentList:
            Data = instance.fetch()
            data = Data['data']
            platform = Data['platform']
            self.data['评论信息'][platform] = len(data)
            for i in data:
                eventID = i[self.CommentInfo_IDIndex]
                if eventID not in self.data['细节数据']:
                    self.data['细节数据'][eventID] = {}
                if platform not in self.data['细节数据'][eventID]:
                    self.data['细节数据'][eventID][platform] = 0
                self.data['细节数据'][eventID][platform] += 1


"""
    def fetch(self):
        self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        return self.info
"""

if __name__ == '__main__':
    x = SummaryData()
    x.load_data()
    print("end")
