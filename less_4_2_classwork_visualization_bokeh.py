"""lesson_4_2_Classwork "Data visualization"

"""

import pandas as pd


# from bokeh.plotting import figure, output_notebook, show


def main():
    # x = [1,2,3,4,5]
    # y = [6,7,2,4,5]
    # output_notebook()
    # p = figure(title='simple line example', x_axis_label='x', y_axis_label='y')
    # p.line(x, y, legend='Temp.', line_width=2)
    # show(p)

    names_by_year = {}
    for year in range(1900, 2001, 10):
        names_by_year[year] = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob{}.txt'.format(year),
                                          names=['Name', 'Gender', 'Count'])
    names_all = pd.concat(names_by_year, names=['Year', 'Pos'])
    # name_common_dynamics = names_all.groupby(level=0).sum()
    # name_common_dynamics.reset_index(level=0, inplace=True)
    exit(0)


if __name__ == '__main__':
    main()
