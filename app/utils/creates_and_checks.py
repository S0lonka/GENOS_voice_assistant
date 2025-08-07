from app.config.config import *
from app.utils.Notification import My_notification

notify = My_notification()

def createFile_token_env() -> bool:
    '''Создаёт  файл токеном/настройками, если его нет'''

    if not os.path.exists(TOKEN_ENV_PATH):
        os.makedirs("app\\env", exist_ok=True)  # Создаёт папку, если её нет(Без папки не создатся файл)

        with open(TOKEN_ENV_PATH, 'w', encoding="UTF-8") as file:
            file.write
            (
                "PICOVOICE_TOKEN=<токен_picovoice>"
            )
            (notify
            .create_notification("Token env created", "the token.env file was created, at app/env/token.env") # Уведомляет пользователя о создании файла
            .show()
            )
        return False
    
    elif not os.path.exists(SETTINGS_ENV_PATH):
        os.makedirs("app\\env", exist_ok=True)  # Создаёт папку, если её нет(Без папки не создатся файл)

        with open(SETTINGS_ENV_PATH, 'w', encoding="UTF-8") as file:
            file.write(  
                "APP_LANG=RU" "                    # EN или RU"                                         "\n"
                r"MODEL_PATH=app\assistant\model"                                                       "\n"
                r"ASSISTANT_NAME_PATH=app\assistant\assistant_name\genas_en_windows_v3_0_0.ppn"         "\n"
                "DEVICE_INDEX=-1" "            # -1 для текущего устройства"                            "\n"
                "WAITING_WHILE_LISTENING=15" " # Время которое будет слушать бот после своего имени"
            )
            (notify
            .create_notification("Settings env created", "the token.env file was created, at app/env/settings.env")
            .show()
            )
        return False
    
    else:
        return True


def checkFile_token_env() -> bool:
    '''Провернка на то что введён токен'''
    with open(TOKEN_ENV_PATH, 'r', encoding="UTF-8") as file:
        token_env_text = file.read()

        # Проверям чтобы был введён токен
        if token_env_text in ["PICOVOICE_TOKEN=<токен_picovoice>", "PICOVOICE_TOKEN","PICOVOICE_TOKEN=" , ""]:
            (notify
            .create_notification("Not found PICOVOICE_TOKEN", "Please fill in the field with the token on the path app/env/token.env")
            .show())
            return False
        else:
            return True

        


def checkModel_path(model_path: str) -> bool:
    '''Проверяет путь до модели и уведомляет'''
    if not os.path.exists(model_path):
        (notify
        .create_notification("Not found model", f"Model not found, on the way: {model_path}"))
        return False
    else:
        return True