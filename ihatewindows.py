import os
import subprocess
import urllib.request
import shutil

shutil.move('Mangio-RVC-Fork', 'RVC-beta')
os.chdir('RVC-beta')
os.rename('RVC-beta0717', 'RVC-beta')

# Copy the entire contents of Mangio-RVC-Fork to RVC-Beta
src_folder = 'Mangio-RVC-Fork'
dst_folder = 'RVC-Beta'

shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)

# Delete the Mangio-RVC-Fork folder
shutil.rmtree(src_folder)

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
