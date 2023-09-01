@echo off
:: Set variables
setlocal
set rvcInstallerName=installer.py
set rvcInstallerURL=https://github.com/3m377/RVC-Utilities/raw/main/installer.py

set vcInstallerName=vcinstaller.py
set vcInstallerURL=https://github.com/3m377/RVC-Utilities/raw/main/vcinstaller.py

set currentVer=1.0.1
set updateCheckURL=https://github.com/3m377/RVC-Utilities/raw/main/version
set updateCheckName=update.txt

set scriptURL=https://github.com/3m377/RVC-Utilities/raw/main/easy-install-rvc.bat
set scriptName=easy-install-rvc.bat

goto startcheck

:: Prompt user for installation choice
:prompt
echo Select an installation option:
echo 1. Install RVC (Mangio-RVC-Fork)
echo 2. Install Realtime RVC Voice Changer
echo 3. Check for updates (script, not RVC)
echo 4. Credits
echo 5. Exit
set /p choice=Enter your choice (1-5): 

:: Validate user input
if "%choice%"=="1" (
    :: Download installer.py
    echo Downloading installer.py
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%rvcInstallerURL%', '%rvcInstallerName%')"

    python %rvcInstallerName%
    del %rvcInstallerName%
) else if "%choice%"=="2" (
    :: Download VC installer script
    echo Downloading %vcInstallerName%
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%vcInstallerURL%', '%vcInstallerName%')"

    :: Check if download was successful
    if not exist %vcInstallerName% (
        echo Failed to download %vcInstallerName%
        pause
        exit /b 1
    )

    :: Run installer script
    python %vcInstallerName%

    :: Check if Python script execution was successful
    if %errorlevel% neq 0 (
        echo %vcInstallerName% encountered an error
        pause
        exit /b %errorlevel%
    )

    :: Delete installer script
    del %vcInstallerName% /f
) else if "%choice%"=="3" (
    :: Check for updates
    goto checkupdate
) else if "%choice%"=="4" (
    :: Display credits
    goto credits
) else if "%choice%"=="5" (
    :: Exit gracefully
    exit /b 0
) else (
    :: Invalid choice
    echo Invalid choice. Please try again.
    pause
    goto menu
)
exit /b 0

:checkupdate
:: Download update.txt
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%updateCheckURL%', '%updateCheckName%')"

:: Check for updates
FOR /F "tokens=* delims=" %%x in (%updateCheckName%) DO set actualVer=%%x
del "%updateCheckName%"

:: If there is an update, download it
if %currentVer% == %actualVer% (
    cls
    echo No updates detected, you are running the latest version of the script: %currentVer%
    goto prompt
) else (
    echo Version does not match up with latest version.
    echo Downloading latest version...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%scriptURL%', '%scriptName%')"
    echo Please restart the script.
    pause
)

:startcheck
:: Download update.txt
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%updateCheckURL%', '%updateCheckName%')"

:: Check for updates
FOR /F "tokens=* delims=" %%x in (%updateCheckName%) DO set actualVer=%%x
del "%updateCheckName%"

:: Warn user if update is detected
if %currentVer% == %actualVer% (
    echo Congrats, you are running the latest version of the script, %currentVer%
    goto prompt
) else (
    echo WARNING: Update detected. Current version: %currentVer%. Most recent version: %actualVer%
    echo To update, select "Check for updates (3)"
    goto prompt
)

:credits
:: Credits
echo Script created by 3m377 (with help from ChatGPT)
echo RVC created by lj1995
echo Mangio-RVC-Fork created by Mangio621 and Kalomaze (and all the other contributors)
echo Realtime RVC Voice Changer (MMVCServerSIO) created by w-okada
echo 7-Zip created by Igor Pavlov
pause
cls
goto prompt
