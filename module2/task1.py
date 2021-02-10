"""
Прочитать данные из файлов Anime.csv, Rating.csv и загрузить их в датафреймы.
"""

import pandas as pd


def get_data_frames():
    print('Задача 1')
    # Data:
    # 2 Files with datasets in google.drive
    filename_anime = 'src/Anime.csv'
    filename_rating = 'src/Rating.csv'

    # Decision:
    # read data from files
    df_anime = pd.read_csv(filename_anime).set_index('anime_id').sort_index()
    df_rating = pd.read_csv(filename_rating)

    # result of program:
    print('Dataframe with animes:')
    print(df_anime.head(5))
    print()
    print('Dataframe with ratings:')
    print(df_rating.head(5))
    ## If you want to check statement (*) (Замечание) you can run the code below and change variables 'anime_id_begin' and 'anime_id_end'.
    ## The variables can be equal from 0 to 12 294 (number of rows in df_anime) but the distance can't be big, because the program isn't optimized.
    # anime_id_begin = 0
    # anime_id_end = 100
    # for anime_id in df_anime.index[anime_id_begin:anime_id_end]:
    #  if df_anime.loc[anime_id].at['rating'] == df_rating.query('anime_id == 1')['rating'].mean():
    #    print(anime_id)
    print()
    return [df_anime, df_rating]
