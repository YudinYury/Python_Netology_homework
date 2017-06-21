'''lesson_2_1 homework «Открытие и чтение файла, запись в файл»
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

#############################################################################################################
def get_cook_book_from_file(file_name):
    cook_bk={}
    one_ing_list={'ingridient_name': '', 'quantity': 0, 'measure': ''}
    one_ing_list_to_add={}
    with open('recipes.txt') as f:
        for l in f:
            culinary_name=l.strip()
            if culinary_name in cook_bk:
                # print('Повтор рецепта !')
                continue
            else:
                cook_bk[culinary_name]=[]
                # print('добавляем блюдо =',cook_bk)
            quant=int(f.readline())
            for i in range(quant):
                ing_list=f.readline().strip().split('|')
                ing_list = list(map(str.strip, ing_list))
                # print('ing_list =',ing_list)
                one_ing_list['ingridient_name']=ing_list[0]
                one_ing_list['quantity']=int(ing_list[1])
                one_ing_list['measure']=ing_list[2]

                # print(type(one_ing_list), 'one_ing_list =', one_ing_list)
                # print(type(cook_bk[culinary_name]), 'cook_bk[',culinary_name,'] =', cook_bk[culinary_name])
                # print('----        Uuuuuuuuse .append()      ----')
                one_ing_list_to_add=copy.deepcopy(one_ing_list)
                cook_bk[culinary_name].append(one_ing_list_to_add)
                # print(type(cook_bk[culinary_name]), 'cook_bk[',culinary_name,'] =', cook_bk[culinary_name])
                # print('cook_bk = ', cook_bk)

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
    shop_lst={}
    # f_name='recipes.txt'
    # сформируем файл рецептов если его нет
    # with open('recipes.txt', 'w') as f:
    #     for key, val in cook_book.items():
    #         f.write(str('{} \n{}\n'.format(key, len(cook_book[key]))))
    #
    #         for ingrad_key in cook_book[key]:
    #             f.write(str('{} | {} | {}\n'.format(ingrad_key['ingridient_name'], ingrad_key['quantity'], ingrad_key['measure'])))
    #     f.write(str('омлет\n3\nяйца | 2 | шт.\nмолоко | 50 | мл.\nпомидоры | 100 | гр.'))

    cook_book=get_cook_book_from_file('recipes.txt')
    # print(cook_book)
    dish_list=get_dish_list(cook_book)
    # print(dish_list)
    print('Введите количество человек: ')
    person_count = int(input())
    shop_lst=get_shop_list_by_dishes(cook_book, dish_list, person_count)
    # print(shop_lst)
    print_shop_list(shop_lst)

#############################################################################################################
main()
