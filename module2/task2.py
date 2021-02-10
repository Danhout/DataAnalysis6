"""
Найти аниме, которое имеет максимальный средний рейтинг и количество оценок которого больше или равно 1000.
"""


def run(dfs):
    print('Задача 2')
    df_anime = dfs[0]
    df_rating = dfs[1]
    df_anime_reverse_sort_ratings = df_anime.sort_values('rating', ascending=False)
    for anime_id in df_anime_reverse_sort_ratings.index:
        number_ratings = df_rating.query(f'anime_id == {anime_id}').shape[0]
        if 1000 <= number_ratings:
            anime_name = df_anime.loc[anime_id].at['name']
            rating = df_anime.loc[anime_id].at['rating']
            print(f'Anime \'{anime_name}\' with anime_id \'{anime_id}\' has the maximum average rating \'{rating}\'')
            break
    print()
