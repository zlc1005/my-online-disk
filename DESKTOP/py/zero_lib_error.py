class zero_error(Exception):#o_error(Exception):
    pass
def zeroerror(t='',error='zero_error'):
    try:
        exec('raise '+error+'("'+t+'")')
    except NameError:
        raise zero_error("错误型类错误")
    except TypeError:
        raise zero_error("数据需要str")

def zero_lib_error_help():
    print('''
    zeroerror(t,error)
    t=错误文字(str)
    error=错误型类(str)
    ''')

'''
# 水果忍者
# 要求 :
# 1. 补充第70行代码，实现每点击一下点击次数加1
# 2. 补充第82行代码，实现每点击一下分数加1
# 3. 补充第149行代码，使用round()保留2位小数位，计算正确率

import pygame, sys, random, time
pygame.init()
screen = pygame.display.set_mode((600, 700))
pygame.display.set_caption("水果忍者")
myFont = pygame.font.SysFont(None, 80)
myFont2 = pygame.font.SysFont("kaiti", 20)
# myFont2 = pygame.font.SysFont("kaittf",20)    # mac系统使用
letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
              "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

l1 = random.choice(letterList)   # 从列表中随机获取元素
c1 = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)) # 颜色随机
x1 = random.randint(100, 700) # x坐标从左右边距各 100 之间随机
y1 = 100

letterWait = []
index1 = random.randint(0, 4)
letterDict = {"word": l1, "color": c1, "x": x1, "y": y1, "index1": index1}
letterWait.append(letterDict)
add_time = time.time() # 记录添加时间

score = 0  # 初始化分数值
chance = 5  # 5次错过字母机会
level = 0 # 关卡初始值

letterSpeed = 1  # 字母下落速度
fruitX = 400  # hero位置
fruitY = 0
yellow = (255, 255, 0)

aaa=0

rate = 0  # 正确率初始值
clickNum = 0  # 点击次数

# 添加图片
bgPic = pygame.image.load("bg.png")
boom1 = pygame.image.load("boom1.png")
boom2 = pygame.image.load("boom2.png")
boom3 = pygame.image.load("boom3.png")
booms = [boom1,boom2,boom3]

# 添加水果图片
fruit1 = pygame.image.load("fruit1.png")
fruit2 = pygame.image.load("fruit2.png")
fruit3 = pygame.image.load("fruit3.png")
fruit4 = pygame.image.load("fruit4.png")
fruit5 = pygame.image.load("fruit5.png")
fruit = [fruit1, fruit2, fruit3, fruit4, fruit5]

# 增加音效
sound1 = pygame.mixer.Sound("boom.wav")
pygame.mixer.music.load("bgmusic.wav")
pygame.mixer.music.play(-1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            sound1.play()
            #作答区域1 补充第70行代码，实现每点击一下点击次数加1
            #------------#
            clickNum+=1
            #------------#

            for letterDict in letterWait:
                if event.key == ord(letterDict["word"]):
                    # 消除时获取字母的位置
                    fruitX = letterDict['x']
                    fruitY = letterDict['y']
                    letterWait.remove(letterDict)
                    
                    #作答区域2 补充第82行代码，实现每点击一下分数加1
                    #-------------------#
                    score+=1
                    #-------------------#
                    for boom in booms:
                        screen.blit(boom, (fruitX-60, fruitY-60))
                        pygame.display.update()
                        time.sleep(0.01)
                    
                    break # 每按一下键消除一个水果得一分
                if event.key == ord('^'):
                    score+=1000
                    clickNum+=1000
                    aaa+=1000
    # 生成字母
    now = time.time()
    if now - add_time >= 2:
        add_time = now
        l1 = random.choice(letterList)
        c1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 150))  # 颜色随机
        x1 = random.randint(50, 550)  # x坐标从左右边距各100之间随机
        y1 = 10
        index1 = random.randint(0, 4)
        letterDict = {"word": l1, "color": c1, "x": x1, "y": y1, "index1": index1}
        letterWait.append(letterDict)

    # 绘制背景
    screen.blit(bgPic, (0, 0))

    # 绘制字母
    for letterDict in letterWait:
        x2 = letterDict["x"]
        y2 = letterDict["y"]
        l2 = letterDict["word"]
        c2 = letterDict["color"]
        index1 = letterDict["index1"]
        textImage = myFont.render(l2, True, c2)
        # 绘制字母的时候也绘制对应的图片
        screen.blit(fruit[index1], (x2 - 60, y2 - 60))
        screen.blit(textImage, (x2, y2))
        
    # 字母下移
    for letterDict in letterWait:
        letterDict["y"] = letterDict["y"] + letterSpeed
        if letterDict["y"] > 800:
            letterWait.remove(letterDict)
            chance = chance - 1
            # 退出
            if chance <= 0:
                print("机会耗尽，886！最后得分", score)
                pygame.quit()
                sys.exit()
        
    # 难度晋级
    if score-aaa % 10 == 0:
        level = score-aaa // 10 + 1
        letterSpeed = level

    # 显示得分
    scoreShow = myFont2.render("score: "+str(score), True, yellow)
    screen.blit(scoreShow, (450, 30))
    # 显示剩余机会
    chanceShow = myFont2.render("chance: "+str(chance), True, yellow)
    screen.blit(chanceShow, (450, 60))
    # 显示关卡数
    levelShow = myFont2.render("level: "+str(level), True, yellow)
    screen.blit(levelShow, (450, 90))

    if clickNum-aaa > 0:
        rate = score / clickNum * 100
        #作答区域3 补充第149行代码，使用round()保留2位小数位，计算正确率
        #--------------------#
        rate=round(rate,2)
        #--------------------#

    rateShow = myFont2.render("正确率："+str(rate)+"%", True, yellow)
    screen.blit(rateShow, (450, 120))

    pygame.display.update()
    time.sleep(0.02)
'''