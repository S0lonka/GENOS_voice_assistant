from app.utils.Translator import Translator

t = Translator()

data = t.get_notify("info", "Token env created")
print(data)
print(data["title"])