from pvrecorder import PvRecorder
import vosk
import yaml
import os
import sys
import inspect
from typing import Union, Tuple, Optional


from app.utils.commands.standard_commands import *

def get_yaml_path(file_name):
    # Путь до файла с командами
    current_dir = os.path.dirname(__file__)  
    yaml_path = os.path.join(current_dir, "..", "commands_text", file_name)
    yaml_path = os.path.normpath(yaml_path)
    return yaml_path

    

def check_command(voice: str) -> Tuple[bool, str | None]:
    ''' Функция обрабатывает команду, путём поиска ключевого слова для вызова команды
    из файла commands.yaml

    Args:
        voice: Распознаный текст без изменений

    Return:
        found_command: найдена ли команда
        result: название функции - если найдена
    '''

    yaml_path = get_yaml_path("commands.yaml") # Парсим yaml с командами

    # Парсим yaml
    with open(yaml_path, "r", encoding="UTF-8") as file:
        file = yaml.safe_load(file)
        
        for command in file:                # Проходимся по командам(функции)
            for key_word in file[command]:  # Проходимся по словам вызывающих команды
                if key_word in voice:       # Сравниванием команду со сказанным словом
                    return True, command    # Команда найдена и есть название

        else:
            return False, None # Команда не найдена
        


#! Основная функция ответа
def voice_assistant_responce(voice: str, recorder: PvRecorder, kaldi_reс: vosk.KaldiRecognizer) -> bool:
    try:
        recorder.stop() # остановим запись во время обработки
        if voice != "": # Только если не тишина, иначе вернём false
            print(f"\n- Распознано: {voice}")
            
            found_command, result = check_command(voice) # Вернёт flag = False если не найдёт команду

            if found_command:
                # Проверяем что такая функция существует И что её можно запустить
                if result in globals() and callable(globals()[result]):
                    print(f"- Команда {result} запущена")
                    handler = globals()[result]

                    sig = inspect.signature(handler)
                    parameters = sig.parameters

                    if "voice" in parameters: # Проверка функций которым нужен параметр - voice
                        handler(voice)
                    else:
                        handler()

                    # globals()[result](voice)

                    return True
                

                else:
                    print("Команду не получилось выполнить")
                    return False
            else:
                print("Команда не найдена")
                return False
        else:
            print("Ничего не распознано")
            return False
    finally:
        kaldi_reс.Reset() #? очистка


