import logging
from package.logger import create_log
from package.add_data import insert_user
from package.display_data import display_all, display
from package.change_data import find_and_change


# Создать информационную систему позволяющую работать с сотрудниками некой компании \ студентами вуза \ учениками школы
# Примерные модули: дозапись, изменение, удаление, вывод данных, логирование. Остальные, которые решите добавить, только
# приветствуются.
if __name__ == '__main__':
    logger = logging.getLogger(create_log(logging.DEBUG))
    while True:
        print("Вас приветствует информационная система учета студентов ВУЗа! \n"
              "Выберите действие, которое хотите выполнить в системе: \n"
              "1. Внести студента в базу \n"
              "2. Изменить информацию о студенте \n"
              "3. Показать содержимое базы \n"
              "4. Найти студента в базе \n"
              "5. Удалить студента из базы \n"
              "0. Выход")
        try:
            user_input = int(input())
            if user_input == 0:
                logger.info(f"Пользователь ввел {user_input}. Завершение работы...")
                break
            elif user_input == 1:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль внесения данных в базу")
                insert_user()
            elif user_input == 2:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль для ")
                find_and_change()
            elif user_input == 3:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль отображения всей базы")
                display_all()
            elif user_input == 4:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль для поиска студента...")
                display()
            elif user_input == 5:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль для удаления студента из базы...")
                print("НУЖНО ДОПИСАТЬ ФУНКЦИЮ")
            elif user_input == 6:
                logger.debug(f"Пользователь ввел {user_input}. Открываю модуль для ")
                print()
            else:
                print("Некорректный ввод, попробуйте еще раз")
        except ValueError:
            print("Некорректный ввод, попробуйте еще раз")
    print("Спасибо за использование нашей системы!")
    logger.info("<---------->")
    pass

# ID,first_name,last_name,email,phone_number,grade