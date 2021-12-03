#源码
import requests
import json
import time,os
def dingmessage(message,key,num=1):
    try:
        with open("webhook.txt",mode="r") as ar:
            a=ar.read()
    except:
        with open("webhook.txt",mode="w") as ar:
            a=ar.write(input("请输入webhook："))
    # 请求的URL，WebHook地址
    webhook  = a#机器人的WebHook
    #webhook2 = ""#机器人的WebHook
    #构建请求头部
    header = {
        "Content-Type": "application/json",
        "Charset": "UTF-8"
    }
    text={
    "at": {
        "atMobiles":[
            ""
        ],
        "atUserIds":[
            ""
        ],
        "isAtAll": False
    },
    "text": {
        "content":message+" "+key
    },
    "msgtype":"text"
}
    #构建请求数据#写要发的通知内容
    #对请求的数据进行json封装
    message_json = json.dumps(text)
    #发送请求
    for i in range(num):
        info = requests.post(url=webhook,data=message_json,headers=header)
        #info = requests.post(url=webhook2,data=message_json,headers=header)
        #打印返回的结果
        print('发送时间为:')
        os.system('echo %time%')
        print(info.text)

dingmessage(message=input("请输入要发送的文字："),key="_",num=int(input("请输入要发送的次数：")))