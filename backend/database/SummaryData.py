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
            "评论信息": {}
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

        for instance in commentList:
            Data = instance.fetch()
            data = Data['data']
            platform = Data['platform']
            self.data['评论信息'][platform] = len(data)


if __name__ == '__main__':
    x = SummaryData()
    x.load_data()
    print("end")