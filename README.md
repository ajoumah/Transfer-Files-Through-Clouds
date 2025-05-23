# Transfer Files Through Clouds

This Python module provides a simple way to **download files from cloud URLs (e.g., Google Drive)** and **manage file transfers and extractions** within cloud storage environments, such as Google Drive mounted in Google Colab.

---

## Overview

The `TransferFiles` script performs the following tasks:

- Downloads a file from a specified cloud URL using HTTP streaming to avoid memory overload.
- Saves the downloaded file to a target directory in the cloud storage.
- Extracts ZIP archives to a specified folder.
- Copies files and directories between different locations within the cloud storage.

This script is particularly useful for:

- Automated dataset preparation.
- Managing large file transfers in cloud-based machine learning workflows.
- Organizing datasets and assets in Google Drive or similar environments.

---

## Code Highlights

- Uses the `requests` library for efficient file downloading with stream support.
- Utilizes shell commands (`unzip`) to extract compressed datasets.
- Employs Python's `shutil.copyfile` and `distutils.dir_util.copy_tree` for copying files and directories.

---

## Usage Example

```python
import requests
from shutil import copyfile
from distutils.dir_util import copy_tree

# Download a file from Google Drive (replace with your own URL)
file_url = "Path"

r = requests.get(file_url, stream=True)

with open("Path/aclImdb.zip", "wb") as file:
    for block in r.iter_content(chunk_size=1024):
        if block:
            file.write(block)

# Unzip the downloaded file into a directory
!unzip "Path/Multi_Label_dataset.zip" -d "/content/drive/MyDrive/UnMulti/"

# Copy a single file from source to destination
copyfile("Path/coco_Dataset", "Path/MS_COCO")

# Copy all contents from one directory to another
copy_tree("Path/Video2images", "Path/Video_Images")
