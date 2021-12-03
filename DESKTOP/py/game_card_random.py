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
import random
x,y=10,3
while True:
    rx,ry=random.randint(1,x),random.randint(1,y)
    print_color('green','INFO:')
    print_color('yellow','x:%s,y:%s' % (rx,ry))
    print('\n')
    input()