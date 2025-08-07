from dotenv import load_dotenv
import os


TOKEN_ENV_PATH = r"app\env\token.env"
SETTINGS_ENV_PATH = r"app\env\config.env"

load_dotenv(SETTINGS_ENV_PATH)
APP_LANG                 = os.getenv("APP_LANG",                 "RU")
MODEL_PATH               = os.getenv("MODEL_PATH",               r"app\assistant\model")
ASSISTANT_NAME_PATH      = os.getenv("ASSISTANT_NAME_PATH",      r"app\assistant\assistant_name\genas_en_windows_v3_0_0.ppn")  # Vosk model - vosk-model-small-ru-0.22
DEVICE_INDEX             = os.getenv("DEVICE_INDEX",             -1)
WAITING_WHILE_LISTENING  = os.getenv("WAITING_WHILE_LISTENING",  15)
SHOW_NOTIFICATION        = os.getenv("SHOW_NOTIFICATION",        True)



load_dotenv(TOKEN_ENV_PATH)
PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN", None)
