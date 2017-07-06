'''lesson_3_1_classwork «3.1. Zen of Python - any developer should know PEP8 and PEP20»

'''

import json
import yaml
from xml.etree import ElementTree as ET
# from xml.dom
import csv
from pprint import pprint
import copy

# examples from http://artifex.org/~hblanks/talks/2011/pep20_by_example.html
# halve_evens_only = lambda nums: map(lambda i: i/2, filter(lambda i: not i%2, nums))
# I made my variant
def halfe_only(arg_list):
    num_list = list(filter(lambda x: x%2==0, arg_list))
    print(num_list)
    return list(map(lambda x: x/2, num_list))
    # and I made translate to funcional-style myself
    # return list(map(lambda x: x / 2, filter(lambda x: x % 2 == 0, arg_list)))
print(halfe_only([i for i in range(1,50)]))


# def main():


# if __name__ == '__main__':
#     main()


