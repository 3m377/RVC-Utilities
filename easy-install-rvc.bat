@echo off
set GIT_SSH_COMMAND="ssh -i %USERPROFILE%.ssh\id_rsa"

echo Downloading 7za.exe

:: Download 7za.exe
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/3m377/RVC-Utilities/raw/main/other/7za.exe', '7za.exe')"

:: Download RVC-beta.7z
echo Downloading RVC-beta.7z
echo This will take a while depending on your internet speed, so please be patient.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC-beta.7z', 'RVC-beta.7z')"
echo Downloaded RVC-beta.7z

:: Extract RVC-beta.7z using 7za.exe
echo Extracting RVC-beta.7z
"%~dp07za.exe" x "%~dp0RVC-beta.7z" -o"%~dp0RVC-beta"
del RVC-beta.7z

:: Clone Mangio-RVC-Fork using Git
git clone https://github.com/Mangio621/Mangio-RVC-Fork
move Mangio-RVC-Fork RVC-beta
cd RVC-beta
REN RVC-beta0717 RVC-beta
echo Please move all files from the Mangio-RVC-Fork folder to the RVC-beta folder.
echo It will tell you "The destination has X files with the same names",
echo Just click "Replace the files in the destination".
echo DO NOT CLOSE THIS WINDOW, THE INSTALLATION WILL END IF YOU DO
echo Once you're done copying all of the files, delete the Mangio-RVC-Fork folder and return to this window.
pause

:: Install python requirements
cd RVC-beta
pip install -r requirements.txt
pip install -r requirements-win-for-realtime_vc_gui.txt
cd ..

:: Download easyGUI_local_installer.zip
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/kalomaze/Mangio-Kalo-Tweaks/releases/download/v3.3/easyGUI_local_installer.zip', 'easyGUI_local_installer.zip')"

powershell Expand-Archive easyGUI_local_installer.zip -DestinationPath RVC-beta
del easyGUI_local_installer.zip
cd RVC-beta
CALL install_easyGUI.bat

:: Download downloadmodel.bat
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/3m377/RVC-Utilities/raw/main/downloadmodel.bat', 'downloadmodel.bat')"

:: Download 7za.exe again
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('https://github.com/3m377/RVC-Utilities/raw/main/other/7za.exe', '7za.exe')"

cd ..
cd ..
del 7za.exe

echo Successfully install RVC-beta and EasyGUI
pause
