# 3m377's RVC Utilities
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://en.wikipedia.org/wiki/MIT_License)

*Latest README update: 2023-09-02*

## Introduction
Here is a list of all of my utility scripts, designed to make life easier when installing and using RVC (Retrieval Based Voice Conversion). These scripts only work on **Windows** systems and have been tested on **Windows 10**. While primarily aimed at Windows 10, any testing on different Windows versions would be highly appreciated.
## Features

- Streamlined automation of the RVC installation process (Now supports w-okada's realtime RVC voice changer client!).
- Convenient model downloads using the downloadmodel.bat script.
## Downloads

*Note: Availability may vary based on README update frequency. I recommend downloading straight from GitHub incase I forget to update these links.*

- [Easy RVC Installer](https://github.com/3m377/RVC-Utilities/releases/download/1.0.3/easy-install-rvc.bat) | A script designed to automate the RVC installation process as much as possible.
- [Model Downloader](https://github.com/3m377/RVC-Utilities/releases/download/1.0.3/downloadmodel.bat) | This script is automatically downloaded when using the Easy RVC Installer script. Alternatively, it can be downloaded separately if RVC is already installed.
## Instructions

### If RVC is already installed
- Place the [Model Downloader](https://github.com/3m377/RVC-Utilities/releases/download/1.0.3/downloadmodel.bat) script into the main RVC folder.

### If RVC is not yet installed
- Make sure you have [Git](https://git-scm.com/downloads) installed. If you don't, the installation will not work.
- Make sure you have [Python](https://www.python.org/downloads/) installed, or the installer will not work.
- Download the [Easy RVC Installer](https://github.com/3m377/RVC-Utilities/releases/download/1.0.3/easy-install-rvc.bat) script and place it in your desired RVC installation folder.
- Run the script.
- When prompted, type 1 to install RVC with Mangio-RVC-Fork.
- Allow it to make changes to your device (It's not a virus, you can look through the very simple code.)
- The Model Downloader will be automatically downloaded and placed in the appropriate folder; no separate download is necessary.
## Changelog
**1.0.3**
- Added progress bars to the installer to show progress of large file downloads.
- Added a check that makes sure `config.txt` exists. If it doesn't it will install tqdm and requests with pip, and then create `config.txt`. This is to ensure the install script will run without errors caused by the user not having tqdm or requests installed.
- Automated the process of moving the files from Mangio-RVC-Fork to RVC-beta and replacing any that already exist.
- Started logging changes in the changelog.

**1.0.2**
- Merged `installer.py` and `vcinstaller.py` into one script.

**1.0.1**
- I have no idea what I added in this release.

**1.0.0**
- Added an automatic check for script updates (only for the script to ensure you have the latest version. This ensures that even if I forget to update the download link you will still be notified of a new update and be prompted to download it).
## Planned changes
- Update the Python script so it is fully automated
- Add a progressbar to the model downloader script to show the model's download progress
- Fix weird bug where it refuses access to the Mangio-RVC-Fork folder (IMPORTANT)
## Contact

For support, feedback, questions, or concerns, please reach out to 3m377 on [Discord](https://discord.com).
## Acknowledgements

- [README Markdown Editor](https://readme.so/)
- [AI HUB Discord server](https://discord.com/invite/aihub/)
- [7-Zip](https://www.7-zip.org)
## DISCLAIMERS
Most of this is written with the help of [ChatGPT](https://chat.openai.com/), since I am not experienced enough to write this myself.

I do not own 7-Zip, nor do I claim to own it. I have only added it to the repository so that the script can easily download it.
