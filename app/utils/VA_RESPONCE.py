from pvrecorder import PvRecorder
import vosk
import yaml
import os
import sys
from typing import Union, Tuple, Optional

from app.utils.commands.standard_commands import *

    
def check_command(voice: str) -> Tuple[bool, str | None, list[str] | None]:
    ''' Функция обрабатывает команду, путём поиска ключевого слова для вызова команды
    из файла commands.yaml

    Args:
        voice: Распознаный текст без изменений

    Return:
        found_command: найдена ли команда
        result: название функции - если найдена
        args: доп аргументы аргументы - если есть
    '''

    # Путь до команд
    current_dir = os.path.dirname(__file__)  
    yaml_path = os.path.join(current_dir, "..", "commands_text", "commands.yaml")
    yaml_path = os.path.normpath(yaml_path)

    # Парсим yaml
    with open(yaml_path, "r", encoding="UTF-8") as file:
        file = yaml.safe_load(file)

        voice_list = voice.split() # Переведём наш текст в последовательность слов

        for voice_list_word in voice_list:  # Проверяем каждое слово(из сказанного), команда ли оно?
            for command in file:            # Проходимся по командам(функции)
                for key in file[command]:     # Проходимся по словам вызывающих команды

                    if isinstance(key, dict):      # Специальная обработка команд с аргументами
                        key_word = next(iter(key)) # Берём ключевое слово - здесь key словарь 
                        
                        if key_word == voice_list_word:
                            args = key[key_word]
                            return True, command, args # Команда с аргументами
                    else:
                        if key == voice_list_word: # Сравниванием команду со сказанным словом
                            return True, command, None # Команда без аргументов

        else:
            return False, None, None # Команда не найдена
        


#! Основная функция ответа
def voice_assistant_responce(voice: str, recorder: PvRecorder, kaldi_reс: vosk.KaldiRecognizer) -> bool:
    try:
        recorder.stop() # остановим запись во время обработки
        if voice != "": # Только если не тишина, иначе вернём false
            print(f"\n- Распознано: {voice}")
            
            found_command, result, args = check_command(voice) # Вернёт flag = False если не найдёт команду

            if found_command:
                # Проверяем что такая функция существует И что её можно запустить
                if result in globals() and callable(globals()[result]):
                    print(f"- Команда {result} выполнена")
                    
                    if args: # Проверка вызова функции с аргументами и без
                        globals()[result](voice, args) # Передадим voice для лишних обработок
                    else:
                        globals()[result]()

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


