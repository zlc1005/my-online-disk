
from itertools import permutations# main()

def split_in(n:str):# split string in list of strings
    list=[]# list of strings
    for _ in range(int(n)):# for each string
        list.append(input().split(' '))# split string in list of strings
    return list# main()

def get_list(n:int,k:int):
    l=[]
    n=n-k
    for _ in range(k):
        l.append(1)
    for _ in range(n):
        l.append(0)
    return l

def list_to_str(l):
    out=''
    for i in l:
        out+=str(i)
    return out

def get_permutations(n:list):
    perm = permutations(n)
    out=[]
    for i in list(perm):
        if i not in out:
            out.append(i)
    return out

def main():
    l=split_in(input())
    for i in l:
        n=int(i[0])
        k=int(i[1])
        l=get_list(n,k)
        perm=get_permutations(l)
        print('The bit patterns are')
        for j in perm:
            print(list_to_str(j))
        print('')

if __name__ == '__main__':
    main()