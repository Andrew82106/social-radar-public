try:
    from database.BaseInfo import BaseInfo
except:
    from BaseInfo import BaseInfo
from hashlib import sha256, sha512, sha384


class UserQuota(BaseInfo):
    def __init__(self):
        super(UserQuota, self).__init__()

    def extract(self, S):
        # print(f"S:{S}")
        res = [ord(i) for i in str(S)]
        # print(sum(res))
        k = {}
        for index, num in enumerate(res):
            k[index] = num
        k = self.normalize_dict_values(k)
        res = [k[i] for i in k]
        return sum(res)/len(res)

    def generate26(self, Text):
        # print(f"generate26:TEXT={Text}")
        plainTextBytes = Text.encode('utf-8')
        encryptor = sha256()
        encryptor.update(plainTextBytes)
        hashCode = encryptor.hexdigest()
        return self.extract(hashCode)

    def generate52(self, Text):
        # print(f"generate52:TEXT={Text}")
        plainTextBytes = Text.encode('utf-8')
        encryptor = sha512()
        encryptor.update(plainTextBytes)
        hashCode = encryptor.hexdigest()
        return self.extract(hashCode)

    def generate84(self, Text):
        # print(f"generate84:TEXT={Text}")
        plainTextBytes = Text.encode('utf-8')
        encryptor = sha384()
        encryptor.update(plainTextBytes)
        hashCode = encryptor.hexdigest()
        return self.extract(hashCode)

    def load_data(self):
        self.data = [
                        {self.ID_Index: i,
                         self.platform_index: 'zhihu',
                         "quta1": self.extract(self.generate26(str(i) + str('zhihu'))),
                         "quta2": self.extract(self.generate26(str('zhihu') + str(i))),
                         } for i in range(1000)
                    ] + [
                        {self.ID_Index: i,
                         self.platform_index: 'bilibili',
                         "quta1": self.extract(self.generate26(str(i) + str('bilibili'))),
                         "quta2": self.extract(self.generate26(str('bilibili') + str(i))),
                         } for i in range(1000)
                    ] + [
                        {self.ID_Index: i,
                         self.platform_index: 'wangyi',
                         "quta1": self.extract(self.generate26(str(i) + str('wangyi'))),
                         "quta2": self.extract(self.generate26(str('wangyi') + str(i))),
                         } for i in range(1000)
                    ]

    def fetch_detail(self, ID, ID2=None, count=None, page=None):
        if self.data is None:
            self.load_data()
        for i in self.data:
            if str(i[self.ID_Index]) == str(ID) and str(i[self.platform_index]) == str(ID2):
                return i
        return None


if __name__ == '__main__':
    x = UserQuota()
    print(x.extract("42rnvoqa2o"))