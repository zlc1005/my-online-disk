@echo off
:c
set ccdd=%c%
echo c
exit
:i
set ccdd=%i%
echo i
exit
set c=C:\Users\29242\zlc1003\zlc1003.github.io
set i=i:\demo_app_1
set ccdd=None
echo 1=C:\Users\29242\zlc1003\zlc1003.github.io
echo 2=i:\demo_app_1
set /p addd=请输入mode:
if %addd% equ 1 goto c

if %addd% equ 2 goto i

set /p input=请输入提交原因:
cd %ccdd%

::git add .
::git commit -m "%input%"
::git push

echo 提交成功
pause