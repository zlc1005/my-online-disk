def 是否相等(text):
    text=str(text)
    LIST=sorted(list(text))
    SET=sorted(list(set(text)))
    if LIST==SET:
        return True
    else:
        return False

INPUT=int(input())+1
outopt=INPUT
while not 是否相等(outopt):
    outopt+=1
print(outopt)