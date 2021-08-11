import os
import shutil
import time

def main():
    deletedFoldersCount=0
    deletedFilesCount=0
    path=""
    days=30
    seconds=time.time()-(days*24*60*60)

    if os.path.exists(path):
        for rootFolder,folders,files in os.walk(path):
            if seconds>=getFileorFolderAge(rootFolder):
                removeFolder(rootFolder)
                deletedFoldersCount+=1
                break
            else:
                for folder in folders:
                    folderPath=os.path.join(rootFolder,folder)
                    if seconds>=getFileorFolderAge(folderPath):
                        removeFolder(folderPath)
                        deletedFoldersCount+=1
        
        for file in files:
            filePath=os.path.join(rootFolder,file)
            if seconds>=getFileorFolderAge(filePath):
                removeFile(filePath)
                deletedFilesCount+=1
            else:
                if seconds>=getFileorFolderAge(path):
                    removeFile(path)
                    deletedFilesCount+=1
    else:
        print(f"Total Folders Deleted:{deletedFoldersCount}")
        print(f"Total Files Deleted:{deletedFilesCount}")

def removeFolder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete")
    
def removeFile(path):
    if not os.remove(path):
        print(f"{path} is removed successfully")
    else:
        print("Unable to delete")

def getFileorFolderAge(path):
    ctime=os.stat(path).st_ctime
    return ctime

main()