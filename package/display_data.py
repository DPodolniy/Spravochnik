import logging
import csv


def parameter_choser():
    logger = logging.getLogger("log")
    logger.info("Запущен выбор параметра")
    parameter = None
    while True:
        try:
            parameter = int(input("Выберите параметр: \n"
                                  "1. Имя студента \n"
                                  "2. Фамилия студента \n"
                                  "3. Email студента \n"
                                  "4. Номер телефона студента \n"
                                  "0. Выход \n"))
        except ValueError:
            print("Некорректный ввод")
            logger.warning(f"ValueError: Некорректный ввод, пользователь ввел {parameter}, ожидался int от 0 до 5")
            continue
        if parameter == 0:
            return "exit"
        elif 1 <= parameter <= 4:
            return parameter
        else:
            print("Некорректный ввод")
            logger.warning("Некорректный ввод, пользователь ввел {parameter}, ожидался int от 0 до 5")
            continue


def display_all():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль вывода всех данных")

    with open('package/database.csv', 'r', encoding='utf-8') as database:
        csv_reader = csv.reader(database, delimiter=',')
        for row in csv_reader:
            print(*row)
    input("Нажмите Enter, чтобы продолжить")


def finder():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль поиска данных")
    parameter = None
    modlist, counter, data = ["ID", "first_name", "last_name", "email", "phone_number", "grade"], 0, []
    something = parameter_choser()
    if something == "exit":
        pass
    elif modlist[something] == "phone_number":
        while True:
            parameter = input(f"Выбранный параметр - {modlist[something]} \n"
                              "Введите поисковый запрос \n")
            if modlist[something] == "phone_number" and (len(parameter) > 11 or not parameter.isdigit()):
                print("Ошибка - недопустимый телефонный номер")
                continue
            elif modlist[something] == "phone_number" and (1 <= len(parameter) <= 11) and parameter.isdigit():
                break
    else:
        parameter = input(f"Выбранный параметр - {modlist[something]} \n"
                          "Введите поисковый запрос \n")
    with open('package/database.csv', 'r', encoding='utf-8') as database:
        reader = csv.DictReader(database, fieldnames=modlist)
        for row in reader:
            if row[modlist[something]] == parameter:
                data.append(f"{row['ID']} {row['first_name']} {row['last_name']} {row['phone_number']} {row['email']} "
                            f"{row['grade']}")
                counter += 1
    if counter == 0:
        return "null"
    print(f"Найдено {counter} совпадений")
    return data


def display():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль вывода данных")
    data = finder()
    for i in data:
        print(i)
    input("Нажмите Enter, чтобы продолжить \n")
