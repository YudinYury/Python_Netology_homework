'''lesson_2_2 classwork «Работа с разными форматами данных»

'''

import json
import yaml
from xml.etree import ElementTree as ET
# from xml.dom
import csv
from pprint import pprint
import copy

##################################################################################################
# read and write YAML
# pip install pyyaml
with open('godfather.yml','r') as godfather_file:
    movie=yaml.load(godfather_file)
# pprint(movie)
# read and write JSON
with open('godfather.2017.json','w') as f:
    json.dump(movie,f,indent=2,ensure_ascii=False)
with open('godfather.2017.json','r') as f:
    data=json.load(f)
# pprint(data)

# read and write XML
xml_tree=ET.parse('godfather.xml')
# for e in xml_tree.iter():
    # print(e)
    # print(e.tag)
    # print(e.tag, e.attrib)
    # print(e.tag, e.attrib, e.text)
main_characters=xml_tree.find('mainCharacters')
main_characters_list=main_characters.findall('mainCharacters')
# print(main_characters_list)
# print(main_characters_list[0].attrib)

# read and write CSV
# построчно, списком
# with open('test_csv.csv') as csv_f:
#     appart=csv.reader(csv_f, delimiter=';')
#     for row in appart:
#         # print(row)
#         print(row[2])
# построчно, словарем
with open('test_csv.csv') as csv_f:
    appart=csv.DictReader(csv_f, delimiter=';') # Python по умолчаниею использует ',', a Excell ';'
    for row in appart:
        # print(row)
        print(row['ID'])

##################################################################################################
# def main():
#################################################################################################
# main()


