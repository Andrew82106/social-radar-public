import datetime
import json


class BaseInfo:
    def __init__(self):
        self.info = {
            "time": str(datetime.datetime.now().strftime("%Y %D %H:%M:%S"))
        }
        self.data = None
        self.platform = ""
        self.ID_Index = "ID"
        self.platform_index = "platform"
        self.ID_UserName = 'username'
        self.ID_Time = 'time'
        self.ID_Like = 'like'
        self.ID_Comment = 'comment'

    def load_data(self):
        pass

    def fetch(self):
        if self.data is None:
            self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        return self.info

    def fetch_detail(self, ID, ID2=None):
        if self.data is None:
            self.load_data()
        dataLst = []
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID):
                dataLst.append(i)
        return json.dumps(dataLst)

    def fetch_associate_event_with_ID(self, ID):
        raise Exception("该函数未重写，无法在此处调用")
