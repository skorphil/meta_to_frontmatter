
import os
import datetime as dt

def Main(vault_path):
    files = Get_file_list(vault_path)

    for path in files:
        Write_frontmatter_to_file(path, Meta_to_frontmatter(path))

    print(f"{len(files)} files saved")


def Meta_to_frontmatter(path):
    '''Return frontmatter header from created and modified dates
    of given file'''
    return f'''---
created: {Get_creation_time(path)}
updated: {Get_modified_time(path)}
---
'''


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

    # https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times


def Write_frontmatter_to_file(path, frontmatter):
    '''write given frontmatter to beginning of given file
    '''
    with open(path,'r') as contents:
        data_from_file = contents.read()
    with open(path,'w') as contents:
        contents.write(frontmatter)
    with open(path,'a') as contents:
        contents.write(data_from_file)

    # https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file


def Get_creation_time(path):
    return dt.datetime.fromtimestamp(os.stat(path).st_birthtime).strftime("%Y-%m-%d %H:%M")


def Get_modified_time(path):
    return dt.datetime.fromtimestamp(os.path.getmtime(path)).strftime("%Y-%m-%d %H:%M")


Main("/Users/philipp/Library/Mobile Documents/iCloud~md~obsidian/Documents/Obsidian_vault")


# --- References ---
# https://stackoverflow.com/questions/946967/get-file-creation-time-with-python-on-mac
# https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times

