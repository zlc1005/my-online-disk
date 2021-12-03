'''
a=int(input())
b=int(input())
c=2
d=18
if a < c:
    print('Before')
if a > c:
    print('After')
if a == c and b < d:
    print('Before')
if a == c and b > d:
    print('Before')    print('After')
if a == c and d == b:
    print('Special')
'''


"""
a='how are you :-) ? ?'#input()
txt=''
happy=0
sad=0
for i in a:
    if i == ':':
        txt=txt+':'
    elif i == '-':
        txt=txt+'-'
    elif i == '(':
        txt=txt+'('
    elif i == ')':
        txt=txt+')'
    elif len(txt) == 3:
        if txt == ':-)':
            happy+=1
        elif txt == ':-(':
            sad+=1
        txt=''
    else:
        txt=''
if sad < happy:
    print('happy')
elif sad > happy:
    print('sad')
elif sad==happy:
    print('unsure')
elif sad==0 and happy==0:
    print('none')
"""


'''
happy=0
sad=0

a="How :-(  :-(are :-)you :-) doing :-("
for i in range (len(a)-2):
    if a[i:i+3]==":-)":
        happy+=1
    elif a[i:i+3]==":-(":
        sad+=1
    else:
        pass

if sad < happy:
    print('happy')
elif sad > happy:
    print('sad')
elif sad==happy:
    print('unsure')
elif sad==0 and happy==0:
    print('none')
'''


'''

while True:
    a=int(input('number:'))
    b=int(input('number:'))
    list=[]
    listb=[]
    lista=[]
    for i in range(a):
        for x in range(a):
            if i*x == a:
                if i not in list:
                    list.append(i)
                elif x not in list:
                    list.append(x)
    list.append(1)
    list.append(a)
    listb.append(1)
    listb.append(b)
    for i in range(b):
        for x in range(b):
            if i*x == b:
                if i not in listb:
                    listb.append(i)
                elif x not in listb:
                    listb.append(x)
    for i in list:
        for x in listb:
            if i==x:
                if i not in lista:
                    lista.append(i)
    print(lista)

'''


'''
a=int(input())
b=int(input())
sum=0
\"""18
a=12
b=3
12*10**0 = 12
12*10**1 = 120
12*10**2 = 1200
12*10**3 = 12000
\"""

for i in range(0,b+1):
    sum+=a*10**i
print(sum)
'''
'''
x=input()
y=input()
if x[0]!='-' and y[0]!='-':
    print(1)
elif x[0]=='-' and y[0]!='-':
    print(2)
elif x[0]=='-' and y[0]=='-':
    print(3)
elif x[0]!='-' and y[0]=='-':
    print(4)
'''
'''
# serch a text in google
import sys
import webbrowser
import time

for i in range(1,6):
    time.sleep(1)
    print(i)
    sys.stdout.flush()
    if i==5:
        webbrowser.open('https://www.google.com/search?q='+input())
        break
###############################################################################
def f(a):
    list=[]
    for i in range(a):
        for x in range(a):
            if i*x == a:
                if i not in list:
                    list.append(i)
                elif x not in list:
                    list.append(x)
    list.append(1)
    return list
a,list=input(),[]
for i in range(int(a)):
    b=input()
    list.append(b)
for i in list:
    c=sum(f(int(i)))
    d=None
    if c == int(i):
        d='perfect'
    elif c > int(i):
        d='abundant'
    elif c < int(i):
        d='deficient'
    print(i,f' is a {d} number.')
'''
import requests
import time
url = 'https://api2.amplitude.com/'
name = 'hack'
GamePin = '3738177'
none = ''
l = '{'
f = '}'
agent = {
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4690.1 Safari/537.36"}
msage = f'[{l}"device_id": "464e5358-40da-41de-ae75-b2449cd7dca9R","user_id": null,"timestamp": time.time(),"event_id": 1,"session_id": 1635986103470,"event_type": "Join Kahoot","version_name": null,"platform": "Web","os_name": "Chrome","os_version": "97","device_model": "Windows","language": "zh-CN","api_properties": {none},"event_properties": {l}"component": "controller","list_id": "controller","url": "https://kahoot.it/v2/join","page_path": "/v2/join","kahoot_version": "v1.1972.1","is_test": false,"nickname": {name},"game_pin": {GamePin},"quiz_type": "quiz","is_team_mode": false,"is_namerator_enabled": false,"is_player_id_enabled": false,"is_personalised_learning_enabled": false,"host_primary_usage": "teacher", "is_magic_link": false,"is_org_invite": false{f},"user_properties": {none},"uuid": "55ab678e-64f8-4940-aeab-9c730bd37b2f","library": {l}"name": "amplitude-js", "version": "5.3.0"{f},"sequence_number": 4,"groups": {none},"group_properties": {none},"user_agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4690.1 Safari/537.36"{f}]'
asdfg = requests.post(
    url, json=f'"e"={msage}&"upload_time"={str(time.time())}&"v"=2&"checksum"= "ec63470b001b84eae651d7f15bb113eb"&"client"= "1ecbdca138dc545d0042617f31fc1556"', headers=agent)
print(asdfg)
print(asdfg.text)
