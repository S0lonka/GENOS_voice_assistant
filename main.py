import os
import struct
import json
import time
import atexit

# models
from pvrecorder import PvRecorder
import pvporcupine
import vosk

# audio
import simpleaudio as sa
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  

#project
from app.config.notification import notification
from app.config.config import *
from app.config.play_sound import play



def createFile_token_env() -> bool:
    '''Создаёт  файл токеном, если его нет'''

    if not os.path.exists("app/env/token.env"):
        with open("app/env/token.env", 'w', encoding="UTF-8") as file:
            file.write("PICOVOICE_TOKEN=<токен_picovoice>")

        notification("First launch", "the token.env file was created, at app/env/token.env") # Уведомляет пользователя о создании файла
        return False
    else:
        return True


def check_model_path(model_path: str) -> bool:
    '''Проверяет путь до модели и уведомляет'''
    if not os.path.exists(model_path):
        notification("Check model path", f"Model not found, on the way: {model_path}")
        return False
    else:
        return True

def on_exit():
    play("assistant_deactivate").wait_done()
    print("Программа завершается!")

atexit.register(on_exit)

# Основная функция ответа
def voice_helper_responce(voice: str, recorder: PvRecorder) -> bool:
    # TODO: add Опредление команды - иначе ответ нейросети
    try:
        recorder.stop() # остановим запись во время обработки
        if voice != "": # Только если не тишина, иначе вернём false
            print(f"\n- Распознано: {voice}")

            if voice == "привет":
                print("Привет я на связи")
                return True

            elif voice == "выключись":
                print("Выключаюсь")
                recorder.delete()
                exit(0)

            else:
                return False

        else:
            print("Ничего не распознано")
            return False
            
    finally:
        kaldi_reс.Reset() #? очистка



def main():
    # devices = PvRecorder.get_available_devices()

    porcupine = pvporcupine.create(access_key=PICOVOICE_TOKEN, keyword_paths=[HELPERNAME_PATH])
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

    recorder.start()
    print("- Я начал работу")
    play("assistant_activate")

    # Заранее уведём время в меньшее(1000) чтобы несработал while
    ltc = time.time() - 1000
    lisen_commands_flag = False # Флаг - что нас слушает бот

    while True:
        try:
            pcm = recorder.read() # читаем аудио(в 0 и 1)
            pcm_result = porcupine.process(pcm) # возвращает 0 если слышит ключевое слово
            
            if pcm_result >= 0: # если слышит ключевое слово
                
                print("- Я тебя слушаю")
                play("assistant_start_lisen", recorder)
                kaldi_reс.Reset() 
    
                ltc = time.time()# обновляем время
                lisen_commands_flag = True



            while lisen_commands_flag:
                if time.time() - ltc <= 10: # Если небыло ключевого слова то - на - даёт + и мы выходим цикла
                    pcm = recorder.read() # читаем аудио(в 0 и 1)

                    audio_data = '' #? очищаем артефакты прошлой записи audio_data(похоже на костыль)
                    audio_data = struct.pack("%dh" % len(pcm), *pcm) # преобразование в байты

                    if kaldi_reс.AcceptWaveform(audio_data): # Если распознано возвращает 1
                        if voice_helper_responce(json.loads(kaldi_reс.Result())["text"], recorder): # Возвращает True если было задействованно ключевое слово
                            ltc = time.time() # Программа выполнилась и мы снова готовы ждать 10 сек

                        kaldi_reс.Reset() 
                        recorder.start()
                        break
                else:
                    print("- Прекращаю слушать")
                    play("assistant_stop_lisen", recorder)
                    lisen_commands_flag = False      
                    

        except KeyboardInterrupt:
            print("Error stop...")
            recorder.stop()
            recorder.delete()



if __name__ == "__main__":
    # Ловим все ошибки на стадии разработки
    try:
        # Проверяем токен и путь до модели
        if createFile_token_env() and check_model_path(MODEL_PATH):
            # Инициализация модели Vosk и создание калди_регонайзера
            model = vosk.Model(MODEL_PATH)
            kaldi_reс = vosk.KaldiRecognizer(model, 16000)

            main()
        else:
            exit(0)

    except Exception as e:
        print(e)
        