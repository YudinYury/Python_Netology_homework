"""lesson_4_2_Classwork "Data visualization"

"""

import numpy as np
import pandas as pd


def main():
    source_path = 'D:\Python_my\Python_Netology_homework\data_names'

    df = pd.DataFrame(np.random.randn(50, 3), columns=['Z', 'B', 'C'])
    plot = df.plot()
    fig = plot.get_figure()
    fig.savefig('less_4_2_fig_graph.png')
    names_by_year = {}
    for year in range(1900, 2001, 10):
        names_by_year[year] = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob{}.txt'.format(year),
                                          names=['Name', 'Gender', 'Count'])
    names_all = pd.concat(names_by_year, names=['Year', 'Pos'])
    # print(names_all.head(10))
    name_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
    # print(name_dynamics.head(10))
    print(name_dynamics.query('Name == ["John", "Mary", "William"]'))
    print(name_dynamics.query('Name == ["John", "Mary", "William"]').unstack('Name').plot)
    gender_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
    gender_dynamics_cols = gender_dynamics.unstack('Gender')
    gender_dynamics_cols.plot(title='Dynamics', grid=True)
    name_dynamics.query('Name == ["John", "Mary", "William"]').unstack('Name').plot.bar()
    names_for_pie = names_all.groupby('Name').sum().sort_values(by='Count', ascending=False).head(5)
    names_for_pie.plot.pie(y='Count')
    # names = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob2000.txt', names=['Name', 'Gender', 'Count'])
    # print(names.head(10))

    exit(0)


if __name__ == '__main__':
    main()
