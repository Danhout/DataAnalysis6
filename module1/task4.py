"""
Выяснить, каков процент мужчин до 45 лет, успешно прошедших курс лечения,
по отношению к общему количеству заболевших мужчин.
"""


def run(df):
	print('Задача 4')
	df_males = df.query('sex == "M"')
	df_alive_under45_males = df_males.query('age <= 45 and status == "A"')
	print(f'Percentage of live males under 45 years of age from all males: ', end='')
	print(f'{round(df_alive_under45_males.shape[0] / df_males.shape[0] * 100, 2)}%')
	print()
