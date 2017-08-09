"""lesson_4_2_Classwork "Data visualization"

"""

import matplotlib.pyplot as plt
import pandas as pd


def scatter_len(group):
    plt.plot(group['Len'], group['Count'], 'o', label=group.name)


def main():
    names = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob2000.txt',
                        names=['Name', 'Gender', 'Count'])
    print(names.head(10))
    print('----------------  Print len of name  ----------------------')
    names['Len'] = names.apply(lambda row: len(row.Name), axis=1)
    print(names.head(10))
    names.plot.scatter(x='Len', y='Count')
    names.groupby('Gender').sum()

    names.groupby('Gender').apply(scatter_len)
    plt.xlabel('Len')
    plt.ylabel('Count')
    plt.legend()

    exit(0)


if __name__ == '__main__':
    main()
