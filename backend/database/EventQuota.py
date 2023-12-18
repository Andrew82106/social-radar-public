try:
    from database.BaseInfo import BaseInfo
except:
    from BaseInfo import BaseInfo


class EventQuota(BaseInfo):
    def __init__(self):
        super(EventQuota, self).__init__()

    def load_data(self):
        self.data = [
            {self.ID_Index: 1,
             self.platform_index: 'bilibili',
             "时间热度指标": 0.57,
             "敏感度热度指标": 0.21,
             "观点对立性热度指标": 0.12,
             "情感激烈性热度指标": 0.23,
             "用户可性度热度指标": 0.72,
             "总热度指标": 0.16,
             },
            {self.ID_Index: 2,
             self.platform_index: 'bilibili',
             "时间热度指标": 0.91,
             "敏感度热度指标": 0.10,
             "观点对立性热度指标": 0.37,
             "情感激烈性热度指标": 0.33,
             "用户可性度热度指标": 0.53,
             "总热度指标": 0.62,
             },
            {self.ID_Index: 1,
             self.platform_index: 'zhihu',
             "时间热度指标": 0.92,
             "敏感度热度指标": 0.62,
             "观点对立性热度指标": 0.12,
             "情感激烈性热度指标": 0.63,
             "用户可性度热度指标": 0.12,
             "总热度指标": 0.63,
             },
            {self.ID_Index: 2,
             self.platform_index: 'zhihu',
             "时间热度指标": 0.67,
             "敏感度热度指标": 0.22,
             "观点对立性热度指标": 0.12,
             "情感激烈性热度指标": 0.21,
             "用户可性度热度指标": 0.27,
             "总热度指标": 0.99,
             },
            {self.ID_Index: 1,
             self.platform_index: 'wangyi',
             "时间热度指标": 0.52,
             "敏感度热度指标": 0.41,
             "观点对立性热度指标": 0.52,
             "情感激烈性热度指标": 0.11,
             "用户可性度热度指标": 0.23,
             "总热度指标": 0.41,
             },
            {self.ID_Index: 2,
             self.platform_index: 'wangyi',
             "时间热度指标": 0.42,
             "敏感度热度指标": 0.53,
             "观点对立性热度指标": 0.44,
             "情感激烈性热度指标": 0.34,
             "用户可性度热度指标": 0.34,
             "总热度指标": 0.88,
             }
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