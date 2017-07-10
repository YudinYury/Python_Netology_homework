'''lesson_2_3 homework «Работа с кодировками, русскими буквами»
https://github.com/netology-code/Python_course/tree/master/PY1_Lesson_2.3
Взять из github-репозитория все файлы с новостями в формате json: newsfr.json, newsit.json, newsafr.json, newscy.json.
Написать программу, которая будет выводить топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для каждого файла.

'''
import chardet
import json
import collections
import yaml
from xml.etree import ElementTree as ET
# from xml.dom
import csv
from pprint import pprint
import copy

##################################################################################################
def read_json_file(json_file):
    with open (json_file, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        s = text.decode(result['encoding'])
    json_data = json.loads(s)
    return json_data
##################################################################################################
def get_top_words_from_news_list_from_json_file(json_file,num_of_word):
    with open (json_file, 'rb') as f:
        text = f.read()  # чтение байтовое
        result = chardet.detect(text)
        s = text.decode(result['encoding'])
    json_data = json.loads(s)
    news_list = list(map(lambda x: x['title'] + ' ' + x['description'], [i for i in json_data['rss']['channel']['items']]))
    news_str = ''.join(news_list)
    news_list = news_str.split(" ")
    news_list = [i for i in news_list if len(i) > 6]  # делаем новый список только для длинных слов
    news_collect = collections.Counter()
    for i in news_list:
        news_collect[i] += 1
    top_words = news_collect.most_common(num_of_word)
    return list(map(lambda x: x[0], [i for i in top_words]))

##################################################################################################
def main():
    json_file_1 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsafr.json'
    json_file_2 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newscy.json'
    json_file_3 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsfr.json'
    json_file_4 = 'D:\Python_my\Python_netology_homework\Python_course\PY1_Lesson_2.3\\newsit.json'
    word_quantity = 10

    top_word_list = []
    top_word_list = get_top_words_from_news_list_from_json_file(json_file_1, word_quantity)
    print('Для файла {} самыми употребимыми являются слова: \n {} \n'.format(json_file_1, top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_2, word_quantity)
    print('Для файла {} самыми употребимыми являются слова: \n {} \n'.format(json_file_1, top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_3, word_quantity)
    print('Для файла {} самыми употребимыми являются слова: \n {} \n'.format(json_file_1, top_word_list))

    top_word_list = get_top_words_from_news_list_from_json_file(json_file_4, word_quantity)
    print('Для файла {} самыми употребимыми являются слова: \n {} \n'.format(json_file_1, top_word_list))

#################################################################################################
main()
