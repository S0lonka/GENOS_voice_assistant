from winotify import Notification
from pvrecorder import PvRecorder
import pvporcupine
import os
import struct
import vosk
import json
import time

from app.config.notification import notification


def create_token_env():
    '''Создаём файл токеном, если его нет'''

    if not os.path.exists("app/env/token.env"):
        with open("app/env/token.env", 'w', encoding="UTF-8") as file:
            file.write("PICOVOICE_TOKEN=<токен_picovoice>")
    

# Путь до модели
    # exit(1) Если ненайдена Завершаем с ошибкой 
# Инициализация модели Vosk и создание калди_регонайзера

# Основная функция распознавания

    # остановим запись во время обработки
    # Только если не тишина, иначе вернём false

    # Команды: если ниодна не выполнилась нужно вернуть false

    # При команде выключись - удаляем рекордер и выходи без ошибки exit(0)


    #? очистка


# main

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
    notification("First launch", "the token.env file was created, at app/env/token.env", 'long')


'''
Vosk model - vosk-model-small-ru-0.22
'''