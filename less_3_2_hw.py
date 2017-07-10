"""lesson_3_2 homework «Работа с кодировками, русскими буквами»
https://github.com/netology-code/Python_course/tree/master/PY1_Lesson_2.3
Взять из github-репозитория все файлы с новостями в формате json: newsfr.json,  newsit.json, newsafr.json, newscy.json
Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов
для каждого файла.
"""


import chardet
import json
import collections


def read_json_file(json_file):
    '''
    :param json_file: file name to open -> string
    :return: json_data: json data from file -> dict
    '''
    with open(json_file, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        s = text.decode(result['encoding'])
    json_data = json.loads(s)
    return json_data


def get_top_words_from_news_list_from_json_file(json_file, num_of_word):
    '''
    :param json_file: file name for search top word list -> string
    :param num_of_word: how many words include to top-list of word -> int
    :return: top-list of word -> list
    '''
    with open(json_file, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        si = text.decode(result['encoding'])
    json_data = json.loads(si)
    news_list = list(map(lambda x: x['title'] + ' ' + x['description'],
                         [i for i in json_data['rss']['channel']['items']]))
    news_str = ''.join(news_list)
    news_list = news_str.split(" ")
    news_list = [i for i in news_list if len(i) > 6]  # make new list for len(words) > 6
    news_collect = collections.Counter()
    for i in news_list:
        news_collect[i] += 1
    top_words = news_collect.most_common(num_of_word)
    return list(map(lambda x: x[0], [i for i in top_words]))


def main():
    json_file_1 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsafr.json'
    json_file_2 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newscy.json'
    json_file_3 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsfr.json'
    json_file_4 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsit.json'
    word_quantity = 10

    top_word_list = []
    top_word_list = get_top_words_from_news_list_from_json_file(json_file_1, word_quantity)
    print('Для файла {} самыми употребимыми являются слова:'.format(json_file_1))
    print('{}'.format(top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_2, word_quantity)
    print('Для файла {} самыми употребимыми являются слова:'.format(json_file_2))
    print('{}'.format(top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_3, word_quantity)
    print('Для файла {} самыми употребимыми являются слова:'.format(json_file_3))
    print('{}'.format(top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_4, word_quantity)
    print('Для файла {} самыми употребимыми являются слова:'.format(json_file_4))
    print('{}'.format(top_word_list))


if __name__ == '__main__':
    main()
