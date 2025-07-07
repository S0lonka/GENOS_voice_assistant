from pvrecorder import PvRecorder
import vosk
import yaml
import os
import sys
from typing import Union, Tuple, Optional

from app.utils.commands.standard_commands import *

    
def check_command(voice: str) -> Tuple[bool, str | None] :
    # Путь до команд
    current_dir = os.path.dirname(__file__)  
    yaml_path = os.path.join(current_dir, "..", "commands_text", "commands.yaml")
    yaml_path = os.path.normpath(yaml_path)

    # Парсим yaml
    with open(yaml_path, "r", encoding="UTF-8") as file:
        file = yaml.safe_load(file)

        for command in file:    # Проходимся по командам
            for key_word in file[command]:    # Проходимся по словам вызывающих команды
                if key_word == voice:
                    return True, command

        else:
            return False, None # команда не найдена
        

#! Основная функция ответа
def voice_assistant_responce(voice: str, recorder: PvRecorder, kaldi_reс: vosk.KaldiRecognizer) -> bool:
    try:
        recorder.stop() # остановим запись во время обработки
        if voice != "": # Только если не тишина, иначе вернём false
            print(f"\n- Распознано: {voice}")
            
            flag, result = check_command(voice) # Вернёт False если не наёдёт команду

            if flag:
                # Проверяем что такая функция существует И что её можно запустить
                if result in globals() and callable(globals()[result]):
                    print(f"Команда {result} выполнена")
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





 
    
            # if voice == "привет":
            #     print("Привет я на связи")
            #     return True

            # elif voice == "выключись":
            #     print("Выключаюсь")
            #     recorder.delete()
            #     sys.exit(0)




# def off_va():
#     print("Выключаюсь")

# def check_yaml(voice):    
#     current_dir = os.path.dirname(__file__)  
#     yaml_path = os.path.join(current_dir, "..", "commands_text", "commands.yaml")
#     yaml_path = os.path.normpath(yaml_path)

#     with open(yaml_path, "r", encoding="UTF-8") as file:
#         file = yaml.safe_load(file)

#         for command in file:
#             for key_word in file[command]:
#                 if key_word == voice:
#                     return command
                
#         else:
#             print("no")
                
# voice = "выключись"
# result = check_yaml(voice)
# print(result)
# if result in globals() and callable(globals()[result]):
#     globals()[result]()

