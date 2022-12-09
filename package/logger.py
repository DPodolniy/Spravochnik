from os import getcwd
import logging


# Создание логгера. Возвращает сконфигурированный логгер, который будет писать логи в файле. По умолчанию стоит уровень
# INFO, можно поменять на DEBUG при вызове
def create_log(level=logging.INFO, log_dir_name=getcwd()):
    logger = logging.getLogger("log")
    form = "%(asctime)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s"
    logger.setLevel(level)

    fh = logging.FileHandler(filename=f"{log_dir_name}/log.txt", encoding="UTF-8")
    fh.setFormatter(logging.Formatter(form))
    fh.setLevel(level)

    logger.addHandler(fh)

    logger.debug(f"Logger was initialized")
    return "log"
