"""
Датасет Anime Recommendations Database, хранящий информацию о предпочтениях 73 516 пользователей на 12 294 аниме.

Датасет содержит 2 CSV файла:

Anime.csv, датафрейм которого содержит 12 294 строк и следующие столбцы:
* anime_id - уникальный идентификатор аниме
* name - название
* genre - список жанров
* type - тип, напр. TV, OVA, и.т.д.
* episodes - количество серий
* rating - средний рейтинг (от 0 до 10)
* members - количество участников группы этого аниме

Rating.csv, датафрейм которого содержит 7 813 737 строк и следующие столбцы:
* user_id - случайный идентификатор пользователя
* anime_id - идентификатор оцениваемого аниме
* rating - рейтинг (от 0 до 10)
"""

from module2 import task1, task2, task3, task4, task5


def run():
	dfs = task1.get_data_frames()
	task2.run(dfs)
	task3.run(dfs)
	task4.run(dfs)
	task5.run(dfs)
