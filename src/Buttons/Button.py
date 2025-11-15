# System
from typing import Callable
from pathlib import Path

# PyQt
from PyQt5.QtWidgets import QPushButton, QShortcut
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QKeySequence
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtSvg import QSvgRenderer

# Module
from .IconEnum import IconEnum
from .Icons import *

class OButton(QPushButton):

    def __init__(self, id: int, button_caption: str, parameter_path: str, button_icon: IconEnum, hint: str = "", action: Callable[[], None] = None, shortcut: QKeySequence = None) -> None:
        super().__init__(f" {button_caption}")
        self.Id = id
        self.MovePath: Path = Path(parameter_path)
        self.icon = button_icon
        self.shortcut = None
        self.setup_hint(hint)
        self.create()
        self.connect(action, shortcut)
    
    def connect(self, action: Callable[[], None], shortcut_sequence: QKeySequence = None) -> None:
        if action != None:
            self.clicked.connect(action)
            
            if shortcut_sequence != None:
                self.shortcut = QShortcut(shortcut_sequence, self)
                self.shortcut.activated.connect(action)
    
    def create(self) -> None:

        icon_const_name = self.icon.name
        svg_data = globals().get(icon_const_name)
        if svg_data is None:
            raise ValueError(f"Ikona o numerze {icon_number} nie istnieje w module icons.py")
        
        byte_array = QByteArray(svg_data.encode('utf-8'))
        renderer = QSvgRenderer(byte_array)
        
        icon = QIcon()
        for size in (16, 24, 32):
            pixmap = QPixmap(size, size)
            pixmap.fill(Qt.transparent)
            painter = QPainter(pixmap)
            renderer.render(painter)
            painter.end()
            icon.addPixmap(pixmap, QIcon.Normal)

        self.setStyleSheet("border:0px")
        self.setIcon(icon)
    
    def setup_hint(self, hint):
        self.hint = ""
        if hint == "":
            self.hint = f"Move photo to {self.MovePath}"
        else:
            self.hint = hint

    def enterEvent(self, event):
        if self.parent():
            hinter: QLabel = self.parent().hint_label
            hinter.setText(self.hint)
        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.parent():
            hinter: QLabel = self.parent().hint_label
            hinter.clear()
        super().leaveEvent(event)