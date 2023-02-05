"""
---- Створення бази даних mysql
"""

import mysql.connector

# Підключення до бази даних
mydb = mysql.connector.connect(
  host="localhost",
  user="ім'я",
  password="пароль"
)

mycursor = mydb.cursor()
# Створення бази даних під назвою «назва_вашої_бази_даних»
mycursor.execute("CREATE DATABASE назва_вашої_бази_даних")
