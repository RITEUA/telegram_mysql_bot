import mysql.connector

# Підключення до бази даних «назва_вашої_бази_даних»
mydb = mysql.connector.connect(
    host="localhost",
    user="ім'я",
    password="пароль",
    database="назва_вашої_бази_даних"
)
mycursor = mydb.cursor()
# Режим SELECT, для отримання даних з таблиці «назва_вашої_таблиці»
mycursor.execute("SELECT * FROM назва_вашої_таблиці")
myresult = mycursor.fetchall()


# Дістаємо зі списку myresult, усі кортежі, 0 індекс яких це назви країн, а 1 - їх столиці
def get_data() -> str:
    result = ""
    for rows in myresult:
        result += f"{rows[0]}: {rows[1]}\n"
    return result  # Повертаємо рядок з усіма країни: столиці
