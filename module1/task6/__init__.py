"""
Построить круговую диаграмму,
отражающую процентное соотношение умерших пациентов в возрасте до 30 лет включительно,
проведя распределение по регионам Австралии.
"""

from module1.task6 import method1, method2


def run(df):
	print('Задача 6')
	query = 'age <= 30 and status == "D"'
	df_number_dead_before30 = df.query(query)['state'].value_counts().sort_index().to_frame(name='number of dead')
	df_number_dead_before30.reset_index(inplace=True)
	df_number_dead_before30 = df_number_dead_before30.rename(columns={'index': 'state'})
	print('Ratio of deceased patients under 30 years of age:')
	print(df_number_dead_before30.head(5))
	method1.run(df_number_dead_before30)
	method2.run(df_number_dead_before30)
	print()