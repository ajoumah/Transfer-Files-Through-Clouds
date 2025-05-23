"""TransferFiles

"""

import requests
file_url = "Path/KF_KGZL9ALx9MMXk_Lg7PklBLCE/view"

r = requests.get(file_url, stream = True)

with open("Path/aclImdb.zip", "wb") as file:
    for block in r.iter_content(chunk_size = 1024):
         if block:
             file.write(block)

#!unzip "Path/aclImdb.zip"
!unzip  "Path/Multi_Label_dataset.zip"  -d "Path/UnMulti/"

from shutil import copyfile
copyfile("Path/coco_Dataset", "Path/MS_COCO")

from distutils.dir_util import copy_tree

# copy subdirectory example
fromDirectory = "Path/Video2images"
toDirectory = "Path/Video_Images"

copy_tree(fromDirectory, toDirectory)
