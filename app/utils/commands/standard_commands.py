import sys
from app.utils.play_sound import play

def hello():
    play("hello_brother_ru", "RU").wait_done()
    print("Привет брат, я тебя слушаю")


def off_va():
    play("ok_goodbye_bro_ru", "RU").wait_done()
    print("Выключаюсь")
    sys.exit(0)

