import simpleaudio as sa
from pvrecorder import PvRecorder

def play(sound_name: str, recorder: PvRecorder) -> None:
    '''Функция проигрывает звук по нужному пути,
    сразу заботясь о остановке и запуске записи'''
    
    recorder.stop()
    sound_path = f"app/sounds/{sound_name}.wav"

    wave_obj = sa.WaveObject.from_wave_file(sound_path).play().wait_done()
    recorder.start()


