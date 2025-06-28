from dotenv import load_dotenv
import os

load_dotenv("app\\env\\tokens.env")

PICOVOICE_TOKEN = os.getenv("PICOVOICE_TOKEN")
