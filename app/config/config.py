from dotenv import load_dotenv
import os

load_dotenv("app\\env\\tokens.env")

'''Vosk model - vosk-model-small-ru-0.22'''
MODEL_PATH="model"

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
