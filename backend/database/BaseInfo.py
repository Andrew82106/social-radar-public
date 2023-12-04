import json
import datetime

try:
    from database.BaseConfig import BaseConfig
    from Utils.NpEncoder import NpEncoder
except:
    from BaseConfig import BaseConfig
    from Utils.NpEncoder import NpEncoder


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
                for j in i:
                    if isinstance(i[j], datetime.time):
                        i[j] = str(i[j])
                dataLst.append(i)

        # json_ = json.dumps(dataLst)
        return self.packetFormat(dataLst)

    def fetch_associate_event_with_ID(self, ID):
        res = []
        for i in self.data:
            if i[self.ID_Index] == ID:
                res.append(i)
        return res
