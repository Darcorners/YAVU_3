import ConnDB
import bcrypt
from ConnDB import connection
try:
    with connection.cursor() as cursor:
        print("Авторизация - 1, Регистрация - 2:")
        ent = int(input())
        if ent == 1:
            print('Введите логин или E-mail')
            login = input()
            print('Введите пароль')
            passw = input()
            select_login = f""" SELECT id FROM customer
            WHERE (`login` = '{login}' OR `email` = '{login}') AND `password` = '{passw}' """
            cursor.execute(select_login)
            res_select_login = cursor.fetchall()
            if res_select_login:
                print("Вход успешен")
            else:
                print("Ошибка, неверный логин или пароль")
        if ent == 2:
            print('Введите имя: ')
            name = input()
            print('Введите фамилию: ')
            Surname = input()
            print('Введите почту (по желанию): ')
            email = input()
            print('Введите номер телефона')
            number = input()
            print('Введите номер паспорта и серию')
            passport = input()
            print('Введите логин')
            login = input()
            print('Введите пароль')
            password = input()
            select_registrate= f""" INSERT INTO customer(`Name`, `Surname`, `email`, `phone`, `passport`, `login`, `password`) VALUES ('{name}', '{Surname}', '{email}', '{number}', '{passport}', '{login}','{password}'); """
            cursor.execute(select_registrate)
            connection.commit()
except Exception as ex:
    print("\nПрограмма выполнена с ошибками")
    print(ex)

    # Adding the salt to password
    #  salt = bcrypt.gensalt()
    # Hashing the password
    #  hashed = bcrypt.hashpw(password, salt)