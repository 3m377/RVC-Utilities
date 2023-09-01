@echo off
:: Set variables
setlocal
set rvcInstallerName=installer.py
set rvcInstallerURL=https://github.com/3m377/RVC-Utilities/raw/main/installer.py

set vcInstallerName=vcinstaller.py
set vcInstallerURL=https://github.com/3m377/RVC-Utilities/raw/main/vcinstaller.py

set currentVer=1.0.0
set updateCheckURL=https://github.com/3m377/RVC-Utilities/raw/main/version
set updateCheckName=update.txt

set scriptURL=https://github.com/3m377/RVC-Utilities/raw/main/easy-install-rvc.bat
set scriptName=easy-install-rvc.bat

goto checkupdate

:: Prompt user for installation choice
:prompt
echo Select an installation option:
echo 1. Install RVC (Mangio-RVC-Fork)
echo 2. Install Realtime RVC Voice Changer
set /p choice=Enter your choice (1 or 2): 

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
) else (
    echo Invalid choice
    pause
    cls
    goto prompt
    exit /b 1
)
goto end

:checkupdate
:: Download update.txt
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%updateCheckURL%', '%updateCheckName%')"

:: Check for updates
FOR /F "tokens=* delims=" %%x in (%updateCheckName%) DO set actualVer=%%x
del "%updateCheckName%"

:: If there is an update, download it
if %currentVer% == %actualVer% (
    echo Version matches with most recent version.
    goto prompt
) else (
    echo Version does not match up with latest version.
    echo Downloading latest version...
    powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%scriptURL%', '%scriptName%')"
    echo Please restart the script.
    pause
)

:end
echo Ending script...
