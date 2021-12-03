
'''
import os, re
import requests
def a_aa(a):
    m=re.compile(r"[\/\\\:\*\?\"\<\>\|]")
    n=re.sub(m,"_",a)
    return n
url = 'https://haokan.baidu.com/web/video/feed?tab=youxi_new&act=pcFeed&pd=pc&num=20&shuaxin_id=1632094390594'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
json_data = response.json()
videos = json_data['data']['response']['videos']
for index in videos:
    title = index['title']
    play_url = index['play_url']
    video_content = requests.get(url=play_url, headers=headers).content
    path = ''
    with open('l:\\'+path + a_aa(title) + '.mp4', mode='wb') as f:
        f.write(video_content)
        print('正在保存：', title)
'''
'''
import requests,parsel,re,os
from tqdm import*
os.system("md video")
def a_aa(a):
    m=re.compile(r"[\/\\\:\*\?\"\<\>\|]")
    n=re.sub(m,"_",a)
    return n
url = 'https://haokan.baidu.com/web/author/listall?app_id=1707890966773713&ctime=16314328568539&rn=10&searchAfter=&_api=1'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
json_data = response.json()
videos = json_data['data']['results']
for i in videos:#tqdm(videos):
    play_url = 'https://haokan.baidu.com/v?vid='+i['content']['vid']
    html_data = requests.get(url=play_url, headers=headers)
    html_data_2 = parsel.Selector(html_data.text)
    href=html_data_2.css("#mse::text").get()
    title=html_data_2.css('.videoinfo-title::text').get()
    video_content = requests.get(url=href, headers=headers).content
    with open("video\\"+a_aa(title)+'.mp4',mode="wb",encoding="utf-8") as f:
        f.write(video_content)
print()
print("爬取成功！")
'#root > div > div:nth-child(2) > div._97d705de994bee2e76ad8876a1648171-scss.player-fullscreen-show-interaction > div.leftContainer._20bc24e2255076f4dbc27d9fe1a241f3-scss > div:nth-child(1) > div.f8f92fbaa6a9978696cbc0d0e2f862ae-scss > div > div.e0855af4151de070355c4d56e74b5c5e-scss > div:nth-child(2) > div.videoWrap.xgplayer_autohide.xgplayer.xgplayer-pc.xgplayer-playing.init-complete.xgplayer-pause > video'
'''
import requests,random,os,re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}
os.system("md ok")
def a_aa(a):
    m=re.compile(r"[\/\\\:\*\?\"\<\>\|]")
    n=re.sub(m,"_",a)
    return n
while True:
    video_content = requests.get(url=input(":"), headers=headers).content
    with open("ok\\"+a_aa(str(random.random()))+'.jpg',mode="wb") as f:
        f.write(video_content)