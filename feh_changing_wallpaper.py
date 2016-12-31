import os
import time
import subprocess

# After a certain timeout, call feh and change the wallpaper

timeout_sec = 300
user_dir = os.path.expanduser("~") + "/"
source_dir = user_dir + "Pictures/bg/"

# get a list of filenames
imglist = os.listdir(source_dir)

while(1>0):
    for filename in imglist:
        subprocess.run(["feh", "--bg-max", source_dir + filename])
        time.sleep(timeout_sec)
