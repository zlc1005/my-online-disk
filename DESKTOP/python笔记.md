# 笔记1

<img src="C:\Users\29242\OneDrive\桌面\学而思网校_笔记拍照\我是打字王（二）：进阶应用\20210911-182017.png" alt="20210911-182017" style="zoom: 50%;" />

<img src="C:\Users\29242\OneDrive\桌面\学而思网校_笔记拍照\我是打字王（二）：进阶应用\20210911-182806.png" alt="20210911-182806" style="zoom:50%;" />

```python
ord("字符")
> 字符的ASCLL编码
```

![20210911-184049](C:\Users\29242\OneDrive\桌面\学而思网校_笔记拍照\我是打字王（二）：进阶应用\20210911-184049.png)

```python
chr("ASCLL编码")
> ASCLL编码的字符
```

## 代码1

```python
#练一练1 使用ord函数获取letterDict["word"]的ASCII码
import pygame, sys, random, time

pygame.init()
screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("打字游戏")
myFont=pygame.font.SysFont(None, 200)
letterList=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

l1 = random.choice(letterList)   # 从列表中随机获取元素
c1 = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)) # 颜色随机
x1 = random.randint(100, 700) # x坐标从左右边距各 100 之间随机
y1 = 100

letterWait = []
letterDict = {"word": l1, "color": c1, "x": x1, "y":y1}
letterWait.append(letterDict)
add_time = time.time() # 记录添加时间

#添加背景音乐
pygame.mixer.music.load("bgSound.wav")
pygame.mixer.music.play(-1)

letterSpeed = 1   # 字母下落速度

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            #作答区域 补充第35行代码 使用ord函数获取letterDict["word"]的ASCII码
            for letterDict in letterWait:
                if event.key == ord(letterDict["word"]):
                    letterWait.remove(letterDict)
                    
   # 添加字母                
    now = time.time()
    if now - add_time >= 2:
        letter1 = random.choice(letterList)
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
        x1 = random.randint(100, 700)  
        y1 = 0
        letterDict = {"word": letter1, "color": color1, "x": x1, "y": y1}
        letterWait.append(letterDict)
        add_time = now
        
    screen.fill((255, 255, 255))
    
    # 绘制字母
    for letterDict in letterWait: 
        x2 = letterDict["x"]
        y2 = letterDict["y"]
        letter2 = letterDict["word"]
        color2 = letterDict["color"]
        textImage = myFont.render(letter2, True, color2)
        screen.blit(textImage, (x2, y2))
        
    # 字母下移
    for letterDict in letterWait:
        letterDict["y"] = letterDict["y"] + letterSpeed
        if letterDict["y"]>500:
            letterWait.remove(letterDict) 

    pygame.display.update()
    time.sleep(0.02)
```

## 代码2

```python
#练一练2 计算分数并显示在画布上
import pygame, sys, random, time

pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("打字游戏")
myFont=pygame.font.SysFont(None,200)

letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            
l1 = random.choice(letterList)   # 从列表中随机获取元素
c1 = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)) # 颜色随机
x1 = random.randint(100, 700) # x坐标从左右边距各 100 之间随机
y1 = 100

letterWait = []
letterDict = {"word": l1, "color": c1, "x": x1, "y":y1}
letterWait.append(letterDict)
add_time = time.time() # 记录添加时间

#添加背景音乐
pygame.mixer.music.load("bgSound.wav")
pygame.mixer.music.play(-1)

letterSpeed = 1   # 字母下落速度初始值

myFont1 = pygame.font.SysFont(None, 30)

score = 0 # 分数初始值
red = (255,0,0) # 分数文字颜色

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            for letterDict in letterWait:
                if event.key == ord(letterDict["word"]):
                    letterWait.remove(letterDict)
                    #作答区域1 补全第45行代码，实现分数统计（累加1）
                    score+=1
    # 添加字母
    now = time.time()
    if now - add_time >= 2:
        letter1 = random.choice(letterList)
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
        x1 = random.randint(100, 700)  
        y1 = 0
        letterDict = {"word": letter1, "color": color1, "x": x1, "y": y1}
        letterWait.append(letterDict)
        add_time = now
        
    screen.fill((255, 255, 255))
    
    # 绘制字母
    for letterDict in letterWait: 
        x2 = letterDict["x"]
        y2 = letterDict["y"]
        letter2 = letterDict["word"]
        color2 = letterDict["color"]
        textImage = myFont.render(letter2, True, color2)
        screen.blit(textImage, (x2, y2))
        
    # 字母下移
    for letterDict in letterWait:
        letterDict["y"] = letterDict["y"] + letterSpeed
        if letterDict["y"]>500:
            letterWait.remove(letterDict) 
            
    #作答区域2 补全第75行代码，实现渲染分数的功能
    sText = myFont1.render("score:"+str(score), True, red)
    screen.blit(sText, (600, 0))

    pygame.display.update()
    time.sleep(0.02)
```

## 显示文字

```python
screen.blit(pygame.font.SysFont(None,200).render("文字", True, (255,0,0)), (600, 0))#200是字号，600是x，(600,0)的0是y，(255,0,0)是rgb颜色
```

## 代码3

```python
#练一练3 补充77和80行代码，更新游戏生命值，完成退出程序功能

import pygame, sys, random, time

pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption("打字游戏")
myFont=pygame.font.SysFont(None,200)

letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
           "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            
l1 = random.choice(letterList)   # 从列表中随机获取元素
c1 = (random.randint(0, 255), random.randint(0,255), random.randint(0, 255)) # 颜色随机
x1 = random.randint(100, 700) # x坐标从左右边距各 100 之间随机
y1 = 100

letterWait = []
letterDict = {"word": l1, "color": c1, "x": x1, "y":y1}
letterWait.append(letterDict)
add_time = time.time() # 记录添加时间

#添加背景音乐
pygame.mixer.music.load("bgSound.wav")
pygame.mixer.music.play(-1)

letterSpeed = 1   # 字母下落速度初始值

myFont1 = pygame.font.SysFont(None, 30)

score = 0 # 分数初始值
red = (255,0,0) # 分数文字颜色

chance = 5 # 生命值初始值

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
            for letterDict in letterWait:
                if event.key == ord(letterDict["word"]):
                    letterWait.remove(letterDict)
                    score = score + 1
    
    # 添加字母
    now = time.time()
    if now - add_time >= 2:
        letter1 = random.choice(letterList)
        color1 = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) 
        x1 = random.randint(100, 700)  
        y1 = 0
        letterDict = {"word": letter1, "color": color1, "x": x1, "y": y1}
        letterWait.append(letterDict)
        add_time = now
        
    screen.fill((255, 255, 255))
    
    # 绘制字母
    for letterDict in letterWait: 
        x2 = letterDict["x"]
        y2 = letterDict["y"]
        letter2 = letterDict["word"]
        color2 = letterDict["color"]
        textImage = myFont.render(letter2, True, color2)
        screen.blit(textImage, (x2, y2))
        
    # 字母下移
    for letterDict in letterWait:
        letterDict["y"] = letterDict["y"] + letterSpeed
        if letterDict["y"]>500:
            letterWait.remove(letterDict) 
            #作答区域1 补充第77行代码，更新游戏生命值（每次减1）
            chance-=1
            #退出
            #作答区域2  补充第80行代码，判断生命值是否耗尽
            if chance<=0:
                print("生命值耗尽，886！最后得分",score)
                pygame.quit()
                sys.exit()

    sText = myFont1.render("socre:"+str(score),True,red)
    screen.blit(sText,(600,0))

    pygame.display.update()
    time.sleep(0.02)
```

---

# 笔记2

## 代码

```python
# 完整演示
import ibox
textList = ibox.aw()
import pygame, sys, random, time,happyHome
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(" 家庭欢乐秀 ")
bgImg = pygame.image.load("bg1.png")
# 弹幕内容和位置坐标
word1 = ""
word2 = ""
word3 = ""
word1X = 0
word2X = 0
word3X = 0
word1Y = 0
word2Y = 0
word3Y = 0
myFont = pygame.font.SysFont("kaiti", 26)
# myFont = pygame.font.SysFont("kaittf", 26)   # mac系统使用
happyHome.picChoice("pic1.png","pic2.png","pic3.png","pic4.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 判断的事件写在 for 循环的外面，可以一直被检测
        if event.type == pygame.KEYDOWN:
            # 空格键出弹幕，设置弹幕的内容和位置
            if event.key == pygame.K_SPACE:
                word1 = random.choice(textList)
                word1X = random.randint(-300, 0)
                word1Y = random.randint(0, 550)

                word2 = random.choice(textList)
                word2X = random.randint(-300, 0)
                word2Y = random.randint(0, 550)

                word3 = random.choice(textList)
                word3X = random.randint(-300, 0)
                word3Y = random.randint(0, 550)
                happyHome.wc(textList,100)
    
    happyHome.bgMove(bgImg,15) #############
    happyHome.picMove(10)   ########
    # 字幕移动
    word1X = word1X + 1
    word2X = word2X + 1
    word3X = word3X + 1
    if word1X > 800:
        word1X = random.randint(-300, 0)
    if word2X > 800:
        word2X = random.randint(-300, 0)
    if word3X > 800:
        word3X = random.randint(-300, 0)
    # 显示弹幕
    textShow1 = myFont.render(word1, True, (0, 255, 0))
    screen.blit(textShow1, (word1X, word1Y))
    textShow2 = myFont.render(word2, True, (0, 0, 255))
    screen.blit(textShow2, (word2X, word2Y))
    textShow3 = myFont.render(word3, True, (0, 255, 255))
    screen.blit(textShow3, (word3X, word3Y))
    happyHome.wm()0
    pygame.display.update()
    time.sleep(0.01)
```

角色图片

```python
happyhome.picHhoice('','','','',......)#选择角色图片
happyhome.picMove(速度)#移动和速度
```

弹窗

```python
import ibox
textLest=ibox.aw()
```

刷屏

```python
happyHome.wc(tl,n)
happyHome.wm()
```
------
------
------
------
------
# 笔记2021-11-27   =1

```python
# 加载背景音乐
pygame.mixer.music.load("bg.mp3")
# 背景音乐开始
pygame.mixer.music.play()
# 背景音乐结束
pygame.mixer.music.stop()
# 背景音乐暂停
pygame.mixer.music.pause()
# 背景音乐恢复
pygame.mixer.music.unpause()

# ===============================

# pygame检测回车键按下开始播放音乐
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_RETURN:
        pygame.mixer.music.play()

# pygame检测s键按下结束播放音乐
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_s:
        pygame.mixer.music.stop()

# pygame检测空格键按下暂停或播放音乐,flag=0 暂停 flag=1 播放
flag = 1
pygame.init()
# ==========================
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
        if flag == 1:
            pygame.mixer.music.pause()
            flag = 0
        elif flag == 0:
            pygame.mixer.music.unpause()
            flag = 1

# pygame检测+键按下音乐增加
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_EQUALS:
        songNum = songNum + 1
        if songNum > len(soundList) - 1:
            songNum = 0
        sygame.mixer.music.load(soundList[songNum])
        pygame.mixer.music.play()

# pygame检测-键按下音乐减少
if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_MINUS:
        songNum = songNum - 1
        if songNum < 0:
            songNum = len(soundList) - 1
        pygame.mixer.music.load(soundList[songNum])
        pygame.mixer.music.play()
```

# 笔记2021-11-27   =2
```python
pygame.Rect('x','y','宽','高')

if songNum > len(soundList)-1:
    songNum = 0
```