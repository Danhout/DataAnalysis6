"""
Постройте график, который показывает разницу между средними оценками аниме датафреймов из файлов Anime.csv и Rating.csv.
"""

import pandas as pd
import math
import matplotlib.pyplot as plt


def run(dfs):
    print('Задача 5')
    df_anime = dfs[0]
    df_rating = dfs[1]
    anime_ids = df_anime.index.values
    anime_ids_df_rating = df_rating['anime_id'].drop_duplicates().values
    anime_ids.sort()
    anime_ids_df_rating.sort()
    df_ratings = pd.DataFrame(index=anime_ids, columns=['df_anime', 'df_rating'])
    array_pair_sum_ratings_number_ratings = [[0 for j in range(2)] for i in range(anime_ids.max() + 1)]
    for i in df_rating.index.values:
        anime_id = df_rating.at[i, 'anime_id']
        rating = df_rating.at[i, 'rating']
        array_pair_sum_ratings_number_ratings[anime_id][0] += rating
        array_pair_sum_ratings_number_ratings[anime_id][1] += 1
    for anime_id in anime_ids:
        rating_df_anime = df_anime.at[anime_id, 'rating']
        if math.isnan(rating_df_anime):
            rating_df_anime = 0
        rating_df_rating = 0
        if anime_id in anime_ids_df_rating:
            sum_ratings = array_pair_sum_ratings_number_ratings[anime_id][0]
            number_ratings = array_pair_sum_ratings_number_ratings[anime_id][1]
            if number_ratings != 0:
                rating_df_rating = sum_ratings / number_ratings
        df_ratings.loc[anime_id] = [rating_df_anime, rating_df_rating]
    # print(df_ratings)
    df_diffs_anime_rating_ratings = pd.DataFrame(index=anime_ids, columns=['diff_rating'])
    df_ratings_copy = df_ratings
    for anime_id in anime_ids:
        diff = df_ratings_copy.at[anime_id, 'df_anime'] - df_ratings_copy.at[anime_id, 'df_rating']
        df_diffs_anime_rating_ratings.loc[anime_id] = diff
    df_diffs_anime_rating_ratings = df_diffs_anime_rating_ratings.sort_values('diff_rating')
    df_diffs_anime_rating_ratings.reset_index(inplace=True, drop=True)
    # print(df_diffs_anime_rating_ratings)
    title = 'Difference between the average ratings of Anime.csv and Rating.csv'
    min_diff = df_diffs_anime_rating_ratings['diff_rating'].min()
    max_diff = df_diffs_anime_rating_ratings['diff_rating'].max()
    font_title = {'family': 'serif', 'color': 'darkred'}
    font_label = {'family': 'serif', 'color': 'darkgreen'}
    df_diffs_anime_rating_ratings.plot.area(by='diff_rating', stacked=False)
    plt.title(title, fontdict=font_title)
    plt.xlabel('Number of anime (not id of anime)', fontdict=font_label)
    plt.legend('', frameon=False)
    plt.axis([0, df_diffs_anime_rating_ratings.shape[0], min_diff, max_diff])
    plt.show()
    df_ratings_copy = df_ratings_copy.sort_values('df_anime')
    df_ratings_copy.reset_index(inplace=True, drop=True)
    df_rating_sort_column = df_ratings_copy['df_rating']
    df_rating_sort_column = df_rating_sort_column.sort_values()
    df_rating_sort_column.reset_index(inplace=True, drop=True)
    df_ratings_copy['df_rating'] = df_rating_sort_column
    title = 'Average ratings of animes in files Animve.csv and Rating.csv'
    df_ratings_copy.plot.area(stacked=False)
    plt.title(title, fontdict=font_title)
    plt.xlabel('Number of anime (not id and the numbers are different for 2 dataframes)', font_label)
    plt.legend(labels=['Anime.csv', 'Rating.csv'])
    plt.axis([0, df_ratings_copy.shape[0], -1, 10])
    plt.show()
    print()
