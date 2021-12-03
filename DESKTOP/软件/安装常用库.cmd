@echo off
@cd beta
@for /f "tokens=*" %%i in ('cscript //nologo c.vbs') do set WS=%%i
@cd %WS%
@cd Scripts
@pip3 install xes-lib
@pip3 install pygame
@pip3 install jieba
@pip3 install numpy
@pip3 install qrcode
@pip3 install imagio
@pip3 install xwPython
@pip3 install turtle