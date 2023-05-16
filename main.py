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

    try:
        create_tablecreate_category_query = """
        CREATE TABLE Category(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name VarChar(255) NOT NULL,
        Opisanie VarChar(255)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_category_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

    try:
        create_tablecreate_customer_query = """
        CREATE TABLE customer(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Name varchar (255) NOT NULL, 
        Surname VarChar(255) NOT NULL,
        email VarChar(255),
        phone VarChar(255) NOT NULL,
        passport VarChar(255) NOT NULL,
        login VarChar(20) NOT NULL,
        password VarChar(20) NOT NULL
        
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_customer_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

    try:
        create_tablecreate_pet_query = """
        CREATE TABLE Pet(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Category_ID int (11) NOT NULL,
        Name varchar (255) NOT NULL,
        Photo blob, 
        Opisanie VarChar(255) NOT NULL,
        Poroda VarChar(255) NOT NULL,
        Age VarChar(255) NOT NULL,
        Gender VarChar(255) NOT NULL,
        price Decimal(6,2) NOT NULL,

        FOREIGN KEY(Category_ID) REFERENCES Category(ID)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_pet_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

    try:
        create_tablecreate_cheque_query = """
        CREATE TABLE cheque(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        Data date NOT NULL, 
        payment VarChar(255) NOT NULL,
        id_customer int(11) NOT NULL,

        FOREIGN KEY(id_customer) REFERENCES customer(ID)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_cheque_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

    try:
        create_tablecreate_Basket_query = """
        CREATE TABLE Basket(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_customer int(11) NOT NULL,
        id_pet int(11) NOT NULL,        
         
        FOREIGN KEY(id_customer) REFERENCES customer(ID),
        FOREIGN KEY(id_pet) REFERENCES Pet(ID)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_Basket_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

    try:
        create_tablecreate_sales_query = """
        CREATE TABLE sales(
        ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
        id_cheque int(11) NOT NULL,
        id_pet int(11) NOT NULL,

        FOREIGN KEY(id_cheque) REFERENCES cheque(ID),
        FOREIGN KEY(id_pet) REFERENCES Pet(ID)
        )
        """
        with connection.cursor() as cursor:
            cursor.execute(create_tablecreate_sales_query)
            connection.commit()
    except ValueError as e:
        print("Ошибка")
        print(e)

        try:
            insert_tableinsert_query = """
            INSERT INTO Category ()
            """
            with connection.cursor() as cursor:
                cursor.execute(insert_tableinsert_query)
                connection.commit()
        except ValueError as e:
            print("Ошибка")
            print(e)


    print('Программа выполнена успешно')
except Exception as ex:
    print("Программа выполнена с ошибками")
    print(ex)

finally:
    connection.close()
    print("Соединенеие закрыто")




