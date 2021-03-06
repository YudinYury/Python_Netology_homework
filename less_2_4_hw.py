'''lesson_2_4 homework «Работа с папками, путями»
Задача №1
Нужные для работы файлы и заготовка кода находятся на GitHub.
Представьте, что вам нужно отыскать файл в формате sql среди десятков других, при этом вы знаете некоторые части этого
файла (на память или из другого источника).
Программа ожидает строку, которую будет искать (input()).
После того, как строка введена, программа ищет её во всех файлах, выводит имена найденных файлов построчно и выводит
количество найденных файлов.
Программа снова ожидает ввод, но теперь поиск происходит только среди отобранных на предыдущем этапе файлов.
Программа снова ожидает ввод.
...
Выход из программы программировать не нужно. Достаточно принудительно ее останавливать, для этого можно нажать Ctrl + C.
Для получения списка всех файлов используйте стандартные функции из os и os.path.
Пример на настоящих данных:

      python3 find_procedure.py
      Введите строку: INSERT
      ... большой список файлов ...
      Всего: 301
      Введите строку: APPLICATION_SETUP
      ... большой список файлов ...
      Всего: 26
      Введите строку: A400M
      ... большой список файлов ...
      Всего: 17
      Введите строку: 0.0
      Migrations/000_PSE_Application_setup.sql
      Migrations/100_1-32_PSE_Application_setup.sql
      Всего: 2
      Введите строку: 2.0
      Migrations/000_PSE_Application_setup.sql
      Всего: 1
Не забываем организовывать собственный код в функции.
Задача №2. Дополнительная (не обязательная)
Генерировать абсолютный путь до папки с миграциями. Скрипт при этом лежит в одной папке с папкой 'Migrations', но запускать мы его можем из любой директории - он будет работать корректно.
'''

import copy
import os
import os.path
from pprint import pprint
import re


# ищет целевой каталог и возвращает: путь к целевому каталогу, список фалов нужного типа
def find_dir(name_target_path_str, type_of_file_str):
    target_path_str = ''
    target_path_list = []
    file_list = []

    start_current_dir = os.path.abspath(os.getcwd())

    migration_dir_list = []
    while not migration_dir_list:
        file_list = os.listdir()
        migration_dir_list = [i for i in file_list if i == name_target_path_str]
        if migration_dir_list:
            break
        else:
            os.chdir(os.path.dirname(os.getcwd()))
            continue

    for dir_s in migration_dir_list:
        if os.path.isdir(dir_s):
            migration_dir_str = dir_s
            break
        else:
            continue

    os.chdir(migration_dir_str)
    work_dir = os.getcwd()
    work_dir = os.path.normcase(work_dir)
    work_dir = os.path.normpath(work_dir)
    target_path_str = os.path.realpath(work_dir)

    file_list = os.listdir()
    file_list = [i for i in file_list if i[-4:] == type_of_file_str]

    os.chdir(start_current_dir)

    return target_path_str, file_list



# ищет в файле нужную строку и возвращает:
# если нашел - True
# если НЕ нашел - False
def search_str_in_file(file_name, search_str):
    with open(os.path.join(file_name)) as f:
        read_str = f.read()
        if search_str in read_str:
            return True

    return False


def main():
    work_dir = []
    start_current_dir = os.path.abspath(os.getcwd())
    print('current_dir in start moment=', start_current_dir)

    migration_dir_str, sql_file_list = find_dir('Migrations', '.sql')

    while True:
        print('Введите строку для поиска:')
        search_str = input()
        # search_str = 'INSERT'
        # search_str = 'APPLICATION_SETUP'

        file_founded_list = []
        count = 0
        file_founded_list = []
        for file_name in sql_file_list:
            if search_str_in_file(os.path.join(migration_dir_str, file_name), search_str):
                count += 1
                file_founded_list.append(file_name)
            else:
                continue

        sql_file_list = copy.deepcopy(file_founded_list)

        if count > 10:
            print('большой список файлов...')
        else:
            for f_name in file_founded_list:
                print(f_name)
        print('Всего:', count)




if __name__ == '__main__':
    main()


