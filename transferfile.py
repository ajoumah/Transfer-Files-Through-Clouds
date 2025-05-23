"""TransferFiles

"""

import requests
file_url = "https://drive.google.com/file/d/1iQV5kKF_KGZL9ALx9MMXk_Lg7PklBLCE/view"

r = requests.get(file_url, stream = True)

with open("/content/drive/MyDrive/multiLabel1/aclImdb.zip", "wb") as file:
    for block in r.iter_content(chunk_size = 1024):
         if block:
             file.write(block)

#!unzip "/content/drive/MyDrive/IMBD1/aclImdb.zip"
!unzip  "/content/drive/MyDrive/Multi_Label_dataset.zip"  -d "/content/drive/MyDrive/UnMulti/"

from shutil import copyfile
copyfile("/content/drive/MyDrive/coco_Dataset", "/content/drive/MyDrive/Wheelchair obstacle detection /Ahmad/MS_COCO")

from distutils.dir_util import copy_tree

# copy subdirectory example
fromDirectory = "/content/drive/MyDrive/Video2images"
toDirectory = "/content/drive/MyDrive/Wheelchair obstacle detection /Ahmad/Video_Images"

copy_tree(fromDirectory, toDirectory)