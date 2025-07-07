import os
import sys
import struct
import json
import time
import atexit
import threading
import logging as log

# models
from pvrecorder import PvRecorder
import pvporcupine
import vosk

# audio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume  

# Configs
from app.config.config import *
from app.config.tray_flag import stop_event

#Commands
from app.utils.VA_RESPONCE import voice_assistant_responce
# from app.utils.notification import notification
from app.utils.play_sound import play
from app.utils.tray import create_tray, run_icon
from app.utils.creates_and_checks import createFile_token_env, checkFile_token_env, checkModel_path 



log.basicConfig(level=log.INFO,
                filename="Genos_logs.log",
                filemode='w',
                format="%(asctime)s - %(levelname)s -/ %(message)s")



def on_exit():
    '''Для добавления в exit() и проигрывания звука при выключении'''

    # if tray_icon:
    #     tray_icon.stop()
    #     print("- Tray остановлен") # Завершаем работу трея

    play("assistant_deactivate", LANG).wait_done() # Ожидаем завершения звука и после завершаем код
    print("Программа завершается!")




def main():
    # devices = PvRecorder.get_available_devices()

    porcupine = pvporcupine.create(access_key=PICOVOICE_TOKEN, keyword_paths=[ASSISTANT_NAME_PATH])
    recorder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
    
    recorder.start()
    print("- Я начал работу")
    play("assistant_activate", LANG)

    # Заранее уведём время в меньшее(1000) чтобы несработал while
    ltc = time.time() - 1000
    lisen_commands_flag = False # Флаг - что нас слушает бот

    while not stop_event.is_set():
        try:
            pcm = recorder.read() # читаем аудио(в 0 и 1)
            pcm_result = porcupine.process(pcm) # возвращает 0 если слышит ключевое слово
            
            if pcm_result >= 0: # если слышит ключевое слово
                
                print("- Я тебя слушаю")
                play("assistant_start_lisen", LANG, recorder)
                kaldi_reс.Reset() 
    
                ltc = time.time()# обновляем время
                lisen_commands_flag = True



            while lisen_commands_flag:
                if time.time() - ltc <= 10: # Если небыло ключевого слова то - на - даёт + и мы выходим цикла
                    pcm = recorder.read() # читаем аудио(в 0 и 1)

                    audio_data = '' #? очищаем артефакты прошлой записи audio_data(похоже на костыль)
                    audio_data = struct.pack("%dh" % len(pcm), *pcm) # преобразование в байты

                    if kaldi_reс.AcceptWaveform(audio_data): # Если распознано возвращает 1
                        if voice_assistant_responce(json.loads(kaldi_reс.Result())["text"], recorder, kaldi_reс): # Возвращает True если было задействованно ключевое слово
                            ltc = time.time() # Программа выполнилась и мы снова готовы ждать 10 сек

                        kaldi_reс.Reset() 
                        recorder.start()
                        break
                else:
                    print("- Прекращаю слушать")
                    play("assistant_stop_lisen", LANG, recorder)
                    lisen_commands_flag = False      
                    

        except KeyboardInterrupt:
            log.error("Ошибка остановки.")
            print("Error stop...")
            recorder.stop()
            recorder.delete()



if __name__ == "__main__":
    try:
        atexit.register(on_exit) # Добавляет звук при завершении программы

        # Проверяем токен и путь до модели
        if createFile_token_env() and checkFile_token_env() and checkModel_path(MODEL_PATH):
            log.info("Проверки пройдены (файл token_env, проверка содержания token_env, проверка модели)")

            # Инициализация модели Vosk и создание калди_регонайзера
            model = vosk.Model(MODEL_PATH)
            kaldi_reс = vosk.KaldiRecognizer(model, 16000)


            # Для синхронизации между потоками
            stop_event = threading.Event()

            # Создаём и запускаем трей(В отдельном потоке)
            icon = create_tray(stop_event)

            thread = threading.Thread(target=run_icon, args=(icon, stop_event))
            thread.daemon = True
            thread.start()

            main()
        else:
            log.warning(f"Проверки не пройдены: файл token_env: {createFile_token_env()},\n\
                        проверка содержания token_env: {checkFile_token_env()},\n\
                        проверка модели: {checkModel_path(MODEL_PATH)}")
            sys.exit(0)

    except Exception as e:
        print(e)
        