for /f "tokens=*" %%i in ('cscript //nologo c.vbs') do set WS=%%i
echo %WS%>%cd%\a.txt
cd %WS%
cd Scripts
pip3 install pyinstaller
