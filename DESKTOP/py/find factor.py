import os
os.system('title find factor')
while True:
    a=int(input('number:'))
    list=[]
    for i in range(a):
        for x in range(a):
            if i*x == a:
                if i not in list:
                    list.append(i)
                elif x not in list:
                    list.append(x)
    list.append(1)
    list.append(a)
    print(sorted(list))