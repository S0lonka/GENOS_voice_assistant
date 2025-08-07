from dotenv import load_dotenv
import os


def str_to_bool(value: str | None) -> bool:
    """Перевод из строки в булевое значение
    
    Args:
        value (str | None) : Строка которую нужно преобразовать в bool.
        
    Returns:
        bool : Проверяет на true, в остальных случаях возвращает False."""
    
    #? Функция должна находиться в файле app\utils\config_utils.py, но файл config.py также пытается её импортировать
    #? Из за чего происходит ошибка, импорт ещё не успел произойти а уже запрашивается повторный
    
    if value is None:
        return False
    
    if isinstance(value, str):
        value = value.strip().lower()
        if value in ('true', '1', 'on', 'yes'):
            return True
        else:
            return False
    else:
        return False


load_dotenv(dotenv_path="app/env/logger_config.env")

# Переменные отвечающие на включение или выключение логгера
MAIN            = str_to_bool(os.getenv("MAIN")             )
NOTIFICATION    = str_to_bool(os.getenv("NOTIFICATION")     )
FILE_UTILS      = str_to_bool(os.getenv("FILE_UTILS")       )
GENERAL_UTILS   = str_to_bool(os.getenv("GENERAL_UTILS")    )
CONFIG_UTILS    = str_to_bool(os.getenv("CONFIG_UTILS")     )
