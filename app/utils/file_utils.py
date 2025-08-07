from pathlib import Path
import os

from app.utils.general_utils import *
from app.utils.Notification import My_notification
from app.template.env_content import config_env_temp




# Настройка логгера
logger = create_logger("main")
toggle_logging(logger)



# Экземпляр класса уведомлений
notyfi = My_notification() 

def check_file(path: str) -> bool:
    """Проверка что файл существует и его заполнение из template
    
    Args:
        path (str) : Относительный путь до файла который нужно проверить.
    
    Returns:
        bool : Если файла не существует, создаёт его и возвращает False в любом случае
    """
    path = fr"{os.getcwd()}\{path}"

    if Path(path).is_file():
        return True
    else:
        name = Path(path).stem                                      # Имя 
        extension = Path(path).suffix                               # Расширение 
        variable_name = globals().get(f"{name}_{extension}_temp")   # Итоговое название переменной
        if create_file(path, variable_name):

            (notyfi  # Показываем уведомление
            .create_notification(f"WARNING | Создан {extension.upper()} файл", f"Создан файл по пути {path} проверьте и заполните его", duration="long")
            .show())

            logger.warning(f"Создан файл по пути: {path}")

            return False

        else:
            logger.error(f"Не найдена итоговая перменная {variable_name}, из за чего не получилось создать файл")
            return False
    

def create_file(filepath: str, line_content: list[str] | None = []) -> bool:
    """Создаёт и записывает заданные линии в файл

    Args:
        filepath     (str)       : Путь до целевого файла
        line_content (list[str]) : Массив строк которыми заполнится файл
    
    Returns:
        bool : False если не найдена строка с линиями для заполнения, при успехе True
    """
    if not line_content is None:
        with open(filepath, "w", encoding="UTF-8") as file:
            file.writelines('\n'.join(line_content))

        return True
    else:
        return False



