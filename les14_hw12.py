'''lesson_1_4 homework «Функции — использование встроенных и создание собственных»
'''

#TODO 1:
# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки,
# на котором он будет храниться.

#TODO 2:
# реализовать дополнительные пользовательские команды, которые будут выполнять следующие функции:
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

import math
import csv

cmd_dict = {
    'P':'people',
    'L':'list',
    'S':'shelf',
    'A':'add',
    'D':'delete',
    'M': 'move',
    'AS': 'add shelf',
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
# countries = {
#     'Tailand': {'sea':True,
#                 'shengen': False,
#                 'aver_temp': 30,
#                 'currensy_rate': 1.8},
#     'Hungary': {'sea': False,
#                 'shengen': True,
#                 'aver_temp': 10,
#                 'currensy_rate': 0.3},
#     'Germany': {'sea': True,
#                 'shengen': True,
#                 'aver_temp': 5,
#                 'currensy_rate': 80},
#     'Japan': {'sea': True,
#                 'shengen': False,
#                 'aver_temp': 21,
#                 'currensy_rate': 0.61},
#     'Russia': {'sea': True,
#               'shengen': False,
#               'aver_temp': 6,
#               'currensy_rate': 1}
# }
def people_cmd(doc_lst):
    print('Pls enter document number')
    doc_num=input()
    s=0
    for d in doc_lst:
        if d['number'] == doc_num:
            print(d['name'])
            s+=1
    print('Found {0} people(s)'.format(s))
    return 0
def list_cmd(doc_lst):
    for p in doc_lst:
        print('{0} "{1}" "{2}"'.format(p['type'],p['number'],p['name']))
        # print(''p['type'])
    return 0
def shelf_cmd(doc_lst):
    print('Pls enter document number')
    doc_num=input()
    # doc_num='10006'
    s=0
    ss=list()
    for si in doc_lst:
        ss=doc_lst[si]
        # print('doc_num= ',doc_num)
        # print(type(ss),'ss= ',ss)
        if doc_num in ss:
            print('Have found  the document {0} in Directories #{1}'.format(doc_num,si))
            s+=1
    print('Found {0} Directories'.format(s))
    return 0
def add_cmd(doc_lst):
    print('add_cmd')
    return 0
def del_cmd(doc_lst):
    print('delete_cmd')
    return 0
def move_cmd(doc_lst):
    print('move_cmd')
    return 0
def add_shelf_cmd(doc_lst):
    print('add_shelf_cmd')
    return 0

def get_cmd(dict):
    while True:
        print('Pls enter user command and press "Enter"(command q for Exit):')
        n1=input().upper()
        if n1.isalpha():
            # print('+++++++')
            if n1 in dict:
                return n1
            elif n1 == 'H':
                print('p – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
                print('l – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин"')
                print('')
                print('')
            else:
                print('You enter wrong command "{0}". Enter "h" for list of command'.format(n1))
                continue
        else:
            print('You enter wrong command "{0}". Enter "h" for list of command'.format(n1))
            continue

def main():
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
        if ucmd == 'A':
            add_cmd(documents)
            continue
        if ucmd == 'D':
            del_cmd(documents)
            continue
        if ucmd == 'M':
            move_cmd(documents)
            continue
        if ucmd == 'AS':
            add_shelf_cmd(documents)
            continue

main()


# def get_warm1(dct, temp=20): # t=20 - значение по умолчанию
#     hot_c = []
#     for country,prop in dct.items():
#         if prop['aver_temp'] > temp:
#             hot_c.append(country)
#     return hot_c
# def input_temp():
#     while True:
#         print('введите температуру и нажмите Enter: ')
#         n1=input()
#         if n1.isdigit():
#             n2=int(n1)
#             return n2
#         else:
#             print('нужно ввести число')
#             continue
# def get_temp():
#     while True:
#         print('введите температуру и нажмите Enter (или введите 0 для выхода): ')
#         n1=input()
#         if n1.isdigit():
#             return n1
#         else:
#             print('нужно ввести число')
#             continue
# def main():
#     while True:
#         temp1=int(get_temp())
#         # n1 = input()
#         if temp1 == 0:
#             print('До свидания ))')
#             return 0
#         c=get_warm1(countries,temp1)
#         print('Warm countries = ', c)
