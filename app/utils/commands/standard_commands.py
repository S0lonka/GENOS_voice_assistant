import sys
from app.utils.play_sound import play

#config
from app.config.numbers_word_ru import number_words

#audio
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume


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
def set_volume(voice, process_names):
    print("Вошёл в функцию")
    for key, value in number_words.items():
        if key in voice:
            volume = float(value)


    process_name = "Яндекс Музыка"
   # Получаем число из слова по словарю number_words(как и в проверке выше)
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
