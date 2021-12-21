INPUT,LIST=input().upper(),['I','O','S','H','Z','X','N']
def AllIn(LIST,INPUT):
    for i in INPUT:
        if i not in LIST:return False
    return True
if AllIn(LIST,INPUT):print('YES')
else:print('NO')