import ConnDB
from ConnDB import connection
import SQL_Queries as SQL_Q

try:
    with connection.cursor() as cursor:
        cursor.execute(SQL_Q.max_cost_pet)
        res_view1 = cursor.fetchall()
        for i in res_view1:
            print(f"Кличка: {i['Name']} \nКатегория: {i['Category_ID']} \nПорода: {i['Poroda']} \nВозраст: {i['Age']} \nПол: {i['Gender']} \nОписание: {i['Opisanie']} \nЦена: {i['price']}")
            print('.' * 20)
            print('\n')
        cursor.execute(SQL_Q.max_categoty_pet)
        res_view2 = cursor.fetchall()
        for i in res_view2:
            print(f"ID Категории: {i['Category_ID']} \nКоличество: {i['count']}")
            print('.' * 20)
            print('\n')
        cursor.execute(SQL_Q.all_koshka_pet)
        res_view3 = cursor.fetchall()
        for i in res_view3:
            print(f"Кличка: {i['Name']}, Категория: {i['Category_ID']}, Порода: {i['Poroda']}, Возраст: {i['Age']}, Пол: {i['Gender']}, Описание: {i['Opisanie']}, Цена: {i['price']}\n")
        print('.' * 20)
        print('\n')
        cursor.execute(SQL_Q.all_customers)
        res_view4 = cursor.fetchall()
        # print(res_view4)
        for i in res_view4:
            print(f"ID чека: {i['ID']}, Дата оплаты: {i['Data']}, Способ оплаты: {i['payment']}, ID Клиента: {i['id_customer']}\nID Клиента: {i['customer.ID']}, Имя: {i['Name']}, Фамилия: {i['Surname']}, Телефон: {i['phone']}\n")

        # cursor.execute(SQL_Q.create_tablecreate_category_query)
        # cursor.execute(SQL_Q.create_tablecreate_pet_query)
        # cursor.execute(SQL_Q.create_tablecreate_customer_query)
        # cursor.execute(SQL_Q.create_tablecreate_Basket_query)
        # cursor.execute(SQL_Q.create_tablecreate_cheque_query)
        # cursor.execute(SQL_Q.create_tablecreate_sales_query)

        connection.commit()
finally:
    connection.close()
    print("\nСоединенеие закрыто")




