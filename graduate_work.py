"""graduate work
Задание:
Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.
В качестве жертвы, на ком тестировать, можно использовать: https://vk.com/tim_leary

Входные данные:
имя пользователя или его id в ВК, для которого мы проводим исследование
Внимание: и имя пользователя (tim_leary) и id (5030613)  - являются валидными входными данными
Ввод можно организовать любым способом:
из консоли
из параметров командной строки при запуске
из переменной
Выходные данные:
файл groups.json в формате
[
{
“name”: “Название группы”,
“gid”: “идентификатор группы”,
“members_count”: количество_участников_собщества
},
{
…
}
]
Форматирование не важно, важно чтобы файл был в формате json

Требования к программе:
Программа не падает, если один из друзей пользователя помечен как “удалён” или “заблокирован”
Показывает что не зависла: рисует точку или чёрточку на каждое обращение к api
Не падает, если было слишком много обращений к API
(Too many requests per second)
Ограничение от ВК: не более 3х обращений к API в секунду.
Могут помочь модуль time (time.sleep) и конструкция (try/except)
Код программы удовлетворяет PEP8

Дополнительные требования (не обязательны для получения диплома):
Показывает прогресс:  сколько осталось до конца работы (в произвольной форме: сколько обращений к API, сколько минут,
сколько друзей или групп осталось обработать)
Восстанавливается если случился ReadTimeout
Показывать в том числе группы, в которых есть общие друзья, но не более, чем N человек, где N задаётся в коде

Псевдокод:
Получаем список групп tim_leary -> tim_leary_groups_list
Получаем список друзей tim_leary -> friends
По каждому другу получаем список его групп и проверяем наличие group_id в списке tim_leary_groups_list:
    при совпадении удаляем group_id из tim_leary_groups_list
По оставшимся в tim_leary_groups_list номерам group_id ->  записываем в файл groups.json
   ->

"""

from time import sleep

# import time
import vk

from less_3_4_hw_VK_access_token import vk_access_token


class VkGroup():
    name = ''
    gid = None
    members_count = 0


def person_get_groups_set(vk_api, vk_id):
    groups_list = []
    sleep(0.400)
    print('I am calling API')
    try:
        # groups_list = vk_api.groups.get(user_id=vk_id, count=18)
        groups_list = vk_api.groups.get(user_id=vk_id)
    except vk.exceptions.VkAPIError:
        print('No user found (for id={})'.format(vk_id))
        return 0, None
    else:
        try:
            groups_list_numbers = groups_list.pop(0)
        except IndexError:
            print('User group list is empty (for id={})'.format(vk_id))
            return 0, None
        else:
            return groups_list_numbers, set(groups_list)


def about_vk_group(vk_api, vk_group_id):
    vk_group = {
        "name": '',
        "gid": None,
        "members_count": 0
    }
    sleep(0.400)
    tim_leary_groups_list = vk_api.groups.getMembers(group_id=vk_group_id, count=3)
    return vk_group


def main():
    vk_group = {
        "name": '',
        "gid": None,
        "members_count": 0
    }
    vk_group_allowed = []
    vk_group_forbidden = []
    vk_group_list = []
    tim_leary_id = 5030613
    tim_leary_first_name = ''
    tim_leary_last_name = ''

    vk_session = vk.Session(access_token=vk_access_token)
    vk_api = vk.API(vk_session)

    status = vk_api.users.get(user_id=tim_leary_id, fields='followers_count, is_friend, friend_status')
    tim_leary_first_name = status[0]['first_name']
    tim_leary_last_name = status[0]['last_name']

    # tim_leary_groups_list = vk_api.groups.get(user_id=tim_leary_id)
    # tim_leary_groups_list = vk_api.groups.get(user_id=tim_leary_id, count=9)
    # tim_leary_groups_numbers = tim_leary_groups_list.pop(0)
    # tim_leary_groups_set = set(tim_leary_groups_list)
    tim_leary_groups_numbers, tim_leary_groups_set = person_get_groups_set(vk_api, vk_id=tim_leary_id)
    print('{} {} состоит в {} группах:'.format(tim_leary_first_name, tim_leary_last_name, tim_leary_groups_numbers))
    print('{} {} состоит в {} группах:'.format(tim_leary_first_name, tim_leary_last_name, len(tim_leary_groups_set)))
    print('tim_leary_groups_set =', tim_leary_groups_set)
    print(len(tim_leary_groups_set))

    friends = vk_api.friends.get(user_id=tim_leary_id)
    # friends = vk_api.friends.get(user_id=tim_leary_id, count=15)
    print('Friends list is {} persons:'.format(len(friends)))
    print(friends)

    for i, friend_id in enumerate(friends):
        friend_groups_set_num, friend_groups_set = person_get_groups_set(vk_api, vk_id=friend_id)
        if friend_groups_set_num == 0:
            continue
        # print('{} состоит в {} группах:'.format(friend_id, friend_groups_set_num))
        # print(friend_groups_set)
        tim_leary_groups_set.difference_update(friend_groups_set)
        print(len(tim_leary_groups_set))
        # print('tim_leary_groups_set =', tim_leary_groups_set)

    print('Finally:')
    print('tim_leary_groups_set =', tim_leary_groups_set)
    print(len(tim_leary_groups_set))

if __name__ == '__main__':
    main()
