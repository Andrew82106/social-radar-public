from BaseInfo import BaseInfo


class BilibiliComment(BaseInfo):
    def __init__(self):
        super(BilibiliComment, self).__init__()
        self.platform = 'bilibili'

    def load_data(self):
        self.data = [
            {'username': '林中小屋', 'time': '2023-08-30 05:23', 'like': 21647,
             'content': '芯片上的那个数字20应该不是年份',
             self.ID_Index: 1},
            {'username': '元寳ATTO', 'time': '2023-08-30 08:27', 'like': 950,
             'content': '回复 @林中小屋 :以后等这个量再大一点再看看吧，我估计这个2035没这么简单',
             self.ID_Index: 1},
            {'username': '林一崇伟', 'time': '2023-08-30 06:25', 'like': 46843,
             'content': '华为:让我康康在这我不在的4年里友商都做了什么突破\n友商:24g运存，240w快充，没有优化好的cmos\n华为:6，谢谢，都是真哥们',
             self.ID_Index: 1},
            {'username': 'Serpentera', 'time': '2023-08-30 08:22', 'like': 1613,
             'content': '还有绿厂放弃了自研芯片',
             self.ID_Index: 1},
            {'username': '林黛玉醉打蒋门神丶', 'time': '2023-08-30 08:35', 'like': 8628,
             'content': '的确，华为被制裁之后，手机市场突然就萎缩了，抛开疫情的原因，这些年确实没出现像样的旗舰机型，更没有让人看一眼就特别想买的手机[微笑]',
             self.ID_Index: 1},
        ]