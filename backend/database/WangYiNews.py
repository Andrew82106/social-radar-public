try:
    from database.BaseInfo import BaseInfo
    from database.loadFromDB import DB_Data
except:
    from BaseInfo import BaseInfo
    from loadFromDB import DB_Data


class WangYiNews(BaseInfo, DB_Data):
    def __init__(self):
        super(WangYiNews, self).__init__()
        self.platform = 'wangyi'

    def load_data(self, Location=None, ID_Index=1, length=-1):
        """
        :param Location: 输入csv或者excel的位置，如果输入api则启用sql，如果是-1则加载默认csv
        :param ID_Index: 和读取数据相关的事件的ID
        :param length: 读取的数据的条数
        :return:
        """
        if Location is None:
            Location = self.AllDataRoute
        if self.data is not None:
            return
        self.readWangyiNews(Location=Location)