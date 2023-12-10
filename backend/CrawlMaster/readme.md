# monk.py

根据爬取的平台特性，我们将平台分成如下几类：

- 评论类，以评论、推文、博文这类中短长度文字来反映舆情，比如微博，bilibili，知乎
- 新闻类，以长篇报道、评论、文章来反应舆情，比如网易新闻，人民日报

现阶段可展示的数据有：

1. 不同评论类平台爬取的舆情对象文本内容和文本相关信息（所有信息），并按照count条信息每页的格式返回第page页
2. 不同新闻类平台爬取的舆情对象文本内容和文本相关信息（所有信息），并按照count条信息每页的格式返回第page页
3. 平台用户相关信息（所有用户信息）
4. 支持的平台信息
5. 不同评论类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息）
6. 不同新闻类平台中**某个事件**的舆情对象文本内容和文本相关信息（仅事件相关信息）
7. 平台**某位用户**相关信息（仅用户相关信息）
8. **某个事件**在**某个平台**中的相关指标
9. **某个用户**在**某个平台**中的相关指标
10. 当前关注的事件列表
11. 添加一个事件
12. 删除一个事件
13. 全文搜索用户名称
14. 全文搜索事件内容
15. 服务器性能统计
16. 总体数据量统计
17. 使用星火大模型API接口进行文本总结
18. 获取不同平台下的时间指标中eventID事件的时间热度序列，按照精确度为mode返回（mode=date则精确到日期，等于其他则为精确到秒）
19. 从某个平台platform中的某个事件eventid中搜索某个关键词keyword，并按照count条信息每页的格式返回第page页
20. 删除项目缓存
21. 查看事件中可选的平台
22. 查看每个平台中包含的事件
23. 在平台类型为platformType的类型中添加平台名为platformName的平台，platformType可选：新闻类平台、用户信息平台、评论类平台
24. 在所有平台类型中删除名为platformName的平台
25. 查询对于事件eventid，平台platform的相关用户的地域分布
26. 查询对于事件eventid，所有平台的相关用户的地域分布
27. 查询敏感词表汇总情况
28. 基于敏感词表计算输入句子中的敏感词汇
29. 基于敏感词表统计platform中eventid事件的敏感词总体情况
30. 计算platform中eventid事件的情感激烈性指标(第一次计算耗时很久，需要写等待效果)，mode参数设置时间的精确度，mode=date则时间精确到日
31. 计算platform中eventid事件的观点指标(第一次计算耗时很久，需要写等待效果)，时间精确到日
32. 计算平台platform中名字为username的用户的指标，返回包括指标在内的用户的所有信息
33. 计算对于事件eventid，平台platform中的用户综合指标，时间精确到日
34. 计算对于事件eventid，平台platform中的总指标，时间精确到日
35. 返回对于事件eventid，平台platform的日期列表，时间精确到日

对应的接口：

1. http://127.0.0.1:5000/fetchcomment/?platform=[platform]&count=[count]&page=[page]
2. http://127.0.0.1:5000/fetchnews/?platform=[platform]&count=[count]&page=[page]
3. http://127.0.0.1:5000/fetchuserinfo/[platform]
4. http://127.0.0.1:5000/supportedplatform
5. http://127.0.0.1:5000/fetchdetailcomment/?id=[EVENTID]&platform=[PLATFORM]
6. http://127.0.0.1:5000/fetchdetailnews/?id=[EVENTID]&platform=[PLATFORM]
7. http://127.0.0.1:5000/fetchdetailuserinfo/?id=[USERID]&platform=[PLATFORM]
8. http://127.0.0.1:5000/fetcheventquota/?id=[EVENTID]&platform=[PLATFORM]
9. http://127.0.0.1:5000/fetchuserquota/?id=[USERID]&platform=[PLATFORM]
10. http://127.0.0.1:5000/eventList
11. http://127.0.0.1:5000/addEvent/[wordlist]
12. http://127.0.0.1:5000/delEvent/[eventID]
13. http://127.0.0.1:5000/searchuser/[keyword]
14. http://127.0.0.1:5000/searchcontent/[keyword]
15. http://127.0.0.1:5000/serverstatus
16. http://127.0.0.1:5000/dataoverview
17. http://127.0.0.1:5000/llmsummarytext/[TEXT]
18. http://127.0.0.1:5000/timequota/gettimeseq/?eventID=[eventID]?mode=[MODE]
19. http://127.0.0.1:5000/searcheventdetail/?eventid=[eventid]&platform=[platform]&keyword=[keyword]&count=[count]&page=[page]
20. http://127.0.0.1:5000/refresh
21. http://127.0.0.1:5000/summaryPlatformByEvent
22. http://127.0.0.1:5000/summaryEventByPlatform
23. http://127.0.0.1:5000/addplatform/?platformType=[platformType]&platformName=[platformName]
24. http://127.0.0.1:5000/deleteplatform/?platformName=[platformName]
25. http://127.0.0.1:5000/summaryLocationByPlatform/?eventID=[eventID]&Platform=[Platform]
26. http://127.0.0.1:5000/summaryLocationall/?eventID=[eventID]
27. http://127.0.0.1:5000/sensitivedataOverview
28. http://127.0.0.1:5000/sensitivedataDetect/[sentence]
29. http://127.0.0.1:5000/sensitivedataOverviewDetail/?eventID=[EVENTID]&Platform=[PLATFORM]
30. http://127.0.0.1:5000/EmotionDataDetail/?eventID=[eventID]&Platform=[Platform]&mode=[mode]
31. http://127.0.0.1:5000/OpinionDataDetail/?eventID=[eventID]&Platform=[Platform]
32. http://127.0.0.1:5000/UserDataDetail/?userName=[userName]&platform=[platform]
33. http://127.0.0.1:5000/UserDataByDate/?eventid=[eventid]&platform=[platform]
34. http://127.0.0.1:5000/SummaryQuota/?eventid=[eventid]&platform=[platform]
35. http://127.0.0.1:5000/timeseq/?eventid=[eventid]&platform=[platform]

比如：

1. http://127.0.0.1:5000/fetchcomment/?platform=bilibili&count=30&page=2
2. http://127.0.0.1:5000/fetchnews/?platform=wangyi&count=30&page=2
3. http://127.0.0.1:5000/fetchuserinfo/bilibili
4. http://127.0.0.1:5000/supportedplatform
5. http://127.0.0.1:5000/fetchdetailcomment/?id=1&platform=zhihu
6. http://127.0.0.1:5000/fetchdetailnews/?id=1&platform=wangyi
7. http://127.0.0.1:5000/fetchdetailuserinfo/?id=1&platform=bilibili
8. http://127.0.0.1:5000/fetcheventquota/?id=1&platform=bilibili
9. http://127.0.0.1:5000/fetchuserquota/?id=1&platform=bilibili
10. http://127.0.0.1:5000/eventList
11. http://127.0.0.1:5000/addEvent/阿里|P0|故障|666
12. http://127.0.0.1:5000/delEvent/2
13. http://127.0.0.1:5000/searchuser/猪
14. http://127.0.0.1:5000/searchcontent/人
15. http://127.0.0.1:5000/serverstatus
16. http://127.0.0.1:5000/dataoverview
17. http://127.0.0.1:5000/llmsummarytext/?content=OpenAI 创始人 Sam Altman 当地时间 11 月 29 日宣布，他将重返 OpenAI 担任首席执行官，Mira Murati 将继续担任首席技术官。
18. http://127.0.0.1:5000/timequota/gettimeseq/?eventID=1&mode=date
19. http://127.0.0.1:5000/searcheventdetail/?eventid=1&platform=bilibili&keyword=我们&count=5&page=0
20. http://127.0.0.1:5000/refresh
21. http://127.0.0.1:5000/summaryPlatformByEvent
22. http://127.0.0.1:5000/summaryEventByPlatform
23. http://127.0.0.1:5000/addplatform/?platformType=评论类平台&platformName=baidu1111
24. http://127.0.0.1:5000/summaryLocationByPlatform/?eventID=1&Platform=bilibili
25. http://127.0.0.1:5000/deleteplatform/?platformName=wangyi
26. http://127.0.0.1:5000/summaryLocationall/?eventID=2
27. http://127.0.0.1:5000/sensitivedataOverview
28. http://127.0.0.1:5000/sensitivedataDetect/明天早上车站那边整个核蛋清扫一下，兵力部属你这边要到位，不然就只能打砸抢了
29. http://127.0.0.1:5000/sensitivedataOverviewDetail/?eventID=1&Platform=bilibili
30. http://127.0.0.1:5000/EmotionDataDetail/?eventID=1&Platform=bilibili&mode=date
31. http://127.0.0.1:5000/OpinionDataDetail/?eventID=1&Platform=bilibili
32. http://127.0.0.1:5000/UserDataDetail/?userName=Reachhalo&platform=bilibili
33. http://127.0.0.1:5000/UserDataByDate/?eventid=1&platform=bilibili
34. http://127.0.0.1:5000/SummaryQuota/?eventid=1&platform=zhihu
35. http://127.0.0.1:5000/timeseq/?eventid=1&platform=zhihu

接口返回的数据格式运行monk.py进行查看。