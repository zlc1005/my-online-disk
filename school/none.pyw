class _main(object):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import random,sys,tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        import urllib.request as ulib# import urllib as ulib
        from urllib.parse import urlencode# from urllib.parse import urlencode
        import json# import json
        self.json=json# set json
        self.urlencode=urlencode# set urlencode to urlencode
        self.simpledialog=simpledialog# set self.simpledialog to simpledialog
        self.messagebox=messagebox# set self.messagebox to messagebox
        self.sys=sys# set self.sys to sys
        self.debug=debugmode# set debugmode to debugmode
        self.random=random# set self.random to random
        self.ulib=ulib# set self.ulib to ulib
        self.errorl=errorl# set self.errorl to errorl
        self.root=tk.Tk()# set self.root to tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()# get screen width
        self.screen_height = self.root.winfo_screenheight()# get screen height
        self.x=self.screen_width//2# set x to screen_width//2
        self.y=self.screen_height//2# set y to screen_height//2
        self.root.geometry(f'+{self.x}+{self.y}')# set geometry
        self.t=False# set t to False
        self.li=l# set li to l
        self.right_time=0# set rtime to 0
        self.hhh={
            f'User-Agent':f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'#set user agent
        }
        self.good_word_list=['good','congratulation','congratulations','nice','well done']# this is a list of good words
        self.root.withdraw()# withdraw root
        self.iswin=False# set iswin to False
        self.data={}#{'name':str(self.NAME),'level':str(self.li),'win':str(self.iswin)}# set data to {name=self.NAME,level=self.li,time=self.right_time}
    def main(self) -> None:
        self.first()# run first
        self.run()# run run
    def log(self,text):
        print(text)
    def ga(self):...
    def getth(self,num) -> None:
        if num==1:
            return 'first'
        elif num==2:
            return 'second'
        elif num==3:
            return 'third'
        elif num==4:
            return 'fourth'
        elif num==5:
            return 'fifth'
        elif num==6:
            return 'sixth'
        elif num==7:
            return 'seventh'
        elif num==9:
            return 'ninth'
        elif num==10:
            return 'tenth'
    def set_m(self):# can't run
        self.root.geometry(f'+{self.x}+{self.y}')# set geometry
    def send_api_l(self):
        self.ulib.urlopen(f'https://lucasz228sd45.herokuapp.com/xxx?'+str(self.urlencode(self.data)))#,headers=self.hhh)
        self.log('sent')
        # request https://lucasz228sd45.herokuapp.com/api?name=Player&level=1&win=False
    def getname(self) -> None:
        self._s=self.get_s()# set s to get_s
        print(self._s)
        ###########debug############
        #self.ulib.urlopen(f'https://lucasz228sd45.herokuapp.com/xxx?'+str(self.urlencode(self.data)))
        ######debug end#############
        self.NAME=self.inputbox('What is your name?')# get name
        if self.NAME==None or self.NAME=='':# if name is none or empty
            self.NAME='Player'# set name to 'Player'
    def get_s(self) -> str:
        json_data=self.ulib.urlopen(f'https://lucasz228sd45.herokuapp.com/get_s')#,headers=self.hhh)
        return self.json.loads(json_data.read().decode('utf-8'))[0]['s']
    def get_data(self) -> None:
        self.data={'name':str(self.NAME),'level':str(self.li),'win':str(self.iswin)}# set data to {name=self.NAME,level=self.li,time=self.right_time}
    def first(self):
        self.mbox(f'Hello,{self.NAME}!')# mbox Hello,Player!
        self.mbox("Welcome to Lucas's math game!!!")# mbox Welcome to Lucas and Alice's math game!!!
        self.mbox(f'you\'re on the first level')# mbox you're on the 1st level
    def runserver(self):
        pass
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)# showinfo message text
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def quit_(self):
        self.get_data()
        self.send_api_l()
        self.sys.exit(self.errorl)# exit with errorl
    def get_good_word(self) -> str:
        return self.random.choice(self.good_word_list)
    def run(self) -> None:
        self.get_data()# get name
        r1=self.random.randint(1,30)# set r1 to random.randint(1,30)
        r2=self.random.randint(1,30)# set r2 to random.randint(1,30)
        r3=self.random.choice(['+','-','x','/'])# set r3 to random.choice(['+','-','x','/'])
        if r3=='+':
            r4=r1+r2
        elif r3=='-':
            while r1<r2:
                r1=self.random.randint(1,30)
                r2=self.random.randint(1,30)
                self.log(f'{r1}+{r2}')
            r4=r1-r2
        elif r3=='x':
            r4=r1*r2
        elif r3=='/':
            while r1%r2!=0:
                r1=self.random.randint(1,30)
                r2=self.random.randint(1,30)
            r4=r1//r2
        self.set_m()
        r5=self.inputbox('What is '+str(r1)+' '+r3+' '+str(r2)+'?')# askstring 'What is r1 r3 r2?'
        if r5==None:
            self.mbox('You quit the game.')
            self.quit_()
        elif r5==self._s:
            self.right_time=4
            self.li=4
        elif r5==str(r4):
            self.mbox('Correct!')
            self.right_time+=1
        elif r5=='':
            if self.t:
                self.mbox('You quit the game.')
                self.quit_()
            else:
                self.mbox('input some number')
                self.t=True
        else:
            self.mbox('Wrong!')
        if self.right_time==5:
            self.li+=1
            self.right_time=0
            self.mbox(f'you\'re on the {self.getth(self.li)} level,{self.get_good_word().title()}')# mbox you're on the 1st level
        if self.li==5:
            self.mbox(f'{self.get_good_word().title()}! You win!')# mbox You win!
            if self.debug:
                self.log('win')
            self.iswin=True
            self.quit_()
        self.run()
# ======================================================================================================================
if __name__ == '__main__':
    app=_main(0)
    app.getname()
    app.main()