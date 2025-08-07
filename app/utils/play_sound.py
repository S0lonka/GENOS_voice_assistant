import simpleaudio
from pvrecorder import PvRecorder
from typing import Optional

from app.config.config import APP_LANG
from app.utils.general_utils import create_logger, toggle_logging


logger = create_logger("play_sound")
toggle_logging(logger)

def play(sound_name: str, recorder: Optional[PvRecorder] = None) -> simpleaudio.PlayObject:
    '''Функция проигрывает звук по нужному пути,
    сразу заботясь о остановке и запуске записи
    
    Args:
        sound_name: имя звукового файла (без расширения)
        recorder: опциональный аргумент, передаётся только если нужно останавливать и запускать запись
    '''
    lang = APP_LANG
    
    if recorder:
        recorder.stop()
    

    # Список общих звуков(для всех языков)
    general_sounds = ["assistant_activate", "assistant_deactivate", "assistant_in_process", "assistant_start_lisen", "assistant_stop_lisen"]

    # Проверяем если звук в общей папке
    if sound_name in general_sounds:
        sound_path = f"app/sounds/general/{sound_name}.wav"
    else:
        sound_path = f"app/sounds/{lang}/{sound_name}.wav"

    wave_obj = simpleaudio.WaveObject.from_wave_file(sound_path).play()
    logger.info(f"Проигран звук {sound_name}")


    if recorder:
        recorder.start()

    return wave_obj # Возвращаем чтобы можно было использовать .wait_done() при вызове


