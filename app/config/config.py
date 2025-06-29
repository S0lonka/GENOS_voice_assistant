from dotenv import load_dotenv
import os

load_dotenv("app\\env\\token.env")

'''Vosk model - vosk-model-small-ru-0.22'''
MODEL_PATH = "model"
HELPERNAME_PATH = "helpername\\genas_en_windows_v3_0_0.ppn"

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")

print(PICOVOICE_TOKEN)