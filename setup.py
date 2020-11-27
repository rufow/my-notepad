from cx_Freeze import setup, Executable

setup(
    name = "Блокнот",
    version = "0.1",
    description = "Блокнот, который ничего не забудет",
    author = "Сергей Руфов",
    author_email = "rufov@freeun.ru",
    options = {"build_exe": {"include_files": ["favicon.ico", "favicon.png"]}},
    executables = [Executable(script = "main.py", icon = "favicon.ico", targetName = "notepad.exe")]
)