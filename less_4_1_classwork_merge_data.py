"""lesson_4_1_Classwork "Data processing tools"

"""

import os

import pandas as pd


def count_of_len(row):
    return len(row.Name)


def agg_count(row):
    # row.Count += row.Count_1900 + row.Count_1950 + row.Count
    return row.Count_1900 + row.Count_1950 + row.Count


def main():
    source_path = 'D:\Python_my\Python_Netology_homework\data_names'
    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    # source_file_1 = os.path.normpath(os.path.join(source_dir_path, 'yob1880.txt'))
    # source_file_2 = os.path.normpath(os.path.join(source_dir_path, 'yob1890.txt'))
    # columns = ['Name','Gender', 'Count']
    # names_1880 = pd.read_csv(source_file_1, names=columns)
    # names_1890 = pd.read_csv(source_file_2, names=columns)
    # names_1880_1890 = pd.merge(names_1880, names_1890, on=['Name','Gender'], suffixes=('_1880', '_1890')).head(10)
    # print(names_1880_1890)

    columns = ['Name', 'Gender', 'Count']
    source_file_1 = os.path.normpath(os.path.join(source_dir_path, 'yob1900.txt'))
    source_file_2 = os.path.normpath(os.path.join(source_dir_path, 'yob1950.txt'))
    names_1900 = pd.read_csv(source_file_1, names=columns)
    names_1950 = pd.read_csv(source_file_2, names=columns)
    names_1900_1950 = pd.merge(names_1900, names_1950, on=['Name', 'Gender'], suffixes=('_1900', '_1950'))
    print(names_1900_1950.head(10))
    print()
    source_file_3 = os.path.normpath(os.path.join(source_dir_path, 'yob2000.txt'))
    names_2000 = pd.read_csv(source_file_3, names=columns)
    names_1900_1950_2000 = pd.merge(names_1900_1950, names_2000, on=['Name', 'Gender'])
    # print(names_1900_1950_2000.head(10))
    # print()
    names_1900_1950_2000['Count_sum'] = names_1900_1950_2000.apply(agg_count, axis=1)
    # print(names_1900_1950_2000.head(10))
    print()

    names_all = pd.concat([names_1900, names_1950], names=['Year', 'Pos'])
    print(names_all.head(10))
    print('----------------  Sort by Count  ----------------------')
    print(names_1900.sort_values(by='Count', ascending=False).head(10))

    names_all = pd.concat({1900: names_1900, 1950: names_1950, 2000: names_2000}, names=['Year', 'Pos'])
    print('----------------  Sort by Name  ----------------------')
    print(names_1900.sort_values(by='Name', ascending=True).head(10))

    print(names_all.groupby('Name').sum().sort_values(by='Count', ascending=False).head(10))
    print(names_1900.groupby('Gender').sum())

    exit(0)


if __name__ == '__main__':
    main()
