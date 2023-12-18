# monk.py

根据爬取的平台特性，我们将平台分成如下几类：

- 评论类，以评论、推文、博文这类中短长度文字来反映舆情，比如微博，bilibili，知乎
- 新闻类，以长篇报道、评论、文章来反应舆情，比如网易新闻，人民日报

现阶段可展示的数据有：

## 1.汇总类接口

> 支持的平台信息
- http://127.0.0.1:5000/supportedplatform
- http://127.0.0.1:5000/supportedplatform

> 当前关注的事件列表
- http://127.0.0.1:5000/eventList
- http://127.0.0.1:5000/eventList

> 服务器性能统计
- http://127.0.0.1:5000/serverstatus
- http://127.0.0.1:5000/serverstatus

> 总体数据量统计
- http://127.0.0.1:5000/dataoverview
- http://127.0.0.1:5000/dataoverview

> 查看事件中可选的平台
- http://127.0.0.1:5000/summaryPlatformByEvent
- http://127.0.0.1:5000/summaryPlatformByEvent

> 查看每个平台中包含的事件
- http://127.0.0.1:5000/summaryEventByPlatform
- http://127.0.0.1:5000/summaryEventByPlatform

> 查询敏感词表汇总情况
- http://127.0.0.1:5000/sensitivedataOverview
- http://127.0.0.1:5000/sensitivedataOverview


## 2 基础数据资料获取接口

获取支撑平台计算的从开源平台爬取的基础数据

### 2.1 按照平台分类

> 不同评论类平台爬取的舆情对象文本内容和文本相关信息（所有信息），并按照count条信息每页的格式返回第page页
- http://127.0.0.1:5000/fetchcomment/?platform=[platform]&count=[count]&page=[page]
- http://127.0.0.1:5000/fetchcomment/?platform=bilibili&count=30&page=2

> 不同新闻类平台爬取的舆情对象文本内容和文本相关信息（所有信息），并按照count条信息每页的格式返回第page页
- http://127.0.0.1:5000/fetchnews/?platform=[platform]&count=[count]&page=[page]
- http://127.0.0.1:5000/fetchnews/?platform=wangyi&count=30&page=2

> 平台用户相关信息（所有用户信息）
- http://127.0.0.1:5000/fetchuserinfo/[platform]
- http://127.0.0.1:5000/fetchuserinfo/bilibili


### 2.2 按照事件分类

> 查询对于事件eventid，所有平台的相关用户的地域分布
- http://127.0.0.1:5000/summaryLocationall/?eventid=[eventid]
- http://127.0.0.1:5000/summaryLocationall/?eventid=2

### 2.3 按照平台和事件分类

> 不同评论类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息），并按照count条信息每页的格式返回第page页
- http://127.0.0.1:5000/fetchdetailcomment/?id=[EVENTID]&platform=[PLATFORM]&count=[count]&page=[page]
- http://127.0.0.1:5000/fetchdetailcomment/?id=2&platform=zhihu&count=6&page=1

> 不同新闻类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息），并按照count条信息每页的格式返回第page页
- http://127.0.0.1:5000/fetchdetailnews/?id=[EVENTID]&platform=[PLATFORM]&count=[count]&page=[page]
- http://127.0.0.1:5000/fetchdetailnews/?id=1&platform=wangyi&count=6&page=1

> 查询对于事件eventid，平台platform的相关用户的地域分布
- http://127.0.0.1:5000/summaryLocationByPlatform/?eventid=[eventid]&Platform=[Platform]
- http://127.0.0.1:5000/deleteplatform/?platformName=wangyi

## 3 后端操作接口

> 添加一个事件
- http://127.0.0.1:5000/addEvent/[wordlist]
- http://127.0.0.1:5000/addEvent/阿里|P0|故障|666

> 删除一个事件
- http://127.0.0.1:5000/delEvent/[eventid]
- http://127.0.0.1:5000/delEvent/2

> 删除项目缓存
- http://127.0.0.1:5000/refresh
- http://127.0.0.1:5000/refresh

> 在平台类型为platformType的类型中添加平台名为platformName的平台，platformType可选：新闻类平台、用户信息平台、评论类平台
- http://127.0.0.1:5000/addplatform/?platformType=[platformType]&platformName=[platformName]
- http://127.0.0.1:5000/addplatform/?platformType=评论类平台&platformName=baidu1111

> 在所有平台类型中删除名为platformName的平台
- http://127.0.0.1:5000/deleteplatform/?platformName=[platformName]
- http://127.0.0.1:5000/summaryLocationByPlatform/?eventid=1&Platform=bilibili

## 4 搜索类接口

### 4.1 全文搜索

> 全文搜索用户名称
- http://127.0.0.1:5000/searchuser/[keyword]
- http://127.0.0.1:5000/searchuser/猪

> 全文搜索事件内容
- http://127.0.0.1:5000/searchcontent/[keyword]
- http://127.0.0.1:5000/searchcontent/人

### 4.2 特定平台搜索

> 平台**某位用户**相关信息（仅用户相关信息）
- http://127.0.0.1:5000/fetchdetailuserinfo/?id=[USERID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetchdetailuserinfo/?id=1&platform=bilibili

### 4.3 特定平台特定事件搜索

> 从某个平台platform中的某个事件eventid中搜索某个关键词keyword，并按照count条信息每页的格式返回第page页
- http://127.0.0.1:5000/searcheventdetail/?eventid=[eventid]&platform=[platform]&keyword=[keyword]&count=[count]&page=[page]
- http://127.0.0.1:5000/searcheventdetail/?eventid=1&platform=bilibili&keyword=我们&count=5&page=0

## 5 指标类接口

指标包括：

1. 时间指标
2. 内容敏感度指标
3. 用户真实度指标
4. 情感激烈性指标
5. 观点对立性指标
6. 总指标

### 5.1 按照事件和平台分类

#### 5.1.1 返回总数值指标

总数值指标是指对于某个对象的汇总值，是一个或多个指标，与时间无关

> **某个事件**在**某个平台**中的相关指标
- http://127.0.0.1:5000/fetcheventquota/?id=[EVENTID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetcheventquota/?id=1&platform=bilibili

> **某个用户**在**某个平台**中的相关指标
- http://127.0.0.1:5000/fetchuserquota/?id=[USERID]&platform=[PLATFORM]
- http://127.0.0.1:5000/fetchuserquota/?id=1&platform=bilibili

#### 5.1.2 返回基于时间序列的指标

基于时间序列是指该指标在每一合法日期都会有一个值

> 计算platform中eventid事件的**情感激烈性指标**(第一次计算耗时很久，需要写等待效果)，mode参数设置时间的精确度，mode=date则时间精确到日
- http://127.0.0.1:5000/EmotionDataDetail/?eventid=[eventid]&Platform=[Platform]&mode=[mode]
- http://127.0.0.1:5000/EmotionDataDetail/?eventid=1&Platform=bilibili&mode=date

> 计算platform中eventid事件的**观点指标**，时间精确到日
- http://127.0.0.1:5000/OpinionDataDetail/?eventid=[eventid]&Platform=[Platform]
- http://127.0.0.1:5000/OpinionDataDetail/?eventid=1&Platform=bilibili

> 计算对于事件eventid，平台platform中的**用户综合指标**，时间精确到日
- http://127.0.0.1:5000/UserDataByDate/?eventid=[eventid]&platform=[platform]
- http://127.0.0.1:5000/UserDataByDate/?eventid=1&platform=bilibili

> 计算对于事件eventid，平台platform中的**总指标**，时间精确到日
- http://127.0.0.1:5000/SummaryQuota/?eventid=[eventid]&platform=[platform]
- http://127.0.0.1:5000/SummaryQuota/?eventid=1&platform=zhihu

> 返回对于事件eventid，平台platform的日期列表，时间精确到日
- http://127.0.0.1:5000/timeseq/?eventid=[eventid]&platform=[platform]
- http://127.0.0.1:5000/timeseq/?eventid=1&platform=zhihu

> 计算对于事件eventid，平台platform中的**时间热度**序列
- http://127.0.0.1:5000/timequota/gettimeseqdetail/?eventid=[eventid]?platform=[PLATFORM]
- http://127.0.0.1:5000/timequota/gettimeseqdetail/?eventid=1&platform=zhihu

> 计算对于事件eventid，平台platform中的**内容敏感度**序列
- http://127.0.0.1:5000/SensitiveDataDetail/?eventid=[eventid]&Platform=[Platform]
- http://127.0.0.1:5000/SensitiveDataDetail/?eventid=1&Platform=zhihu

#### 5.1.3 返回词频统计情况

> 基于敏感词表统计platform中eventid事件的敏感词总体情况
- http://127.0.0.1:5000/sensitivedataOverviewDetail/?eventid=[EVENTID]&Platform=[PLATFORM]
- http://127.0.0.1:5000/sensitivedataOverviewDetail/?eventid=1&Platform=bilibili

### 5.2 按照事件分类

#### 5.2.1 返回序列

> 获取不同平台下的时间指标中eventID事件的时间热度序列，按照精确度为mode返回（mode=date则精确到日期，等于其他则为精确到秒）
- http://127.0.0.1:5000/timequota/gettimeseq/?eventid=[eventid]?mode=[MODE]
- http://127.0.0.1:5000/timequota/gettimeseq/?eventid=1&mode=date

> 获取不同平台下的时间指标中eventID事件的**内容敏感度**序列，按照精确度为日期返回
- http://127.0.0.1:5000/SensitiveDataOverAll/?eventid=[eventid]
- http://127.0.0.1:5000/SensitiveDataOverAll/?eventid=2

> 获取不同平台下的时间指标中eventID事件的**用户真实度**序列，按照精确度为日期返回
- http://127.0.0.1:5000/UserQuotaOverAll/?eventid=[eventid]
- http://127.0.0.1:5000/UserQuotaOverAll/?eventid=2

> 获取不同平台下的时间指标中eventID事件的**情感激烈性**序列，按照精确度为日期返回
- http://127.0.0.1:5000/EmotionQuotaOverAll/?eventid=[eventid]
- http://127.0.0.1:5000/EmotionQuotaOverAll/?eventid=2

> 获取不同平台下的时间指标中eventID事件的**观点对立性**序列，按照精确度为日期返回
- http://127.0.0.1:5000/OpinionQuotaOverAll/?eventid=[eventid]
- http://127.0.0.1:5000/OpinionQuotaOverAll/?eventid=2

> 获取不同平台下的时间指标中eventID事件的**总指标**序列，按照精确度为日期返回
- http://127.0.0.1:5000/SummaryQuotaOverAll/?eventid=[eventid]
- http://127.0.0.1:5000/SummaryQuotaOverAll/?eventid=2

### 5.3 按照其他方式分类

> 计算平台platform中名字为username的用户的指标，返回包括指标在内的用户的所有信息
- http://127.0.0.1:5000/UserDataDetail/?userName=[userName]&platform=[platform]
- http://127.0.0.1:5000/UserDataDetail/?userName=Reachhalo&platform=bilibili

## 6 其他接口

> 使用星火大模型API接口进行文本总结
- http://127.0.0.1:5000/llmsummarytext/[TEXT]
- http://127.0.0.1:5000/llmsummarytext/?content=OpenAI 创始人 Sam Altman 当地时间 11 月 29 日宣布，他将重返 OpenAI 担任首席执行官，Mira Murati 将继续担任首席技术官。

> 基于敏感词表计算输入句子中的敏感词汇
- http://127.0.0.1:5000/sensitivedataDetect/[sentence]
- http://127.0.0.1:5000/sensitivedataDetect/明天早上车站那边整个核蛋清扫一下，兵力部属你这边要到位，不然就只能打砸抢了

接口返回的数据格式运行monk.py进行查看。