# --coding:utf-8--
import os
import sys

current_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(current_path))
sys.path.append(os.path.join(os.path.dirname(current_path), '/CrawlMaster'))
sys.path.append(os.path.join(os.path.dirname(current_path), '/database'))

try:
    from database.EventQuota import EventQuota
    from database.UserQuota import UserQuota
    from database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from database.EventList import EventLst
    from database.Search import Search
except:
    from ..database.EventQuota import EventQuota
    from ..database.UserQuota import UserQuota
    from ..database.globalConfig import SupportedPlatform, commentList, newsList, userList
    from ..database.EventList import EventLst
    from ..database.Search import Search

from flask import Flask, request
from flask_cors import CORS

EventList = EventLst()


app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])
app.config["SECRET_KEY"] = "ABCDFWA"


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


@app.route('/eventList')
def supportedEventList():
    return EventList.fetch()


@app.route('/fetchdetailcomment/')
def fetchDetailComment():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    for identity in commentList:
        if identity.platform == platform:
            return identity.fetch_detail(eventid)
    return f"NO such platform called {platform}"


@app.route('/fetchdetailnews/')
def fetchDetailNews():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    for identity in newsList:
        if identity.platform == platform:
            return identity.fetch_detail(eventid)
    return f"NO such platform called {platform}"


@app.route('/fetchdetailuserinfo/')
def fetchDetailUser():
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    for identity in userList:
        if identity.platform == platform:
            return identity.fetch_detail(eventid)
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
    return a.SearchContent(keyword)


if __name__ == '__main__':
    app.run(debug=True)
