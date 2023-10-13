from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['GW49rVUG7Fg6oFif8vyIT9wDYYbS/pXWkD4qaeMpZvjCHP4dz0Mx8yi1yR63UjbAeodDrA8Ee/roRxOET0fACRUNTnGajG6/RHtryJxEq4N4jsMqVGaDnMr5Zp6TNhEXsfNCJRsQur/M+/wYSMR8vAdB04t89/1O/w1cDnyilFU='])
handler = WebhookHandler(os.environ['2867e21d1ce2209251dbb5b826e794df'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)