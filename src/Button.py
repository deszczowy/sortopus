from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPainter
from PyQt5.QtCore import QByteArray, Qt
from PyQt5.QtSvg import QSvgRenderer

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

def create_icon_button(icon_number: int, label: str) -> QPushButton:
    """
    Tworzy QPushButton z ikoną SVG o podanym numerze i etykietą.
    
    :param icon_number: numer ikony (1, 2, ...)
    :param label: tekst etykiety przycisku
    :return: skonfigurowany QPushButton
    """
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
    
    button = QPushButton(label)
    button.setIcon(icon)
    return button