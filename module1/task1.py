"""
Чтение данных из файла Aids2.csv и загрузка их в датафрейм.
"""

import pandas as pd


def get_data_frame():
	print('Задача 1')
	df = pd.read_csv('src/Aids2.csv')
	# Удаление неразличимых столбцов из исходного датафрейма
	df.drop(['Unnamed: 0', 'diag', 'death'], axis='columns', inplace=True)
	# Вывод 5 первых строк фрейма
	print('Dataframe:')
	print(df.head(5))
	print()
	return df
