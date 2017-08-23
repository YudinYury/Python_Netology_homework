"""lesson_3_4_homework «API VK, Oauth protocol»

"""

# from urllib.parse import urlencode
from time import sleep

import vk

from less_3_4_hw_VK_access_token import vk_access_token
from less_3_4_hw_VK_access_token import vk_json


# vk_first_request = ''
# vk_version = '5.9'
# outh_url = 'https://oauth.vk.com/authorize'
# vk_first_request = 'https://oauth.vk.com/authorize?client_id=' + auth_data['app_id'] + \
#                    '&display=page&redirect_uri=' + auth_data['redirect_url'] + \
#                    '&scope=' + auth_data['scope'] + '&' \
#                    'response_type=' + auth_data['response_type'] + '&v=' + vk_version
# print(vk_first_request)


def main():
    auth_data = vk_json
    # vk_api_url = 'https://api.vk.com/method/'
    params = {
        "vk_access_token": vk_access_token,
        "client_id": auth_data['app_id'],
        "display": auth_data['display'],
        "scope": 'friends, status, video',
        "response_type": auth_data['response_type'],
        "v": auth_data['version']
    }

    vk_session = vk.Session(access_token=vk_access_token)
    vk_api = vk.API(vk_session)

    # альтернативная авторизация: без token, а через login и password
    # vk_api = vk.API(app_id, vk_login, vk_password)
    # vk_api.access_token = vk_access_token

    # print(auth_data['scope'])
    # session = vk.AuthSession(auth_data['app_id'], vk_login, vk_password, scope=auth_data['scope'])
    # vk_api = vk.API(session)

    # https://vk.com/id421546279, I'm
    status = vk_api.users.get(user_id=421546279, fields='online, last_seen, followers_count, is_friend, friend_status')
    # print(status[0])
    if status[0]['online']:
        is_online = 'online'
    else:
        is_online = 'offline'
    print('{} {} is {}.'.format(status[0]['first_name'], status[0]['last_name'], is_online))
    print('{} have {} friends.'.format(status[0]['first_name'], status[0]['is_friend']))
    print('{} have {} followers.'.format(status[0]['first_name'], status[0]['followers_count']))

    # https://vk.com/id329990009, Вася Носов
    status = vk_api.users.get(user_id=329990009, fields='online, last_seen, followers_count, is_friend, friend_status')
    if status[0]['online']:
        is_online = 'online'
    else:
        is_online = 'offline'
    print('{} {} is {}.'.format(status[0]['first_name'], status[0]['last_name'], is_online))
    print('{} have {} friends.'.format(status[0]['first_name'], status[0]['is_friend']))
    print('{} have {} followers.'.format(status[0]['first_name'], status[0]['followers_count']))

    params['user_id'] = '329990009'  # https://vk.com/id329990009, Вася Носов
    # params['user_id'] = '421546279'  # I'm
    params['count'] = status[0]['followers_count']
    params['fields'] = 'followers_count, last_seen'

    # friends_lists = vk_api.friends.getLists(params=params)
    # print(friends_lists)
    sleep(1)
    followers_lists = vk_api.users.getFollowers(user_id=329990009, fields='followers_count, last_seen')
    print("Vanya's Followers:")
    followers_count = followers_lists['count']
    for i in range(followers_count):
        print('{}) {} {} '.format(i + 1, followers_lists['items'][i]['first_name'],
                                  followers_lists['items'][i]['last_name']))


if __name__ == '__main__':
    main()
