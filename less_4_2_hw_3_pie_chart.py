"""lesson_4_2_Homework "Data visualization"

"""

import os

import pandas as pd

source_path = 'D:\Python_my\Python_Netology_homework\data_names'
source_dir_path = os.path.normpath(os.path.abspath(source_path))


def main():
    source_path = 'D:\Python_my\Python_Netology_homework\data_names'
    source_dir_path = os.path.normpath(os.path.abspath(source_path))
    source_file = os.path.normpath(os.path.join(source_dir_path, 'yob{}.txt'.format(1950)))
    year_data = pd.read_csv(source_file, names=['Name', 'Gender', 'Count'])
    year_data = year_data.drop(['Gender'], axis=1)
    r_name = year_data[(year_data.Name.str.startswith('R'))]
    top_10 = r_name.groupby('Name').sum().sort_values('Count', ascending=False).head(10)
    print(top_10)
    top_10.plot.pie(y='Count')

    exit(0)


if __name__ == '__main__':
    main()
