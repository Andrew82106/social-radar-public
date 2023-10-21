# monk.py

根据爬取的平台特性，我们将平台分成如下几类：

- 评论类，以评论、推文、博文这类中短长度文字来反映舆情，比如微博，bilibili，知乎
- 新闻类，以长篇报道、评论、文章来反应舆情，比如网易新闻，人民日报

现阶段可展示的数据有：

- 不同评论类平台爬取的舆情对象文本内容和文本相关信息（所有信息）
- 不同新闻类平台爬取的舆情对象文本内容和文本相关信息（所有信息）
- 平台用户相关信息（所有用户信息）
- 支持的平台信息
- 不同评论类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息）
- 不同新闻类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息）
- 平台**某位用户**相关信息（仅用户相关信息）
- **某个事件**在**某个平台**中的相关指标
- **某个用户**在**某个平台**中的相关指标

对应的接口：

- http://127.0.0.1:5000/fetchcomment/[platform]
- http://127.0.0.1:5000/fetchnews/[platform]
- http://127.0.0.1:5000/fetchuserinfo/[platform]
- http://127.0.0.1:5000/supportedplatform
- http://127.0.0.1:5000/fetchdetailcomment/?id=[EVENTID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetchdetailnews/?id=[EVENTID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetchdetailuserinfo/?id=[USERID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetcheventquota/?id=[EVENTID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetchuserquota/?id=[USERID]&platform=[PLATFORM]

比如：

- http://127.0.0.1:5000/fetchcomment/bilibili
- http://127.0.0.1:5000/fetchnews/wangyi
- http://127.0.0.1:5000/fetchuserinfo/bilibili
- http://127.0.0.1:5000/supportedplatform
- http://127.0.0.1:5000/fetchdetailcomment/?id=1&platform=zhihu
- http://127.0.0.1:5000/fetchdetailnews/?id=1&platform=wangyi
- http://127.0.0.1:5000/fetchdetailuserinfo/?id=1&platform=bilibili
- http://127.0.0.1:5000/fetcheventquota/?id=1&platform=bilibili
- http://127.0.0.1:5000/fetchuserquota/?id=1&platform=bilibili

接口返回的数据格式运行monk.py进行查看。

# 爬虫部分

待开发