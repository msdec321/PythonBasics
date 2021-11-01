#! python3

#This is the backup folder script. This script will compress a specified folder
#  as a backup. The filename of the zip should increment _+1 each time it's created.

import shutil, zipfile, os, sys
from pathlib import Path

def zipper(myFile):

    i=1
    while True:

        zipFile = str(myFile) + '_' + str(i)
        if zipFile in os.listdir('./'):
            i+=1
            continue
        else:
            shutil.copy(myFile, zipFile)
            newZip = zipfile.ZipFile(zipFile, 'w')
            newZip.write(zipFile, compress_type=zipfile.ZIP_DEFLATED)
            newZip.close()
            break


p=Path('./')

if len(sys.argv)!=2:
    print('Error: Please specify a file to backup.')

else:
    zipper(sys.argv[1])
