from PyQt5.QtWidgets import QPushButton, QColorDialog, QFrame

from .Field import OField

class OColorField(OField):
    def __init__(self, parent=None):
        super().__init__(parent)

        self._preview = QFrame()
        self._preview.setStyleSheet("background-color: transparent; border: 1px solid #000;")
        btn = QPushButton("...")
        btn.setFixedWidth(25)
        btn.clicked.connect(self.choose)
        self.layout.addWidget(self._preview)
        self.layout.addWidget(btn)

    def choose(self):
        color = QColorDialog.getColor(parent=self, title="Select color")
        if color.isValid():
            self._value = color.name()
            self._preview.setStyleSheet(f"background-color: {self._value}; border: 1px solid #000;")