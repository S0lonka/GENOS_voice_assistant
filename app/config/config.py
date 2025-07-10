from dotenv import load_dotenv
import os

TOKEN_ENV_PATH = r"app\env\token.env"
SETTINGS_ENV_PATH = r"app\env\settings.env"

if load_dotenv(SETTINGS_ENV_PATH):
    LANG = os.getenv("LANG")

    '''Vosk model - vosk-model-small-ru-0.22'''
    MODEL_PATH = os.getenv("MODEL_PATH")
    ASSISTANT_NAME_PATH = os.getenv("ASSISTANT_NAME_PATH")
    DEVICE_INDEX = os.getenv("DEVICE_INDEX")
    WAITING_WHILE_LISTENING = os.getenv("WAITING_WHILE_LISTENING")


else: # Аннотация типов ругается что значения не могут быть None, поэтому нужно их заполнить принудительно
    # БАЗОВЫЕ НАСТРОЙКИ
    LANG = "RU"
    MODEL_PATH = r"app\assistant\model"
    ASSISTANT_NAME_PATH = r"app\assistant\assistant_name\genas_en_windows_v3_0_0.ppn"
    DEVICE_INDEX = -1
    WAITING_WHILE_LISTENING=15

if load_dotenv(TOKEN_ENV_PATH):
    PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
