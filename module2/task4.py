"""
Какое аниме имеет наибольшее количество отзывов (оценок)?
"""


def run(dfs):
    print('Задача 4')
    df_anime = dfs[0]
    df_rating = dfs[1]
    anime_ids = df_rating['anime_id'].values
    max_anime_id = anime_ids.max()
    array_anime_id_ratings = [0] * (max_anime_id + 1)
    for anime_id in anime_ids:
        array_anime_id_ratings[anime_id] += 1
    max_numbers_ratings = max(array_anime_id_ratings)
    anime_ids_with_max_numbers_ratings = []
    for anime_id in range(max_anime_id + 1):
        if array_anime_id_ratings[anime_id] == max_numbers_ratings:
            anime_ids_with_max_numbers_ratings.append(anime_id)
    if len(anime_ids_with_max_numbers_ratings) == 1:
        anime_id = anime_ids_with_max_numbers_ratings[0]
        anime_name = df_anime.at[anime_id, 'name'] if anime_id in df_anime.index.values else '?'
        print(
            f'Anime \'{anime_name}\' with anime_id \'{anime_id}\' has the highest number of ratings equal to {max_numbers_ratings}')
    else:
        print('Animes:')
        for anime_id in anime_ids_with_max_numbers_ratings:
            anime_name = df_anime.at[anime_id, 'name'] if anime_id in df_anime.index.values else '?'
            print(f'\'{anime_name}\' with anime_id \'{anime_id}\'')
        print(f'have the highest number of ratings equal to {max_numbers_ratings}')
    print()
