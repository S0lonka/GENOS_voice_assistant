from dotenv import load_dotenv
import os

TOKEN_ENV_PATH = "app\\env\\token.env"
SETTINGS_ENV_PATH = "app\\env\\settings.env"

if load_dotenv(SETTINGS_ENV_PATH):
    LANG = os.getenv("LANG")

    '''Vosk model - vosk-model-small-ru-0.22'''
    MODEL_PATH = os.getenv("MODEL_PATH")
    ASSISTANT_NAME_PATH = os.getenv("ASSISTANT_NAME_PATH")

else: # Аннотация типов ругается что значения не могут быть None, поэтому нужно их заполнить принудительно
    LANG = ""
    MODEL_PATH = ""
    ASSISTANT_NAME_PATH = ""

if load_dotenv(TOKEN_ENV_PATH):
    PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
