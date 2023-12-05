import json
import datetime

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

    def fetchPage(self, count=None, page=None):
        if self.data is None:
            self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        if count is not None:
            assert page is not None, 'para Page is None!'
            count = int(count)
            page = int(page)
            try:
                self.info['dataPage'] = self.info['data'][page*count:page*count + count]
            except:
                self.info['dataPage'] = f"参数错误，数据读取失败。self.info['data']长{len(self.info['data'])}"

        return self.packetFormat(self.info['dataPage'])

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
