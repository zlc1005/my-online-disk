'''
# 补充67、68行，参考data7和data8 设计像素图
# 补充95行，将设计的像素图存储在列表sd3中
# 使用按键切换自己设计的像素动画sd3
import pygame, sys, time, xesDraw

pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("电音Party")
# 添加背景音乐
pygame.mixer.music.load("bg.wav")
pygame.mixer.music.play(-1)
# 设计像素图
data1 = [[9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 1, 1, 1, 1, 9, 9],
        [9, 9, 1, 9, 9, 1, 9, 9],
        [9, 9, 1, 9, 9, 1, 9, 9],
        [9, 1, 1, 9, 9, 1, 9, 9],
        [9, 1, 1, 9, 9, 1, 9, 9],
        [9, 9, 9, 9, 1, 1, 9, 9],
        [9, 9, 9, 9, 1, 1, 9, 9]]
data2 =[[6, 6, 6, 6, 6, 6, 6, 6],
        [6, 6, 7, 7, 7, 7, 6, 6],
        [6, 6, 7, 6, 6, 7, 6, 6],
        [6, 6, 7, 6, 6, 7, 6, 6],
        [6, 7, 7, 6, 6, 7, 6, 6],
        [6, 7, 7, 6, 6, 7, 6, 6],
        [6, 6, 6, 6, 7, 7, 6, 6],
        [6, 6, 6, 6, 7, 7, 6, 6]]
data3 =[[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 1, 1]]

data4= [[0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]]
data5 = [[0, 0, 7, 7, 7, 7, 0, 0],
        [0, 7, 0, 0, 0, 0, 7, 0],
        [7, 0, 9, 0, 0, 9, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 9, 9, 9, 9, 0, 7],
        [0, 7, 0, 0, 0, 0, 7, 0],
        [0, 0, 7, 7, 7, 7, 0, 0]]
data6 = [[0, 0, 7, 7, 7, 7, 0, 0],
        [0, 7, 0, 0, 0, 0, 7, 0],
        [7, 0, 9, 0, 0, 9, 0, 7],
        [7, 0, 0, 0, 0, 0, 0, 7],
        [7, 0, 9, 0, 0, 9, 0, 7],
        [7, 0, 0, 9, 9, 0, 0, 7],
        [0, 7, 0, 0, 0, 0, 7, 0],
        [0, 0, 7, 7, 7, 7, 0, 0]]

#用二维列表设计几副像素图，可以参考data7和data8已经给出的排列方式
#各个数字代表的颜色：0-深紫，1-黄色，2-蓝色，3-粉色，4-天蓝，5-紫罗兰，6-红色，7-黄绿色，8-橙色，9-白色
# ————————————————————————————————————————————————————————————————————————————————
#作答区域 可参考69到84行的示例补充data7和data8 
data7 = [[9, 9, 9, 9, 9, 9, 9, 9],
        [9, 9, 9, 1, 1, 9, 9, 9],
        [9, 1, 1, 3, 3, 1, 1, 9],
        [1, 3, 3, 2, 2, 3, 3, 1],
        [1, 3, 3, 2, 2, 3, 3, 1],
        [9, 1, 1, 3, 3, 1, 1, 9],
        [9, 9, 9, 1, 1, 9, 9, 9],
        [9, 9, 9, 9, 9, 9, 9, 9]]
data8 = [[5, 5, 5, 5, 5, 5, 5, 5],
        [5, 5, 5, 1, 1, 5, 5, 5],
        [5, 1, 1, 3, 3, 1, 1, 5],
        [1, 3, 3, 4, 4, 3, 3, 1],
        [1, 3, 3, 4, 4, 3, 3, 1],
        [5, 1, 1, 3, 3, 1, 1, 5],
        [5, 5, 5, 1, 1, 5, 5, 5],
        [5, 5, 5, 5, 5, 5, 5, 5]]


# ————————————————————————————————————————————————————————————————————————————————

# sd1-sd3动画对应的按键是上、下、右
sd1 = [data1, data2, data3, data1, data2]
sd2 = [data5,data6,data5,data4]
#作答区域 将设计的像素图存在 sd3 中
#sd3 = [data7,data8,data4]
# ————————————————————————————————————————————————————————————————————————————————
sd3 = [data7,data8,data4]
# ————————————————————————————————————————————————————————————————————————————————

# 选中图形列表
select = sd1
# 选中图形列表的长度
n = len(sd1)
# 选中图形列表中的序号
num = 0

while True:
    # 设置背景底色为白色
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # 使用上下左键切换动画和音乐,设定播放时背景音暂停
            if event.key == pygame.K_UP:
                select = sd1
                n = len(sd1)
                num = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sound1.wav")
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_DOWN:
                select = sd2
                n = len(sd2)
                num = 0
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sound2.wav")
                pygame.mixer.music.play(-1)
            #作答区域 选择sd3，用按键切换自己设计的动画sd3
            # ————————————————————————————————————————————————————
            elif event.key == pygame.K_RIGHT:
                select = sd3
                n = len(sd3)
                num = 0
            # ————————————————————————————————————————————————————
                pygame.mixer.music.stop()
                pygame.mixer.music.load("sound3.wav")
                pygame.mixer.music.play(-1)
            
    #用学而思库绘制像素图
    xesDraw.draw(select[num])
    #判断是否为最后一幅画
    num = num + 1
    if num > n - 1:
        num = 0
    #更新画布
    pygame.display.update()
    #延时
    time.sleep(0.5)
'''
import tkinter as tk ,random,pygame,time,sys
from tkinter import filedialog
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()

admin=tk.Tk()
admin.withdraw()
WT = admin.winfo_screenwidth()
HE = admin.winfo_screenheight()

from PIL import Image

# class tttk(tk.Tk()):
#     def __init__(self) -> None:
#         super().__init__()
#         self.title("bulabula")
#         self.geometry("+12+33")
#         self.resizable(False, False)
#         self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
#         self.canvas.pack()
#         img_png = tk.PhotoImage(file=r'awesome_copy.gif')
#         label_img = tk.Label(admin, image=img_png)
#         label_img.pack()
#         tttk.shake(admin)
#     def shake(a):
#         c=str(random.randint(0,WT))
#         d=str(random.randint(0,HE))
#         a.geometry(f'+{c}+{d}')
#         tk.after(10, lambda: tttk.shake(a))

# github copilot, make a function to use pygame show the image
def show_image(image_path):
    foo = pygame.image.load(image_path).get_rect().size
    print(foo)
    screen = pygame.display.set_mode((foo[0], foo[1]))
    screen.fill((255, 255, 255))
    img = pygame.image.load(image_path)
    img = pygame.transform.scale(img, (800, 600))
    screen.blit(img, (0, 0))
    pygame.display.update()
    time.sleep(1)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def main():
    # 设置每个像素区块的大小
    block_size = 75
    img = Image.open(file_path)
    # 获取图片的宽高
    width, height = img.size
    # 获取像素点对应RGB颜色值，可以改变img_array中的值来改变颜色值
    img_array = img.load()
    # 为了处理最后的区块，加了一次循环
    max_width = width + block_size
    max_height = height + block_size
    for x in range(block_size - 1, max_width, block_size):
        for y in range(block_size - 1, max_height, block_size):
            # 如果是最后一次循环，则x坐标等于width - 1
            if x == max_width - max_width % block_size - 1:
                x = width - 1
            # 如果是最后一次循环，则x坐标等于height - 1
            if y == max_height - max_height % block_size - 1:
                y = height - 1
            # 改变每个区块的颜色值
            change_block(x, y, block_size, img_array)
            y += block_size
        x += block_size
    img.save(r'awesome_copy.png')
    show_image(r'awesome_copy.png')
"""
:param x坐标 x: 
:param y坐标 y: 
:param 区块大小 black_size: 
:param 可操作图片数组 img_array: 
"""
def change_block(x, y, black_size, img_array):

    color_dist = {}
    block_pos_list = []
    for pos_x in range(-black_size + 1, 1):
        for pos_y in range(-black_size + 1, 1):
            # todo print(x + pos_x,y + pos_y)
            block_pos_list.append([x + pos_x, y + pos_y])
    for pixel in block_pos_list:
        if not str(img_array[pixel[0], pixel[1]]) in color_dist.keys():
            color_dist[str(img_array[pixel[0], pixel[1]])] = 1
        else:
            color_dist[str(img_array[pixel[0], pixel[1]])] += 1
    # key-->value => value-->key
    new_dict = {v: k for k, v in color_dist.items()}
    max_color = new_dict[max(color_dist.values())]
    # 将区块内所有的颜色值设置为颜色最多的颜色
    for a in block_pos_list:
        img_array[a[0], a[1]] = tuple(list(map(int, max_color[1:len(max_color) - 1].split(","))))


def get_key(dict, value):
    return [k for k, v in dict.items() if v == value]


if __name__ == "__main__":
    main()