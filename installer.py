import os
import subprocess
import urllib.request
import shutil

# Set GIT_SSH_COMMAND
GIT_SSH_COMMAND = 'ssh -i ' + os.path.join(os.environ['USERPROFILE'], '.ssh', 'id_rsa')

print('Downloading 7za.exe')

# Download 7za.exe
urllib.request.urlretrieve('https://github.com/3m377/RVC-Utilities/raw/main/other/7za.exe', '7za.exe')

print('Downloading RVC-beta.7z')
print('This will take a while depending on your internet speed, so please be patient.')

# Download RVC-beta.7z
urllib.request.urlretrieve('https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC-beta.7z', 'RVC-beta.7z')
print('Downloaded RVC-beta.7z')

print('Extracting RVC-beta.7z using 7za.exe')
subprocess.run(['7za.exe', 'x', 'RVC-beta.7z', '-oRVC-beta'])
os.remove('RVC-beta.7z')

# Clone Mangio-RVC-Fork using Git
subprocess.run(['git', 'clone', 'https://github.com/Mangio621/Mangio-RVC-Fork/'])
shutil.move('Mangio-RVC-Fork', 'RVC-beta')
os.chdir('RVC-beta')
os.rename('RVC-beta0717', 'RVC-beta')

print('Please move all files from the Mangio-RVC-Fork folder to the RVC-beta folder.')
print('It will tell you "The destination has X files with the same names",')
print('Just click "Replace the files in the destination".')
print('DO NOT CLOSE THIS WINDOW, THE INSTALLATION WILL END IF YOU DO')
print('Once you\'re done copying all of the files, delete the Applio-RVC-Fork folder and return to this window.')
os.system('pause')

# Install python requirements
os.chdir('RVC-beta')
subprocess.run(['pip', 'install', '-r', 'requirements.txt'])
subprocess.run(['pip', 'install', '-r', 'requirements-win-for-realtime_vc_gui.txt'])
os.chdir('..')

# Download easyGUI_local_installer.zip
urllib.request.urlretrieve('https://github.com/kalomaze/Mangio-Kalo-Tweaks/releases/download/v3.3/easyGUI_local_installer.zip', 'easyGUI_local_installer.zip')

# Extract easyGUI_local_installer.zip
shutil.unpack_archive('easyGUI_local_installer.zip', 'RVC-beta')
os.remove('easyGUI_local_installer.zip')
os.chdir('RVC-beta')

# Run install_easyGUI.bat
subprocess.run(['install_easyGUI.bat'])

# Download downloadmodel.bat
urllib.request.urlretrieve('https://github.com/3m377/RVC-Utilities/raw/main/downloadmodel.bat', 'downloadmodel.bat')

# Remove 7za.exe
os.chdir('..')
os.chdir('..')
os.remove('7za.exe')

# Pause for user review
os.system('pause')
