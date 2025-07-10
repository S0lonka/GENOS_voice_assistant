import sys
import os
import yaml

# utils
from app.utils.play_sound import play

#config
from app.config.numbers_word_ru import number_words

#audio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume




def get_yaml_path(file_name):
    # Путь до файла с командами
    current_dir = os.path.dirname(__file__)  
    yaml_path = os.path.join(current_dir, "..", "..", "commands_text", file_name)
    yaml_path = os.path.normpath(yaml_path)
    return yaml_path




# Приветствие
def hello():
    play("hello_brother_ru", "RU").wait_done()
    print("Привет брат, я тебя слушаю")



# Выключение Genos
def off_va():
    play("ok_goodbye_bro_ru", "RU").wait_done()
    print("Выключаюсь")
    sys.exit(0)



# Установить звук
def set_volume(voice):
    # Изначально зададим значения чтобы избежать None
    volume=0 
    process_name=""

    # ищем числовое значение в запросе
    for key, value in number_words.items(): 
        if key in voice:
            volume = float(value)



    yaml_path = get_yaml_path("process_names.yaml")
    # Парсим yaml
    with open(yaml_path, "r", encoding="UTF-8") as file:
        file = yaml.safe_load(file)

        for app_name in file:                # Проходимся по командам(функции)
            for key_word in file[app_name]:  # Проходимся по словам вызывающих команды
                if key_word in voice:   
                    process_name = app_name 
        

    if volume and process_name: # Проверим что переменные не пусты
        volume *= 0.01   # переводим в сотые доли
    
        if 0.0 <= volume and volume <= 1.0:     # Проверка что запрос в реальном диапозоне
            # Получаем список всех аудиосессий
            sessions = AudioUtilities.GetAllSessions()

            for session in sessions:
                if session.Process and session.Process.name() == f"{process_name}.exe":
                    # Получаем интерфейс управления громкостью для этого процесса
                    volume_interface = session._ctl.QueryInterface(ISimpleAudioVolume)
                    volume_interface.SetMasterVolume(float(volume), None)
                    print(f"Громкость для {process_name} установлена на {volume}")
                    break

            else:
                print(f"Процесс {process_name} не найден в аудиосессиях")
        else:
            print("Не верный диапозон")
    else:
        print("Не найдена громкость или процесс(приложение)")



def genos():
    print("Да, я тут, я уже слушаю")
