"""
Основываясь на информации из датасета, выяснить,
кого больше в процентном соотношении: мужчин или женщин,
зазазившихся СПИДом.
"""


def run(df):
	print('Задача 3')
	df_males = df.loc[df['sex'] == 'M']
	df_females = df.loc[df['sex'] == 'F']
	print('Number of people infected with AIDS in Australia:')
	print(f'males: {round(df_males.shape[0] / df.shape[0] * 100, 2)}%')
	print(f'females: {round(df_females.shape[0] / df.shape[0] * 100, 2)}%')
	print()
