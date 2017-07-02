'''lesson_2_5 homework «Вызов других программ»
convert input.jpg -resize 200 output.jpg
# with open('recipes.txt', encoding='cp1251') as f:
#     text=f.read()
    # print(text)

'''
import copy
import os
import sys
import subprocess
import shutil
import time


def printerr(arg_str):
    print(arg_str, file=sys.stderr)


def make_new_dir(name_str):
    file_list = os.listdir()
    for file_str in file_list:
        if file_str == name_str:
            if os.path.isdir(file_str):
                return 0
            else:
                # printerr('Founded file Result, not dir')
                continue
        else:
            continue
    if find_dir(name_str) == 0:
        # print('Already exist', name_str)
    else:
        # print('Make =', name_str)
        os.mkdir(os.path.normpath(name_str))
    return 0


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


def copy_dir_to_dir(arg_source_dir, arg_dest_dir):
    start_dir = os.path.normpath(os.path.abspath(os.getcwd()))
    dest_dir_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), arg_dest_dir)))
    source_dir_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), arg_source_dir)))

    os.chdir(arg_source_dir)
    file_list = os.listdir()
    os.chdir(start_dir)

    for file_name in file_list:
        src_file = os.path.normpath(os.path.join(source_dir_path, file_name))
        # print('from =', src_file)
        dest_file = os.path.normpath(os.path.join(dest_dir_path, file_name))
        # print('to = ', dest_file)
        shutil.copyfile(src_file, dest_file)

    os.chdir(start_dir)
    return file_list, dest_dir_path


def main():
    source_dir = 'Source'
    tmp_dir = 'Tmp'
    destination_dir = 'Result'

    start_current_dir = os.path.abspath(os.getcwd())

    if find_dir(source_dir) == 1:
        print('Source dir not found')
        exit(1)

    make_new_dir(tmp_dir)

    file_list, source_dir_path = copy_dir_to_dir(source_dir, tmp_dir)

    destination_dir_path = os.path.normpath(os.path.abspath(os.path.join(os.getcwd(), destination_dir)))

    for file_name in file_list:
        src_file = os.path.normpath(os.path.join(source_dir_path, file_name))
        dest_file = os.path.normpath(os.path.join(destination_dir_path, file_name))
        # print('src_file =', src_file)
        # print('dest_file =', dest_file)

        resize = subprocess.run('convert {} -resize 200 {}'.format(src_file, dest_file))
        os.remove(src_file) # удаляю использованный временный исходный файл

    os.chdir(start_current_dir)
    # input('to delete DIR')
    os.rmdir(tmp_dir) # удаляю использованный временный исходный каталог

    exit(0)


#################################################################################################
if __name__ == '__main__':
    main()


