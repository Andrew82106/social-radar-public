import math
from datetime import datetime, timedelta
import random
from sklearn.preprocessing import MinMaxScaler
try:
    from database.BaseConfig import BaseConfig
except:
    from BaseConfig import BaseConfig


class BaseInfo(BaseConfig):
    def __init__(self):
        super().__init__()
        self.aimDate = '2023-12-29'

    def load_data(self):
        pass

    @staticmethod
    def _map_to_range(value):
        sine_value = math.sin(value)
        mapped_value = (sine_value + 1) * 4 + random.randint(-100, 100)/100
        return mapped_value

    @staticmethod
    def _calcMetric(name):
        return random.randint(0, len(str(name)))

    @staticmethod
    def _newD(c):
        return c + timedelta(days=1)

    @staticmethod
    def _calculate_date_difference(start_date_str, target_date_str):
        if "/" in start_date_str:
            start_date_str = start_date_str.replace('/', "-")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        target_date = datetime.strptime(target_date_str, "%Y-%m-%d")
        date_difference = (target_date - start_date).days
        return date_difference

    def fetch(self):
        if self.data is None:
            self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        return self.info

    def fetchPage(self, count=None, page=None, data=None):
        if self.data is None:
            self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        if count is not None:
            assert page is not None, 'para Page is None!'
            count = int(count)
            page = int(page)
            try:
                if data is None:
                    self.info['dataPage'] = self.info['data'][page*count:min(page*count + count, len(self.info['data']))]
                else:
                    self.info['dataPage'] = data[page*count:min(page*count + count, len(data))]
            except:
                self.info['dataPage'] = f"参数错误，数据读取失败。self.info['data']长{len(self.info['data'])}"

        return self.packetFormat({
            'datalist': self.info['dataPage'],
            'maximumPage': math.ceil(len(self.info['data'])/count) - 1 if data is None else math.ceil(len(data)/count) - 1
        })

    def packetFormat(self, data):
        return {
            'platform': self.platform,
            'data': data,
            'time':  self.info['time']
        }

    def fetch_detail(self, ID, ID2=None, count=None, page=None):
        if self.data is None:
            self.load_data()
        dataLst = []
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID):
                for j in i:
                    if not (isinstance(i[j], str) or isinstance(i[j], int)):
                        i[j] = str(i[j])

                dataLst.append(i)
        if count is None:
            return self.packetFormat(dataLst)
        else:
            assert page is not None, "page is None"
            return self.fetchPage(count, page, data=dataLst)

    def fetch_associate_event_with_ID(self, ID):
        res = []
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID):
                res.append(i)
        return res

    @staticmethod
    def normalize_dict_values(input_dict: dict):
        if not len(input_dict):
            return input_dict

        values = list(input_dict.values())

        # 计算值的范围
        min_val = min(values)
        max_val = max(values)

        # 将值进行中心化缩放到[-0.5, 0.5]范围内
        scaled_values = [(val - min_val - (max_val - min_val) / 2) / (max_val - min_val) for val in values]

        # 将缩放后的值映射到[0, 1]范围内
        normalized_values = [(val + 0.5) for val in scaled_values]

        # 构建新的字典
        normalized_dict = {key: normalized_values[i] for i, key in enumerate(input_dict.keys())}
        return normalized_dict

    @staticmethod
    def _averageAt(D):
        if len(D) == 0:
            return {}
        D1 = {}
        m = 0
        for Date in D:
            m += D[Date]
        m = m/len(D)
        for S in D:
            D1[S] = max(0, D[S] + ((0.9+0.019*(len(str(D[S]*271)) % 100))*(m - D[S])))
        return D1