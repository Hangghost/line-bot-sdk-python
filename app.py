import openai

from flask import Flask, request

# 載入 json 標準函式庫，處理回傳的資料格式
import json
import os

# 載入 LINE Message API 相關函式庫
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

@app.route("/", methods=['POST'])
def linebot():
    body = request.get_data(as_text=True)                    # 取得收到的訊息內容
    json_data = json.loads(body)                         # json 格式化訊息內容
    try:
        access_token = 'EU16pZnitJZotJBmSSMxizmnT7TsmYrVI6GLIzDHJDWFHs/1IMKW3rUMB0pJc2razv8npE2l7LT9u47K1c7ytC4493F4w3U4U+8XbdI3rhV6ceOw0zP5LhOIz/1DB9Urm3SBadKi/I4naS+7+mxXsgdB04t89/1O/w1cDnyilFU='
        secret = 'fa5368b825917a6136d1f10fa753f1de'
        line_bot_api = LineBotApi(access_token)              # 確認 token 是否正確
        handler = WebhookHandler(secret)                     # 確認 secret 是否正確
        signature = request.headers['X-Line-Signature']      # 加入回傳的 headers
        handler.handle(body, signature)                      # 綁定訊息回傳的相關資訊
        tk = json_data['events'][0]['replyToken']            # 取得回傳訊息的 Token
        type = json_data['events'][0]['message']['type']     # 取得 LINe 收到的訊息類型
        if type=='text':
            msg = json_data['events'][0]['message']['text']  # 取得 LINE 收到的文字訊息
            ai_msg = msg[:6].lower()                         # 取出文字的前五個字元，轉換成小寫
            reply_msg = ""                                   # 預設回覆訊息
            if ai_msg == 'hi ai:':                                
                openai.api_type = "azure"
                openai.api_base = "https://herme-service.openai.azure.com/"
                openai.api_version = "2023-03-15-preview"
                openai.api_key = os.getenv("d6576c8d912946aeb070b712e1ca43d5")
                response = openai.Completion.create(         
                    engine="GPT-35-turbo",
                    messages = [{"role":"system","content":"You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."},{"role":"user","content":"How much is a PS5?"},{"role":"assistant","content":"I apologize, but I do not have information about the prices of other gaming devices such as the PS5. My primary focus is to assist with issues regarding Xbox devices. Is there a specific issue you are having with your Xbox device that I may be able to help with?"}],
                    prompt=msg[6:],                            # 將第六個字元之後的訊息發送給 OpenAI
                    temperature=0,
                    max_tokens=350,
                    top_p=0.95,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=None
                    )
                # 接收到回覆訊息後，移除換行符號
                reply_msg = response["choices"][0]["text"].replace('\n','')
            else:
                reply_msg = msg
        else:
            reply_msg = '你傳的不是文字呦～'
        line_bot_api.reply_message(tk,TextSendMessage(reply_msg))# 回傳訊息
    except:
        print(body)                                          # 如果發生錯誤，印出收到的內容
    return 'OK'                                              # 驗證 Webhook 使用，不能省略

if __name__ == "__main__":
    app.run()