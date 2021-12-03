# import pyautogui# import pyautogui
# # make a gui
# #a=pyautogui.confirm('Are you sure?')
# # make a input box
# b=pyautogui.prompt('input the pos(use the space to split)','input box').split()
# # x1, y1 = input("Enter the coordinates of the point: ").split()
# pyautogui.moveTo(int(b[0]), int(b[1]))# move to the point
# print('aa\b')
# # x, y = pyautogui.position()# get mouse position
# # pyautogui.click()# click mouse
#import pyautogui, sys, time

'''
import pyautogui
while True:
    x,y=pyautogui.position()
    positionstr='X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
    print(positionstr,end='')
    print('\b'*len(positionstr),end='',flush=True)

import random
while True:
    a='asdfghjklqwertyuiopmnbvcxzASDFGHJKLMNBVCXZQWERTYUIOP1234567890/*-+!@#$%^&*()_=[]\\\';/.,<>?:"{\}| '
    b=random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)+random.choice(a)
    print(b,end='')
    print('\b'*len(a),end='',flush=True)

'''








'''

import subprocess,pyautogui,time
def copy(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
def type_text(text, interval=0.1):
    for c in text:
        if c.isdigit():
            pyautogui.hotkey('shift', c, interval=0.1)
        else:
            pyautogui.press(c)
        time.sleep(interval)
import tkinter as tk
window = tk.Tk()
window.title('自动输入器')
window.geometry('300x300')
window.resizable(0,0)
label = tk.Label(window, text='要输入的文本', font=('Arial', 12))
label.pack()
text = tk.Text(window, font=('Arial', 12))
text.pack()
print(text)
window.mainloop()
'''






















'''''''''''''''

from tkinter import messagebox
import tkinter as tk ,pyautogui,time

window = tk.Tk()
window.title('自动输入器')
window.geometry('450x100')

# user information
# tk.Label(window, text='User name: ').place(x=50, y= 150)

entry_usr_pwd = tk.Text(window,  width=50, height=3)
entry_usr_pwd.place(x=50, y=0)
def d(a):
    print('\b'*len(a),end='',flush=True)
########################################################################################################################
def type_text(text, interval=0.01):
    for c in text:
        if c.isdigit():
            pyautogui.hotkey('shift', c, interval=0.1)
        else:
            pyautogui.press(c)
        time.sleep(interval)
########################################################################################################################
def a():
    global entry_usr_pwd
    if entry_usr_pwd.get('0.0', 'end') == '':
        messagebox.showinfo('提示', '请输入要输入的文本')
    else:
        time.sleep(3)
        type_text(entry_usr_pwd.get('0.0', 'end'))
        messagebox.showinfo('提示', '输入完成')
# login and sign up button
btn_sign_up = tk.Button(window, text='输入', command=a)
btn_sign_up.place(x=150, y=50)

window.mainloop()



'''''''''''''''


















'''
def get_pos(copy):
    try:
        while True:
            x,y=pyautogui.position()
            positionstr='X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
            print(positionstr,end='')
            print('\b'*len(positionstr),end='',flush=True)
    except KeyboardInterrupt:
        copy(str(x)+','+str(y))
        print('\n')
a=493,635
b=591,366
pyautogui.moveTo(a[0],a[1])
pyautogui.doubleClick()
time.sleep(0.5)
pyautogui.moveTo(b[0],b[1])
pyautogui.doubleClick()
'''
