"""lesson_3_7_Classwork 3.7 "API Yandex Metrika"

"""

import chardet
import os
import pprint
import requests
from urllib.parse import urlencode, urljoin


# import osa
# from xml.etree.ElementTree import fromstring, ElementTree


def get_yandex_token(token_file):
    with open(token_file, 'rb') as f:
        text = f.read()
        result = chardet.detect(text)
        source_text = text.decode(result['encoding'])
    token = source_text.split(' ')[1].lstrip().rstrip()
    return token


def get_counters(access_token):
    responce_json = {}
    url = 'https://api-metrika.yandex.ru/management/v1/counters'
    headers = {
        'Authorization': 'OAuth {}'.format(access_token),
        'Content - Type': 'application / x - yametrika + json'
    }
    responce = requests.get(url, headers=headers)
    print('responce.status_code = {}'.format(responce.status_code))
    responce_json = responce.json()
    # print(responce_json)
    print('number of counters = {}'.format(responce_json['rows']))
    print('counter.name = {}'.format(responce_json['counters'][0]['name']))
    print('counter.site = {}'.format(responce_json['counters'][0]['site']))
    counters = responce_json['counters']
    return counters


class YandexMetrikaBase:
    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def get_headers(self, token):
        return {
            'Authorization': 'OAuth {}'.format(token),
            'Content-Type': 'application/x-yametrika+json',
            'User-Agent': 'asdasdasd'
        }


class YandexMetrika(YandexMetrikaBase):
    number_of_counters = None
    counters = []
    token = None

    def __init__(self, token):
        self.token = token

    def show_token(self):
        print('my token is {}'.format(self.token))

    def get_counters(self):
        url = urljoin(self.MANAGEMENT_URL, 'counters')
        headers = self.get_headers(self.token)
        response = requests.get(url, headers=headers, params={'pretty': 1})
        counters = response.json()['counters']
        return [Counter(self.token, c['id']) for c in counters]


        # def get_counters(self):
        #     # url = 'https://api-metrika.yandex.ru/management/v1/counters'
        #     url = urljoin(self.MANAGEMENT_URL, 'counters')
        #     headers = self.get_headers(self.token)
        #     responce = requests.get(url, headers=headers)
        #     responce_json = responce.json()
        #     self.counters = responce_json['counters']
        #     self.number_of_counters = int(responce_json['rows'])
        #     return self.number_of_counters, self.counters

        # def get_counter_visits(self, counter_id):
        #     # url = 'https://api-metrika.yandex.ru/stat/v1/data.csv'
        #     headers = self.get_headers(self.token)
        #     params = {
        #         'id': counter_id,
        #         'metrics': 'ym:s:visits'
        #     }
        #     responce = requests.get(self.STAT_URL, params, headers=headers)
        #     # print(responce)
        #     responce_json = responce.json()
        #     print(responce_json)
        #     # print('number of counters = {}'.format(responce_json['rows']))
        #     # print('counter.name = {}'.format(responce_json['counters'][0]['name']))
        #     # print('counter.site = {}'.format(responce_json['counters'][0]['site']))
        #     # counters = int(responce_json['counters'])
        #
        #     print(responce)
        #     return responce


class Counter(YandexMetrikaBase):
    def __init__(self, token, counter_id):
        self.token = token
        self.id = counter_id

    def get_visits(self):
        headers = self.get_headers(self.token)
        params = {
            'id': self.id,
            'metrics': 'ym:s:visits'
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response.json()['data'][0]['metrics'][0]

    @property
    def views(self):
        headers = self.get_headers(self.token)
        params = {
            'id': self.id,
            'metrics': 'ym:s:pageviews'
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response.json()['data'][0]['metrics'][0]

    def get_visit_unic_users(self):
        headers = self.get_headers(self.token)
        params = {
            'id': self.id,
            'metrics': 'ym:pv:users'
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        # print(response.json())
        return response.json()['data'][0]['metrics'][0]


def main():
    access_token = get_yandex_token('API_Yandex_test_token.txt')
    ym = YandexMetrika(access_token)
    counters = ym.get_counters()
    # print(counters)
    for counter in counters:
        print('visits = {}'.format(counter.get_visits()))
        print('views = {}'.format(counter.views))
        print('unic users = {}'.format(counter.get_visit_unic_users()))



        # number_of_counters, counters = ym.get_counters()
        # print('number_of_counters = {}'.format(number_of_counters))
        # list_ids = [int(c['id']) for c in counters]
        # list_ids = [c['id'] for c in counters]
        # temp_id = list_ids[0]
        # print(type(temp_id), temp_id)
        # print(ym.get_counter_visits(temp_id))


if __name__ == '__main__':
    main()
