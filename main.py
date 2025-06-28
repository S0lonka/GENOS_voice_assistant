from winotify import Notification
from pvrecorder import PvRecorder
import pvporcupine
import os
import struct
import vosk
import json
import time

from app.config.notification import notification
from app.config.config import *

def createFile_token_env():
    '''Создаёт  файл токеном, если его нет'''

    if not os.path.exists("app/env/token.env"):
        with open("app/env/token.env", 'w', encoding="UTF-8") as file:
            file.write("PICOVOICE_TOKEN=<токен_picovoice>")

        notification("First launch", "the token.env file was created, at app/env/token.env") # Уведомляет пользователя о создании файла

        exit(0) # Завершает без ошибки
    

def check_model_path(model_path: str) -> None:
    '''Проверяет путь до модели и уведомляет'''
    if not os.path.exists(model_path):
        notification("Check model path", f"Model not found, on the way: {model_path}")
        exit(1)


# Инициализация модели Vosk и создание калди_регонайзера

# Основная функция ответа
def voice_helper_responce():
    pass
    # остановим запись во время обработки
    # Только если не тишина, иначе вернём false

    # Команды: если ниодна не выполнилась нужно вернуть false

    # При команде выключись - удаляем рекордер и выходи без ошибки exit(0)


    #? очистка


# main
def main():
    pass
    # devices = PvRecorder.get_available_devices()
    # Путь до имени помошника и ключ
    # Обработчик ключевого слова(porcupine создаём модель с ключём access_key и ключевым словом keyword_paths)

    # Создаём запись аудио и начинаем запись(индекс устройства и длина фрейма=порцупайн.длина фрейма)

    # Заранее уведём время в меньшее(1000) чтобы несработал while

    # Основной цикл

    # проверка на ошибки с остановкой и удалением рекордера

    # читаем аудио(в 0 и 1)
    # возвращает 0 если слышит ключевое слово

    # если слышит ключевое слово
    # останавливаем запись 
    # и очищаем буфер

    # После сказанного слова возобновляем запись

    # обновляем время

    # Если небыло ключевого слова то - на - даёт + и мы не входи цикл(время - ltc <= 10)
    # читаем аудио(в 0 и 1)

    #? очищаем артефакты прошлой записи audio_data(похоже на костыль)
    # преобразование в байты struct.pack("%dh" % len(pcm), *pcm)

    # Если распознано возвращает 1(подтвержаем волну аудио даты через калди рек)

    # json.loads(kaldi_rec.Result())["text"] это и есть Voice
    # Возвращает True если было задействованно ключевое слово
    # Программа выполнилась и мы снова готовы ждать 10 сек(обновляем время)

    # Очищаем буфер kaldi_rec
    # Снова начинаем запись
    # Выходим из циклв


if __name__ == "__main__":
    print("start")
    # Ловим все ошибки на стадии разработки
    try:
        createFile_token_env()
        check_model_path(MODEL_PATH)

        main()

    except Exception as e:
        print(e)