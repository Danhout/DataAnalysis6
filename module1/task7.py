"""
Подсчитать средний возраст умерших в представленный в датасете период от СПИДа пациентов для каждого региона и для Астралии в целом.
Результат представить гистограммой с группировкой.
"""

import pandas as pd
import matplotlib.pyplot as plt


def run(df):
	print('Задача 7')
	df_state_mean_age_dead = pd.DataFrame(columns=['state', 'median age'])
	states = df['state'].drop_duplicates()
	states.reset_index(inplace=True, drop=True)
	for i in range(states.size):
		query = f'status == "D" and state == "{states[i]}"'
		df_state_mean_age_dead.loc[i] = [states[i], df.query(query)['age'].mean()]
	df_state_mean_age_dead.loc[states.size] = ['all', df.query('status == "D"')['age'].mean()]
	print('Average age of deaths in the States:')
	print(df_state_mean_age_dead)
	title = 'Average age of death in Australian States'
	font_title = {'family': 'serif', 'color': 'darkred'}
	font_label = {'family': 'serif', 'color': 'darkgreen'}
	df_state_mean_age_dead.plot.bar(x='state', color='darkred', rot=0)
	plt.title(title, fontdict=font_title)
	plt.xlabel('State', fontdict=font_label)
	plt.grid(axis='y', color='k')
	plt.show()
	print()
