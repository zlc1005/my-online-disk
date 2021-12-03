import os
os.system('title lcm')
def lcm(x, y):
    m = max(x, y)
    n = min(x, y)
    while m%n:
        m, n = n, m%n
    return x*y//n
while True:
    print(lcm(int(input('number:')),int(input('number:'))))