# Самый длинный фильм
# Теперь нам нужно узнать, какой самый длинный
# фильм среди тех, которые были сняты в 2019 году.
# Выводим название и его длительность.
#
# Пример результата:
# 100 Meters — 200 минут
#
# Структура таблицы
# -----------------------
# show_id — id тайтла
# type — фильм или сериал
# title — название
# director — режиссер
# cast — основные актеры
# country — страна производства
# date_added — когда добавлен на Нетфликс
# release_year — когда выпущен в прокат
# rating — возрастной рейтинг
# duration — длительность
# duration_type — минуты или сезоны
# listed_in — список жанров и подборок
# description — краткое описание
# -----------------------
import sqlite3

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = """
               SELECT title, duration
               FROM netflix
               WHERE "type" = 'Movie'
               AND release_year = 2019
               ORDER BY duration DESC 
               LIMIT 1
               """
cur.execute(sqlite_query)
result = cur.fetchall()

# TODO Результат запроса сохраните в переменной result
# для последующей выдачи в требуемом формате

movie_title = result[0][0]
duration = result[0][1]
result = (f'{movie_title} — {duration} минут')

if __name__ == '__main__':
    print(result)
