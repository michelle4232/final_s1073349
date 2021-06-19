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
line_bot_api = LineBotApi('Zf8dczdo9U7hVl5kRxb+mTHD/xpxRuBTVGPxzT4WTFQy0yCyMYahIUXdsL8hPtNV1Bja/WY4PwgJPbaFtdmf/vNnkjoGoDprnrpdqksGLXCijTkJfVVkQ8zz3ALCNb7m6pnuiEfWkfhlUi4S1thB5wdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1e9a05fa42febda9fc4f8e629dfe2e75')

#line_bot_api.push_message('Ue0e081b868223a8e25b8b3cd7898611d', TextSendMessage(text='你可以開始了'))

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
    line_bot_api.push_message('Ue0e081b868223a8e25b8b3cd7898611d', TextSendMessage(text='你可以開始了'))
    return 'OK'

#訊息傳遞區塊
##### 基本上程式編輯都在這個function #####
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

