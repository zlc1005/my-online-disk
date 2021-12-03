import os
os.system('title prime factor')
while True:
    n = int(input('number:'))
    print('%d='%n,end='')
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                n=int(n/i)
                if n==1:
                    print('%d'%i,end='')
                else:
                    print('%dX'%i,end='')
                break
    print()