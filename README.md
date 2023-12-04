# Win-Win WindowsTools
## Lock your Windows (like: WINDOWS + L) when hovering at the bottom left of the screen.
### How to start
You need Python installed.
You need to install the dependencies:
```
pip install pyautogui pystray Pillow
```
You need the python file, donwload the .zip file.
Double click on start.bat
This opens a cmd window, which I personally do not like, so i made two 'start-hidden.blabla' files which starts the programm hidden.
#### .vbs (visual basic script)
My Antivirus does not like .vbs, so i made a .ps1 version.
#### .ps1 (powershell)
Right click, then 'run with powershell'.
### Does it auto start?
No, you have to start the script everytime you reboot windows.
Or move the file to one of your autostart folders:
#### User:
```
C:\Users\<YourUsername>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
#### System:
```
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```
### Ok cool but, Why?
My friend has a Mac Book, with that specific functionality, so i decided to convert the idea into windows.
### Can it do more?
No, I could add more things to it later, for example the ability to choose your own action. (probably not)
### How do I close it?
Right-click the ugly black-blue icon in your system tray (arrow at bottom right), then click exit