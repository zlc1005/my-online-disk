@set pythoncd=C:\Users\29242\AppData\Local\Programs\Python\Python39
@echo off
@set a=%cd%
@color 70
@cd %pythoncd%
@cd Scripts
@for /f "delims=" %%a in ('mshta "%~f0"') do set acd=%%a
pyinstaller -w %acd% --onefile
@cd dist
@"C:\Windows\explorer.exe" %cd%
@cd %a%
@cd beta
@cls
echo ok
pause

<input type=file id=f>
<script>
f.click();new ActiveXObject('Scripting.FileSystemObject').GetStandardStream(1).Write(f.value);close();
</script>