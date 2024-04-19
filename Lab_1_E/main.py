import os
import sys

def find_file(name, top_path="\\"):
    return_list = []
    for root, dirs, files in os.walk(top_path):
        if name in files:
            return_list.append(os.path.join(root, name))
    if len(return_list)>0:
        return return_list
    else:
        return -1 #no such file(-s) in the directory

print(find_file("1.txt"))

sys.exit()