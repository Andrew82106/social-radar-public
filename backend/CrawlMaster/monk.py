# --coding:utf-8--
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current_path))
sys.path.append(os.path.join(os.path.dirname(current_path), '/CrawlMaster'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/database'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/SparkModel_V30'))

try:
    from database.EventQuota import EventQuota
    from database.UserQuota import UserQuota
    from database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from database.EventList import EventLst
    from database.Search import Search
    from database.ServerStatus import ServerStatus
    from database.SummaryData import SummaryData
    from database.AutoCache import Cache
    from SparkModel_V30.SparkApi import SparkChatModel
    from QuotaCalculate.timeQuota import TimeQuota
    from QuotaCalculate.SensitiveQuota import SensitiveQuota
    from QuotaCalculate.EmotionEvaluationQuota import EmotionEvaluationQuota
    from QuotaCalculate.OpinionQuota import OpinionQuota
except:
    from ..database.EventQuota import EventQuota
    from ..database.UserQuota import UserQuota
    from ..database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from ..database.EventList import EventLst
    from ..database.Search import Search
    from ..database.ServerStatus import ServerStatus
    from ..database.SummaryData import SummaryData
    from ..database.AutoCache import Cache
    from ..SparkModel_V30.SparkApi import SparkChatModel
    from ..QuotaCalculate.timeQuota import TimeQuota
    from ..QuotaCalculate.SensitiveQuota import SensitiveQuota
    from ..QuotaCalculate.EmotionEvaluationQuota import EmotionEvaluationQuota
    from ..QuotaCalculate.OpinionQuota import OpinionQuota

from flask import Flask, request
from flask_cors import CORS

cache = Cache()
EventList = EventLst()

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config["SECRET_KEY"] = "ABCDFWA"
SupportedPlatform = SupportedPlatform()


@app.route('/fetchcomment/')
def fetchComment():
    platform = request.args.get("platform")
    count = request.args.get("count")
    page = request.args.get("page")
    for identity in commentList:
        if identity.platform == platform:
            return identity.fetchPage(count, page)
    return f"NO such platform called {platform}"


@app.route('/fetchnews/')
def fetchNews():
    platform = request.args.get("platform")
    count = request.args.get("count")
    page = request.args.get("page")
    for identity in newsList:
        if identity.platform == platform:
            return identity.fetchPage(count, page)
    return f"NO such platform called {platform}"


@app.route('/fetchuserinfo/<platform>')
def fetchUser(platform):
    for identity in userList:
        if identity.platform == platform:
            return identity.fetch()
    return f"NO such platform called {platform}"


@app.route('/supportedplatform')
def supportedPlatform():
    return SupportedPlatform.fetch()


@app.route('/eventList')
def supportedEventList():
    return EventList.fetch()


@app.route('/fetchdetailcomment/')
def fetchDetailComment():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    # print(eventid, platform)
    for identity in commentList:
        if identity.platform == platform:
            res = identity.fetch_detail(eventid)
            return res

    return f"NO such platform called {platform}"


@app.route('/fetchdetailnews/')
def fetchDetailNews():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    for identity in newsList:
        if identity.platform == platform:
            res = identity.fetch_detail(eventid)
            return res
    return f"NO such platform called {platform}"


@app.route('/fetchdetailuserinfo/')
def fetchDetailUser():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    for identity in userList:
        if identity.platform == platform:
            res = identity.fetch_detail(eventid)
            return res
    return f"NO such platform called {platform}"


@app.route('/fetcheventquota/')
def fetchEventQuota():
    eventQuota = EventQuota()
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    res = eventQuota.fetch_detail(eventid, platform)
    if res is None:
        return eventQuota.packetFormat(f"NO such event {eventid} in {platform}")
    else:
        return eventQuota.packetFormat(res)


@app.route('/fetchuserquota/')
def fetchUserQuota():
    userQuota = UserQuota()
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    res = userQuota.fetch_detail(eventid, platform)
    if res is None:
        return userQuota.packetFormat(f"NO such event {eventid} in {platform}")
    else:
        return userQuota.packetFormat(res)


@app.route('/addEvent/<wordlist>')
def addEvent(wordlist):
    Lst = str(wordlist).split("-")
    EventList.addEvent(Lst)
    return EventList.fetch()


@app.route('/delEvent/<eventid>')
def delEvent(eventid):
    EventList.delEvent(eventid)
    return EventList.fetch()


@app.route('/searchuser/<keyword>')
def searchUser(keyword):
    a = Search()
    return a.SearchUserName(keyword)


@app.route('/searchcontent/<keyword>')
def searchContent(keyword):
    a = Search()
    res = a.SearchContent(keyword)
    return res


@app.route('/serverstatus/')
def ServerState():
    a = ServerStatus()
    return a.fetch()


@app.route('/dataoverview/')
def dataOverview():
    a = SummaryData()
    return a.fetch()


@app.route('/llmsummarytext/<TEXT>')
def llmSummary(TEXT):
    a = SparkChatModel()
    a.chat(TEXT)
    return a.fetch()


@app.route('/timequota/gettimeseq/')
def getTimeSeq():
    eventid = request.args.get("eventid")
    mode = request.args.get("mode")
    a = TimeQuota()
    a.getDateListofAllPlatform(int(eventid), mode)
    return a.fetch()


@app.route('/searcheventdetail/')
def searchEventDetail():
    eventid = request.args.get("eventid")
    platform = request.args.get("platform")
    keyword = request.args.get("keyword")
    count = request.args.get("count")
    page = request.args.get("page")
    a = Search()
    a.SearchContentInDetail(keyword, platform, eventid)
    return a.fetchPage(count, page)


@app.route('/refresh/')
def refresh():
    return cache.del_cache()


@app.route('/summaryEventByPlatform')
def summaryEventByPlatform():
    return SupportedPlatform.summaryEventByPlatform()


@app.route('/summaryPlatformByEvent')
def summaryPlatformByEvent():
    return SupportedPlatform.summaryPlatformByEvent()


@app.route('/deleteplatform/')
def deletePlatform():
    platformName = request.args.get("platformName")
    SupportedPlatform.delPlatform(platformName)
    return SupportedPlatform.fetch()


@app.route('/addplatform/')
def addPlatform():
    platformName = request.args.get("platformName")
    platformType = request.args.get("platformType")
    SupportedPlatform.addPlatform(platformType, platformName)
    return SupportedPlatform.fetch()


@app.route('/summaryLocationByPlatform/')
def summaryLocationByPlatform():
    eventID = request.args.get("eventID")
    Platform = request.args.get("Platform")
    for instance in userList:
        if instance.platform != Platform:
            continue
        return instance.summary_location(eventID)


@app.route('/summaryLocationall/')
def summaryLocationall():
    eventID = request.args.get("eventID")
    res = {}
    for instance in userList:
        res_for_instance = instance.summary_location(eventID)['data']
        for location in res_for_instance:
            if location not in res:
                res[location] = 0
            res[location] += res_for_instance[location]
    return userList[0].packetFormat(res)


x = SensitiveQuota()


@app.route('/sensitivedataOverview/')
def sensitivedataOverview():
    return x.sensitiveDataOverview()


@app.route('/sensitivedataDetect/<sentence>')
def sensitivedataDetect(sentence):
    return x.sensitiveWordCheck(sentence)


@app.route('/sensitivedataOverviewDetail/')
def sensitivedataOverviewDetail():
    eventID = request.args.get("eventID")
    Platform = request.args.get("Platform")
    return x.summarySensitiveWord(eventID, Platform)


y = EmotionEvaluationQuota()


@app.route('/EmotionDataDetail/')
def EmotionDataDetail():
    eventID = request.args.get("eventID")
    Platform = request.args.get("Platform")
    mode = request.args.get("mode")
    return y.calcScoreByEventAndPlatform(eventID, Platform, mode)


y1 = OpinionQuota()


@app.route('/OpinionDataDetail/')
def OpinionDataDetail():
    eventID = request.args.get("eventID")
    Platform = request.args.get("Platform")
    return y1.calcOpinionQuota(eventID, Platform)


if __name__ == '__main__':
    app.run(debug=True)
