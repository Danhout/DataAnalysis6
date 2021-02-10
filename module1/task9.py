"""
Какими способами происходило заражение СПИДом по регионам?
Результат в виде количества случаев заражения визуализируйте гистограммой.
"""

import pandas as pd
import matplotlib.pyplot as plt


def run(df):
	print('Задача 9')
	states = df['state'].drop_duplicates()
	states.reset_index(inplace=True, drop=True)
	t_categories = df['T.categ'].drop_duplicates()
	t_categories.reset_index(inplace=True, drop=True)
	states_t_categories_frame = pd.DataFrame(columns=t_categories.values)
	for state in states:
		data_state_frame = df.query(f'state == "{state}"')
		state_t_categories_sizes = []
		for t_categ in t_categories:
			state_t_categories_sizes.append(data_state_frame.loc[data_state_frame['T.categ'] == t_categ].shape[0])
		states_t_categories_frame.loc[state] = state_t_categories_sizes
	states_t_categories_frame.plot.bar(rot=0)
	title = 'The number of infected by States, depending on the method of infection'
	font_title = {'family': 'serif', 'color': 'darkred'}
	font_label = {'family': 'serif', 'color': 'darkgreen'}
	plt.title(title, fontdict=font_title)
	plt.xlabel('States', fontdict=font_label)
	plt.ylabel('Number of patients', fontdict=font_label)
	plt.grid(axis='y')
	plt.legend(title='T.categ')
	plt.show()
	print()
