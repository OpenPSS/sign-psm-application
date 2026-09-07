#!/usr/bin/python3

import os
import platform
import requests
import subprocess
import sys
import stat

INSTALL_LOCATION = "sign_pss"


def download_unix(url):
    print("Downloading: "+url)
    open(INSTALL_LOCATION, "wb").write(requests.get(url).content)
    st = os.stat(INSTALL_LOCATION)
    os.chmod(INSTALL_LOCATION, st.st_mode | stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH )

def download_windows(url):
    print("Downloading: "+url)
    open(INSTALL_LOCATION, "wb").write(requests.get(url).content)

if platform.system() == "Windows":
    INSTALL_LOCATION += ".exe"
    download_windows("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_win64.exe")
elif platform.system() == "Linux":
    INSTALL_LOCATION = "./"+INSTALL_LOCATION
    download_unix("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_linux64")
elif platform.system() == "Darwin":
    INSTALL_LOCATION = "./"+INSTALL_LOCATION
    download_unix("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_mac64")
else:
    print("Unknown platform: "+platform.system())
    sys.exit(-1)

cmd = [INSTALL_LOCATION]
cmd += sys.argv[1:]

print("Running: "+ " ".join(cmd))
sys.exit(subprocess.run(cmd).returncode)