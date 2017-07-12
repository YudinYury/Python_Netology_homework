"""lesson_3_3_homework «Requests Lib and HTTP-requests»

"""

import chardet
import os
import requests


def translate_it(text, lang='en-ru'):
    """
    YANDEX translation plugin
    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': lang,
        'text': text,
    }

    response_raw = requests.get(url, params=params)
    # print('Body =', response_raw.content)
    response = response_raw.json()
    # response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))


def translate_file(source_file, destination_file, source_lang, destination_lang='ru'):
    """
    translate file with YANDEX translation plugin
    :param source_file: <str> source file name for translation
    :param destination_file: <str> destination file name for translation
    :param source_lang: <str> source language (from)
    :param destination_lang: <str> destination language (to)
    :return: None
    """
    # lang = 'ru-en'
    lang = source_lang + '-' + destination_lang
    with open(source_file, 'rb') as f:  # чтение байтовое
        text = f.read()
        result = chardet.detect(text)
        source_text = text.decode(result['encoding'])
        text_translated = translate_it(source_text, lang)

    # print(text_translated)
    with open(destination_file, 'w') as f:
        f.write(text_translated)

    return


def find_dir(dir_name):
    _, dir_name = os.path.split(dir_name)
    return dir_name in os.listdir()


def make_new_dir(dir_name):
    if find_dir(dir_name):
        pass
        # print('dir_name already exist')
    else:
        os.mkdir(os.path.normpath(dir_name))


def main():
    source_path = '3.2-requests'
    source_lang = ''
    destination_lang = 'ru'

    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    destination_dir_path = os.path.normpath(source_dir_path + '_translated')
    make_new_dir(destination_dir_path)

    file_names_list = os.listdir(source_dir_path)
    file_names_list = [x for x in file_names_list if x.endswith('.txt')]
    for file_name in file_names_list:
        source_lang, _ = file_name.split('.')
        source_lang = source_lang.lower()
        source_file = os.path.normpath(os.path.join(source_dir_path, file_name))
        # print(source_file)
        destination_file = os.path.normpath(os.path.join(destination_dir_path, file_name))
        translate_file(source_file, destination_file, source_lang)

    print('Результаты перевода сохранены в папке "{}"'.format(destination_dir_path))


if __name__ == '__main__':
    main()
