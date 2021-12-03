import requests,json,time
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}
a={
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
        "content":'aaaa_aaaa'
    },
    "msgtype":"text"
}
while True:
    req = requests.post('https://oapi.dingtalk.com/robot/send?access_token=5b7db7b54c0e16ae8f997650ef3f84fc57b53a2980081f307d0ae231b893bd8b',data=json.dumps(a),headers=header)
    print(req)
    print(req.text)
    time.sleep(3)