import sys
from PyQt4.Core import *
from PyQt4.Gui import *

class MainWindow(QMainWindow):
    """A Simple window"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main()
