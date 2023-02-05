"""
---- Отримання та відображання даних з таблиці бази даних mysql
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

# Отримуємо кортежі рядків з таблиці
mycursor.execute("SELECT * FROM назва_вашої_таблиці")
myresult = mycursor.fetchall()
for rows in myresult:
    print(rows)
