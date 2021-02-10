"""
Датасет Australian AIDS Survival Data,
хранящий данные о пациентах,
проходивших лечение от СПИДа до 1 июля 1991.

Датасет содержит 2843 строки и следующие столбцы:
* state -Аббревиатура названия региона Австралии.
* sex - Пол пациента.
* diag* - Дата диагноза.
* death* - Дата смерти или окончания лечения.
* status - "A" (жив) или "D" (мёртв) на момент окончания лечения.
* T.categ - Способ заражения.
* age - Возраст, когда пациенту был поставлен диагноз.
"""

from module1 import task1, task2, task3, task4, task5, task6, task7, task8, task9, task10


def run():
	df = task1.get_data_frame()
	task2.run(df)
	task3.run(df)
	task4.run(df)
	task5.run(df)
	task6.run(df)
	task7.run(df)
	task8.run(df)
	task9.run(df)
	task10.run(df)
