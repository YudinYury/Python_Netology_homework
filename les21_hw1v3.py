'''lesson_2_1 homework «Открытие и чтение файла, запись в файл» -- version 2
Список рецептов должен храниться в отдельном файле в следующем формате:
      Название блюда
      Kоличество ингредиентов
      Название ингредиента | Количество | Единица измерения
Пример:
      Омлет
      3
      Яйца | 2 | шт
      Молоко | 50 | г
      Помидор | 100 | мл
В одном файле может быть произвольное количество блюд.
Читать список рецептов из этого файла.
Соблюдайте кодстайл, разбивайте новую логику на функции и не используйте глобальных переменных.
Код выглядел следующим образом:
    cook_book = {
      'яйчница': [
        {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
        ],
      'стейк': [
        {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
        {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
        ],
      'салат': [
        {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
        {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
        {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
        ]
      }

    def get_shop_list_by_dishes(dishes, person_count):
      shop_list = {}
      for dish in dishes:
        for ingridient in cook_book[dish]:
          new_shop_list_item = dict(ingridient)

          new_shop_list_item['quantity'] *= person_count
          if new_shop_list_item['ingridient_name'] not in shop_list:
            shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
          else:
            shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=
              new_shop_list_item['quantity']
      return shop_list

    def print_shop_list(shop_list):
      for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

    def create_shop_list():
      person_count = int(input('Введите количество человек: '))
      dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
      shop_list = get_shop_list_by_dishes(dishes, person_count)
      print_shop_list(shop_list)

    create_shop_list()

'''

#TODO 1:
# чтение рецептов из файла, формирование списка покупок
# сформируем рабочий файл recipes.txt из словаря cook_book
# cook_book = {
#       'яичница': [
#         {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#         ],
#       'стейк': [
#         {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#         ],
#       'салат': [
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#         ]
#       }


import copy


def printerr(arg_str):
    print(arg_str, file=sys.stderr)


def get_cook_book_from_file(file_name):
    cook_bk = {}
    # one_ing_dict = {'ingridient_name': '', 'quantity': 0, 'measure': ''}
    one_ing_list_to_add = {}
    with open('recipes.txt') as f:
        for l in f:
            culinary_name = l.strip()
            if culinary_name in cook_bk:
                # print('Повтор рецепта !')
                continue
            else:
                cook_bk[culinary_name] = []
                # print('добавляем блюдо =',cook_bk)
            quant = int(f.readline())
            for i in range(quant):
                one_ing_dict = {}
                ing_list = f.readline().strip().split('|')
                ing_list = list(map(str.strip, ing_list))
                one_ing_dict['ingridient_name'] = ing_list[0]
                one_ing_dict['quantity'] = int(ing_list[1])
                one_ing_dict['measure'] = ing_list[2]
                cook_bk[culinary_name].append(one_ing_dict)
    return cook_bk


def get_shop_list_by_dishes(ck_book, dishes, person_count):
  shop_list = {}
  for dish in dishes:
    for ingridient in ck_book[dish]:
      new_shop_list_item = dict(ingridient)
      new_shop_list_item['quantity'] *= int(person_count)
      if new_shop_list_item['ingridient_name'] not in shop_list:
          shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
      else:
          # k=int(new_shop_list_item['quantity'])
          shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
  return shop_list


def print_shop_list(shop_list):
    for shopp_values in shop_list.values():
        print('{}: {} {} '.format(shopp_values['ingridient_name'], shopp_values['quantity'],shopp_values['measure']))


def get_dish_list(ck_book):
    dish_list_for_return = []
    inputed_dish_list = list(ck_book.keys())
    print('Введите через пробел цифры названий для трех блюд обеда. При этом используйте буквы:')
    for i, dish in enumerate(inputed_dish_list, start=1):
        print(i, ' для ', dish)

    print('Введите через пробел цифры названий для трех блюд обеда: ')
    dishes_num = input().lower().split(' ')
    for num in dishes_num:
        k = int(num)-1
        dish_list_for_return.append(inputed_dish_list[k])
    return dish_list_for_return


def main():
    shop_lst = {}
    cook_book = get_cook_book_from_file('recipes.txt')
    dish_list = get_dish_list(cook_book)
    print('Введите количество человек: ')
    person_count = int(input())
    shop_lst = get_shop_list_by_dishes(cook_book, dish_list, person_count)
    print_shop_list(shop_lst)


#############################################################################################################
#TODO 2:
# Напишите, для чего используются типы данных: json, xml, yaml.
# Используются для обмена данными. В json и yaml данные хранятся в парах ключ:значение, при этом они являются строками,
# а в xml даннеу распределяются при помощи тегов.
# вот эта статья (https://habrahabr.ru/post/248147/) в качестве объяснения про json-xml-yaml мне понравилась больше.
# JSON - самый распространенный. Используется для получения данных от разных сайтов.
# Вот тут хороший пример https://toster.ru/q/326979

main()
