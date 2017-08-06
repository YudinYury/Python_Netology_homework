"""lesson_4_1_Classwork "Data processing tools"

"""

import os

import pandas as pd


def count_of_len(row):
    return len(row.Name)


def main():
    source_path = 'D:\Python_my\Python_Netology_homework\data_names'

    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    source_file = os.path.normpath(os.path.join(source_dir_path, 'yob1900.txt'))
    names = pd.read_csv(source_file, names=['Name', 'Gender', 'Count'])
    # print(names.head(10))
    # print(names.query('Count > 5000 & Gender == "M"'))
    # print(names[(names.Count > 5000) | (names.Gender == 'M')].head(10))
    # print(names[(names.Count > 5000) | (names.Name.str.startswith('M'))].head(10))
    print(names[(names.Count > 3000) & (names.Name.str.startswith('M'))].head(10))
    # dest_file = os.path.normpath(os.path.join(source_dir_path, 'yob1900.csv'))
    # names[(names.Count > 3000) & (names.Name.str.startswith('M'))].to_csv(dest_file, index=False) # добавить параметр header=False, чтобы не записывать в файл шапку таблицы

    # print(names[(names.Count > 3000) & (names.Name.str.startswith('M'))].sort_values(by=Name, ascending=False))
    # print(names.sort_values(by=Name, ascending=False))
    print()
    # print(names.query('Gender == "M"').Count.sum())
    # names['Len'] = names.apply(count_of_len, axis=1).head(10) #  axis=1 - это обход по строкам
    names['Len'] = names.apply(lambda row: len(row.Name), axis=1).head(10)  # axis=1 - это обход по строкам
    print(names.head(10))

    exit(0)


if __name__ == '__main__':
    main()
