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


def Get_files(path):
    file_list = []

    for file in os.listdir(path):
        if file.endswith(".md"):
            file_list.append([f"{path}]/",file])
    return file_list

def Match_files(path_source, path_target):
    source = Get_files(path_source)
    target = Get_files(path_target)

    print(source[1][1])

    # set(target[]).intersection(source[])

    # for file in target:

Match_files("/Users/philipp/Desktop/NCT_obs_renamed_restored","/Volumes/GoogleDrive/My Drive/NCT/NCT_obsidian")        

# print("desktop")
# print(Get_files("/Users/philipp/Desktop/NCT_obs_renamed_restored"))
# print("---")
# print(Get_files("/Volumes/GoogleDrive/My Drive/NCT/NCT_obsidian"))


    