"""
Библиотека plotly.
"""

import plotly.express as px


def run(df):
	print('Способ 2 (см. в браузере)')
	title = 'Number of dead over 14 years old (Method 2)'
	px.line(df, x='age', y='number of dead', title=title).show()
