# Фильмы о поездах
# Выведите фильмы ('Movie'), в названии которых
# встречается слово “train”.
#
# +-------------------------------------+
# |                title                |
# +-------------------------------------+
# |                23:59                |
# |              100 Meters             |
# |              14 Blades              |
# +-------------------------------------+
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
import prettytable

con = sqlite3.connect("../netflix.db")
cur = con.cursor()
sqlite_query = """
               SELECT title
               FROM netflix 
               WHERE title LIKE '%train%' 
               AND "type" = 'Movie'
               """
result = cur.execute(sqlite_query)

# не удаляйте код дальше, он нужен для вывода результата
# запроса в красивом формате

mytable = prettytable.from_db_cursor(result)
mytable.max_width = 30

if __name__ == '__main__':
    print(mytable)
