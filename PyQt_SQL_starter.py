try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
except:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    
import sys
import pdb

from SQLController import *
from DisplayWidget import *

class MainWindow(QMainWindow):
    """A Simple window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        #create actions
        self.open_database = QAction("Open Database", self)
        self.close_database = QAction("Close Database", self)
        self.find_products = QAction("Find Products", self)
        self.show_products = QAction("Show Products", self)

        #add menu bar
        self.menu = QMenuBar()
        self.database_toolbar = QToolBar()

        #add database actions to menu bar
        self.database_menu = self.menu.addMenu("Database")
        self.database_menu.addAction(self.open_database)
        self.database_menu.addAction(self.close_database)

        #add product actions to menu bar
        self.products_menu = self.menu.addMenu("Product")
        self.products_menu.addAction(self.find_products)
        self.products_menu.addAction(self.show_products)

        #make products menu items inactive
        self.find_products.setEnabled(False)
        self.show_products.setEnabled(False)

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
        self.find_products.triggered.connect(self.display_products)
        self.show_products.triggered.connect(self.display_products)

        #keyboard shortcuts
        self.open_database.setShortcut('Ctrl+O')
        self.close_database.setShortcut('Ctrl+Shift+C')
        self.find_products.setShortcut('Ctrl+F')
        self.show_products.setShortcut('Ctrl+Shift+F')

    def open_connection(self):
        #pdb.set_trace() 
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print("Database connection established: {0}".format(ok))
        self.find_products.setEnabled(True)
        self.show_products.setEnabled(True)

    def close_connection(self):
        self.connection.close_database()
        print("Database Closed")
        self.find_products.setEnabled(False)
        self.show_products.setEnabled(False)
        

    def display_products(self):
        if not hasattr(self, "display_widget"):
            self.display_widget = DisplayWidget()
        self.setCentralWidget(self.display_widget)
        query = self.connection.find_products_by_number((1,))
        self.display_widget.show_results(query)

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main()
