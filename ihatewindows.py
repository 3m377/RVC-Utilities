import os
import subprocess
import urllib.request
import shutil
import argparse

def install_rvc():
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
    urllib.request.urlretrieve(vcFileURL, vcFileName)
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
