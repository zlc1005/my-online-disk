class _main():
    def __init__(self):
        import random
        self.random=random
        self.jjcc = {'+':['add {a} and {b}','{a} increased by {b}','the sum of {a} and {b}','add {a} to {b}','{a} plus {b}'],'-':['subtract {b} from {a}','{b} less than {a}','{a} decreased by {b}','{a} minus {b}','the difference of {a} and {b}'],'*':['{a} times {b}','multiply {a} by {b}','the product of {a} and {b}'],'/':['divide {a} by {b}','the quotient of {a} and {b}']}
    def get_quiz(self,list_):
        a=int(list_[0])
        b=int(list_[1])
        jjjcc=list_[2]
        tf=False
        if jjjcc == '+':
            thesum=a+b
        elif jjjcc == '-':
            if tf:
                while a<b or a==b:
                    a=self.random.randint(1,30)
                    b=self.random.randint(1,30)
                    # self.log(f'{r1}+{r2}')
            thesum=a-b
        elif jjjcc == '*':
            thesum=a*b
        elif jjjcc == '/':
            if tf:
                while a%b!=0:
                    a=self.random.randint(1,30)
                    b=self.random.randint(1,30)
            thesum=a/b
        return [self.random.choice(self.jjcc[jjjcc]).format(a=a,b=b),thesum,f'{a}{jjjcc}{b}']
    def ai_get(self,ss):
        aiout=[]
        jjcc=''
        if '+' in ss:
            jjcc='+'
            aiout.append(ss.split('+')[0])
            aiout.append(ss.split('+')[1])
        if '-' in ss:
            jjcc='-'
            aiout.append(ss.split('-')[0])
            aiout.append(ss.split('-')[1])
        if '*' in ss:
            jjcc='*'
            aiout.append(ss.split('*')[0])
            aiout.append(ss.split('*')[1])
        if '/' in ss:
            jjcc='/'
            aiout.append(ss.split('/')[0])
            aiout.append(ss.split('/')[1])
        aiout.append(jjcc)
        return aiout
    def ai_ex_to_qu(self,ex):
        return self.get_quiz(list_=self.ai_get(ex))
if __name__ == '__main__':
    main=_main()
    print(main.get_quiz(['2','3','+']))