import logging
import csv


def insert_user():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль записи данных")
    name = input("Введите имя студента \n")
    logger.debug({name})
    last_name = input("Введите фамилию студента \n")
    logger.debug(last_name)
    while True:
        phone_number = input("Введите номер телефона (11 цифр без специальных символов) \n")
        if len(phone_number) == 11 and phone_number.isdigit():
            break
        elif phone_number == '':
            break
        else:
            print("Некорректный формат ввода")
    logger.debug(phone_number)
    email = input("Введите электронную почту студента \n")
    logger.debug(email)
    while True:
        try:
            grade = float(input("Введите средний балл студента (Число от 2 до 5)\n"))
        except ValueError:
            print("Некорректный формат ввода")
            continue
        if 5 >= grade >= 2:
            break
        elif grade == '':
            break

    with open("package/database.csv", "r", encoding="utf-8") as database:
        reader = csv.DictReader(database)
        student_id = 1
        for row in reader:
            if student_id <= int(row['ID']):
                student_id = int(row['ID']) + 1

    with open("package/database.csv", "a", encoding="utf-8") as database:
        writer = csv.DictWriter(database, delimiter=',', fieldnames=['ID', 'first_name', 'last_name', 'phone_number',
                                                                     'email', 'average_grade'])
        writer.writerow({'ID': student_id,
                         'first_name': name,
                         'last_name': last_name,
                         'phone_number': phone_number,
                         'email': email,
                         'average_grade': grade})
