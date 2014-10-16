from PyQt4.QtCore import *
from PyQt4.QtGui import *

class DisplayWidget():

    def __init__(self):
        self.stacked_layout = QStackedLayout()
        self.setLayout(self.stacked_layout)
        self.model = None

    def display_results_layout(self):
        self.results_table = QTableView()
        self.results_layout = QVBoxLayout()

        self.results_layout.addWidget(self.results_table)

        self.results_widget = QWidget()
        self.results_widget.setLayout(self.results_layout)

        self.stacked_layout.addWidget(self.results_widget)
