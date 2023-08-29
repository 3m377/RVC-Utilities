@echo off
:: Download installer.py
echo Downloading installer.py
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/3m377/RVC-Utilities/raw/main/installer.py', 'installer.py')"

python installer.py
del installer.py
pause
