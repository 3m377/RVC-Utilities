import os
import urllib.request
import shutil

vcVersion = "1.5.3.13"
vcFileName = "MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.13.zip"
vcFileURL = "https://huggingface.co/wok000/vcclient000/resolve/main/MMVCServerSIO_win_onnxgpu-cuda_v.1.5.3.13.zip"

os.system("cls")
print("WARNING: This may not be updated, it depends if I remember to update the script.")
print(f"Current version: {vcVersion}")
input("Press Enter to continue...")
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
input("Press Enter to exit...")
