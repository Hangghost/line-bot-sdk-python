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
        access_token = os.environ['LINE_ACCESS_TOKEN']
        secret = os.environ['LINE_SECRET']
        openai.api_type = "azure"
        openai.api_base = os.environ['AZURE_OPENAI_ENDPOINT']
        openai.api_version = "2023-03-15-preview"
        openai.api_key = os.environ['AZURE_OPENAI_KEY']
        # cogsearch_endpoint = os.environ['AZURE_COGNITIVE_SEARCH_ENDPOINT']  ## https://herme-line-search.search.windows.net
        # cogsearch_key = os.environ['AZURE_COGNITIVE_SEARCH_KEY']          ## eBqWb0ajjRqtWsihRbR2htNZzYyanrMiqOjSHD5EyvAzSeCPf5u3
        # cogsearch_index_name = os.environ['AZURE_COGNITIVE_SEARCH_INDEX_NAME']        ## azureblob-index-l-l-2
        
        
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
                response = openai.ChatCompletion.create(         
                    engine="gpt-35-turbo",
                    dataSources = [
                        {
                              "type": "AzureCognitiveSearch",
                              "parameters": {
                                "endpoint": "https://herme-line-search.search.windows.net",
                                "key": "eBqWb0ajjRqtWsihRbR2htNZzYyanrMiqOjSHD5EyvAzSeCPf5u3",
                                "indexName": "azureblob-index-l-l-2"
                              }
                        }
                    ],
                    messages = [
                        {"role":"system","content":"You are a customer service assistant from the yoga studio, HerMe, whose primary goal is to help users with issues they are experiencing with their yoga class. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to HerMe."},
                        {"role":"user","content":msg[6:]}
                        ],                        # 將第六個字元之後的訊息發送給 OpenAI
                    temperature=0.1,
                    max_tokens=350,
                    top_p=0.90,
                    frequency_penalty=0,
                    presence_penalty=0,
                    stop=None
                    )
                # 接收到回覆訊息後，移除換行符號
                reply_msg = response["choices"][0]["message"]["content"]
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