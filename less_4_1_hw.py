"""lesson_4_1_Classwork "Data processing tools"

"""

import os

import pandas as pd


def count_of_len(row):
    return len(row.Name)


def agg_count(row):
    # row.Count += row.Count_1900 + row.Count_1950 + row.Count
    return row.Count_1900 + row.Count_1950 + row.Count


source_path = 'D:\Python_my\Python_Netology_homework\data_names'


def count_top3(arg_list):
    global source_path
    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    columns = ['Name', 'Gender', 'Count']
    names = []
    res = []
    for year in arg_list:
        source_file = os.path.normpath(os.path.join(source_dir_path, 'yob' + str(year) + '.txt'))
        names.append(pd.read_csv(source_file, names=columns))
    names_all = pd.concat(names, names=['Year', 'Gender'])
    # print(names_all.head(10))
    # print(names_all.sort_values(by='Count', ascending=False).head(10))
    result = names_all.groupby('Name').sum().sort_values(by='Count', ascending=False).head(3)
    # result.apply(lambda x: res.append(x.Name), axis=1)
    print(result.iloc[0])
    # print([x for x in result.keys()])


def count_dynamics(arg_list):
    global source_path
    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    columns = ['Name', 'Gender', 'Count']
    result_per_gender = {'F': [], 'M': []}
    for year in arg_list:
        source_file = os.path.normpath(os.path.join(source_dir_path, 'yob' + str(year) + '.txt'))
        gend = pd.read_csv(source_file, names=columns).groupby('Gender').sum()
        # print(gend)
        result = gend.query('Gender == "M"')
        result_per_gender['M'].append(result['Count'][0])
        result = gend.query('Gender == "F"')
        result_per_gender['F'].append(result['Count'][0])
    return result_per_gender


def main():
    # print(count_top3([1880]))
    # print(count_top3([1900, 1950, 2000]))
    print(count_dynamics([1900, 1950, 2000]))

    exit(0)


if __name__ == '__main__':
    main()
