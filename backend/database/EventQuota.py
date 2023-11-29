from database.BaseInfo import BaseInfo


class EventQuota(BaseInfo):
    def __init__(self):
        super(EventQuota, self).__init__()

    def load_data(self):
        self.data = [
            {self.ID_Index: 1,
             self.platform_index: 'bilibili',
             "quta1": 0.912,
             "quta2": 0.210,
             "quta3": 0.312,
             "quta4": 0.123,
             "quta5": 0.712,
             "quta6": 0.216,
             },
            {self.ID_Index: 2,
             self.platform_index: 'bilibili',
             "quta1": 0.912,
             "quta2": 0.210,
             "quta3": 0.312,
             "quta4": 0.123,
             "quta5": 0.712,
             "quta6": 0.216,
             },
            {self.ID_Index: 1,
             self.platform_index: 'zhihu',
             "quta1": 0.912,
             "quta2": 0.210,
             "quta3": 0.312,
             "quta4": 0.123,
             "quta5": 0.712,
             "quta6": 0.216,
             },
            {self.ID_Index: 2,
             self.platform_index: 'wangyi',
             "quta1": 0.912,
             "quta2": 0.210,
             "quta3": 0.312,
             "quta4": 0.123,
             "quta5": 0.712,
             "quta6": 0.216,
             },
        ]
        # 这里的ID_Index和platform_index分别指事件ID和平台名称
        # 每一个事件暂定有6个指标，分别表示：
        # 时间敏感度指标、内容敏感度指标、用户真实度指标、情感激烈性指标、观点对立性指标和热度持续性指标
        # 每一个事件在所有的支持平台都有指标

    def fetch_detail(self, ID, ID2=None):
        if self.data is None:
            self.load_data()
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID) and str(i[self.platform_index]) == str(ID2):
                return i
        return None