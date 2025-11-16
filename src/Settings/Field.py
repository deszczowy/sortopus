from PyQt5.QtWidgets import QWidget, QHBoxLayout

class OField(QWidget):

    def __init__(self, current_value, parent=None) -> None:
        super().__init__(parent)
        self._value = current_value
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.layout)
    
    def choose(self):
        pass

    def get_value(self):
        return self._value