from database.BaseInfo import BaseInfo


class UserQuota(BaseInfo):
    def __init__(self):
        super(UserQuota, self).__init__()

    def load_data(self):
        self.data = [
            {self.ID_Index: 1,
             self.platform_index: 'bilibili',
             "quta1": 0.912,
             "quta2": 0.210,
             },
            {self.ID_Index: 2,
             self.platform_index: 'bilibili',
             "quta1": 0.912,
             "quta2": 0.210,
             },
            {self.ID_Index: 1,
             self.platform_index: 'zhihu',
             "quta1": 0.912,
             "quta2": 0.210,
             },
            {self.ID_Index: 2,
             self.platform_index: 'zhihu',
             "quta1": 0.912,
             "quta2": 0.210,
             },
        ]

    def fetch_detail(self, ID, ID2=None):
        if self.data is None:
            self.load_data()
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID) and str(i[self.platform_index]) == str(ID2):
                return i
        return None