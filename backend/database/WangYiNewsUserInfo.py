try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class WangYiNewsUserInfo(BaseInfo, DB_Data):
    def __init__(self):
        super(WangYiNewsUserInfo, self).__init__()
        self.platform = 'wangyi'

    def load_data(self):
        self.readWangyiUserInfo()