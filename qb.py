import clipboard
from pathlib import Path
from qbittorrent import Client
dlpath_file = Path("C:\\qbclip\\conf.txt\\")  
if dlpath_file.is_file():
    with open(dlpath_file, "r") as f:
        dlpath = Path(f.read())
        f.close()
    config = 1
else:
    exit("Config file not found.")
qb = Client('http://127.0.0.1:PORT/')
qb.login('USERNAME', 'PASSWORD')
magnet = clipboard.paste()
if magnet.startswith("magnet:"):
    qb.download_from_link(magnet, savepath=dlpath)
    qb.logout()
else:
    qb.logout()
    exit("No magnet link found in clipboard.")
