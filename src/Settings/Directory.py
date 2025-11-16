from PyQt5.QtWidgets import QPushButton, QLineEdit, QFileDialog

from .Field import OField

class ODirectoryField(OField):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._line = QLineEdit()
        self._line.setReadOnly(True)
        btn = QPushButton("...")
        btn.setFixedWidth(25)
        btn.clicked.connect(self.choose)
        self.layout.addWidget(self._line)
        self.layout.addWidget(btn)

    def choose(self):
        directory = QFileDialog.getExistingDirectory(self, "Select directory", "")
        if directory:
            self._value = directory
            self._line.setText(directory)