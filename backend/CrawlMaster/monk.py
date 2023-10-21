# --coding:utf-8--
import sys
sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend')
sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/CrawlMaster')
sys.path.append('/Users/andrewlee/Desktop/Projects/2023大创/social-radar/backend/database')
from database.BaseInfo import BaseInfo
from database.BilibiliUserInfo import BilibiliUserInfo
from database.BilibiliComment import BilibiliComment
from database.ZhihuComment import ZhihuComment
from database.WangYiNews import WangYiNews
from database.EventQuota import EventQuota
from database.UserQuota import UserQuota
import json
from flask import Flask, request
import datetime
app = Flask(__name__)
app.config["SECRET_KEY"] = "ABCDFWA"


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
            "新闻类平台": [i.platform for i in newsList],
            "用户信息平台": [i.platform for i in userList]
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
        return f"NO such event {eventid} in {platform}"
    else:
        return res


@app.route('/fetchuserquota/')
def fetchUserQuota():
    userQuota = UserQuota()
    eventid = request.args.get("id")
    platform = request.args.get("platform")
    print(eventid, platform)
    res = userQuota.fetch_detail(eventid, platform)
    if res is None:
        return f"NO such user {eventid} in {platform}"
    else:
        return res


if __name__ == '__main__':
    app.run()
