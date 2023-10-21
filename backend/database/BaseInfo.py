import datetime


class BaseInfo:
    def __init__(self):
        self.info = {
            "time": str(datetime.datetime.now().strftime("%Y %D %H:%M:%S"))
        }
        self.data = None
        self.platform = ""
        self.ID_Index = "ID"
        self.platform_index = "platform"

    def load_data(self):
        pass

    def fetch(self):
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