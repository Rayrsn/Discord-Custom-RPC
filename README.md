# Discord-Custom-RPC

<p align="center">
	<img src="https://img.shields.io/github/v/release/Rayrsn/Discord-Custom-RPC?style=for-the-badge" />
</p>
<p align="center" href="https://github.com/qwertyquerty/pypresence">
	<img src="https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20" />
</p>

<p align="center">
  <img width="512" height="512" src="https://rayr.ml/Github/rpclogo.png">
</p>

### <h2 align="center"> <i> <b> A Discord Custom RPC app with GUI </b> </i> </h2>



<br>

# Usage
### <b> Just head to the [Releases](https://github.com/Rayrsn/Discord-Custom-RPC/releases) tab and download the latest version. </b>
## How do i get the client id and the other stuff
1. Go to [Discord's Developer Portal](https://discord.com/developers/applications/).
2. Make a New Application and name it whatever you want. (this is also the name of your RPC)

![DevPortal](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/newapp.png?raw=true)

3. Then head to the Rich Presence tab.

![RichPresence](https://github.com/Rayrsn/Discord-Custom-RPC/raw/main/images/richpresence.png?raw=true)

4. Here you can upload any image you want. (it has to be 512x512, there are many online tools that resize images for you)
5. Also remember you can't rename the image once you hit the "Save Changes" button. (it has to be deleted and reuploaded)

## Running from source 
1. Make sure you have Python 3 installed.
2. Run `python pip install -r requirements.txt` or `python3 -m pip install --requirement requirements.txt` if you're on Linux.
3. Then run `python main.py` or `python3 main.py` if you're on linux.
## Building from source
1. Follow steps 1 and 2 from the previous section.
2. Install PyInstaller by running `python pip install pyinstaller` or `python3 -m pip install pyinstaller` if you're on Linux.
3. Run `python pyinstaller --noconsole --onefile --icon=icon.ico main.py` or `python3 pyinstaller --noconsole --onefile --icon=icon.ico main.py` if you're on Linux. (Replace <b> icon.ico </b> with your own icon)
4. Move `config.json` and the .bmp files to the directory.
## Features
* Automatically loads the last used RPC.
## Known Bugs
* Sometimes the RPC doesn't get updated on your local client but it does get updated. (you can check with other devices)
* The enable time check box doesn't work
## To-Do List
- [x] Make a functioning enable time check box
- [ ] Minimize to tray feature 
- [ ] Add presets
