
import sqlite3


def create_connection(db_file):
    connection = None
    try:
        connection = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return connection


my_connection = create_connection('countries.db')
if my_connection is not None:
    print('Успешно подключено')


def get_cities():
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, area, country_id FROM cities")
    cities = cursor.fetchall()
    conn.close()
    return cities


def get_country(country_id):
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM countries WHERE id=?', (country_id,))
    country = cursor.fetchone()
    conn.close()
    return country[0] if country else None


def get_city_info(city_id):
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, area FROM cities WHERE id=?", (city_id,))
    city_info = cursor.fetchone()
    conn.close()
    return city_info


def get_students(city_id):
    conn = sqlite3.connect('countries.db')
    cursor = conn.cursor()
    cursor.execute("SELECT first_name, city_id FROM students WHERE city_id=?", (city_id,))
    students = cursor.fetchall()
    conn.close()
    return students


def main():
    while True:
        print("Вы можете отобразить список учеников по выбранному"
              " id города из перечня городов ниже, для выхода из программы введите 0:")
        cities = get_cities()
        for city in cities:
            country = get_country(city[3])  # Получаем название страны по идентификатору страны
            print(f"{city[0]}: {city[1]}, Страна: {country}")  # Выводим название страны вместе с
        city_id = int(input("Введите id города: "))
        if city_id == 0:
            break

        students = get_students(city_id)
        if students:
            city_name, city_area = get_city_info(city_id)
            country = get_country(cities[city_id-1][3])  # Получаем название страны по id города
            for student in students:
                print(f"Имя: {student[0]}, Город проживания: {city_name}, Страна: {country}, Площадь города: {city_area}")
        else:
            print("Нет учеников в выбранном городе.")


if __name__ == "__main__":
    main()
