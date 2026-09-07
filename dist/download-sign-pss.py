#!/usr/bin/python3

import os
import platform
import requests
import subprocess
import sys

INSTALL_LOCATION = "sign_pss"

def download_unix(url):
    print("Downloading: "+url)
    open(INSTALL_LOCATION, "wb").write(requests.get(url).content)
    os.chmod(INSTALL_LOCATION, stat.S_IXGRP)
    os.chmod(INSTALL_LOCATION, stat.S_IXUSR)
    os.chmod(INSTALL_LOCATION, stat.S_IXOTH)

def download_windows(url):
    print("Downloading: "+url)
    open(INSTALL_LOCATION+".exe", "wb").write(requests.get(url).content)

if platform.system() == "Windows":
    download_windows("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_win64.exe")
elif platform.system == "Linux":
    download_unix("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_linux64")
elif platform.system() == "Darwin":
    download_unix("https://github.com/OpenPSS/sign_pss/releases/latest/download/sign_pss_mac64")


cmd = [INSTALL_LOCATION]
cmd += sys.argv[1:]

print("Running: "+ " ".join(cmd))
subprocess.run(cmd)