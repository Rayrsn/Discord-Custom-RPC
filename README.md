# Discord-Custom-RPC

<p align="center">
	<img src="https://img.shields.io/github/v/release/Rayrsn/Discord-Custom-RPC?style=for-the-badge&logoWidth=20&color=8829d6" />
	<img src="https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20&color=8829d6" />
</p>

<p align="center">
  <img width="512" height="512" src="https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/rpclogo.png?raw=true">
</p>

### <h2 align="center"> <i> <b> A Discord Custom RPC app with GUI </b> </i> </h2>



<br>

<p>
  <img width=70% height=70% src="https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/preview_win.png?raw=true">
</p>

# Usage
### <b> Just head to the [Releases](https://github.com/Rayrsn/Discord-Custom-RPC/releases) tab and download the latest version. <ins>(Only works with Windows)</ins> </b>
### <b>For running on Linux and Mac go to [Running from source](https://github.com/Rayrsn/Discord-Custom-RPC#running-from-source)</b>
## How do i get the client id and the other stuff?
1. Go to [Discord's Developer Portal](https://discord.com/developers/applications/).
2. Make a New Application and name it whatever you want. (this is also the name of your RPC)

![DevPortal](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/newapp.png?raw=true)

3. Then head to the Rich Presence tab.

![RichPresence](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/richpresence.png?raw=true)

4. Scroll down to the "Rich Presence Assets" section

5. Here you can upload any image you want. (it has to be 512x512, there are many online tools that resize images for you)
Also remember you can't rename the image once you hit the "Save Changes" button. (it has to be deleted and reuploaded)

![Uploading](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/Uploading.png?raw=true)

6. Then head back to the "General Information" tab and copy the Application ID. (this is the same as Client ID)

![AppID](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/appid.png?raw=true)

## Running from source 
1. Make sure you have Python 3 installed.
2. Run `python -m pip install -r requirements.txt` or `python3 -m pip install --requirement requirements.txt` if you're on Linux or Mac.
3. Then run `python main.py` or `python3 main.py` if you're on Linux or Mac.
## Building from source
* This also works with Linux (i haven't tested it with Mac yet) which means you can also make Linux executables
1. Follow steps 1 and 2 from the previous section.
2. Install PyInstaller by running `python pip install pyinstaller` or `python3 -m pip install pyinstaller` if you're on Linux or Mac.
3. Run `python pyinstaller --noconsole --onefile --icon=icon.ico main.py` or `python3 pyinstaller --noconsole --onefile --icon=icon.ico main.py` if you're on Linux or Mac. (Replace <b> icon.ico </b> with your own icon)
4. Move `config.json` and the .bmp files to the directory.
## Features
* Automatically loads the last used RPC.
## Known Bugs
* ~~Sometimes the RPC doesn't get updated on your local client but it does get updated. (you can check with other devices)~~
* ~~The enable time check box doesn't work.~~

All of the mentioned bugs are fixed.

## Acknowledgments and FAQ
* Why can't I click on my own button? 
You just can't. (Discord Limitation)

* The reason I haven't uploaded a Linux executable is that there are too many Linux distros and each one of them has a specific requirement. And the file size for each Linux executable is much larger than the Windows version.

* Why doesn't it work with wine on Linux?
Because if it's launched by wine, the program won't detect the running discord session. this is neither a bug nor a mistake, it's simply a software limitaion.

## To-Do List
- [x] Make a functioning enable time check box.
- [x] Minimize to tray feature.
- [ ] Add presets.
- [ ] A better UI/UX? (no promises tho)

## Questions
### If yall have any questions or just wanna talk, add me on [Discord](https://rayr.ml/LinkInBio) or use my username Rayr#6709 (this might change so it's better to just use the link)
