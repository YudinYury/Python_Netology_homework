'''lesson_2_3 classwork «Работа с кодировками, русскими буквами»

'''
# pip install chardet
import chardet
import json
import yaml
from xml.etree import ElementTree as ET
# from xml.dom
import csv
from pprint import pprint
import copy

##################################################################################################
# with open('recipes.txt', encoding='cp1251') as f:
#     text=f.read()
    # print(text)
with open('recipes.txt', 'rb') as f:
    text=f.read() # чтение байтовое
    result = chardet.detect(text)
    print('detect result ', result)
    s = text.decode(result['encoding'])
    print(s)

# with open('recipes_koi8.txt', 'w', encoding='koi8-r') as f:
#     f.write(text)
# with open('recipes_utf8.txt', 'w', encoding='utf8') as f:
#     f.write(text)
# with open('recipes_cp1251.txt', 'w', encoding='cp1251') as f:
#     f.write(text)

##################################################################################################
# def main():
#################################################################################################
# main()


