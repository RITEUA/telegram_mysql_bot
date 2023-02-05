"""
---- Створення таблиці в базі даних mysql
"""

import mysql.connector

# Підключення до бази даних «назва_вашої_бази_даних»
mydb = mysql.connector.connect(
  host="localhost",
  user="ім'я",
  password="пароль",
  database="назва_вашої_бази_даних"
)

mycursor = mydb.cursor()
# Створення таблиці «ім'я_таблиці». Ви можете змінити колонки «країна» та «столиця», на інші, які вам потрібні
mycursor.execute(r"CREATE TABLE назва_вашої_таблиці (країна VARCHAR(255), столиця VARCHAR(255))")

# Для перевірки наявності вашої таблиці у базі даних
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
