import ConnDB
from ConnDB import connection
import SQL_Queries as SQL_Q
import Login as Log

while True:
    try:
        with connection.cursor() as cursor:
            pets = str()
            Log.Login()
            if 3:
                print("Взять товар в корзину - 1, Купить - 2:, Выход - 3")
                ent = int(input())
                if ent == 1:
                    print("Выберите категорию: 1 - Кошка, 2 - Собака, 3 - Все животные")
                    entb = int(input())
                    print('\n')
                    if entb == 1:
                        cursor.execute(SQL_Q.all_koshka_pet)
                        res_view = cursor.fetchall()
                        for i in res_view:
                            print(f"ID: {i['ID']} \nКличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
                            print('.' * 20)
                            print('\n')
                    elif entb == 2:
                        cursor.execute(SQL_Q.all_sobaka_pet)
                        res_view = cursor.fetchall()
                        for i in res_view:
                            print(f"ID: {i['ID']} \nКличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
                            print('.' * 20)
                            print('\n')
                    elif entb == 3:
                        cursor.execute(SQL_Q.all_pet)
                        res_view = cursor.fetchall()
                        for i in res_view:
                            print(f"ID: {i['ID']} \nКличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
                            print('.' * 20)
                            print('\n')
                    while True:
                        print('Выберите id животного')
                        idpet = str(input())
                        pet = f""" 
                            SELECT * FROM Pet
                            WHERE ID = '{idpet}'
                            """
                        cursor.execute(pet)
                        res_view = cursor.fetchall()
                        for i in res_view:
                            print(f"\nID: {i['ID']} \nКличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
                        print('Вы уверены? : 1 - Да, 2 - Нет')
                        entc = int(input())
                        if entc == 1:
                            pets += idpet + " "
                            print(pets)
                        else:
                            print("Отменено")
            else:
                break
            # cursor.execute(SQL_Q.max_cost_pet)
            # res_view1 = cursor.fetchall()
            # for i in res_view1:
            #     print(f"Кличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
            #     print('.' * 20)
            #     print('\n')
            # cursor.execute(SQL_Q.max_categoty_pet)
            # res_view2 = cursor.fetchall()
            # for i in res_view2:
            #     print(f"ID Категории: {i['Category_ID']} \nКоличество: {i['count']}")
            #     print('.' * 20)
            #     print('\n')
            # cursor.execute(SQL_Q.all_koshka_pet)
            # res_view3 = cursor.fetchall()
            # for i in res_view3:
            #     print(f"Кличка: {i['Name']}, Категория: {i['Category_ID']}, Порода: {i['Poroda']}, Возраст: {i['Age']}, Пол: {i['Gender']}, Описание: {i['Opisanie']}, Цена: {i['price']}\n")
            # print('.' * 20)
            # print('\n')
            # cursor.execute(SQL_Q.all_customers)
            # res_view4 = cursor.fetchall()
            # # print(res_view4)
            # for i in res_view4:
            #     print(f"ID чека: {i['ID']}, Дата оплаты: {i['Data']}, Способ оплаты: {i['payment']}, ID Клиента: {i['id_customer']}\nID Клиента: {i['customer.ID']}, Имя: {i['Name']}, Фамилия: {i['Surname']}, Телефон: {i['phone']}\n")

            # cursor.execute(SQL_Q.create_tablecreate_category_query)
            # cursor.execute(SQL_Q.create_tablecreate_pet_query)
            # cursor.execute(SQL_Q.create_tablecreate_customer_query)
            # cursor.execute(SQL_Q.create_tablecreate_Basket_query)
            # cursor.execute(SQL_Q.create_tablecreate_cheque_query)
            # cursor.execute(SQL_Q.create_tablecreate_sales_query)

            connection.commit()

        if ent == 3:
            print("До свидания!")
            break
    finally:
        connection.close()
        print("\nСоединенеие закрыто")
        break




