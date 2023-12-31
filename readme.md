# 工作总览

![img.png](asset/img.png)

# 项目相关文档

[项目总结书](backend/后端项目书.md)

[后端项目接口](backend/CrawlMaster/readme.md)

[各指标计算原理](backend/QuotaCalculate/readme.md)

# 工作进度表


| 工作项目           | 内容                                                 | 完成度     | 备注 |
| ------------------ | ---------------------------------------------------- | ---------- | ---- |
| 爬虫工具构建       | 确定接口格式，构建统一接口                           | finish     |      |
|                    | 编写爬虫工具，选取某一平台进行数据爬取               | finish     |      |
| 数据清洗           | 建立数据库                                           | finish     |      |
|                    | 对接爬虫工具和数据库，进行数据入库工作               | finish     |      |
| 指标构建与后端开发 | 基于爬取的时间信息构建**时间敏感性计算方法**         | finish     |      |
|                    | 基于敏感词表构建**内容敏感性计算方法**               | finish     |      |
|                    | 基于贴文相关数据（比如点赞）构建**内容热度计算方法** | finish     |      |
|                    | 基于贴文相关数据构建**自媒体趋势评分计算方法**       | finish     |      |
|                    | 基于已有指标拟合**总评分**                           | finish     |      |
|                    | 结合社交机器人识别统一化评分计算接口                 | finish     |      |
| 前端开发           | 开发相应前端数据可视化页面等                         | processing |      |
| 编写项目报告书     | 包括理论分析，实验结果，项目说明书等内容             | finish     |      |

# old version social radar

in file **social-radar(version 0.1)** run command:``npm run dev``

效果图：

![img.png](asset/img1.png)
