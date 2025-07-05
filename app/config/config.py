from dotenv import load_dotenv
import os

TOKEN_ENV_PATH = "app\\env\\token.env"

load_dotenv(TOKEN_ENV_PATH)

LANG = "RU"

'''Vosk model - vosk-model-small-ru-0.22'''
MODEL_PATH = "app\\assistant\\model"
ASSISTANT_NAME_PATH = "app\\assistant\\assistant_name\\genas_en_windows_v3_0_0.ppn"

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
