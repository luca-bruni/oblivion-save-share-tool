import os
import sys
import time
from config_parser import ConfigManager
from save_script import save

def listSimpleFilesInDirectory(dir, character_name):
    relevantSaveFiles = {}

    for file in os.listdir(dir):
        filename = os.fsdecode(file)
        if filename.endswith(".ess") and (' ' + character_name + ' ') in filename:
            relevantSaveFiles[filename] = os.path.getmtime(os.path.join(dir, filename))
    
    return relevantSaveFiles

def getNewFiles(prevFileDict, curFileDict):
    newFiles = {k:v for k,v in curFileDict.items() if k not in prevFileDict}
    return(newFiles)

def main(args):
    config_manager = ConfigManager()
    config_object = config_manager.get_config()
    character_name = config_object.character_name
    save_folder_path = os.path.normpath(config_object.oblivion_directory)
    poll_time = 5

    while True:
        if 'watching' not in locals(): # First time watch
            watching = True
            prevFileList = listSimpleFilesInDirectory(save_folder_path, character_name)
            print(prevFileList)
            if len(prevFileList) > 1:
                print(f"Multiple saves with character name \"{character_name}\" under game save directory.")
                exit(1)

        time.sleep(poll_time)

        curFileList = listSimpleFilesInDirectory(save_folder_path, character_name)
        print(curFileList)
        if len(curFileList) > 1:
                print(f"Multiple saves with character name \"{character_name}\" under game save directory.")
                exit(1)
        if curFileList == prevFileList: continue

        newFiles = getNewFiles(prevFileList, curFileList)

        if len(newFiles) > 1: # Multiple saves with same name as character_name were added
            print(f"Multiple saves with character name \"{character_name}\" under game save directory.")
            exit(1)
        print("saving")
        save(character_name, save_folder_path)

        prevFileList = curFileList

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)