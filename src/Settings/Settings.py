from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QGridLayout, QHBoxLayout

from .Directory import ODirectoryField
from .Color import OColorField

class OSettings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.setGeometry(100, 100, 300, 200)
        
        layout = QVBoxLayout()
        
        label = QLabel("This is the settings dialog.")
        layout.addWidget(label)
        
        general_label = QLabel("Ogólne")
        layout.addWidget(general_label)

        general_layout = QGridLayout()
        name_label = QLabel("Nazwa:")
        self.name_field = ODirectoryField("~/")
        general_layout.addWidget(name_label, 0, 0)
        general_layout.addWidget(self.name_field, 0, 1)

        value_label = QLabel("Wartość:")
        self.value_field = ODirectoryField("~/")
        general_layout.addWidget(value_label, 1, 0)
        general_layout.addWidget(self.value_field, 1, 1)

        layout.addLayout(general_layout)

        colors_label = QLabel("Kolory")
        layout.addWidget(colors_label)

        colors_layout = QGridLayout()

        bg_label = QLabel("Kolor tła:")
        self.bg_field = OColorField("#000000")
        colors_layout.addWidget(bg_label, 0, 0)
        colors_layout.addWidget(self.bg_field, 0, 1)

        text_label = QLabel("Kolor tekstu:")
        self.text_field = OColorField("#000000")
        colors_layout.addWidget(text_label, 1, 0)
        colors_layout.addWidget(self.text_field, 1, 1)

        layout.addLayout(colors_layout)
        layout.addStretch()

        print_button = QPushButton("Print Values")
        print_button.clicked.connect(self._print_values)
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)
        close_button.clicked.connect(lambda: QApplication.instance().quit())

        button_row = QHBoxLayout()
        button_row.addStretch()
        button_row.addWidget(print_button)
        button_row.addWidget(close_button)
        layout.addLayout(button_row)

        self.setLayout(layout)

    def _print_values(self):
        print("Nazwa:", self.name_field.get_value())
        print("Wartość:", self.value_field.get_value())
        print("Kolor tła:", self.bg_field.get_value())
        print("Kolor tekstu:", self.text_field.get_value())