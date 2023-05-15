import pymysql
from config import host, user, password, db_name


try:
    connection = pymysql.connect(
        host = host,
        port = 3306,
        user = user,
        password = password,
        database = db_name
    )
    print('Соединение успешно')
except Exception as ex:
    print("Соединение не установлено")
    print(ex)



# try:
#     create_db_query = """
#     CREATE DATABASE ZooShop;
#     """
#     with connection.cursor() as cursor:
#         cursor.execute(create_db_query)
#         connection.commit()
# except ValueError as e:
#     print("Ошибка")
#     print(e)



try:
    create_tablecreate_category_query = """
    USE ZooShop
    CREATE TABLE Category(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Category VarChar(255),
    Opisanie VarChar(255),
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_tablecreate_category_query)
        connection.commit()
except ValueError as e:
    print("Ошибка")
    print(e)



try:
    create_tablecreate_pet_query = """
    USE ZooShop
    CREATE TABLE Pet(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Category ID int (11) NOT NULL,
    Name varchar (255),
    Photo blob,
    Opisanie VarChar(255),
    Poroda VarChar(255),
    Age VarChar(255),
    Gender VarChar(255),
    price Decimal(10,2),
    
    FOREIGN KEY(Category) REFERENCES Category(ID),
    )
    """
    with connection.cursor() as cursor:
        cursor.execute(create_tablecreate_pet_query)
        connection.commit()
except ValueError as e:
    print("Ошибка")
    print(e)

