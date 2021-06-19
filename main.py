#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import re
import os
from flask import Flask, request, abort
import requests
import json
from googletrans import Translator

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Zf8dczdo9U7hVl5kRxb+mTHD/xpxRuBTVGPxzT4WTFQy0yCyMYahIUXdsL8hPtNV1Bja/WY4PwgJPbaFtdmf/vNnkjoGoDprnrpdqksGLXCijTkJfVVkQ8zz3ALCNb7m6pnuiEfWkfhlUi4S1thB5wdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1e9a05fa42febda9fc4f8e629dfe2e75')

#line_bot_api.push_message('Ue0e081b868223a8e25b8b3cd7898611d', TextSendMessage(text='你可以開始了'))

print('aaa')



def text_to_translate(text,dest='en'):
    translator = Translator()
    result = translator.translate(text, dest).text
    return result

#氣象預報
def GetWeather(station):
    end_point = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWB-6B01579C-E0F7-4DE2-A51A-AD5FDFFF709F"

    data = requests.get(end_point).json()
    data = data["records"]["location"]

    target_station = "not found"
    for item in data:
        if item["locationName"] == str(station):
            target_station = item
    return target_station


def MakeWeather(station):
    WeatherData = GetWeather(station)
    if WeatherData == "not found":
        return False

    msg = "天氣報告 - " + station
    # for i in range(5):
    # WeatherData = WeatherData["weatherElement"][i]["time"][0]["parameter"]["parameterName"]
    msg += "\n" + WeatherData["weatherElement"][0]["time"][0]["parameter"]["parameterName"] + "\n"
    msg += "降雨率 = " + WeatherData["weatherElement"][1]["time"][0]["parameter"]["parameterName"] + "%\n"
    msg += "最低溫 = " + WeatherData["weatherElement"][2]["time"][0]["parameter"]["parameterName"] + "℃\n"
    msg += "體感 = " + WeatherData["weatherElement"][3]["time"][0]["parameter"]["parameterName"] + "\n"
    msg += "最高溫 = " + WeatherData["weatherElement"][4]["time"][0]["parameter"]["parameterName"] + "℃\n"
    #msg += MakeAQI(station)
    print(msg)
    return msg


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    print('bbb')
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print('ccc')
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = text=event.message.text
    cmd = event.message.text.split(" ")
    '''
    if mtext == '告訴我秘密':
        image_message = ImageSendMessage(
            original_content_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2F9c8c1e647eb14e01898043c0c60bf03a&methods=resize%2C1000%2C5000',
            preview_image_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2Ffd2258c5ea6c43f591e8d9930d152b94&methods=resize%2C1000%2C5000'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    '''

    if mtext == '你好':
        line_bot_api.reply_message(event.reply_token, '嗨嗨')
    elif cmd[0] == "@天氣":#e.g. 天氣 新竹市
        station = cmd[1]
        print(station)
        WeatherMsg = MakeWeather(station)

        if not WeatherMsg:
            WeatherMsg = "沒這個氣象站!"

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=WeatherMsg))
    elif cmd[0] == '@翻譯':
        txt = cmd[1]
        print(txt)
        result = text_to_translate(text=txt, dest='zh-tw')
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(mtext))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

