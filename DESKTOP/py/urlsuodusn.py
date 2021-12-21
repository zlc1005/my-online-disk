from re import U
import requests,parsel,pyperclip
class TkGuiApp(object):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        from urllib.parse import urlencode# from urllib.parse import urlencode
        import urllib.request as ulib# import urllib.request as urllib
        import requests,json,parsel
        self.urlencode=urlencode
        self.ulib=ulib
        self.requests=requests
        self.json=json
        self.parsel=parsel
        self.messagebox=messagebox
        self.simpledialog=simpledialog
        self.tk=tk
        self.hhh={
            f'User-Agent':f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'#set user agent
        }
    def init(self):
        self.root=self.tk.Tk()
        self.root.withdraw()
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)
    def send_api_l(self,data):
        self.ulib.urlopen(f'https://lucasz228sd45.herokuapp.com/surlset?'+str(self.urlencode(data)))#,headers=self.hhh)
        print('sent')
    def get_short_url(self,url):
        surlb=requests.post('https://www.shorturl.at/shortener.php',headers=self.hhh,data={'u':url})
        soup=self.parsel.Selector(surlb.text)
        url=soup.css(f'#shortenurl::attr(value)').get()
        return url

app=TkGuiApp()
app.init()
oldurl=app.inputbox('Enter the URL to shorten: ')
url=app.get_short_url(oldurl)
app.send_api_l({'surl':url,'old':oldurl})
pyperclip.copy(url)
app.mbox(f'The shortened URL is: {url} \n and has been copied to your clipboard.')


'''
https://cutt.ly/scripts/shortenUrl.php
post
{url:url,domain:0}

https://soo.gd/processreq.php
post
{txt_url:url,txt_name:name}

https://is.gd/create.php
post
{url:url,shorturl:'',opt=0}
css:'#short_url::attr(value)'
'''