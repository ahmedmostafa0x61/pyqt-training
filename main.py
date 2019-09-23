from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import MySQLdb

main_ui, _ = loadUiType('login.ui')


class MainApp(QMainWindow, main_ui):
    def __init__(self):
        super(MainApp, self).__init__()
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.buttons()

    def buttons(self):
        self.pushButton.clicked.connect(self.new_user)


    def new_user(self):
        # Database connections
        self.db = MySQLdb.connect(host='localhost', user='root', password='159753852456', db='simple')
        self.cur = self.db.cursor()
        # Getting info from UI
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        # Inserting info into the DB
        self.cur.execute('''
            INSERT INTO users (username,password) VALUES ($s,$s)
        ''', (username,password))
        # # Commit Changes
        self.db.commit()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



