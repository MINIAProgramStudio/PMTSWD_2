import os
import sys

def find_file(name, top_path="C:\\"):
    for root, dirs, files in os.walk(top_path):
        if name in files:
            return os.path.join(root, name)
        else:
            return -1

print(find_file("1.txt"))

sys.exit()