from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtSvg import QSvgRenderer
from enum import IntEnum
from typing import Callable

class Icon(IntEnum):
    ICON1 = 1
    ICON2 = 2
    ICON3 = 3

ICON1 = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg
   width="1cm"
   height="1cm"
   viewBox="0 0 1 1"
   version="1.1"
   id="icon1"
   xmlns="http://www.w3.org/2000/svg">

    <ellipse
       style="fill:#ff0000;stroke-width:0.359792"
       id="path263"
       cx="0.5"
       cy="0.5"
       rx="0.5"
       ry="0.5" />
</svg>"""

class OButton(QPushButton):

    def __init__(self, button_caption: str, button_icon: Icon, action: Callable[[], None] = None) -> None:
        super().__init__(button_caption)
        self.icon = button_icon
        self.create()
        self.connect(action)
    
    def connect(self, action: Callable[[], None]) -> None:
        if action != None:
            self.clicked.connect(action)
    
    def create(self) -> None:

        icon_number = self.icon.value
        icon_const_name = f"ICON{icon_number}"
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
        
        #self.setText(self.caption)
        self.setStyleSheet("border:0px")
        self.setIcon(icon)
        #return self.button