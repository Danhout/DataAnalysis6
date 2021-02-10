"""
Показать, как соотносятся возраст и смертность у пациентов старше 14 лет (включительно с 14 годами).
Построить график функции.
"""

from module1.task5 import method1, method2


def run(df):
	print('Задача 5')
	query = 'age >= 14 and status == "D"'
	df_age_over14_number_dead = df.query(query)['age'].value_counts().sort_index().to_frame(name='number of dead')
	df_age_over14_number_dead.reset_index(inplace=True)
	df_age_over14_number_dead = df_age_over14_number_dead.rename(columns={'index': 'age'})
	print('Age-to-death ratio in patients over 14 years of age:')
	print(df_age_over14_number_dead.head(5))
	method1.run(df_age_over14_number_dead)
	method2.run(df_age_over14_number_dead)
	print()
