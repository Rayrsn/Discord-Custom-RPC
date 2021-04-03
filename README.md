# Discord-Custom-RPC


![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/Rayrsn/Discord-Custom-RPC?style=for-the-badge)

<p align="center">
  <img width="512" height="512" src="https://rayr.ml/Github/rpclogo.png">
</p>

### <h2 align="center"> <i> <b> A Discord Custom RPC app with GUI </b> </i> </h2>



<br>

# How To Use
## <b> Just head to the [Releases](https://github.com/Rayrsn/Discord-Custom-RPC/releases) tab and download the latest version. </b>


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

## To-Do List
- [ ] Add presets
