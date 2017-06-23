'''lesson_2_2 homework «Работа с разными форматами данных»
Прочитать JSON/YAML файл и вывести список покупок
решение задач с HackerRank
'''

#TODO 1:
# Прочитать JSON/YAML файл и вывести список покупок

#TODO 2:
############################################################################################################

import json
import yaml
from xml.etree import ElementTree as ET
# from xml.dom
import csv
from pprint import pprint
import copy

#############################################################################################################
# возвращает словарь с рецептами блюд
def get_cook_book_from_txt_file(file_name):
    cook_bk={}
    one_ing_list={'ingridient_name': '', 'quantity': 0, 'measure': ''}
    one_ing_list_to_add={}
    with open('recipes.txt') as f:
        for l in f:
            culinary_name=l.strip()
            if culinary_name in cook_bk:
                continue
            else:
                cook_bk[culinary_name]=[]
            quant=int(f.readline())
            for i in range(quant):
                ing_list=f.readline().strip().split('|')
                ing_list = list(map(str.strip, ing_list))
                one_ing_list['ingridient_name']=ing_list[0]
                one_ing_list['quantity']=int(ing_list[1])
                one_ing_list['measure']=ing_list[2]
                one_ing_list_to_add=copy.deepcopy(one_ing_list)
                cook_bk[culinary_name].append(one_ing_list_to_add)

    return cook_bk
#############################################################################################################
# возвращает словарь с рецептами блюд
def get_cook_book_from_json_file(file_name):
    cook_bk={}
    one_ing_list={'ingridient_name': '', 'quantity': 0, 'measure': ''}
    one_ing_list_to_add={}

    with open(file_name) as f:
        cook_bk = json.load(f)
        # for l in f:
        #     culinary_name=l.strip()

    return cook_bk

#############################################################################################################
#
def get_cook_book_from_yaml_file(file_name):
    cook_bk={}
    one_ing_list={'ingridient_name': '', 'quantity': 0, 'measure': ''}
    one_ing_list_to_add={}

    with open(file_name) as f:
        cook_bk = yaml.load(f)
        # for l in f:
        #     culinary_name=l.strip()

    return cook_bk

#############################################################################################################
def get_shop_list_by_dishes(ck_book, dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in ck_book[dish]:
      new_shop_list_item = dict(ingridient)

      new_shop_list_item['quantity'] *= int(person_count)
      if new_shop_list_item['ingridient_name'] not in shop_list:

          shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
          k=int(new_shop_list_item['quantity'])
          shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=new_shop_list_item['quantity']
  return shop_list
#############################################################################################################
def print_shop_list(shop_list):
    for shopp_values in shop_list.values():
        print('{}: {} {} '.format(shopp_values['ingridient_name'], shopp_values['quantity'],shopp_values['measure']))
#############################################################################################################
def get_dishes_for_person(lst):

    return dish
#############################################################################################################
def get_dish_list(ck_book):
    dish_list=[]
    dish_lst=[]
    dish_lst=list(ck_book.keys())
    # print(type(dish_lst),'dish_lst =',dish_lst)
    print('Введите через пробел цифры названий для трех блюд обеда. При этом используйте буквы:')
    i=1
    for dish  in dish_lst:
        print(i, ' для ', dish)
        i+=1
    dishes=input('Введите через пробел цифры названий для трех блюд обеда: ').lower().split(' ')
    for j in range(3):
        k=int(dishes[j])-1
        print(dish_lst[k])
        dish_list.append(dish_lst[k])

    return dish_list
#############################################################################################################

def main():
    # чтение из recipes.txt используем для создания *.json и *.yml и для сравнения получаемых списков
    txt_cook_book=get_cook_book_from_txt_file('recipes.txt')

    # создаем JSON-файл с рецептами - один раз
    # with open('recipes.json','w') as cook_file: # , encoding='utf-8'
    #     json.dump(txt_cook_book, cook_file, ensure_ascii=False)

    # создаем YAML-файл с рецептами - один раз
    # with open('recipes.yml','w') as cook_file: # , encoding='utf-8'
    #     json.dump(txt_cook_book, cook_file, ensure_ascii=False)


    shop_lst={}
    # чтение из recipes.txt используем для сравнения получаемых списков покупок
    json_cook_book = get_cook_book_from_json_file('recipes.json')
    yaml_cook_book = get_cook_book_from_yaml_file('recipes.yml')

    dish_list_from_txt=get_dish_list(txt_cook_book)
    dish_list_from_json = get_dish_list(json_cook_book)
    dish_list_from_yaml = get_dish_list(yaml_cook_book)

    if dish_list_from_txt == dish_list_from_json:
        print('*******   dish lists are identical   *******')

    print('Введите количество человек: ')
    person_count = int(input())

    shop_lst = get_shop_list_by_dishes(txt_cook_book, dish_list_from_txt, person_count)
    # print_shop_list(shop_lst)

    if shop_lst == get_shop_list_by_dishes(json_cook_book, dish_list_from_json, person_count):
        print('*******   shop lists are identical   *******')

    # shop_lst = get_shop_list_by_dishes(json_cook_book, dish_list_from_json, person_count)
    # print_shop_list(shop_lst)


#############################################################################################################
main()
