"""
Метод plot.line.
"""

import matplotlib.pyplot as plt


def run(df):
	print('Способ 1 (см. раздел plots)')
	font_title = {'family': 'serif', 'color': 'darkred'}
	font_label = {'family': 'serif', 'color': 'darkgreen'}
	df.plot.line(x='age', y='number of dead')
	plt.title('Number of dead over 14 years old (Method 1)', fontdict=font_title)
	plt.xlabel('Age', fontdict=font_label)
	plt.ylabel('Number of dead', fontdict=font_label)
	plt.legend('', frameon=False)
	plt.grid(True)
	plt.axis([14, df['age'].max(), 0, df['number of dead'].max()])
	plt.show()
