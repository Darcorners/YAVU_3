import re
import ConnDB
from ConnDB import connection

Loginon = bool(False)


def Login():
    while True:
        try:
            with connection.cursor() as cursor:
                global Loginon
                patternE = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'
                patternN = '^[0-9]{11}$'
                Loginon = False
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
                        Loginon = True
                        break
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
                    if CheckerE == False:
                        print('Неправильный формат почты')
                    else:
                        print('Введите номер телефона')
                        Number = input()
                        digits_only = re.sub(r'\D+', '', Number)
                        CheckerN = bool(re.match(patternN, digits_only))
                        # Reg_Check = f""" SELECT number FROM customer WHERE '{digits_only}' = ` REPLACE(number, '[^0-9]', '') `"""
                        if CheckerN == False:
                            print('Неправильный номер телефона')
                        # elif RegCheck:
                        #     print('Телефон занят')
                        else:
                            print('Введите номер паспорта и серию')
                            Passport = input()
                            digits_only = re.sub(r'\D+', '', Passport)
                            CheckerPp = bool(len(digits_only) == 10)
                            Reg_Check = f""" SELECT passport FROM customer WHERE '{Passport}' = `passport`"""
                            cursor.execute(Reg_Check)
                            RegCheck = cursor.fetchall()
                            if CheckerPp == False:
                                print('Неправильный номер паспорта')
                            elif RegCheck:
                                print('Паспорт занят')
                            else:
                                print('Введите логин')
                                Login = input()
                                CheckerL = bool(re.match('^[a-zA-Z0-9._%+-]{4,}$', Login))
                                Reg_Check = f""" SELECT password FROM customer WHERE MD5('{Login}') = `login` OR '{Login}' = `login`"""
                                cursor.execute(Reg_Check)
                                RegCheck = cursor.fetchall()
                                if CheckerL == False:
                                    print('Для ввода допустимы только английские символы, Минимальное число символов 4')
                                elif RegCheck:
                                    print('Логин существует')
                                else:
                                    print('Введите пароль')
                                    Password = input()
                                    CheckerP = bool(re.match('^[a-zA-Z0-9._%+-]{4,}$', Password))
                                    if CheckerP == True:
                                        select_registrate= f""" INSERT INTO customer(`Name`, `Surname`, `email`, `phone`, `passport`, `login`, `password`) VALUES ('{Name}', '{Surname}', '{Email}', ('{Number}'), ('{Passport}'), MD5('{Login}'),MD5('{Password}')); """
                                        cursor.execute(select_registrate)
                                        connection.commit()
                                        print('Регистрация успешна')
                                    else:
                                        print('Для ввода допустимы только английские символы, Минимальное число символов 4')

        except Exception as ex:
            print("\nПрограмма выполнена с ошибками")
            print(ex)

        if ent == 3:
            print("До свидания!")
            break