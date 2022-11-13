import sys
import os
import shutil
from datetime import datetime

def build_save_path(save_folder_path, save_file_name):
    save_file = save_folder_path
    if save_file.endswith("/") == False:
        save_file += "/"
    return save_file + save_file_name

def main(args):
    character_name = args[0]

    home_directory = os.path.expanduser('~')
    save_folder_path = f"{home_directory}/Documents/My Games/Oblivion/Saves"
    if len(args) > 1:
        save_folder_path = args[1]

    save_file_names = [f for f in os.listdir(save_folder_path) if character_name in f]
    
    if len(save_file_names) > 1:
        print(f"Found more than one character matching name {character_name}.")
        exit(1)
    if len(save_file_names) == 0:
        print(f"Could not find save file with character name {character_name}.")
        exit(1)

    save_path = build_save_path(save_folder_path, save_file_names[0])
    present_working_directory = os.path.abspath(os.getcwd())
    git_save_path = os.path.join(present_working_directory, "..", "saves")
    shutil.copy2(save_path, git_save_path)

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    os.system("git add ../saves/.")
    os.system(f"git commit -m \"{character_name} - {dt_string}\"")
    os.system("git push")

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)