"""
В какой возрастной группе (до 30, от 31 до 54, от 55) процен выживших пациентов больше, чем умерших?
Если таких несколько, перечислите все.
"""

import matplotlib.pyplot as plt


def run(df):
	print('Задача 10')
	data_young_frame = df.query('age <= 30')
	data_midlife_frame = df.query('31 <= age <= 54')
	data_old_frame = df.query('55 <= age')
	pct_alive_young = data_young_frame.query('status == "A"').shape[0] / data_young_frame.shape[0] * 100
	pct_alive_midlife = data_midlife_frame.query('status == "A"').shape[0] / data_midlife_frame.shape[0] * 100
	pct_alive_old = data_old_frame.query('status == "A"').shape[0] / data_old_frame.shape[0] * 100
	title = 'The survival rate depending on the age'
	font_title = {'family': 'serif', 'color': 'darkred'}
	font_label = {'family': 'serif', 'color': 'darkgreen'}
	plt.bar(['under 30', 'over 31 and under 54', 'over 55'], [pct_alive_young, pct_alive_midlife, pct_alive_old])
	plt.title(title, fontdict=font_title)
	plt.xlabel('Age', fontdict=font_label)
	plt.ylabel('Percents of survival', fontdict=font_label)
	plt.ylim(0, 100)
	plt.grid(axis='y')
	plt.show()
