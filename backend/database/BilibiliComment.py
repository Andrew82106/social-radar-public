from database.BaseInfo import BaseInfo
import pandas as pd
import tqdm


class BilibiliComment(BaseInfo):
    def __init__(self):
        super(BilibiliComment, self).__init__()
        self.platform = 'bilibili'

    def load_data(self, Location=None, ID_Index=1, length=-1):
        """
        :param Location: 输入csv或者excel的位置，如果输入api则启用sql
        :param ID_Index: 和读取数据相关的事件的ID
        :param length: 读取的数据的条数
        :return:
        """
        if self.data is not None:
            return
        if Location is None:
            self.data = [
                {self.ID_UserName: '林中小屋', self.ID_Time: '2023-08-30 05:23', self.ID_Like: 21647,
                 self.ID_Comment: '芯片上的那个数字20应该不是年份',
                 self.ID_Index: 1},
                {self.ID_UserName: '元寳ATTO', self.ID_Time: '2023-08-30 08:27', self.ID_Like: 950,
                 self.ID_Comment: '回复 @林中小屋 :以后等这个量再大一点再看看吧，我估计这个2035没这么简单',
                 self.ID_Index: 1},
                {self.ID_UserName: '林一崇伟', self.ID_Time: '2023-08-30 06:25', self.ID_Like: 46843,
                 self.ID_Comment: '华为:让我康康在这我不在的4年里友商都做了什么突破\n友商:24g运存，240w快充，没有优化好的cmos\n华为:6，谢谢，都是真哥们',
                 self.ID_Index: 1},
                {self.ID_UserName: 'Serpentera', self.ID_Time: '2023-08-30 08:22', self.ID_Like: 1613,
                 self.ID_Comment: '还有绿厂放弃了自研芯片',
                 self.ID_Index: 1},
                {self.ID_UserName: '林黛玉醉打蒋门神丶', self.ID_Time: '2023-08-30 08:35', self.ID_Like: 8628,
                 self.ID_Comment: '的确，华为被制裁之后，手机市场突然就萎缩了，抛开疫情的原因，这些年确实没出现像样的旗舰机型，更没有让人看一眼就特别想买的手机[微笑]',
                 self.ID_Index: 1},
            ]
        elif '.csv' in Location or '.xlsx' in Location:
            print("loading data from excel or csv")
            if '.csv' in Location:
                _DF = pd.read_csv(Location)
            else:
                _DF = pd.read_excel(Location)
            self.data = []
            cnt = 0
            for i in tqdm.tqdm(range(len(_DF))):
                dfi = _DF.iloc[i:i+1]
                self.data.append({
                    self.ID_UserName: dfi[self.ID_UserName].iloc[0],
                    self.ID_Time: dfi[self.ID_Time].iloc[0],
                    self.ID_Like: dfi[self.ID_Like].iloc[0],
                    self.ID_Comment: dfi[self.ID_Comment].iloc[0],
                    self.ID_Index: ID_Index
                })
                cnt += 1
                if cnt > length and (length != -1):
                    break
        else:
            print("loading data from remote database")

    def fetch_associate_event_with_ID(self, ID):
        res = []
        for i in self.data:
            if i[self.ID_Index] == ID:
                res.append(i)
        return res


if __name__ == '__main__':
    a = BilibiliComment()
    a.load_data(
        Location="/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/database/example_data/巴以冲突B站视频500条详细评论清洗版.csv",
        length=10
    )
    print(len(a.fetch()))

    print("end")