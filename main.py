import os
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
import sqlite3
from sqlite3 import Error
import design  # Это наш конвертированный файл дизайна

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.setWindowIcon(QIcon('favicon.png'))
        # Выборка записи
        cursorObj.execute('SELECT * FROM notepad WHERE id = 1')
        rows = cursorObj.fetchall()
        for row in rows:
            self.plainTextEdit.appendPlainText(str(row[1]))
        self.saveButton.clicked.connect(self.savePost)

    def savePost(self):
        # Обновление записи
        cursorObj.execute('UPDATE notepad SET body = "'+ str(self.plainTextEdit.toPlainText())+'" WHERE id = 1')
        con.commit()
        cursorObj.execute('SELECT * FROM notepad WHERE id = 1')
        rows = cursorObj.fetchall()
        for row in rows:
            self.plainTextEdit.setPlainText(str(row[1]))

def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение

new_insert = False

if (os.path.exists("database.db") == False):
    new_insert = True

con = sql_connection()
cursorObj = con.cursor()

# Создание таблицы
cursorObj.execute("CREATE TABLE if not exists notepad (id integer PRIMARY KEY, body text)")
con.commit()

# Создание первой записи
if new_insert:
    cursorObj.execute("INSERT INTO notepad(id, body) VALUES(1, '')")
    con.commit()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()

con.close()
