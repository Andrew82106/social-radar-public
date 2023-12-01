import _thread as thread
import base64
import datetime
import hashlib
import hmac
import json
from urllib.parse import urlparse, urlencode
import ssl
from datetime import datetime
from time import mktime
from wsgiref.handlers import format_date_time
import websocket

try:
    from database.BaseInfo import BaseInfo
except:
    from ..database.BaseInfo import BaseInfo

# 初始化全局变量
answer = ""
result = []
text = []

# 配置 WebSocket 相关参数
appid = "6f0151b0"
api_secret = "MDZhYmZhMDE0YTU3OWNiOWM5MjA3NzQ1"
api_key = "061743f1e3f7ebcb6d00aa2a7ed207a5"
domain = "generalv3"
Spark_url = "ws://spark-api.xf-yun.com/v3.1/chat"


# WebSocket 参数类
class Ws_Param(object):
    def __init__(self, APPID, APIKey, APISecret, Spark_url):
        self.APPID = APPID
        self.APIKey = APIKey
        self.APISecret = APISecret
        self.host = urlparse(Spark_url).netloc
        self.path = urlparse(Spark_url).path
        self.Spark_url = Spark_url

    def create_url(self):
        now = datetime.now()
        date = format_date_time(mktime(now.timetuple()))

        signature_origin = "host: " + self.host + "\n"
        signature_origin += "date: " + date + "\n"
        signature_origin += "GET " + self.path + " HTTP/1.1"

        signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                 digestmod=hashlib.sha256).digest()

        signature_sha_base64 = base64.b64encode(signature_sha).decode(encoding='utf-8')

        authorization_origin = f'api_key="{self.APIKey}", algorithm="hmac-sha256", headers="host date request-line", signature="{signature_sha_base64}"'

        authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')

        v = {
            "authorization": authorization,
            "date": date,
            "host": self.host
        }
        url = self.Spark_url + '?' + urlencode(v)
        return url


# WebSocket 相关回调函数
def on_error(ws, error):
    print("### error:", error)


def on_close(ws, one, two):
    print(" ")


def run(ws, *args):
    data = json.dumps(gen_params(appid=ws.appid, domain=ws.domain, question=ws.question))
    ws.send(data)


def on_open(ws):
    thread.start_new_thread(run, (ws,))


def on_message(ws, message):
    data = json.loads(message)
    code = data['header']['code']
    if code != 0:
        print(f'请求错误: {code}, {data}')
        ws.close()
    else:
        choices = data["payload"]["choices"]
        status = choices["status"]
        content = choices["text"][0]["content"]
        global answer
        answer += content
        if status == 2:
            ws.close()
            result.append(answer)


# 消息生成和处理
def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length


def checklen(text):
    while getlength(text) > 8000:
        del text[0]
    return text


def getText(role, content):
    jsoncon = {"role": role, "content": content}
    text.append(jsoncon)
    return text


def gen_params(appid, domain, question):
    data = {
        "header": {
            "app_id": appid,
            "uid": "1234"
        },
        "parameter": {
            "chat": {
                "domain": domain,
                "temperature": 0.7,
                "max_tokens": 4096
            }
        },
        "payload": {
            "message": {
                "text": question
            }
        }
    }
    return data


# 主要功能函数
def main(question):
    wsParam = Ws_Param(appid, api_key, api_secret, Spark_url)
    websocket.enableTrace(False)
    wsUrl = wsParam.create_url()
    ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close, on_open=on_open)
    ws.appid = appid
    ws.question = checklen(getText("user", question))
    ws.domain = domain
    ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})


def start_new_conversation(question):
    global answer, result
    answer = ""
    result = []
    main(question)
    return result[0] if result else None


class SparkChatModel(BaseInfo):
    def __init__(self):
        super().__init__()

    @staticmethod
    def SummaryText(Content):
        prompt = "假设你现在是一个文书工作人员，你需要对我给你的这段文本材料用中文进行一个总结摘要。你的摘要应该以'以下是对文本的总结：'这类的开头开始。以下是我给你的文本的内容：\n"
        res = start_new_conversation(prompt + Content)
        return res

    def chat(self, Content):
        self.data = self.SummaryText(Content)
        if self.data is None:
            self.data = "非常抱歉，根据相关法律法规，我们无法提供关于以下内容的答案，包括但不限于：\n\t(1) 涉及国家安全的信息；\n\t(2) 涉及政治与宗教类的信息；\n\t(3) 涉及暴力与恐怖主义的信息；\n\t(4) 涉及黄赌毒类的信息；\n\t(5) 涉及不文明的信息。\n我们会继续遵循相关法规法律的要求，共创一个健康和谐网络环境，谢谢您的理解。\n"


if __name__ == '__main__':
    pass