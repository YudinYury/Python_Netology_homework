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

    def get_count(self, type_of_count):
        headers = self.get_headers(self.token)
        if type_of_count == 'unic_users':
            type_of_count = 'ym:pv:users'
        elif type_of_count == 'views':
            type_of_count = 'ym:s:pageviews'
        elif type_of_count == 'visits':
            type_of_count = 'ym:s:visits'
        else:
            print('Encorrect type of view')
            return 1

        params = {
            'id': self.id,
            'metrics': type_of_count
        }
        response = requests.get(self.STAT_URL, params, headers=headers)
        return response.json()['data'][0]['metrics'][0]


def main():
    access_token = get_yandex_token('API_Yandex_test_token.txt')
    ym = YandexMetrika(access_token)
    counters = ym.get_counters()
    # print(counters)
    for counter in counters:
        print('visits = {}'.format(counter.get_count('visits')))
        print('views = {}'.format(counter.get_count('views')))
        print('unic users = {}'.format(counter.get_count('unic_users')))


if __name__ == '__main__':
    main()
