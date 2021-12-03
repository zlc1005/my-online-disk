'''
import sys
a=input()
output=""
abc='abcdefghijklmnopqrstuvwxyz'
a_=['a','e','i','o','u']
b={'a':0,'e':0,'i':0,'o':0,'u':0}


def minValue(b):
    curKey=None
    curMin=sys.maxsize
    for k in b.keys():
        if b[k]<curMin:
            curMin=b[k]
            curKey=k
    return {'v':curMin,'k':curKey}
# find closest vowel
def vowel(x:str) -> str:
    abc='abcdefghijklmnopqrstuvwxyz'
    a_=['a','e','i','o','u']
    b={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in a_:
        a_index=abc.index(i)
        b_index=abc.index(x)
        d=abs(a_index-b_index)
        b[i]=d
    bmax=minValue(b)['k']
    return bmax

def nextConsonant(x:str) -> str:
    if x == 'z' :return 'z'
    abc='abcdefghijklmnopqrstuvwxyz'
    a_=['a','e','i','o','u']
    index=abc.index(x)
    if abc[index+1] in a_:
        return abc[index+2]
    else:
        return abc[index+1]

for i in a:
    if i in a_:
        output+=i
    else:
        output+=i
        output+=vowel(i)
        output+=nextConsonant(i)
print(output)
'''
'''
a,b,output=input(),int(input()),None
output=int(a)
for sdfghjkl in range(b):
    a+='0'
    output+=int(a)
print(output)
#------------------------------
import sys
def aaa(x) -> bool:
    if x%2==0:
        aa=True
    else:
        aa=False
    return aa
def main() -> None:
    a=input().split(' ')
    b=input().split(' ')
    c=int(input())
    abs0=abs(int(a[0])-int(b[0]))
    abs1=abs(int(a[1])-int(b[1]))
    distance=abs0+abs1
    if c>=distance:
        pass
    else:
        print('N')
        sys.exit(0)
    if aaa(c-distance):
        print('Y')
    else:
        print('N')
if __name__=='__main__':
    main()
'''
import requests,os
os.system('echo a > a.html')
herder={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84'}
a=requests.get(url='https://baidu.com',headers=herder)
with open('a.html',mode='w',encoding='UTF-8') as w:
    w.write(str(a.text.encode('utf-8')))
