'''
MIT License

Copyright (c) 2022 René Descartes Muala

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import os
from sys import argv
from glob import glob

def map_folders(base_path: str)->list[str]:
    return glob(os.path.join(base_path, "*/node_modules/"))

def filter_folder(folders:list[str])->list[str]:
    final_folders : list[str] = []
    for folder in folders:
        if os.path.isdir(folder) and not (folder == "/" or  folder == "."):
            final_folders.append(folder)
    return final_folders

def warn_user(folders:list[str])->bool:
    if len(folders) == 0:
        print("--> No valid folders found.")
        return False
    return str(input(f"Allow nmr to delete the following folders? \n{folders}\nType \"yes\" to confirm: ")) == "yes"

def delete_folders(folders:list[str]):
    for folder in folders:
        if os.system(f"rm -rf {folder}") == 0:
            print(f"- {folder}: deleted")
        else:
            print(f"- {folder}: failed")

if __name__ == "__main__":
    if len(argv) == 1:
        print("--> Error: Provide a base folder")
        exit(0)
    for arg in argv[1:]:
        folder_list = map_folders(arg)
        folder_list = filter_folder(folder_list)
        if(warn_user(folder_list)):
            delete_folders(folder_list)
            print(f"--> {len(folder_list)} node_modules deleted.")
        else:
            print("--> Nothing done.")
