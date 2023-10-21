from BaseInfo import BaseInfo


class WangYiNews(BaseInfo):
    def __init__(self):
        super(WangYiNews, self).__init__()
        self.platform = 'wangyi'

    def load_data(self):
        self.data = [
            {self.ID_Index: 1,
             'location': '北京', 'time': '2023-09-04 10:22:14',
             'source': "手机中国",
             'read': 451,
             'content': '【手机中国新闻】最近，华为再度开售了两款Mate60系列手机，吸引了大量网友的关注。而9月4日，手机中国注意到，Global Times（环球日报）制作了一张“华为突破美国技术封锁”的讽刺漫画，并且将它发表在了X平台（原推特平台）上。我们可以看到，图中带有华为“HUAWEI”字母LOGO的车辆突破了美国人在公路上设置的路障，然后扬长而去，只让对方留下了一个惊讶的表情……有海外网友在Global Times的评论区回复到，在埃隆马斯克的“推特”平台上，华为已经走在了前面。全球卫星通信，这是一个巨大的游戏规则改变者，而华为现在正在该领域处于领先地位。'},
            {self.ID_Index: 1,
             'location': '北京', 'time': '2023-09-04 20:25:19',
             'source': "手机中国",
             'read': 0,
             'content': '【手机中国新闻】华为在上周突然宣布开售新机Mate 60系列新机的消息，不仅在国内引发了热议，同时在全球范围内更是吸引了不少个人和媒体的关注，其所搭载的麒麟9000S自研芯片更是震惊了无数人。而不少国外网友，也在X（原推特）发表了对这款华为新机的看法。'},
        ]