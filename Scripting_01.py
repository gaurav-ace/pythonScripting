
#first python script

#print('testing python scripting...')


#script for arranging the files of a folder as per extensions of files

# take all files in a folder
# annotate respective category based on the extension

import os
from pathlib import Path
subdirectory = {
    'Videos' : ['.mp4', '.3gp', '.avi', '.mov'],
    'Pictures' : ['.jpg', '.jpeg', '.png'],
    'Documents' : ['.txt', '.pdf', '.docx'],
    'Audio' : ['.m4a', '.m4b', '.mp3']
}

def findFolder(extension):
    for key,values in subdirectory.items():
        for value in values:
            if value == extension:
                return key
    return 'MISC'

#testing the findFolder functionality -
#print(findFolder('.pdf'))

def OrganizeDir():
    for item in os.scandir():
        if item.is_dir():
            continue

        filePath = Path(item)
        #print(filePath)

        #print(filePath.suffix)
        ext = filePath.suffix.lower() #this will give the file extension type
        folder  = findFolder(ext)
        folderPath = Path(folder)
        if folderPath.is_dir() != True:
            folderPath.mkdir()

        filePath.rename(folderPath.joinpath(filePath))    


OrganizeDir()
    