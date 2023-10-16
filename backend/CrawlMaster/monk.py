# --coding:utf-8--
from flask import Flask
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCDFWA"


class BaseInfo:
    def __init__(self):
        self.info = {
            "time": str(datetime.datetime.now().strftime("%Y %D %H:%M:%S"))
        }
        self.data = ""
        self.platform = ""

    def load_data(self):
        pass

    def fetch(self):
        self.load_data()
        self.info['platform'] = self.platform
        self.info['data'] = self.data
        return self.info


class BilibiliUserInfo(BaseInfo):
    def __init__(self):
        super(BilibiliUserInfo, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.data = [
            [
                {'UserID': '金渐层烤乳牛', 'register time': '2023-09-04 10:22:14',
                 'IP location': "中国 台湾",
                 'Level': 6
                 },
                {'UserID': '幻舞*Ustd', 'register time': '2019-07-01 07:22:14',
                 'IP location': "哈萨克斯坦",
                 'Level': 5
                 },
            ]
        ]


class BilibiliComment(BaseInfo):
    def __init__(self):
        super(BilibiliComment, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.data = [
            [
                {'username': '林中小屋', 'time': '2023-08-30 05:23', 'like': 21647,
                 'content': '芯片上的那个数字20应该不是年份'},
                {'username': '元寳ATTO', 'time': '2023-08-30 08:27', 'like': 950,
                 'content': '回复 @林中小屋 :以后等这个量再大一点再看看吧，我估计这个2035没这么简单'},
            ],
            [
                {'username': '林一崇伟', 'time': '2023-08-30 06:25', 'like': 46843,
                 'content': '华为:让我康康在这我不在的4年里友商都做了什么突破\n友商:24g运存，240w快充，没有优化好的cmos\n华为:6，谢谢，都是真哥们'},
                {'username': 'Serpentera', 'time': '2023-08-30 08:22', 'like': 1613,
                 'content': '还有绿厂放弃了自研芯片'},
                {'username': '林黛玉醉打蒋门神丶', 'time': '2023-08-30 08:35', 'like': 8628,
                 'content': '的确，华为被制裁之后，手机市场突然就萎缩了，抛开疫情的原因，这些年确实没出现像样的旗舰机型，更没有让人看一眼就特别想买的手机[微笑]'},
            ],
        ]


class ZhihuComment(BaseInfo):
    def __init__(self):
        super(ZhihuComment, self).__init__()
        self.platform = 'zhihu'

    def load_data(self):
        self.data = [
            [
                {'username': '卡松', 'location': '江西', 'reliability': 0.91, 'time': '2023-09-04 20:22', 'like': 4869,
                 'type': 'answer',
                 'content': '中兴：我挨打了，他们敲诈我十亿美元。众人沉默。华为：我也挨打了，美国人封锁我。众人沉默，惴惴不安。海康、曙光等一众继续挨打。众人开始扎堆讨论，TMD美国人不能信啊，不能把命交到海外供应链里。于是：工信部出来讲话，要自强；发改委财政部出来给支持；中科院说缺啥咱就搞啥，但光靠我不行，要大家一起上；证监会说我给大家整科创板，打通社会融资。缺设备，上海方阵议论了一会儿，中微站起来，说我是中字头，我先上，把蚀刻做了。华创说，哥，我来搭把手。上微看了华为一眼，说光刻我从二十多纳米开始追。缺大硅片，沪硅想了一会儿站起来，看了一眼京津冀方阵，说我还年轻，死就死了，我上。中环握紧拳头致意。缺光刻胶，一众个头小的企业手拉手站起来，说我们一个人干不成，但可以一起干。缺EDA，大家都面面相觑，北京方阵站起来个小个子，华大九天哭着说，大家帮帮我，我去试试。设备出来总要有人试。中芯才要站起来，华虹按住他，说我先来。华润微说，咱一起来。中芯问那谁来做下游，谁来做应用。封测三雄站起来说义不容辞。兆易汇顶韦尔澜起也纷纷站起来。整个深圳方阵都站起来，还坐着的企业几乎都站起来了。大基金看了一圈说，钱不够的我去找。中国烟草当即掏出支票簿。证监会说我以最快速度批上市重组定增。发改委说，谁这时候骗补，我弄死谁。华为沉默着抽完最后几口烟，站起来说，只要我一天不死，就和大家努力自建IDM一天。'},
                {'username': 'daniellin', 'location': '福建', 'reliability': 0.97, 'time': '2023-09-04 00:22',
                 'like': 422,
                 'type': 'comment',
                 'content': '之前看到一个人说过：你生于这个国家，就回避不了宏大的叙事背景，这是生于大国的国民宿命。'},
                {'username': '上下求索', 'location': '浙江', 'reliability': 0.80, 'time': '2023-09-04 01:02',
                 'like': 93,
                 'type': 'comment',
                 'content': '这也是中国人几千年的文化基因，也是中国人区别于其他民族的地方。\n全世界也有其他大国，但是像中国这样宏大叙事，仅此一家。'}
            ]
        ]


class WangYiNews(BaseInfo):
    def __init__(self):
        super(WangYiNews, self).__init__()
        self.platform = 'wangyi'

    def load_data(self):
        self.data = [
            [
                {'location': '北京', 'time': '2023-09-04 10:22:14',
                 'source': "手机中国",
                 'read': 451,
                 'content': '【手机中国新闻】最近，华为再度开售了两款Mate60系列手机，吸引了大量网友的关注。而9月4日，手机中国注意到，Global Times（环球日报）制作了一张“华为突破美国技术封锁”的讽刺漫画，并且将它发表在了X平台（原推特平台）上。我们可以看到，图中带有华为“HUAWEI”字母LOGO的车辆突破了美国人在公路上设置的路障，然后扬长而去，只让对方留下了一个惊讶的表情……有海外网友在Global Times的评论区回复到，在埃隆马斯克的“推特”平台上，华为已经走在了前面。全球卫星通信，这是一个巨大的游戏规则改变者，而华为现在正在该领域处于领先地位。'},
                {'location': '北京', 'time': '2023-09-04 20:25:19',
                 'source': "手机中国",
                 'read': 0,
                 'content': '【手机中国新闻】华为在上周突然宣布开售新机Mate 60系列新机的消息，不仅在国内引发了热议，同时在全球范围内更是吸引了不少个人和媒体的关注，其所搭载的麒麟9000S自研芯片更是震惊了无数人。而不少国外网友，也在X（原推特）发表了对这款华为新机的看法。'},
            ]
        ]


commentList = [
    BilibiliComment(),
    ZhihuComment()
]

newsList = [
    WangYiNews()
]

userList = [
    BilibiliUserInfo()
]


class SupportedPlatform(BaseInfo):
    def __init__(self):
        super(SupportedPlatform, self).__init__()

    def load_data(self):
        self.data = {
            "评论类平台": [i.platform for i in commentList],
            "新闻类平台": [i.platform for i in newsList]
        }


@app.route('/fetchcomment/<platform>')
def fetchComment(platform):
    for identity in commentList:
        if identity.platform == platform:
            return identity.fetch()
    return f"NO such platform called {platform}"


@app.route('/fetchnews/<platform>')
def fetchNews(platform):
    for identity in newsList:
        if identity.platform == platform:
            return identity.fetch()
    return f"NO such platform called {platform}"


@app.route('/fetchuserinfo/<platform>')
def fetchUser(platform):
    for identity in userList:
        if identity.platform == platform:
            return identity.fetch()
    return f"NO such platform called {platform}"


@app.route('/supportedplatform')
def supportedPlatform():
    a = SupportedPlatform()
    return a.fetch()


if __name__ == '__main__':
    app.run()
