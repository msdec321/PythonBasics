#! python3

#This is a tutorial on file organization.
#The shutil (shell utilities) module allows you to copy, move, rename, and delete files.
import shutil

#To copy a file/directory (source, destination)
shutil.copy('text.txt', '..')   #(Can rename in the destination)
#To copy an entire directory, use shutil.copytree()
#To move, use shutil.move()  - Remember to specify file extensions (.py, .txt, etc)

#To delete a single file or single empty folder, use the os module.
#os.unlink(path)
#os.rmdir(path)

#To delete a folder and all files inside, use the shutil module.
#shutil.rmtree(path)

#BEWARE this -permanently- deletes files irreversibly.
#To safely (reversibly) delete files, use the "send2trash" module.
import send2trash
#newFile = open("newFile.txt", 'w')
#newFile.write("Bacon is not a vegetable.")
#newFile.close()
#send2trash.send2trash('newFile.txt')

#Walking a tree (recursive renaming)
import os

for folderName, subfolders, filenames in os.walk('./'):
    print(f'The current folder is: {folderName}')

    for subfolder in subfolders:
        print(f'Subfolder of {folderName}: {subfolder}')

    for filename in filenames:
        print(f'Filename in {folderName}: {filename}')

    print('')


#To compress files, use the "zipfile" module
import zipfile

#Compressing to zip
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('text.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

#Extracting zips
exampleZip = zipfile.ZipFile('new.zip') #To add to a zip, use (,a) argument
exampleZip.extractall()
exampleZip.close()
