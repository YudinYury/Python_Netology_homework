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

"""

from time import sleep

import vk

from less_3_4_hw_VK_access_token import vk_access_token


class VkGroup():
    name = ''
    gid = None
    members_count = 0


def main():
    vk_group = {
        "name": '',
        "gid": None,
        "members_count": 0
    }
    vk_group_list = []
    tim_leary_id = 5030613
    tim_leary_first_name = ''
    tim_leary_last_name = ''

    vk_session = vk.Session(access_token=vk_access_token)
    vk_api = vk.API(vk_session)

    status = vk_api.users.get(user_id=tim_leary_id, fields='followers_count, is_friend, friend_status')
    tim_leary_first_name = status[0]['first_name']
    tim_leary_last_name = status[0]['last_name']

    # friends_lists = vk_api.friends.getLists(user_id=tim_leary_id, fields='nickname, contacts, status', count=3)
    # print(friends_lists)

    tim_leary_groups_list = vk_api.groups.get(user_id=tim_leary_id, count=3)
    print('{} {} состоит в {} группах:'.format(tim_leary_first_name, tim_leary_last_name, len(tim_leary_groups_list)))

    # friends = vk_api.friends.get(user_id=tim_leary_id, fields='nickname, contacts')
    friends = vk_api.friends.get(user_id=tim_leary_id, fields='nickname, contacts', count=5)
    print('Friends list is {} persons:'.format(len(friends)))
    frnd_id = 0
    for frnd in friends:
        sleep(1)
        print(frnd)
        frnd_id = frnd['uid']
        friend_groups_list = vk_api.groups.get(user_id=frnd_id, count=3)
        print(friend_groups_list)
        print('{} состоит в {} группах:'.format(frnd_id, len(friend_groups_list)))



        # json_data = json.loads(frnd)
        # print(json_data)

        # print(frnd['first_name'], friends['user_id'])

        # print('{} {}'.format(frnd['first_name'], friends['last_name']))
        # print('{} {} aka "{}" have id: {}'.format(frnd['first_name'], friends['last_name'], friends['nickname'], friends['user_id']))

    sleep(1)


if __name__ == '__main__':
    main()
