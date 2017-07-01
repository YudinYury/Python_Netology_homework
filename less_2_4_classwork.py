'''lesson_2_4 classwork «Работа с папками, путями»
'''

import copy
import os
from pprint import pprint

##################################################################################################
current_dir = os.getcwd()
print(current_dir)
# pprint(os.listdir())

# print(os.path.join(*['some', 'directory', 'path']))
# print(__file__)

print(os.path.join('some', 'directory', 'path'))
os_path = ['some', 'directory', 'path']
print(os.path.join(*os_path))

# os.chdir('hey')
# print(os.getcwd())
# print('{}'.format(os.listdir('.')))

# os.chdir('ho')
# print(os.getcwd())
# print('{}'.format(os.listdir('.')))

os_path = ['D:','Python_my', 'Python_netology_homework', 'Python_course', 'PY1_Lesson_2.3']
f_name = 'recipes.txt'
full_path = os.path.join(*os_path, f_name)
print(type(full_path), full_path)

print(os.path.dirname('less_2_4_classwork.py'))  # и тут печатается пустая строка, т.к. мы уже в текущем каталоге
print(os.path.abspath(os.path.dirname('less_2_4_classwork.py')))

# setup_py = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setup.py')
# берем папку файла, поднимаемся на папку выше и добавляем в путь имя нового файла setup.py

f_name = 'less_2_4_classwork.py'
p_path = os.path.dirname(os.path.abspath(f_name))
print(type(p_path), 'os_path =', p_path)
os_path = p_path.split('\\')
print(type(os_path), 'os_path =', os_path)
full_path = os.path.join(*os_path, f_name)
print('full_path =', full_path)
print(os.path.exists(f_name))
print(os.path.exists(full_path))

migrations_file_path = 'https://github.com/netology-code/Python_course/blob/master/homework/2.3-paths/Migrations/000_1-28_Create_user_grant_rights_A350.sql'
migrations_path = 'https://github.com/netology-code/Python_course/tree/master/homework/2.3-paths/Migrations'
print(os.path.dirname(migrations_file_path))
print(os.path.exists(migrations_file_path))

#
# migrations_github_path = 'https://github.com/netology-code/Python_course/blob/master/homework/2.3-paths/Migrations/000_1-28_Create_user_grant_rights_A350.sql'
# migrations_path_str = 'D:\Python_my\Python_Netology_homework\Python_course\homework\2.3-paths\Migrations'
# os_path = ['D:','Python_my', 'Python_netology_homework', 'Python_course', 'PY1_Lesson_2.3']
# work_dir = []
# # migrations_file_path_list = migrations_file_path_str
#
#
# os.chdir(os.path.normpath(migrations_path_str))
# print('current_dir =', os.getcwd())
# pprint(os.listdir())
#
# print(os.path.abspath(migrations_path_str))
#
# os.path.abspath(migrations_path_str)

# print(os.path.join(*['some', 'directory', 'path']))
# print(__file__)

# os.chdir('hey')
# print(os.getcwd())
# print('{}'.format(os.listdir('.')))

# os.chdir('ho')
# print(os.getcwd())
# print('{}'.format(os.listdir('.')))

##################################################################################################
# def main():
#################################################################################################
# if __name__ == '__main__':
#     main()


