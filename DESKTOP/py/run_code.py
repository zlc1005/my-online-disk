def delete_extra__zero(n):
    n='{:g}'.format(n)
    n= float(n) if '.' in n else int(n)
    return n
def print_color(color, message):
    if color.lower() == "red":
        print("\033[31m%s\033[0m" % message,end='')
    elif color.lower() == "green":
        print("\033[32m%s\033[0m" % message,end='')
    elif color.lower() == "yellow":
        print("\033[33m%s\033[0m" % message,end='')
    elif color.lower() == "blue":
        print("\033[34m%s\033[0m" % message,end='')
    elif color.lower() == "purple":
        print("\033[35m%s\033[0m" % message,end='')
    elif color.lower() == "skyblue":
        print("\033[36m%s\033[0m" % message,end='')
    elif color.lower() == "white":
        print("\033[37m%s\033[0m" % message,end='')
    else:
        print("\033[31m%s\033[0m" % "输入错误，请输入正确的颜色")
def make__whole(num):
    return delete_extra__zero(num // 1)
import time
lib_list=['os','sys','time','tkinter','pygame','math','threading','queue','subprocess','requests','re','json','socket','smtplib','email','smtplib','email.mime.text','email.mime.audio']
while True:
    nowtime=time.time()*1000
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('import random...')
    time.sleep(1)
    print_color("yellow","%s WARNING:" % str(make__whole(time.time()*1000-nowtime)))
    print('random can\'t import')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('make *.pkg ...')
    time.sleep(0.5)
    print_color("red","%s ERROR:" % str(make__whole(time.time()*1000-nowtime)))
    print('make *.pkg failed')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('make *.pkg ...')
    time.sleep(2)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('make *.pkg success')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('make *.pkg ...')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install random\'...')
    time.sleep(0.5)
    print_color("red","%s ERROR:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install random\' failed')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install random\' ...')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install random\' success')
    time.sleep(2)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/r/random/random-0.4.1.tar.gz ...')
    time.sleep(0.5)
    print_color("red","%s ERROR:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/r/random/random-0.4.1.tar.gz failed')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/r/random/random-0.4.1.tar.gz ...')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/r/random/random-0.4.1.tar.gz success')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('import pyautogui...')
    time.sleep(0.5)
    print_color("yellow","%s WARNING:" % str(make__whole(time.time()*1000-nowtime)))
    print('pyautogui can\'t import')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install pyautogui\'...')
    time.sleep(0.5)
    print_color("red","%s ERROR:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install pyautogui\' failed')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install pyautogui\' ...')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/p/pyautogui/pyautogui-0.8.0.tar.gz ...')
    time.sleep(0.5)
    print_color("red","%s ERROR:"    % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/p/pyautogui/pyautogui-0.8.0.tar.gz failed')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/p/pyautogui/pyautogui-0.8.0.tar.gz ...')
    time.sleep(0.5)
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('get https://pypi.python.org/packages/source/p/pyautogui/pyautogui-0.8.0.tar.gz success')
    print_color("green","%s INFO:" % str(make__whole(time.time()*1000-nowtime)))
    print('run \'pip install pyautogui\' success')
    time.sleep(2)
    for i in lib_list:
        print_color('green','%s INFO:' % str(make__whole(time.time()*1000-nowtime)))
        print('import %s...' % i)
        time.sleep(0.1)
        print_color('green','%s INFO:' % str(make__whole(time.time()*1000-nowtime)))
        print('%s import success' % i)