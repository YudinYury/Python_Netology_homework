'''lesson_2_5 homework «Вызов других программ»
convert input.jpg -resize 200 output.jpg
# with open('recipes.txt', encoding='cp1251') as f:
#     text=f.read()
    # print(text)

'''

import os
import sys
import subprocess
import shutil
import time


def printerr(arg_str):
    print(arg_str, file=sys.stderr)


def find_dir(dir_name):
    file_list = os.listdir()
    for file_str in file_list:
        if file_str == dir_name:
            if os.path.isdir(file_str):
                return 0
            else:
                continue
        else:
            continue
    return 1


def make_new_dir(name_str):
    file_list = os.listdir()

    for file_str in file_list:
        if file_str == name_str:
            if os.path.isdir(file_str):
                return 0
            else:
                printerr('Founded file Result, not dir')
                continue
        else:
            continue
    if find_dir(name_str) == 0:
        pass
    else:
        os.mkdir(os.path.normpath(name_str))
    return 0



def get_file_list(arg_source_dir):
    start_dir = os.path.normpath(os.path.abspath(os.getcwd()))
    os.chdir(arg_source_dir)
    file_list = os.listdir()
    os.chdir(start_dir)
    return file_list



def main():
    source_dir = 'Source'
    destination_dir = 'Result'

    start_current_dir = os.path.abspath(os.getcwd())

    if find_dir(source_dir) == 1:
        print('Source dir not found')
        exit(1)

    file_list = get_file_list(source_dir)
    make_new_dir(destination_dir)
    source_dir_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), source_dir)))
    destination_dir_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), destination_dir)))

    for file_name in file_list:
        src_file = os.path.normpath(os.path.join(source_dir_path, file_name))
        dest_file = os.path.normpath(os.path.join(destination_dir_path, file_name))
        resize = subprocess.run('convert {} -resize 200 {}'.format(src_file, dest_file))

    os.chdir(start_current_dir)
    # input('to delete DIR')

    exit(0)


#################################################################################################
if __name__ == '__main__':
    main()


