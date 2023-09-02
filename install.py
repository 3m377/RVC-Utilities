import atexit
import os
import subprocess
import requests
import urllib.request
import shutil
import sys
import ctypes
import argparse
from tqdm import tqdm

# Check if script is running with admin priveledges
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Define function to run script with admin priveledges
def run_as_admin():
    if is_admin():
        return
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit()

run_as_admin()

def download_with_progress(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(filename, 'wb') as file, tqdm(
        desc=filename,
        total=total_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
        miniters=1,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)
            bar.update(len(data))

def install_rvc():
    # Set GIT_SSH_COMMAND
    GIT_SSH_COMMAND = 'ssh -i ' + os.path.join(os.environ['USERPROFILE'], '.ssh', 'id_rsa')

    print('Downloading 7za.exe')

    # Download 7za.exe
    urllib.request.urlretrieve('https://github.com/3m377/RVC-Utilities/raw/main/other/7za.exe', '7za.exe')

    print('Downloading RVC-beta.7z')
    print('This will take a while depending on your internet speed, so please be patient.')

    # Download RVC-beta.7z
    download_with_progress('https://huggingface.co/lj1995/VoiceConversionWebUI/resolve/main/RVC-beta.7z', 'RVC-beta.7z')
    print('Downloaded RVC-beta.7z')

    print('Extracting RVC-beta.7z using 7za.exe')
    subprocess.run(['7za.exe', 'x', 'RVC-beta.7z', '-oRVC-beta'])
    os.remove('RVC-beta.7z')

    # Clone Mangio-RVC-Fork using Git
    subprocess.run(['git', 'clone', 'https://github.com/Mangio621/Mangio-RVC-Fork/'])
    try:
        shutil.move('Mangio-RVC-Fork', 'RVC-beta')
    except PermissionError:
        # If permission denied, try to run the script with elevated privileges (as administrator)
        print("Moving files requires administrator privileges. Please enter your admin password.")
        subprocess.run(['runas', '/user:Administrator', 'python', sys.argv[0]])
    os.chdir('RVC-beta')
    os.rename('RVC-beta0717', 'RVC-beta')

    # Copy the entire contents of Mangio-RVC-Fork to RVC-Beta
    src_folder = 'Mangio-RVC-Fork'
    dst_folder = 'RVC-Beta'

    shutil.copytree(src_folder, dst_folder, dirs_exist_ok=True)

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

    print('Installation completed.')
    print('Please manually delete the "Mangio-RVC-Fork" folder.')
    os.system('pause')

def install_vc():
    vcVersion = "1.5.3.13"
    vcFileName = "MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.13.zip"
    vcFileURL = "https://huggingface.co/wok000/vcclient000/resolve/main/MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.13.zip"

    # If user has updated version, use it instead
    input("Do you have an updated version of the voice changer? (y/n): ")
    if input == "y": 
        vcVersion = "User Specified"
        vcFileName = "MMVCServerSIO_userspecified.zip"
        print("EXAMPLE LINK: https://huggingface.co/wok000/vcclient000/resolve/main/MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.13.zip")
        vcFileURL = input("Please input the direct download link to the updated version: ")

    os.system("cls")
    print("WARNING: This may not be updated, it depends if I remember to update the script.")
    print(f"Current version: {vcVersion}")
    os.system('pause')
    os.system("cls")

    # Download MMVCServerSIO
    print(f"Downloading {vcFileName}")
    print("This may take some time depending on your internet speed.")
    download_with_progress(vcFileURL, vcFileName)
    os.system("cls")

    # Extract MMVCServerSIO
    print(f"Extracting {vcFileName}")
    shutil.unpack_archive(vcFileName, "MMVCServerSIO")
    os.remove(vcFileName)
    os.system("cls")

    # Install finished
    print("Realtime RVC Voice Changer has been installed.")
    print("To use, run \"start_http.bat\"")
    os.system('pause')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Installer for RVC and VC")
    parser.add_argument("--install-mangio-rvc", action="store_true", help="Install Mangio-RVC-Fork (RVC)")
    parser.add_argument("--install-realtime-vc", action="store_true", help="Install Realtime VC Voice Changer")

    # When running the script:
    # python installer.py --install-mangio-rvc
    # python installer.py --install-realtime-vc

    args = parser.parse_args()

    if args.install_mangio_rvc:
        install_rvc()
    elif args.install_realtime_vc:
        install_vc()
    else:
        print("Please specify either --install-mangio-rvc or --install-realtime-vc.")
