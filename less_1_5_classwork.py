'''lesson_1_5 classwork «Функции, циклы, коллекции»
летний салат: огурцы 100г,помидоры 100г, майонез 20г
глазунья: яйцо 2 шт, лук 10г, помидоры 50г
бутерброд: злеб 20г, колбаса 100г, сыр 100г

'''

import copy
import math
import csv

cookbook = {
    'летний салат': [
        {'name': 'огурцы','quantity': 100, 'measure': 'g'},
        {'name': 'помидоры', 'quantity':100, 'measure': 'g'},
        {'name': 'майонез', 'quantity': 20, 'measure': 'g'}
    ],
    'глазунья': [
        {'name':'яйцо','quantity': 2, 'measure': 'pcs'},
        {'name':'лук','quantity': 10, 'measure': 'g'},
        {'name':'помидоры','quantity': 50, 'measure': 'g'}
    ],
    'бутерброд': [
        {'name': 'хлеб','quantity': 200, 'measure': 'g'},
        {'name': 'колбаса', 'quantity': 100, 'measure': 'g'},
        {'name': 'сыр', 'quantity': 100, 'measure': 'g'}
    ]
}

##################################################################################################
# обработать список блюд и получить инградиенты
def get_shop_list_by_dishes(dishes,person_count):
    shop_l={}
    for dish in dishes:
        # print('dish = ', dish)
        for ing in cookbook[dish]:

            # name=ing['name'] # мое решение
            # qua=ing['quantity']*person_count
            # if name in shop_l:
            #     shop_l[name]+=qua #если инградиент уже есть в словаре, то добавляю количество
            # else:
            #     shop_l[name] = qua # если нет, то вношу через присваивание нового

            new_shop_l_item=dict(ing)  # это решение преподавателя, копируем инградиент
            new_shop_l_item['quantity']*=person_count # количество инградиента по количеству человек
            shop_l[new_shop_l_item['name']]=new_shop_l_item
            if new_shop_l_item['name'] not in shop_l: # еще нет инградиента ?
                shop_l[new_shop_l_item['name']]=new_shop_l_item # добавляем инградиент (его имя)
            else:
                shop_l[new_shop_l_item['name']]['quantity'] += new_shop_l_item['quantity']
    return shop_l
##################################################################################################
def print_shop_list(shop_list):
    # for shop_values in shop_list.values():
    #     print('{}: {} {} '.format(shop_values['name'], shop_values['quantity'],shop_values['measure']))
    # переписываем при помощи kwarg
    for shop_values in shop_list.values():
        print('{name}: {quantity} {measure} '.format(**shop_values))
##################################################################################################
def main():
    # dishes = ['летний салат', 'глазунья', 'бутерброд']
    dishes=input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    print(dishes)
    person_count = int(input('Введите количество человек: '))
    shop_list=get_shop_list_by_dishes(dishes,person_count)
    print_shop_list(shop_list)
#################################################################################################

main()


