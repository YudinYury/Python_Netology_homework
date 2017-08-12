"""lesson_4_2_Homework "Data visualization"

"""

import os

import matplotlib.pyplot as plt
import pandas as pd

source_path = 'D:\Python_my\Python_Netology_homework\data_names'
source_dir_path = os.path.normpath(os.path.abspath(source_path))


def scatter_len(group):
    plt.plot(group['Len'], group['Count'], 'o', label=group.name)


def count_consonant(name):
    count = 0
    for ch in name.lower():
        if ch in 'qwrtypsdfghjklzxcvbnm':
            count += 1
        else:
            pass
    return count


def main():
    names_dict = {}
    names_list = []
    for i in range(1900, 1905):
        source_file = os.path.normpath(os.path.join(source_dir_path, 'yob{}.txt'.format(i)))
        year_data = pd.read_csv(source_file, names=['Name', 'Gender', 'Count'])
        year_data = year_data.drop(['Gender'], axis=1)
        year_data['consonants'] = year_data.apply(lambda row: count_consonant(row.Name), axis=1)

        # year_data = year_data.groupby('Name').sum().sort_values(by='Count', ascending=False).head(5)
        year_data = year_data.groupby('Name').sum().sort_values(by='Count', ascending=False)
        names_list.append(year_data)

    century_data = pd.concat(names_list)
    century_data = century_data.groupby('Name').sum().sort_values(by='Count', ascending=False)
    # century_data = century_data.groupby('Name')
    print(century_data)
    # century_data['consonants'] = century_data.apply(lambda row: count_consonant(row.Name), axis=1)
    print(century_data)

    # plt.xlabel('consonants')
    # plt.ylabel('Count')
    # plt.legend()


    # century_data.groupby('Gender').apply(scatter_len)


    exit(0)


if __name__ == '__main__':
    main()
