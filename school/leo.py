# the write word gime]
class TkGuiApp(object):# class _main
    def __init__(self,errorl=0,l=1,debugmode=False) -> None:# class _main
        import tkinter as tk# import random,sys,tkinter as tk
        from tkinter import simpledialog# from tkinter import simpledialog
        from tkinter import messagebox# from tkinter import messagebox
        self.messagebox=messagebox
        self.simpledialog=simpledialog
        self.tk=tk
    def init(self):
        self.root=self.tk.Tk()
        self.root.withdraw()
    def inputbox(self,text):
        return self.simpledialog.askstring('quiz', text)# askstring quiz text
    def mbox(self,text):# mbox
        self.messagebox.showinfo('message', text)
import random
word_list=['cat','world','some','one','after','codeing','two','fore']
def str_to_list(word):
    word_list=[]
    for i in word:
        word_list.append(i)
    return word_list
def list_to_str(word_list):
    word=''
    for i in word_list:
        word=word+i
    return word
app=TkGuiApp()
app.init()
for _ in range(5):
    random_word=random.choice(word_list)
    word=random.choice(random_word)
    qu_index=random_word.index(word)
    quword=random_word
    str_quword=str_to_list(quword)
    str_quword[qu_index]='?'
    quword=list_to_str(str_quword)
    # app.mbox(''.join(quword))
    answer=app.inputbox(quword+'\nyour answer:')
    if answer==word:
        app.mbox('you are right')
    else:
        app.mbox('you are wrong')
        app.mbox('the answer is {}'.format(word))
        # break
app.mbox('the end')