from winotify import Notification
import os

# Функция по созданию уведомлений (windows)
def notification(title: str, msg: str, duration: str = "long") -> None:
    # Путь до иконки
    current_dir = os.path.dirname(__file__)  
    icon_path = os.path.join(current_dir, "..", "img", "icon", "Genos_icon.ico")
    icon_path = os.path.normpath(icon_path)

    # Конструктор уведомления
    toast = Notification(
        "Genos",   # App_id
        title,
        msg,
        icon_path, # icon - path
        duration
    )
    
    toast.show() # Вызов уведомления
