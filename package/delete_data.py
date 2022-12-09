import logging
import csv


def delete_one():
    pass


def delete_all():
    logger = logging.getLogger("log")
    logger.info("Запущен модуль очистки всей базы")
    user_input = input("Введите Y, чтобы удалить все данные")
    if user_input.lower() == "y":
        pass
    else:
        pass
