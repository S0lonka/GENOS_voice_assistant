
#! Важно называть переменные по шаблону 

# Начало     это имя файла      config_logger   
# Дальше     расширение         env
# Последнее  окончание на темп  temp

# Все они разделяются нижним подчёркиванием: config_logger_env_temp

config_env_temp = [
    "APP_LANG=RU",
    r"MODEL_PATH=app\assistant\model",
    r"ASSISTANT_NAME_PATH=app\assistant\assistant_name\genas_en_windows_v3_0_0.ppn",
    "DEVICE_INDEX=-1  # -1 для текущего устройства",
    "WAITING_WHILE_LISTENING=15",
    "", 
    ""
]

token_env_temp = [
    "PICOVOICE_TOKEN="
]

config_logger_env_temp = [
    "#----- ENABLE LOGGING ----",
    "# True  - ON",
    "# False - OFF",
    "",
    "MAIN               = True",
    "NOTIFICATION       = True",
    "FILE_UTILS         = True",
    "GENERAL_UTILS      = True",
    "CONFIG_UTILS       = True",
    "BROWSER_ACTIONS    = True",
    "TRAY               = True",
    "PLAY_SOUND         = True"
]



