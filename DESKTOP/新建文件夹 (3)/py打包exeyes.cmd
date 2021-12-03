set pythoncd=C:\Users\29242\AppData\Local\Programs\Python\Python39
set b=\OneDrive\
@echo off
set a=%cd%
color a
cd %pythoncd%
cd Scripts
pyinstaller -F d:\code.py
cd dist
copy code.exe %HOMEDRIVE%%HOMEPATH%%B%desktop
del code.exe
del d:\code.py
cd %a%
a.vbs
b.vbs
cls
echo ok
pause