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

import logging
from time import sleep

import requests

from less_3_4_hw_VK_access_token import vk_access_token

# logging.basicConfig(format = u'[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)
logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s', level=logging.DEBUG,
                    filename=u'graduate_work.log')

class VkFriends():
    root_friend_id = None  # 5030613
    root_friend_first_name = None
    root_friend_last_name = None
    friend_count = 0
    friend_id_list = []
    friend_id_set = None
    groups_count = 0
    root_friend_groups_set = None
    different_group_set = None
    vk_group_allowed = []
    vk_group_forbidden = []
    url = 'https://https://api.vk.com/method/'
    dot_count = 0  # counter for "progress line"
    name = ''
    gid = None
    members_count = 0

    def __init__(self, vk_id):
        """
        https://https://api.vk.com/method/users.get?
        user_id=<user_id>
         & access_token=<VK-token>
         & v=<версия интерфейса>
        :param vk_id: <int> or <str> user_id.
        :return: <json> info about user (user_id).
        """
        self.root_friend_id = vk_id
        params = {
            'user_ids': self.root_friend_id,
            'access_token': vk_access_token,
            # 'count': 3,
            'v': 5.68
        }
        # https://api.vk.com/method/users.get?user_ids=5030613&fields=bdate&access_token=vk_access_token&v=5.68
        response = requests.get('https://api.vk.com/method/users.get', params=params)
        # print(response.status_code)
        if response.status_code == requests.codes.ok:
            self.print_dot()
        else:
            print(response.raise_for_status())
        response_json = response.json()['response'][0]
        self.root_friend_first_name = response_json['first_name']
        self.root_friend_last_name = response_json['last_name']
        print('User {} is founded.'.format(self.root_friend_id))
        # print('His name is "{} {}".'.format(self.root_friend_first_name, self.root_friend_last_name))

    def print_dot(self):
        """
        print "progress bar" from a lot of dot
        30 dots - border for clearing "progress bar"
        """

        # if self.dot_count == 30:
        #     self.dot_count = 0
        #     print('.')
        # else:
        #     self.dot_count += 1
        #     print('.', end='')

    def make_friend_id_list(self):
        """
        https://api.vk.com/method/users.get?
        user_id=<user_id> User, for which a list of friends is created
         & access_token=<VK-token>
         & v=<версия интерфейса VK>
         & count=<количество выводимых id друзей>
        :param self: <int> or <str> self.root_friend
        :return: <int> friend_count and <list> friend_id_list
        """
        params = {
            'user_id': self.root_friend_id,
            'access_token': vk_access_token,
            # 'count': 117,
            'v': 5.68
        }
        # response = requests.post(url, data=json.dumps(payload))
        # https://api.vk.com/method/friends.get?params[user_id] = 5030613 & params[count] = 3 & params[v] = 5.68
        sleep(0.400)
        response = requests.get('https://api.vk.com/method/friends.get', params=params)
        if response.status_code == requests.codes.ok:
            self.print_dot()
        else:
            print(response.raise_for_status())
        response_json = response.json()['response']
        self.friend_count = response_json['count']
        # print('self.friend_count =', self.friend_count)
        self.friend_id_list = response_json['items']
        self.friend_id_set = set(self.friend_id_list)
        print(
            '{} {} have {} friends.'.format(self.root_friend_first_name, self.root_friend_last_name, self.friend_count))

    def print_root_user_info(self):
        print('--------- info about root friend ---------')
        print('Name: {} {}'.format(self.root_friend_first_name, self.root_friend_last_name))
        print('friend_count = {}'.format(self.friend_count))
        # print('self.friend_id_list =', self.friend_id_set)
        print('groups_count = {}'.format(self.groups_count))

    def root_friend_make_groups_set(self):
        self.groups_count, self.root_friend_groups_set = self.person_get_groups_set(self.root_friend_id)
        # print('self.groups_count = {}, '.format(self.groups_count))

    def person_get_groups_set(self, vk_id):
        params = {
            'user_id': vk_id,
            'access_token': vk_access_token,
            # 'count': 15,
            'v': 5.68
        }
        groups_list = []
        sleep(0.400)
        # print('--------- person_get_groups_set metod ---------')
        # print('friend_id =', vk_id)
        # try:
        self.print_dot()
        response = requests.get('https://api.vk.com/method/groups.get', params=params)
        # print(response.json())
        # except vk.exceptions.VkAPIError:
        #     print('No user found (for id={})'.format(vk_id))
        #     return 0, None
        try:
            response_json = response.json()['response']
        except KeyError:
            print(' ')
            # print('--------- Attention ! KeyError "response" ---------')
            logging.debug(
                u'vk_id: {}, error code: {}, error_msg: {}'.format(vk_id, response.json()['error']['error_code'],
                                                                   response.json()['error']['error_msg']))

            # print('vk_id: {}, error code: {}, error_msg: {}'.format(vk_id, response.json()['error']['error_code'],
            #                                                         response.json()['error']['error_msg']))
            return 0, None
        else:
            # print(response_json)
            groups_list_numbers = response_json['count']
            groups_list = response_json['items']
            # print('groups_list_numbers =', groups_list_numbers)
            # print('groups_list =', groups_list)
            return groups_list_numbers, set(groups_list)

    def make_different_group_list(self):
        counter = 0
        for friend_id in self.friend_id_set:
            if counter % 10 == 0:
                print('{} from {}'.format(counter, self.friend_count))
            # print('friend_id =', friend_id)
            friend_groups_set_num, friend_groups_set = self.person_get_groups_set(vk_id=friend_id)
            if friend_groups_set_num == 0:
                continue
            self.root_friend_groups_set.difference_update(friend_groups_set)
            counter += 1
            # print('root_friend_groups_set ='.format(self.root_friend_groups_set))
        self.different_group_set = self.root_friend_groups_set
        print('')
        print('Numbers of "tim_leary" exclusive groups: {}'.format(len(self.different_group_set)))
        print('different_group_set = {}'.format(self.root_friend_groups_set))



def main():
    vk_group = {
        "name": '',
        "gid": None,
        "members_count": 0
    }
    tim_leary = VkFriends(5030613)
    tim_leary_id = 5030613

    tim_leary.make_friend_id_list()
    tim_leary.root_friend_make_groups_set()
    tim_leary.print_root_user_info()

    tim_leary.make_different_group_list()



if __name__ == '__main__':
    main()
