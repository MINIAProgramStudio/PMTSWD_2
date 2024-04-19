import os
import sys


DEFAULT_TOP_PATH = "\\"

def get_args(recived_input_line):
    file_name = recived_input_line[recived_input_line.find('-f ')+3:recived_input_line.find(';',)]
    top_path = recived_input_line[recived_input_line.find(' ')+1:]

    if not os.path.isdir(top_path):
        sys.stderr.write("ERR_GA_1: No such directory")
        return -1
    return [file_name, top_path]

def find_file(name, top_path=DEFAULT_TOP_PATH):
    return_list = []
    for root, dirs, files in os.walk(top_path):
        if name in files:
            return_list.append(os.path.join(root, name))
    if len(return_list) > 0:
        return return_list
    else:
        sys.stderr.write("ERR_FF_1: No such file in the directory")
        return -1  # no such file(-s) in the directory

def find_file_from_stdin():
    args = get_args_from_lines(get_lines_from_stdin())
    return find_file(args[0],args[1])

# main loop
while True:
    for line in sys.stdin:
        if 'Exit' == line.rstrip():
            break
        args = get_args(line.rstrip())
        if isinstance(args,list):
            file_list = find_file(args[0],args[1])
            for file in file_list:
                sys.stdout.write(file)
        else:
            sys.stderr.write("ERR_MAIN_1: Arg check failed")
            continue

sys.exit()