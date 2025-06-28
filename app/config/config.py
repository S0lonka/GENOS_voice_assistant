from dotenv import load_dotenv
import os

load_dotenv("app\\env\\tokens.env")

MODEL_PATH="model"

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
