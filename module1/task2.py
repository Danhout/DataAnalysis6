"""
Узнать информацию о размере датасета и типах хранящихся в нём данных.
"""


def run(df):
	print('Задача 2')
	# типы данных каждого столбца
	print('dtypes:')
	print(df.dtypes)
	# количество строк умноженное на количество столбцов
	print('size:')
	print(df.size)
	# количество строк и стролбцов
	print('shape:')
	print(df.shape)
	print()
