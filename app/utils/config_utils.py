import sys

from app.utils.general_utils import *


# Настройка логгера
logger = create_logger("config_utils")
toggle_logging(logger)





#! --------- CHECKS ---------
def check_content(method: str, contents: list[str]) -> str | None:
    """Проверка что метот входа указан верно"""

    if method in contents:
        return method
    else:
        logger.error("Не верно указан метод входа в ____.env")
        sys.exit(1)

