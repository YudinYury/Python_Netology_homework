'''lesson_1_4 homework «Функции — использование встроенных и создание собственных»
'''

#TODO 1:
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться.

#TODO 2:
# реализовать дополнительные пользовательские команды, которые будут выполнять следующие функции:
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

import copy
import math
from pprint import pprint

def people_cmd(doc_lst):  # have done
    print('Pls enter document number')
    doc_num=input()
    s=0
    for d in doc_lst:
        if d['number'] == doc_num:
            print(d['name'])
            s+=1
    print('Found {0} people(s)'.format(s))
    return 0

##################################################################################################
def list_cmd(doc_lst):  # have done
    for p in doc_lst:
        print('{0} "{1}" "{2}"'.format(p['type'],p['number'],p['name']))
        # print(''p['type'])
    return 0

##################################################################################################
def shelf_cmd(doc_lst):  # have done
    print('Pls enter document number')
    doc_num=input()
    # doc_num='10006'
    s=0
    ss=list()
    for si in doc_lst:
        ss=doc_lst[si]
        if doc_num in ss:
            print('Have found  the document {0} in Directories #{1}'.format(doc_num,si))
            s+=1
    print('Found {0} Directories'.format(s))
    return 0

##################################################################################################
# def add_shelf_cmd(dir_dict): # have done   as – add shelf – команда, которая спросит номер новой полки (new key) и добавит ее в перечень;
# получим от пользователя номер, а затем добавим его в список ключ:значение всех из словаря dir_dict и вернем этот список
def add_shelf_cmd(dir_dict): # have done   as – add shelf – команда, которая спросит номер новой полки (new key) и добавит ее в перечень;
    # получим от пользователя номер, а затем добавим его в список ключ:значение всех из словаря dir_dict и вернем этот список
    dir_lst_keys=list()
    dir_lst_keys=dir_dict.keys() # get keys of old 'directories'
    new_key=''
    while True: # get new key
        print('Pls enter number of Directories (digit)')
        new_key=input()
        if new_key.isdigit():
            if new_key in dir_lst_keys:
                print('Entered number is already exist')
                continue
            else:
                # print('good new key')
                break
        else:
            print('Enter Key is not digit.')
            continue
    # print('Directore number of new Document', new_key)
    # new_dic.append(new_key)
    # new_dic.append(list())
    # print(new_dic)
    return new_key

##################################################################################################
def get_cmd(dict):
    while True:
        print('Pls enter user command and press "Enter"(command q for Exit):')
        n1=input().upper()
        if n1.isalpha():
            if n1 in dict:
                return n1
            elif n1 == 'H':
                print('p – команда people, которая спросит номер документа и выведет имя человека, которому он принадлежит')
                print('l – команда list, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
                print('s – команда shelf, которая спросит номер документа и выведет номер полки, на которой он находится')
                print('a – команда  add, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца \
и номер полки, на котором он будет храниться')
                print('d – команда delete, которая спросит номер документа и удалит его (документ) из каталога и из перечня полок')
                print('m – команда move, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую')
                print('as – команда add shelf, которая спросит номер новой полки и добавит ее в перечень')
            else:
                print('You enter wrong command "{0}". Enter "h" for list of command'.format(n1))
                continue
        else:
            print('You enter wrong command "{0}". Enter "h" for list of command'.format(n1))
            continue

##################################################################################################
def get_new_dir(dir_dict):  #  получает от пользователя номер новой полки и возвращает string с этим номером
                        # dict - словарь существующих полок
    dir_lst_keys=list()
    dir_lst_keys=dir_dict.keys() # get keys of old 'directories'
    while True: # get new key
        print('Pls enter number of Directories (digit)')
        new_key=input()
        if new_key.isdigit():
            if new_key in dir_lst_keys:
                print('Entered number is already exist')
                continue
            else:
                break
        else:
            print('Enter Key is not digit.')
            continue
    # return '4'
    return new_key

##################################################################################################
# get_dir(): string - получает от пользователя номер полки и возвращает string с этим номером
def get_dir():
    while True:
        print('Pls enter number of destination Directories (digit)')
        new_key = input()
        if new_key.isdigit():
            return new_key
        else:
            print('Enter Key is not digit.')
            continue

##################################################################################################
# получает от пользователя номер документа и возвращает string с этим номером
def get_doc_num():
    while True:
        print('Pls enter document number')
        new=input()
        if new.isalpha():
            print('В номере не должно быть букв','номер = ',new)
            continue
        else:
            break
    return new
    # return '11-2'

##################################################################################################
def get_doc(): # получает от пользователя key:value для нового документ и возвращает list с этими
    new_doc={'type':'', 'number': '', 'name': ''}
    ins=''
    print('Pls enter type of document')
    ins=input()
    new_doc.update({'type':ins})
    ins=get_doc_num()
    new_doc.update({'number':ins})
    print('Pls enter name of document owner')
    ins=input()
    new_doc.update({'name':ins})

    # new_doc={'type':'pass', 'number': '10007', 'name': 'Juri'} # временно
    return new_doc

##################################################################################################
def doc_find_number(doc_list_for_find, number):
    for d in doc_list_for_find:
        if d['number'] == number:
            return True
    return False
##################################################################################################
# add_cmd(documents_list, directories_dict):
#  a – add – команда, которая добавит новый документ в каталог и в перечень полок,
# спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
def add_cmd(documents_list, directories_dict):
    new_doc=dict()
    new_doc = get_doc()
    documents_list.append(new_doc)
    new_dir=''
    new_dir=get_dir()
    dkl=directories_dict.keys()
    if new_dir in dkl:
        # print('такая папка уже есть')
        directories_dict[new_dir].append(new_doc['number'])
    else:
        # print('новая папка')
        directories_dict[new_dir] = []
        directories_dict[new_dir].append(new_doc['number'])
    # print('directories = ',directories_dict)
    return documents_list, directories_dict

##################################################################################################
# del_cmd(documents_list, directories_dict):
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
def del_cmd(documents_list, directories_dict):
    doc_num = get_doc_num()
    if doc_find_number(documents_list, doc_num):
        for dd in directories_dict:
            # print(type(directories[d]), 'directories[d] = ', directories[d])
            if doc_num in directories_dict[dd]:
                directories_dict[dd].remove(doc_num)
                break
        if len(directories_dict[dd]) == 0:
            print('Directories "{}" is empty ... will be deleted.'.format(dd))
            del directories_dict[dd]
        else:
            print('Document number {} not found'.format(doc_num))

        for dl in documents_list:
            if dl['number'] == doc_num:
                documents_list.remove(dl)
    else:
        return documents_list, directories_dict

    return documents_list, directories_dict

##################################################################################################
# def move_cmd(documents_list, directories_dict):
# move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
def move_cmd(documents_list, directories_dict):
    new_directories_dict = {}
    tmp_dict = dict()
    doc_num = get_doc_num()

    if doc_find_number(documents_list, doc_num):
        # d_moved = dict()
        for di in directories_dict:  # удаляем документ с полки
            if doc_num in directories_dict[di]:
                directories_dict[di].remove(doc_num)

        dir_num = get_dir()
        old_value = directories_dict.setdefault(dir_num, [])
        old_value.append(doc_num)
        directories_dict.update({dir_num: old_value})
    else:
        print('Document number {} not found'.format(doc_num))
        return directories_dict

    return directories_dict

##################################################################################################
def main():
    cmd_dict = {
        'P': 'people',  # have done
        'L': 'list',  # have done
        'S': 'shelf',  # have done
        'A': 'add',  # have done
        'D': 'delete',
        'M': 'move',
        'AS': 'add shelf',  # have done
        'Q': 'quit'
    }
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
    }

    while True:
        ucmd=get_cmd(cmd_dict)
        if ucmd == 'Q':
                print('Bye ... ))')
                exit(0)
        if ucmd == 'P':
            people_cmd(documents)
            continue

        if ucmd == 'L':
            list_cmd(documents)
            continue

        if ucmd == 'S':
            shelf_cmd(directories)
            continue

        if ucmd == 'A': # add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
            # и вернет новый каталог документов
            documents, directories = add_cmd(documents, directories)
            continue

        if ucmd == 'D': # d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
            documents, directories = del_cmd(documents, directories)

        if ucmd == 'M': # move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
            directories = move_cmd(documents, directories)
            continue

        if ucmd == 'AS':
            # new_d=add_shelf_cmd(directories)  # получаю новый номер полки
            new_d=get_new_dir(directories) # получаю новый номер полки
            directories[new_d]=list() # присвоение по новому ключу (новому номеру) расширяет словарь
            # print('new directories = ', directories)
            continue

# I read https://habrahabr.ru/post/180509/ and use it
if __name__ == '__main__':
    main()

