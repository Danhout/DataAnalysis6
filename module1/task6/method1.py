"""
Метод plot.pie.
"""

import matplotlib.pyplot as plt


def run(df):
	print('Способ 1 (см. раздел plots)')
	values = df['number of dead']
	sum_values = sum(values)
	explode = [0.05] * values.count()
	labels = df['state']
	autopct = lambda pct: f'{round(pct, 1)}%\n{round(pct * sum_values / 100)} people'
	wedgeprops = dict(width=0.8, edgecolor='w')
	df.plot.pie(y='number of dead', explode=explode, shadow=True, autopct=autopct,
	            startangle=-90, wedgeprops=wedgeprops, labeldistance=None)
	title = 'The number of deaths up to 30 years in the Australian States (Method 1)'
	font_title = {'family': 'serif', 'color': 'darkred'}
	plt.title(title, fontdict=font_title)
	plt.legend(labels)
	plt.show()
