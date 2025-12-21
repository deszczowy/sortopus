from PyQt5.QtWidgets import QLabel, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from .Core import OWidget

class OAbout(OWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        if parent is None:
            self.setWindowFlags(self.windowFlags() | Qt.Window)

        self.setWindowTitle("About Sortopus")
        self.setGeometry(0,0,100,200)

        multiline_text = """The weapon of choice for everyone who is flooded with photos. Gather all files, configure the tool, then make yourself comfortable and just sort it out. It is early version, so go easy on me. It works, that's important! Application will present You all your pictures, one by one, each with options to leave it where it is, delete it, or move into one of two optional directories."""
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Obrazek
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        pix = QPixmap("./src/gfx/octo.png")
        if not pix.isNull():
            # skaluj do maksymalnej szerokości 300 px zachowując proporcje
            scaled = pix.scaledToWidth(200, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled)
        else:
            self.image_label.setText("(obrazek nie znaleziony)")
        layout.addWidget(self.image_label, alignment=Qt.AlignCenter)

        # QLabel (np. tytuł/etykieta)
        self.title_label = QLabel("Sortopus")
        self.title_label.setAlignment(Qt.AlignCenter)
        # możesz dopasować styl, np. powiększyć czcionkę:
        # self.title_label.setStyleSheet("font-size: 16pt; font-weight: bold;")
        layout.addWidget(self.title_label, alignment=Qt.AlignCenter)

        # Tekst wieloliniowy
        self.text_label = QLabel(multiline_text)
        self.text_label.setWordWrap(True)
        self.text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.text_label, alignment=Qt.AlignCenter)

        # Guzik zamykający okienko
        self.close_button = QPushButton("Zamknij")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button, alignment=Qt.AlignCenter)

        self.setLayout(layout)
        self.setAttribute(Qt.WA_DeleteOnClose)