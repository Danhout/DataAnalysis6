"""
Сколько аниме с не менее чем 1000 отзывами (оценками) имеют средний рейтинг больше или равный 9?
"""


def run(dfs):
    print('Задача 3')
    df_anime = dfs[0]
    df_rating = dfs[1]
    number_anime_ratings_over1000 = 0
    df_anime_reverse_sort_ratings = df_anime.sort_values('rating', ascending=False)
    revers_sort_ratings = df_anime_reverse_sort_ratings['rating'].values
    number_anime_rating_over9 = 0
    for i in range(revers_sort_ratings.size):
        if revers_sort_ratings[i] < 9:
            number_anime_rating_over9 = i
            break
    for anime_id in df_anime_reverse_sort_ratings.index[:number_anime_rating_over9]:
        if df_rating.query(f'anime_id == {anime_id}').shape[0] >= 1000:
            number_anime_ratings_over1000 += 1
    print(f'{number_anime_ratings_over1000} animes has over 1000 ratings and average rating greater than 9.')
    print()
