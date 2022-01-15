# from main import Get_file_list
import os

def Get_file_list(vault_path):
    '''return list of paths to md files
    in given directory
    '''
    file_list = []
    for root, directories, files in os.walk(vault_path, topdown=False):
        for name in files:
            if name.endswith('.md'):
                file_list.append(os.path.join(root, name))
    return file_list
print("desktop")
print(Get_file_list("/Users/philipp/Desktop/NCT_obs_renamed_restored"))
print("---")
print(Get_file_list("/Volumes/GoogleDrive/My Drive/NCT/NCT_obsidian"))
