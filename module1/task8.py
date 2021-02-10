"""
Определить возраст самого молодого и самого старого умерших пациентов в каждом регионе.
В каких регионах среди инфицированных было больше пожилых людей (от 55)?
В каких преобладает моодёжь (до 30)?
В каких больше всего людей среднего возраста (от 31 до 54)?
"""


def func_age_statistic(df):
	df_dead = df.query('status == "D"')
	df_dead_ages = df_dead['age']
	min_age_dead = df_dead_ages.min()
	max_age_dead = df_dead_ages.max()
	print(f'The youngest deceased patient was {min_age_dead} years old')
	print(f'The oldest deceased patient was {max_age_dead} years old')
	number_young = df.query('age <= 30')['age'].size
	number_midlife = df.query('31 <= age <= 54')['age'].size
	number_old = df.query('age >= 55')['age'].size
	main_ages = []
	if number_young >= number_midlife and number_young >= number_old:
		main_ages.append('young')
	if number_midlife >= number_young and number_midlife >= number_old:
		main_ages.append('midlife')
	if number_old >= number_young and number_old >= number_midlife:
		main_ages.append('old')
	print(f'There are the most {str(main_ages)} patients here')


def run(df):
	print('Задача 8')
	states = df['state'].drop_duplicates()
	states.reset_index(inplace=True, drop=True)
	print('All States:')
	func_age_statistic(df)
	for state in states:
		print(f'State "{state}":')
		func_age_statistic(df.query(f'state == "{state}"'))
	print()
