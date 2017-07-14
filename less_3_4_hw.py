"""lesson_3_4_homework «API VK, Oauth protocol»

"""

import json
import requests
from urllib.parse import urlencode
import urllib.request
import vk


# import vk_auth_port_by_bulates1

def get_token(token_file):
    with open(token_file) as f:
        vk_api_access = json.load(f)
    return vk_api_access['access_token']


def main():
    id_file_name_json = 'VK_API_test.json'
    vk_first_request = ''
    vk_version = '5.67'
    outh_url = 'https://oauth.vk.com/authorize'

    with open(id_file_name_json) as f:
        auth_data = json.load(f)

    # vk_first_request = 'https://oauth.vk.com/authorize?client_id=' + auth_data['app_id'] + \
    #                    '&display=page&redirect_uri=' + auth_data['redirect_url'] + \
    #                    '&scope=' + auth_data['scope'] + '&' \
    #                    'response_type=' + auth_data['response_type'] + '&v=' + vk_version
    # print(vk_first_request)

    access_token = get_token('VK_API_access_token.json')
    vk_api_url = 'https://api.vk.com/method/'
    params = {
        "access_token": access_token,
        "client_id": auth_data['app_id'],
        "display": auth_data['display'],
        "scope": 'friends, status, video',
        "response_type": auth_data['response_type'],
        "v": auth_data['version']
    }

    params['user_id'] = '421546279'  # I'm
    # params['user_id'] = '329990009'  # https://vk.com/id329990009, Вася Носов
    vk_response = requests.get('https://api.vk.com/method/status.get', params).json()
    print('My status -> {}'.format(vk_response['response']['text']))
    # vk_response = requests.get('https://api.vk.com/method/users.get', params).json()
    # print(vk_response)
    params['order'] = 'random'
    vk_response = requests.get('https://api.vk.com/method/friends.getLists', params).json()
    print('I have {} friends'.format(vk_response['response']['count']))
    # if vk_response['response']['count'] == 0:
    #     print('Have no friends')


if __name__ == '__main__':
    main()


    # vk_first_request = 'https://oauth.vk.com/authorize?client_id=' + auth_data['app_id'] + \
    #                    '&display=page&redirect_uri=' + auth_data['redirect_url'] + \
    #                    '&scope=friends&' \
    #                    'response_type=' + auth_data['response_type'] + '&v=' + vk_version
    # print(vk_first_request)

    # vkapi = vk.API(app_id, login, password)
    # vkapi.access_token = vk_auth_port_by_bulates1.auth(login, password, app_id, 'wall')
    # vkapi.wall.post(message="Test from python 3.4")
