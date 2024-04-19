import os
import sys



DEFAULT_TOP_PATH = "С:\\"

def get_args(recived_input_line):
    global DEFAULT_TOP_PATH
    minus_f = recived_input_line.find('-f ')
    minus_p = recived_input_line.find('-p ')
    minus_d = recived_input_line.find('-d ')

    if not minus_f == -1:
        file_name = recived_input_line[minus_f+3:recived_input_line.find(';',minus_f)]
    else:
        file_name = recived_input_line
        top_path = DEFAULT_TOP_PATH

    if not minus_p == -1:
        top_path = recived_input_line[minus_p+3:recived_input_line.find(';',minus_p)]
    else:
        top_path = DEFAULT_TOP_PATH

    if not minus_d == -1:
        new_default_top_path = recived_input_line[minus_d+3:recived_input_line.find(';',minus_d)]
        if not os.path.isdir(new_default_top_path):
            sys.stderr.write("ERR_GA_1: New DEFAULT_TOP_PATH is not a valid path")
            sys.exit(-1)
        else:
            DEFAULT_TOP_PATH = new_default_top_path
    return [file_name,top_path]

def find_file(name, top_path=DEFAULT_TOP_PATH):
    return_list = []
    for root, dirs, files in os.walk(top_path):
        if name in files:
            return_list.append(os.path.join(root, name))
    if len(return_list) > 0:
        return return_list
    else:
        sys.stderr.write("ERR_FF_1: No such file in the directory")
        sys.exit(-1)

def find_file_from_stdin():
    args = get_args_from_lines(get_lines_from_stdin())
    return find_file(args[0],args[1])

# main loop
while True:
    line = input()
    if 'Exit' == line.rstrip():
        break
    args = get_args(line.rstrip())
    if isinstance(args,list):
        file_list = find_file(args[0],args[1])
        if isinstance(file_list,list):
            for file in file_list:
                print(file)
        else:
            sys.stderr.write("ERR_Main_2: No files found")
            sys.exit(-2)
    else:
        sys.stderr.write("ERR_Main_1: Arguments check failed")
        sys.exit(-1)

sys.exit()