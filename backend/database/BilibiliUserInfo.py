try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class BilibiliUserInfo(BaseInfo, DB_Data):
    def __init__(self):
        super(BilibiliUserInfo, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.readBiliBiliUserInfo()


if __name__ == '__main__':
    a = BilibiliUserInfo()
    p = a.platform