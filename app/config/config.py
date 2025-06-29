from dotenv import load_dotenv
import os

load_dotenv("app\\env\\token.env")

'''Vosk model - vosk-model-small-ru-0.22'''
MODEL_PATH = "app\\model"
HELPERNAME_PATH = "app\\helpername\\genas_en_windows_v3_0_0.ppn"

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
