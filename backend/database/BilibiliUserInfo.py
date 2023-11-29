from database.BaseInfo import BaseInfo


class BilibiliUserInfo(BaseInfo):
    def __init__(self):
        super(BilibiliUserInfo, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.data = [
            {'Username': '金渐层烤乳牛', 'register time': '2023-09-04 10:22:14',
             'IP location': "中国 台湾",
             'Level': 6,
             self.ID_Index: 1
             },
            {'Username': '幻舞*Ustd', 'register time': '2019-07-01 07:22:14',
             'IP location': "哈萨克斯坦",
             'Level': 5,
             self.ID_Index: 2
             },
        ]