from app.config.config import *
from app.config.notification import notification


def createFile_token_env() -> bool:
    '''Создаёт  файл токеном, если его нет'''

    if not os.path.exists(TOKEN_ENV_PATH):
        os.makedirs("app\\env", exist_ok=True)  # Создаёт папку, если её нет(Без папки не создатся файл)

        with open(TOKEN_ENV_PATH, 'w', encoding="UTF-8") as file:
            file.write("PICOVOICE_TOKEN=<токен_picovoice>")
            notification("First launch", "the token.env file was created, at app/env/token.env") # Уведомляет пользователя о создании файла

        return False
    else:
        return True


def checkFile_token_env() -> bool:
    '''Провернка на то что введён токен'''
    with open(TOKEN_ENV_PATH, 'r', encoding="UTF-8") as file:
        token_env_text = file.read()

        # Проверям чтобы был введён токен
        if token_env_text in ["PICOVOICE_TOKEN=<токен_picovoice>", ""]:
            notification("Not found PICOVOICE_TOKEN", "Please fill in the field with the token on the path app/env/token.env")
            return False
        else:
            return True

        


def checkModel_path(model_path: str) -> bool:
    '''Проверяет путь до модели и уведомляет'''
    if not os.path.exists(model_path):
        notification("Check model path", f"Model not found, on the way: {model_path}")
        return False
    else:
        return True