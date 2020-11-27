from cx_Freeze import setup, Executable

setup(
    name = "Блокнот", # Имя программы
    version = "0.1", # Версия программы
    description = "Блокнот, который ничего не забудет", # Краткое описание о программе
    author = "Сергей Руфов", # Автор
    author_email = "rufov@freeun.ru", # Адрес email автора
    options = {"build_exe": {"include_files": ["favicon.ico", "favicon.png"]}}, # Подключение нужно для того чтобы в папке программы оказались иконки программы
    executables = [Executable(script = "main.py", icon = "favicon.ico", targetName = "notepad.exe")] # Информация о сборке
)
