# qbclip
Win+2 to add a magnet link from your clipboard to qbittorent
Using this program is a lot faster than clicking on the magnet link, setting the download folder, clicking download, and minimizing qbittorrent

An easy program to add magnet links to your qbitttorrent

# Setup
Enable qbittorrent webui like so

![image](https://user-images.githubusercontent.com/47696465/148408354-e44898fa-8659-49ef-ab4f-5f1c28b02aca.png)

Then edit qb.py to include your local ip and the port you set earlier. Drag qb.py to C:\ and make a folder named "qbclip"

In this folder make a file called "conf.txt" and edit it to include the path you would like your torrents to download too...

Example:

```
C:\Users\Admin\Downloads\
```

Then drag the already compiled exe "qb.exe" or compile the project yourself with ```cargo build``` (rustlang)

Its suggested you create a shortcut and set run mode to "minimized" so when you run it a console doesnt pop up 

Then drag the shortcut or exe to your taskbar!
Depending on where you put it will corrispond to WIN + <NUM>
