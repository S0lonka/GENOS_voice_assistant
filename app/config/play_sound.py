import simpleaudio as sa
from pvrecorder import PvRecorder
from typing import Optional

def play(sound_name: str, recorder: Optional[PvRecorder] = None) -> None:
    '''Функция проигрывает звук по нужному пути,
    сразу заботясь о остановке и запуске записи
    
    Args:
        sound_name: имя звукового файла (без расширения)
        recorder: опциональный аргумент, передаётся только если нужно останавливать и запускать запись
    '''
    if recorder:
        recorder.stop()

    sound_path = f"app/sounds/{sound_name}.wav"
    wave_obj = sa.WaveObject.from_wave_file(sound_path).play()

    if recorder:
        recorder.start()


