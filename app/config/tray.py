from pystray import Icon, Menu, MenuItem
from PIL import Image

def off_assistant(icon):
    icon.stop()



def create_tray():
    '''Основной конструктор иконки трея'''

    icon_image = Image.open("app/icon/Genos_hand_whiteBackground_icon.jpg")

    # Создаём трей
    tray_icon = Icon(
        name = "Genos VA",
        title = "Genos VA",
        icon = icon_image,

        # Настройка пунктов меню
        menu = Menu(
            MenuItem('Выйти', off_assistant)
        )
    )

    return tray_icon

tray_icon = create_tray().run()
