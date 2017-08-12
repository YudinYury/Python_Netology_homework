"""lesson_4_2_Homework "Data visualization"

"""

import os

import pandas as pd

source_path = 'D:\Python_my\Python_Netology_homework\data_names'
source_dir_path = os.path.normpath(os.path.abspath(source_path))


def download_year_data(year):
    source_file = os.path.normpath(os.path.join(source_dir_path, 'yob{}.txt'.format(year)))
    year_data = pd.read_csv(source_file, names=['Name', 'Gender', 'Count'])
    # year_data['Year'] = year_data.apply(lambda x: int(year), axis=1)
    year_data = year_data.drop(['Gender'], axis=1)
    # print(year_data.query('Name == "Ruth" | Name == "Robert"').groupby('Name').sum())
    return year_data.query('Name == ["Ruth", "Robert"]').groupby('Name').sum()


def ruth_n_robert():
    global source_dir_path
    names = []
    names_dict = {}
    # ruth_n_robert_all_time = reduce(lambda x,y: pd.concat([x,y]), [download_year_data(i) for i in range(1900, 1903)])
    # data = download_year_data(1900)
    ruth_n_robert_all_time = {}
    for i in range(1900, 1904):
        # ruth_n_robert_all_time = pd.concat([data, download_year_data(i)])
        # names.append(download_year_data(i))
        names_dict[i] = download_year_data(i)

    ruth_n_robert_all_time = pd.concat(names_dict, names=['Year'])
    # print(ruth_n_robert_all_time)
    print()
    # print(ruth_n_robert_all_time.unstack('Name'))
    ruth_n_robert_all_time.unstack('Name').plot(title='Ruth vs Robert', grid=True)
    # gender_dynamics_cols.plot(title='Dynamics', grid=True)




    return 0


def main():
    ruth_n_robert()

    # df = pd.DataFrame(np.random.randn(50, 3), columns=['Z', 'B', 'C'])
    # plot = df.plot()
    # fig = plot.get_figure()
    # fig.savefig('less_4_2_fig_graph.png')
    # names_by_year = {}
    # for year in range(1900, 2001, 10):
    #     names_by_year[year] = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob{}.txt'.format(year),
    #                                       names=['Name', 'Gender', 'Count'])
    # names_all = pd.concat(names_by_year, names=['Year', 'Pos'])
    # # print(names_all.head(10))
    # name_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
    # # print(name_dynamics.head(10))
    # print(name_dynamics.query('Name == ["John", "Mary", "William"]'))
    # print(name_dynamics.query('Name == ["John", "Mary", "William"]').unstack('Name').plot)
    # gender_dynamics = names_all.groupby([names_all.index.get_level_values(0), 'Name']).sum()
    # gender_dynamics_cols = gender_dynamics.unstack('Gender')
    # gender_dynamics_cols.plot(title='Dynamics', grid=True)
    # name_dynamics.query('Name == ["John", "Mary", "William"]').unstack('Name').plot.bar()
    # names_for_pie = names_all.groupby('Name').sum().sort_values(by='Count', ascending=False).head(5)
    # names_for_pie.plot.pie(y='Count')
    # names = pd.read_csv('D:\Python_my\Python_Netology_homework\data_names\yob2000.txt', names=['Name', 'Gender', 'Count'])
    # print(names.head(10))

    exit(0)


if __name__ == '__main__':
    main()
