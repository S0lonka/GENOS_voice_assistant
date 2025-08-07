from pystray import Icon, Menu, MenuItem
from PIL import Image

from app.config.tray_flag import stop_event 

# Глобальный флаг для выхода
exit_flag = False


def create_tray(stop_event_flag):
    '''Основной конструктор иконки трея'''

    icon_image = Image.open("app/img/icon/Genos_hand_whiteBackground_icon.jpg")

    # Создаём трей
    tray_icon = Icon(
        name = "Genos VA",
        title = "Genos VA",
        icon = icon_image,

        # Настройка пунктов меню
        menu = Menu(
            MenuItem('Выйти', lambda icon, item: off_assistant(icon, item, stop_event_flag))
        )
    )

    return tray_icon


def run_icon(icon, flag_event):
    icon.run()
    flag_event.set()  # Сигнализируем, что трея завершился


def off_assistant(icon, item, stop_event_flag):
    print("Пользователь выбрал 'Выход'")
    
    icon.stop()
    stop_event_flag.set()