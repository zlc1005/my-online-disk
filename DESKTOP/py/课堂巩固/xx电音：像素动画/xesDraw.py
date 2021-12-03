import  pygame

pygame.init()
screen = pygame.display.set_mode((400,400))

def draw(select):
    for i in range(8):
        for j in range(8):
            if select[i][j] == 0:
                c1 = (148, 0, 211) #深紫
            if select[i][j] == 1:
                c1 = (255, 255, 0) #黄色
            if select[i][j] == 2: # 蓝色
                c1 = (0, 200, 255)
            if select[i][j] == 3: #  粉色
                c1 = (255, 20, 147)
            if select[i][j] == 4:  #天蓝
                c1 = (135, 206, 235)
            if select[i][j] == 5:
                c1 = (238, 130, 238) #紫罗兰
            if select[i][j] == 6:
                c1 = (255, 0, 0) # 红
            if select[i][j] == 7:
                c1 = (173, 255, 47 )#黄绿色
            if select[i][j] == 8:
                c1 = (255, 165, 0) #橙色
            if select[i][j] == 9: # 白色
                c1 = (255, 255, 255)
            if select[i][j] == 10:
                c1 = (0,0,0)
            myRect1 = pygame.Rect(j * 50, i * 50, 50, 50)
            pygame.draw.rect(screen, c1, myRect1, 0)

