import random

import pandas as pd
import tqdm
try:
    from database.BaseConfig import BaseConfig
except:
    from BaseConfig import BaseConfig
from datetime import datetime, timedelta

EventList = {
    'maximum ID': 5,
    'finished': {1: ["巴以", "加沙"],
                 2: ["阿里", '车祸', '血槽姐']},
    'processing': {
        4:
            {
                'keyword': ['流感', '甲流'],
                'start time': (datetime.now() - timedelta(hours=3)).strftime("%Y %D %H:%M:%S"),
                'schedule': 0.55
            },
        5:
            {
                'keyword': ['旧金山访问', '亚太会议'],
                'start time': (datetime.now() - timedelta(hours=6)).strftime("%Y %D %H:%M:%S"),
                'schedule': 0.55
            }
    },
    'trash': []
}

"""
EventList存放所有的事件信息

maximum ID存放当前使用到的事件数

finished 存放已经爬取好的事件

processing 存放正在处理的事件

trash 存放已经丢弃的事件
"""


"""
为各个类的load data方法提供接口
"""


class DB_Data(BaseConfig):

    def __init__(self):
        super().__init__()
        self.maxID = None

    def readCommentTable(self):
        res = None
        for r in self.CommentTableRoute:
            if '.csv' in r:
                _DF = pd.read_csv(r)
            else:
                _DF = pd.read_excel(r)
            if res is None:
                res = _DF
            else:
                res = pd.concat([res, _DF], ignore_index=1)
        return res

    def readNewsTable(self):
        res = None
        for r in self.newsTableRoute:
            if '.csv' in r:
                _DF = pd.read_csv(r, index_col=0)
            else:
                _DF = pd.read_excel(r, index_col=0)
            if res is None:
                res = _DF
            else:
                res = pd.concat([res, _DF], ignore_index=1)
        return res

    def readBiliBiliComment(self, Location=None, ID_Index=1, length=-1):
        """
        :param Location: 输入csv或者excel的位置，如果输入api则启用sql，如果是-1则加载默认csv
        :param ID_Index: 和读取数据相关的事件的ID
        :param length: 读取的数据的条数
        :return:
        """
        if Location == -1:
            Location = self.AllDataRoute
        if Location is None:
            self.data = [
                {self.CommentInfo_UserName: '林中小屋', self.CommentInfo_time: '2023-08-30 05:23', self.CommentInfo_like: 21647,
                 self.CommentInfo_content: '芯片上的那个数字20应该不是年份',
                 self.ID_Index: 1},
                {self.CommentInfo_UserName: '元寳ATTO', self.CommentInfo_time: '2023-08-30 08:27', self.CommentInfo_like: 950,
                 self.CommentInfo_content: '回复 @林中小屋 :以后等这个量再大一点再看看吧，我估计这个2035没这么简单',
                 self.ID_Index: 1},
                {self.CommentInfo_UserName: '林一崇伟', self.CommentInfo_time: '2023-08-30 06:25', self.CommentInfo_like: 46843,
                 self.CommentInfo_content: '华为:让我康康在这我不在的4年里友商都做了什么突破\n友商:24g运存，240w快充，没有优化好的cmos\n华为:6，谢谢，都是真哥们',
                 self.ID_Index: 1},
                {self.CommentInfo_UserName: 'Serpentera', self.CommentInfo_time: '2023-08-30 08:22', self.CommentInfo_like: 1613,
                 self.CommentInfo_content: '还有绿厂放弃了自研芯片',
                 self.ID_Index: 1},
                {self.CommentInfo_UserName: '林黛玉醉打蒋门神丶', self.CommentInfo_time: '2023-08-30 08:35', self.CommentInfo_like: 8628,
                 self.CommentInfo_content: '的确，华为被制裁之后，手机市场突然就萎缩了，抛开疫情的原因，这些年确实没出现像样的旗舰机型，更没有让人看一眼就特别想买的手机[微笑]',
                 self.ID_Index: 1},
            ]
        else:
            print("loading data from excel or csv")
            _DF = self.readCommentTable()
            self.data = []
            cnt = 0
            for i in tqdm.tqdm(range(len(_DF))):
                dfi = _DF.iloc[i:i + 1]
                if dfi[self.CommentInfo_platform].iloc[0] != self.platform:
                    continue
                # print(dfi.columns)
                self.data.append({
                    self.CommentInfo_UserName: str(dfi[self.CommentInfo_UserName].iloc[0]),
                    self.CommentInfo_time: str(dfi[self.CommentInfo_time].iloc[0]),
                    self.CommentInfo_like: int(dfi[self.CommentInfo_like].iloc[0]),
                    self.CommentInfo_content: str(dfi[self.CommentInfo_content].iloc[0]),
                    self.CommentInfo_type: 'response',
                    self.ID_Index: int(dfi[self.CommentInfo_IDIndex].iloc[0])
                })
                cnt += 1
                if cnt > length and (length != -1):
                    break

    def readBiliBiliUserInfo(self):
        self.data = [
            {self.UserInfo_UserName: '金渐层烤乳牛', self.UserInfo_RegisterTime: '2023-09-04 10:22:14',
             self.UserInfo_IPLocation: "中国 台湾",
             self.UserInfo_Level: 6,
             self.ID_Index: 1
             },
            {self.UserInfo_UserName: '幻舞*Ustd', self.UserInfo_RegisterTime: '2019-07-01 07:22:14',
             self.UserInfo_IPLocation: "哈萨克斯坦",
             self.UserInfo_Level: 5,
             self.ID_Index: 2
             },
        ]

    def readWangyiNews(self, Location=None, ID_Index=1, length=-1):
        if Location is None:
            self.data = [
                {self.ID_Index: 1,
                 self.NewsInfo_location: '北京',
                 self.NewsInfo_Time: '2023-09-04 10:22:14',
                 self.NewsInfo_source: "网易新闻",
                 self.NewsInfo_read: 451,
                 self.NewsInfo_Title: "华为Mate60再度开售",
                 self.NewsInfo_content: '【手机中国新闻】最近，华为再度开售了两款Mate60系列手机，吸引了大量网友的关注。而9月4日，手机中国注意到，Global Times（环球日报）制作了一张“华为突破美国技术封锁”的讽刺漫画，并且将它发表在了X平台（原推特平台）上。我们可以看到，图中带有华为“HUAWEI”字母LOGO的车辆突破了美国人在公路上设置的路障，然后扬长而去，只让对方留下了一个惊讶的表情……有海外网友在Global Times的评论区回复到，在埃隆马斯克的“推特”平台上，华为已经走在了前面。全球卫星通信，这是一个巨大的游戏规则改变者，而华为现在正在该领域处于领先地位。'},
                {self.ID_Index: 1,
                 self.NewsInfo_location: '北京',
                 self.NewsInfo_Time: '2023-09-04 20:25:19',
                 self.NewsInfo_source: "网易新闻",
                 self.NewsInfo_read: 0,
                 self.NewsInfo_Title: "华为Mate60新机开售",
                 self.NewsInfo_content: '【手机中国新闻】华为在上周突然宣布开售新机Mate 60系列新机的消息，不仅在国内引发了热议，同时在全球范围内更是吸引了不少个人和媒体的关注，其所搭载的麒麟9000S自研芯片更是震惊了无数人。而不少国外网友，也在X（原推特）发表了对这款华为新机的看法。'},
            ]
        else:
            print("loading data from excel or csv")
            _DF = self.readNewsTable()
            self.data = []
            cnt = 0
            for i in tqdm.tqdm(range(len(_DF))):
                dfi = _DF.iloc[i:i + 1]
                if dfi[self.NewsInfo_platform].iloc[0] != self.platform:
                    continue
                self.data.append({
                    self.NewsInfo_Title: dfi[self.NewsInfo_Title].iloc[0],
                    self.NewsInfo_content: str(dfi[self.NewsInfo_content].iloc[0]),
                    self.NewsInfo_Time: str(dfi[self.NewsInfo_Time].iloc[0]),
                    self.NewsInfo_location: str(dfi[self.NewsInfo_location].iloc[0]),
                    self.NewsInfo_read: random.randint(0, 10000),
                    self.NewsInfo_source: "网易新闻",
                    self.ID_Index: int(dfi[self.ID_Index].iloc[0])
                })
                cnt += 1
                if cnt > length and (length != -1):
                    break

    def readWangyiUserInfo(self):
        self.data = [
            {self.UserInfo_UserName: '金渐层烤乳牛', self.UserInfo_RegisterTime: '2023-09-04 10:22:14',
             self.UserInfo_IPLocation: "中国 台湾",
             self.UserInfo_Level: 6,
             self.ID_Index: 1
             },
            {self.UserInfo_UserName: '猪猪侠', self.UserInfo_RegisterTime: '2019-07-01 07:22:14',
             self.UserInfo_IPLocation: "巴林",
             self.UserInfo_Level: 5,
             self.ID_Index: 2
             },
        ]

    def readZhihuComment(self, Location=None, ID_Index=1, length=-1):
        if Location is None:
            self.data = [
                {self.CommentInfo_UserName: '卡松', 'location': '江西', 'reliability': 0.91, 'time': '2023-09-04 20:22',
                 self.CommentInfo_like: 4869,
                 self.CommentInfo_type: 'answer',
                 self.ID_Index: 1,
                 self.CommentInfo_content: '中兴：我挨打了，他们敲诈我十亿美元。众人沉默。华为：我也挨打了，美国人封锁我。众人沉默，惴惴不安。海康、曙光等一众继续挨打。众人开始扎堆讨论，TMD美国人不能信啊，不能把命交到海外供应链里。于是：工信部出来讲话，要自强；发改委财政部出来给支持；中科院说缺啥咱就搞啥，但光靠我不行，要大家一起上；证监会说我给大家整科创板，打通社会融资。缺设备，上海方阵议论了一会儿，中微站起来，说我是中字头，我先上，把蚀刻做了。华创说，哥，我来搭把手。上微看了华为一眼，说光刻我从二十多纳米开始追。缺大硅片，沪硅想了一会儿站起来，看了一眼京津冀方阵，说我还年轻，死就死了，我上。中环握紧拳头致意。缺光刻胶，一众个头小的企业手拉手站起来，说我们一个人干不成，但可以一起干。缺EDA，大家都面面相觑，北京方阵站起来个小个子，华大九天哭着说，大家帮帮我，我去试试。设备出来总要有人试。中芯才要站起来，华虹按住他，说我先来。华润微说，咱一起来。中芯问那谁来做下游，谁来做应用。封测三雄站起来说义不容辞。兆易汇顶韦尔澜起也纷纷站起来。整个深圳方阵都站起来，还坐着的企业几乎都站起来了。大基金看了一圈说，钱不够的我去找。中国烟草当即掏出支票簿。证监会说我以最快速度批上市重组定增。发改委说，谁这时候骗补，我弄死谁。华为沉默着抽完最后几口烟，站起来说，只要我一天不死，就和大家努力自建IDM一天。'},
                {self.CommentInfo_UserName: 'daniellin', 'location': '福建', 'reliability': 0.97, 'time': '2023-09-04 00:22',
                 self.CommentInfo_like: 422,
                 self.CommentInfo_type: 'comment',
                 self.ID_Index: 1,
                 self.CommentInfo_content: '之前看到一个人说过：你生于这个国家，就回避不了宏大的叙事背景，这是生于大国的国民宿命。'},
                {self.CommentInfo_UserName: '上下求索', 'location': '浙江', 'reliability': 0.80, 'time': '2023-09-04 01:02',
                 self.CommentInfo_like: 93,
                 self.CommentInfo_type: 'comment',
                 self.ID_Index: 1,
                 self.CommentInfo_content: '这也是中国人几千年的文化基因，也是中国人区别于其他民族的地方。\n全世界也有其他大国，但是像中国这样宏大叙事，仅此一家。'}
            ]
        else:
            print("loading data from excel or csv")
            _DF = self.readCommentTable()
            self.data = []
            cnt = 0
            for i in tqdm.tqdm(range(len(_DF))):
                dfi = _DF.iloc[i:i + 1]
                if dfi[self.CommentInfo_platform].iloc[0] != self.platform:
                    continue
                self.data.append({
                    self.CommentInfo_UserName: dfi[self.CommentInfo_UserName].iloc[0],
                    self.CommentInfo_time: str(dfi[self.CommentInfo_time].iloc[0]),
                    self.CommentInfo_like: int(dfi[self.CommentInfo_like].iloc[0]),
                    self.CommentInfo_content: dfi[self.CommentInfo_content].iloc[0],
                    self.CommentInfo_type: 'response',
                    self.ID_Index: int(dfi[self.CommentInfo_IDIndex].iloc[0])
                })
                cnt += 1
                if cnt > length and (length != -1):
                    break

    def readZhihuUserInfo(self):
        self.data = [
            {self.UserInfo_UserName: '金渐层烤乳牛猪', self.UserInfo_RegisterTime: '2023-09-04 10:22:14',
             self.UserInfo_IPLocation: "中国 台湾",
             self.UserInfo_Level: 6,
             self.ID_Index: 1
             },
            {self.UserInfo_UserName: '幻舞*Ustd', self.UserInfo_RegisterTime: '2019-07-01 07:22:14',
             self.UserInfo_IPLocation: "哈萨克斯坦",
             self.UserInfo_Level: 5,
             self.ID_Index: 2
             },
        ]

    def readEventList(self):
        self.data = EventList
        self.maxID = int(self.data['maximum ID'])