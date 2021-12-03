import os
os.system('title gcf')
while True:
    a=int(input('number:'))
    b=int(input('number:'))
    list=[]
    listb=[]
    lista=[]
    for i in range(a):
        for x in range(a):
            if i*x == a:
                if i not in list:
                    list.append(i)
                elif x not in list:
                    list.append(x)
    list.append(1)
    list.append(a)
    listb.append(1)
    listb.append(b)
    for i in range(b):
        for x in range(b):
            if i*x == b:
                if i not in listb:
                    listb.append(i)
                elif x not in listb:
                    listb.append(x)
    for i in list:
        for x in listb:
            if i==x:
                if i not in lista:
                    lista.append(i)
    print(max(lista))