import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name,
        cursorclass = pymysql.cursors.DictCursor
    )
    print('Соединение успешно')
    print('.' * 20)
    print('\n')

except Exception as ex:
    print("\nПрограмма выполнена с ошибками")
    print(ex)
