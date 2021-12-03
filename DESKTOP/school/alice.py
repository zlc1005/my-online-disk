import random as r,os as o
while True:
    list=[r.randint(1,100) for _ in range(2)]
    a=input(f'what is {list[0]}+{list[1]}?')
    if a=='':
        print('quit');o.system('pause');break
    elif int(a)==list[0]+list[1]:
        print('correct')
    else:
        print('wrong')