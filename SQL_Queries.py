create_tablecreate_category_query = """
    CREATE TABLE Category(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name VarChar(255) NOT NULL,
    Opisanie VarChar(255)
    )
    """

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
    price Decimal(8,2) NOT NULL,

    FOREIGN KEY(Category_ID) REFERENCES Category(ID)
    )
    """

create_tablecreate_cheque_query = """
    CREATE TABLE cheque(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Data date NOT NULL, 
    payment VarChar(255) NOT NULL,
    id_customer int(11) NOT NULL,

    FOREIGN KEY(id_customer) REFERENCES customer(ID)
    )
    """

create_tablecreate_Basket_query = """
    CREATE TABLE Basket(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_customer int(11) NOT NULL,
    id_pet int(11) NOT NULL,        

    FOREIGN KEY(id_customer) REFERENCES customer(ID),
    FOREIGN KEY(id_pet) REFERENCES Pet(ID)
    )
    """

create_tablecreate_sales_query = """
    CREATE TABLE sales(
    ID int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    id_cheque int(11) NOT NULL,
    id_pet int(11) NOT NULL,

    FOREIGN KEY(id_cheque) REFERENCES cheque(ID),
    FOREIGN KEY(id_pet) REFERENCES Pet(ID)
    )
    """

insert_tableinsert_query = """
    INSERT INTO Category (Name, Opisanie) VALUES ('Кошка','Мяу');
    INSERT INTO Category (Name, Opisanie) VALUES ('Собака','Гав');
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Милаха', 3 , 'Кошка', 1, 'Шотландская вислоухая', 'Уши внизу', 15000.00);
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Кусака', 1 , 'Кот', 1, 'Сфинкс', 'Укусила меня за бочок', 10000.00);
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Соня', 6 , 'Сука', 2, 'Венгеская овчарка', 'Очень спокойная', 50000.00);
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Кин', 2 , 'Сука', 2, 'Сиба-ину', 'Тявкалка', 35000.00);
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Тутао', 3 , 'Кобель', 2, 'Доберман', 'Уши не купированы', 20000.00);
    INSERT INTO pet(Name, Age, Gender, Category_ID, Poroda, Opisanie, price) VALUES ('Берия', 2 , 'Кобель', 2, 'Нагази', 'Приготовит вам хинкали', 999999.99);
    INSERT INTO customer(`Name`, `Surname`, `email`, `phone`, `passport`, `login`, `password`) VALUES ('Geordge', 'Geordge', 'Geordge@mail.com',  '+7-999-999-99-99', '41 14 411114', 'KOOOK', 'Passik');
    INSERT INTO customer(`Name`, `Surname`, `phone`, `passport`, `login`, `password`) VALUES ('Hoip', 'Edge', '+7-999-666-59-95', '41 14 433114', 'LOI', 'Pasok');
    INSERT INTO customer(`Name`, `Surname`, `email`, `phone`, `passport`, `login`, `password`) VALUES ('Kol', 'L', 'KOOOOOOOOOOOOOOL@mail.com',  '+7-999-444-54-45', '41 14 451344', 'KOL', 'Pask');
    """

max_cost_pet = """ 
    SELECT * FROM Pet
    ORDER BY price
    DESC LIMIT 1;
    """

max_categoty_pet = """
    SELECT Category_ID, COUNT(*) AS count FROM Pet 
    GROUP BY Category_ID
	ORDER BY count
    DESC LIMIT 1;
    """

all_koshka_pet = """ 
    SELECT * FROM Pet
    ORDER BY Category_ID;
    """

all_customers = """ 
    SELECT * FROM cheque
    INNER JOIN customer
    ON cheque.id_customer = customer.ID;
    """