import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QMainWindow):
    """A Simple window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        #create actions
        self.open_database = QAction("Open Database", self)
        self.close_database = QAction("Close Database", self)

        #add menu bar
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        #add actions to menu bar
        self.database_menu = self.menu.addMenu("database")
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        #add actions to tool_bar
        self.database_toolbar.addAction(self.open_database)
        self.database_toolbar.addAction(self.close_database)

        #create tool_bar
        self.addToolBar(self.database_toolbar)

        #create menu_bar
        self.setMenuBar(self.menu)

        #connections
        self.open_database.triggered.connect(self.open_connection)
        self.close_database.triggered.connect(self.close_connection)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)

    def close_connection(self):
        print("Close Connection")

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main()
