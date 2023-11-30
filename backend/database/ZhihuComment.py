try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class ZhihuComment(BaseInfo, DB_Data):
    def __init__(self):
        super(ZhihuComment, self).__init__()
        self.platform = 'zhihu'

    def load_data(self):
        self.readZhihuComment()