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
app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Zf8dczdo9U7hVl5kRxb+mTHD/xpxRuBTVGPxzT4WTFQy0yCyMYahIUXdsL8hPtNV1Bja/WY4PwgJPbaFtdmf/vNnkjoGoDprnrpdqksGLXCijTkJfVVkQ8zz3ALCNb7m6pnuiEfWkfhlUi4S1thB5wdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('1e9a05fa42febda9fc4f8e629dfe2e75')

#line_bot_api.push_message('Ue0e081b868223a8e25b8b3cd7898611d', TextSendMessage(text='你可以開始了'))

print('aaa')
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
    if mtext == '告訴我秘密':
        image_message = ImageSendMessage(
            original_content_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2F9c8c1e647eb14e01898043c0c60bf03a&methods=resize%2C1000%2C5000',
            preview_image_url='https://images.builderservices.io/s/cdn/v1.0/i/m?url=https%3A%2F%2Fstorage.googleapis.com%2Fproduction-bluehost-v1-0-9%2F659%2F790659%2FAtmP8Pmy%2Ffd2258c5ea6c43f591e8d9930d152b94&methods=resize%2C1000%2C5000'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    elif mtext == '你好':
        line_bot_api.reply_message(event.reply_token, '嗨嗨')
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(mtext))

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

