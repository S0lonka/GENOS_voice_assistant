import os
import struct
import json
import time
import atexit
import threading

# models
from pvrecorder import PvRecorder
import pvporcupine
import vosk

# audio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  

# project
from app.config.config import *
from app.config.notification import notification
from app.config.play_sound import play
from app.config.tray import create_tray
from app.config.creates_and_checks import createFile_token_env, checkFile_token_env, checkModel_path 





# Переменная для управления иконкой
tray_icon = None

def run_icon(icon):
    global tray_icon
    tray_icon = icon
    icon.run()


def on_exit():
    '''Для добавления в exit() и проигрывания звука при выключении'''

    if tray_icon:
        tray_icon.stop() # Завершаем работу трея

    play("assistant_deactivate").wait_done() # Ожидаем завершения звука и после завершаем код
    print("Программа завершается!")



#! Основная функция ответа
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
        atexit.register(on_exit) # Добавляет звук при завершении программы

        # Проверяем токен и путь до модели

        if createFile_token_env() and checkFile_token_env() and checkModel_path(MODEL_PATH):
            # Инициализация модели Vosk и создание калди_регонайзера
            model = vosk.Model(MODEL_PATH)
            kaldi_reс = vosk.KaldiRecognizer(model, 16000)

            # Создаём и запускаем трей(В отдельном потоке)
            icon = create_tray()
            thread = threading.Thread(target=run_icon, args=(icon,))
            thread.daemon = True
            thread.start()


            main()
        else:
            exit(0)

    except Exception as e:
        print(e)
        