import re
import ConnDB
from ConnDB import connection

patternE = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+.[a-zA-Z]{2,}$'
patternN = '^[0-9]{11}$'

while True:
    try:
        with connection.cursor() as cursor:
            print("Авторизация - 1, Регистрация - 2:, Выход - 3")
            ent = int(input())
            if ent == 1:
                print('Введите логин или E-mail')
                Login = input()
                print('Введите пароль')
                Password = input()
                select_login = f""" SELECT id FROM customer
                WHERE (`login` = MD5('{Login}') OR `email` = '{Login}') AND `password` = MD5('{Password}')   """
                cursor.execute(select_login)
                res_select_login = cursor.fetchall()
                if res_select_login:
                    print("Вход успешен")
                else:
                    print("Ошибка, неверный логин или пароль")
            if ent == 2:
                print('Введите имя: ')
                Name = input()
                print('Введите фамилию: ')
                Surname = input()
                print('Введите почту: ')
                Email = str(input())
                CheckerE = bool(re.match(patternE, Email))
                print('Введите номер телефона')
                Number = input()
                CheckerN = bool(re.match(patternN, Number))
                print('Введите номер паспорта и серию')
                Passport = input()
                CheckerPp = bool(len(Passport) == 10)
                print('Введите логин')
                Login = input()
                CheckerL = bool(re.match('^[a-zA-Z]+$', Login))
                print('Введите пароль')
                Password = input()
                CheckerP = bool(re.match('^[a-zA-Z]+$', Password))
                if CheckerE == False:
                    print('Неправильный формат почты')
                elif CheckerN == False:
                    print('Неправильный номер телефона')
                elif CheckerPp == False:
                    print('Неправильный номер паспорта')
                elif CheckerP == True and CheckerL == True:
                    select_MD5 = f""" SELECT MD5( '{Password}' );'); """
                    select_registrate= f""" INSERT INTO customer(`Name`, `Surname`, `email`, `phone`, `passport`, `login`, `password`) VALUES ('{Name}', '{Surname}', '{Email}', MD5('{Number}'), MD5('{Passport}'), MD5('{Login}'),MD5('{Password}')); """
                    cursor.execute(select_registrate)
                    connection.commit()
                    print('Регистрация успешна')
                else:
                    print('Для ввода допустимы только английские символы')

    except Exception as ex:
        print("\nПрограмма выполнена с ошибками")
        print(ex)

    if ent == 3:
        print("Goodbye!")
        break