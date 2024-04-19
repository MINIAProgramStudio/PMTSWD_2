import os
import sys


def get_lines_from_stdin():
    recived_lines = []
    for line in sys.stdin:
        if line.rstrip in ['exit', 'Exit']:
            sys.exit()
        else:
            recived_lines.append(line)
    return recived_lines


def find_file(name, top_path="\\"):
    return_list = []
    for root, dirs, files in os.walk(top_path):
        if name in files:
            return_list.append(os.path.join(root, name))
    if len(return_list) > 0:
        return return_list
    else:
        return -1  # no such file(-s) in the directory


print(find_file("1.txt"))

sys.exit()
