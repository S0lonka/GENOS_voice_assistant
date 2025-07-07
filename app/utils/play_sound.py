import simpleaudio as sa
import simpleaudio
from pvrecorder import PvRecorder
from typing import Optional

def play(sound_name: str, lang: str, recorder: Optional[PvRecorder] = None) -> simpleaudio.PlayObject:
    '''Функция проигрывает звук по нужному пути,
    сразу заботясь о остановке и запуске записи
    
    Args:
        sound_name: имя звукового файла (без расширения)
        lang: язык на котором говорит Genos
        recorder: опциональный аргумент, передаётся только если нужно останавливать и запускать запись
    '''
    
    if recorder:
        recorder.stop()
    

    # Список общих звуков(для всех языков)
    general_sounds = ["assistant_activate", "assistant_deactivate", "assistant_in_process", "assistant_start_lisen", "assistant_stop_lisen"]

    # Проверяем если звук в общей папке
    if sound_name in general_sounds:
        sound_path = f"app/sounds/general/{sound_name}.wav"
    else:
        sound_path = f"app/sounds/{lang}/{sound_name}.wav"

    wave_obj = sa.WaveObject.from_wave_file(sound_path).play()


    if recorder:
        recorder.start()

    return wave_obj # Возвращаем чтобы можно было использовать .wait_done() при вызове


