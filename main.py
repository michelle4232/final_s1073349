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
import requests
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import googlemaps

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('ra82QMewyxn2gn9uZkwidIc1QNxhKiRQvSFeDxath6YR1OzzyWANu7M2KdnRpMcaXsPhjJJ5Zkz2/yULW+5PSh5ET2CG+MvKAZvOa6VY2cCjz/W3EHfCzicTEMcO3NvtndYZcSdsXX/jYssor8lG7QdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('a0b4d2d97a0b66c6e6e0b90c3394c906')

#line_bot_api.push_message('Ue0e081b868223a8e25b8b3cd7898611d', TextSendMessage(text='你可以開始了'))

'''
# 獲取Googlemap API
gmaps = googlemaps.Client(key='AIzaSyAhk8_pbKnD6Yx8Ii-8sc3U3ddymGmXHjg')

def MakeAQI(station):
    end_point = "http://opendata.epa.gov.tw/webapi/api/rest/datastore/355000000I-000259?filters=SiteName eq '" + station + "'&sort=SiteName&offset=0&limit=1000"

    data = requests.get(end_point)
    AQImsg = ""

    if data.status_code == 500:
        return "無 空氣品質 資料"
    else:
        AQIdata = data.json()["result"]["records"][0]
        AQImsg += "AQI = " + AQIdata["AQI"] + "\n"
        AQImsg += "PM2.5 = " + AQIdata["PM2.5"] + " μg/m3\n"
        AQImsg += "PM10 = " + AQIdata["PM10"] + " μg/m3\n"
        AQImsg += "空品：" + AQIdata["Status"]
        return AQImsg


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
    msg += MakeAQI(station)
    print(msg)
    return msg

def convert(city):
    tw = [
        "臺北市", "新北市", "桃園市", "臺中市", "臺南市", "高雄市", "基隆市", "新竹市", "嘉義市", "新竹縣",
        "苗栗縣", "彰化縣", "南投縣", "雲林縣", "嘉義縣", "屏東縣", "宜蘭縣", "花蓮縣", "臺東縣", "澎湖縣"]
    en = ["Taipei City", "New Taipei City", "Taoyuan City", "Taichung City", "Tainan City",
          "Kaohsiung City", "Keelung City", "Hsinchu City", "Chiayi City", "Hsinchu County",
          "Miaoli County", "Changhua County", "Nantou County", "Yunlin County", "Chiayi County",
          "Pingtung County", "Yilan County", "Hualian County", "Taitung County", "Penghu county"]
    for c in range(len(city)):
        for i in range(len(en)):
            if en[i] == city[c]:
                return tw[i]

def spot(place):
    # 設定地圖搜尋中心(地點)
    geocode_result = gmaps.geocode(place)
    # 取得地點資料(list第0項=資料的dictionary型態)
    geocode_result = geocode_result[0]
    return geocode_result
'''

# 監聽所有來自 /callback 的 Post Request
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

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
    message = text=event.message.text
    if re.match('告訴我秘密',message):
        # 貼圖查詢：https://developers.line.biz/en/docs/messaging-api/sticker-list/#specify-sticker-in-message-object
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='1'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

    '''
   elif mtext[-2:] == '天氣':
        place = mtext.split(' ')[0]  # 取得現在位置
        print(place)
        city = []
        for i in range(len(spot(place)['address_components'])):
            city.append(spot(place)['address_components'][i]['long_name'])  # 取得現在位置的所處縣市
        city = convert(city)  # 換成中文
        WeatherMsg = MakeWeather(city)

        if not WeatherMsg:
            WeatherMsg = "沒這個氣象站!"
        try:
            message = TextSendMessage(
                text=WeatherMsg
            )
            line_bot_api.reply_message(event.reply_token, message)
        except:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='中間訊息輸入有誤!!'))
        '''