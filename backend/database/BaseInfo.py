import datetime
import json
try:
    from database.BaseConfig import BaseConfig
except:
    from BaseConfig import BaseConfig


class BaseInfo(BaseConfig):
    def __init__(self):
        super().__init__()

    def load_data(self):
        pass

    def fetch(self):
        if self.data is None:
            self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        return self.info

    def packetFormat(self, data):
        return {
            'platform': self.platform,
            'data': data,
            'time':  self.info['time']
        }

    def fetch_detail(self, ID, ID2=None):
        if self.data is None:
            self.load_data()
        dataLst = []
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID):
                dataLst.append(i)
        return self.packetFormat(json.dumps(dataLst))

    def fetch_associate_event_with_ID(self, ID):
        raise Exception("该函数未重写，无法在此处调用")
