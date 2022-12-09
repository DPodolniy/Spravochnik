import csv
import logging
from package.display_data import finder, parameter_choser


def find_and_change():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль поиска и изменений строки")
    modlist = ["ID", "first_name", "last_name", "email", "phone_number", "grade"]
    data = finder()
    chosen_row, zapros = 1, ""
    if data == "null":
        print("Данные не найдены")
        pass
    else:
        if len(data) > 1:
            for i in data:
                print(i)
            while True:
                try:
                    chosen_row = int(input("Похоже, что под запрос подошло больше одного студента. \n"
                                           "Введите порядковый номер строки, которую хотите заменить \n"))
                except ValueError:
                    print("Некорректный ввод")
                    continue
                if chosen_row <= len(data):
                    break
                else:
                    print("Некорректный ввод, введенное число превышает количество строк")
                    continue

        chosen_row = data[chosen_row - 1]
        parameter = parameter_choser()
        print(f"parameter = {parameter}")
        print(f"chosen_row = {chosen_row}")
        if parameter == "exit":
            pass
        elif parameter == 4:
            while True:
                zapros = input(f"Выбранный параметр - {modlist[parameter]} \n"
                               "Введите замену \n")
                if len(zapros) > 11 or not zapros.isdigit():
                    print("Ошибка - недопустимый телефонный номер")
                    continue
                elif 1 <= len(zapros) <= 11 and zapros.isdigit():
                    break
        else:
            zapros = input(f"Выбранный параметр - {modlist[parameter]} \n"
                           "Введите замену \n")
        acces = input(f"Значение {modlist[parameter]} будет изменено с {chosen_row[parameter]} на {zapros}")

        with open("package/database.csv", "rw", encoding="utf-8") as database:
            reader = csv.DictWriter(database, fieldnames=modlist)
            for row in reader:
                if row["ID"] == chosen_row[0]:
                    row[modlist[parameter]] = zapros
                else:
                    continue
