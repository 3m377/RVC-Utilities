@echo off

echo WARNING: READ ALL OF THIS BEFORE PROVIDING A LINK
echo When pasting a link, it must automatically download the model.
echo If the link requires you to click a button to download the model, it will not work.
echo Example of a correct download link (using huggingface):
echo https://huggingface.co/3m377/CASSIEsl/resolve/main/CASSIEv2.zip //hey, that's my model!
echo Notice how it has "resolve" in it?
echo Now look at this link:
echo https://huggingface.co/3m377/CASSIEsl/blob/main/CASSIEv2.zip
echo Because this link has "blob" instead of "resolve", it will not work.
echo You can easily fix this by replacing "blob" with "resolve", however this will only work with huggingface links.
set /p link= Paste the link to your model: 

echo Downloading the model...
echo This may take a while depending on your internet speed.
powershell.exe -NoProfile -ExecutionPolicy Bypass -Command "(New-Object Net.WebClient).DownloadFile('%link%', 'download.zip')"

echo The name of the model should be whatever there is at the end of the link.
echo Example: https://huggingface.co/3m377/CASSIEsl/resolve/main/CASSIEv2.zip
echo This model would be named "CASSIEv2", because the filename at the end of the link is "CASSIEv2.zip"
set /p name=Input the name of your model: 
powershell Expand-Archive download.zip -DestinationPath %name%-download
del download.zip

for /r "%name%-download" %%x in (*.pth) do ren "%%x" %name%.pth
for /r "%name%-download" %%x in (*.pth) do move "%%x" "weights"
mkdir %name%
for /r "%name%-download" %%x in (*.index) do move "%%x" "%name%"
move %name% logs
rmdir %name%-download
pause