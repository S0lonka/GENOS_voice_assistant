import json

from app.config.config import APP_LANG


class Translator:
    '''
    Класс отвечающий за изменение языка в проекте
    '''
    def __init__(self, lang=APP_LANG):
        self.lang = lang
        self.notification = self._load_file("notification")
        self.log = self._load_file("log")
        # self.translations = self._load_translations()

    # Внутренняя функция чтения файла
    def _load_file(self, file_type: str):
        file_path = f"app/locales/{self.lang}/{file_type}.json"
        try:
            with open(file_path, "r", encoding="UTF-8") as file:
                return json.load(file)
            
        except FileNotFoundError:
            raise ValueError(f"File '{file_path}' not found")


    def get_notify(self, type: str, key: str):
        data = self.notification[type][key]

        if not data:
            print(f"Перевод ненайден для {key}")
            return {'title':'', 'msg':''}
        else:           
            return data


    def get_log(self, key: str, **placeholders):
        pass

