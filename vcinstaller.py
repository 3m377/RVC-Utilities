import os
import urllib.request
import shutil

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
