from pathlib import Path

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QShortcut,
)

from PyQt5.QtGui import (
    QPixmap,
    QImage,
    QKeySequence,
)

from PyQt5.QtCore import Qt

from . import Sortopus
from . import Button

class MainWindow(QWidget):
    def __init__(self, sorter: Sortopus):
        super().__init__()
        self.sorter = sorter
        self.setWindowTitle('Sortopus')
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setStyleSheet('background-color: #222; color: #fff;')
        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet('QPushButton{width: 100px; height: 25px; }')

        # przyciski
        self.btn_prev = QPushButton('Previous')
        self.btn_leave = Button.ButtonGenerator("Leave here", Button.Icon.ICON1).create() # QPushButton('Leave here')
        self.btn_defer1 = QPushButton(self.sorter.defer1_label)
        self.btn_defer2 = QPushButton(self.sorter.defer2_label)
        self.btn_defer3 = QPushButton(self.sorter.defer3_label)
        self.btn_delete = QPushButton('Delete')
        self.btn_next = QPushButton('Next')

        self.btn_prev.clicked.connect(self.on_prev)
        self.btn_leave.clicked.connect(self.on_leave)
        self.btn_defer1.clicked.connect(self.on_defer1)
        self.btn_defer2.clicked.connect(self.on_defer2)
        self.btn_defer3.clicked.connect(self.on_defer3)
        self.btn_delete.clicked.connect(self.on_delete)
        self.btn_next.clicked.connect(self.on_next)
        self.create_shortcuts()

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_prev)
        btn_layout.addWidget(self.btn_leave)
        btn_layout.addWidget(self.btn_defer1)
        btn_layout.addWidget(self.btn_defer2)
        btn_layout.addWidget(self.btn_defer3)
        btn_layout.addWidget(self.btn_delete)
        btn_layout.addWidget(self.btn_next)
        btn_layout.addStretch()

        layout = QVBoxLayout()
        layout.addWidget(self.image_label, stretch=1)
        layout.addWidget(self.status_label)
        layout.addLayout(btn_layout)

        self.setLayout(layout)

        self.update_ui()
    
    def create_shortcuts(self):
        # Definitions
        self.shortPrevious = QShortcut(QKeySequence(Qt.Key_Left), self)
        self.shortLeave = QShortcut(QKeySequence("Q"), self)
        self.shortMove1 = QShortcut(QKeySequence("1"), self)
        self.shortMove2 = QShortcut(QKeySequence("2"), self)
        self.shortMove3 = QShortcut(QKeySequence("3"), self)
        self.shortDelete = QShortcut(QKeySequence("Delete"), self)
        self.shortNext = QShortcut(QKeySequence(Qt.Key_Right), self)

        # Bindings
        self.shortPrevious.activated.connect(self.on_prev)
        self.shortLeave.activated.connect(self.on_leave)
        self.shortMove1.activated.connect(self.on_defer1)
        self.shortMove2.activated.connect(self.on_defer2)
        self.shortMove3.activated.connect(self.on_defer3)
        self.shortDelete.activated.connect(self.on_delete)
        self.shortNext.activated.connect(self.on_next)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_image_display()

    def update_ui(self):
        item = self.sorter.get_current_item()
        if item is None:
            self.image_label.setText('No photos')
            self.status_label.setText('')
            self.set_buttons_enabled(False)
            return
        self.set_buttons_enabled(True)
        # disable prev if first
        if self.sorter.current_index == 0:
            self.btn_prev.setEnabled(False)
        else:
            self.btn_prev.setEnabled(True)

        self.update_image_display()
        self.update_status_label()

    def set_buttons_enabled(self, enabled: bool):
        for b in (self.btn_prev, self.btn_leave, self.btn_defer1, self.btn_defer2, self.btn_delete, self.btn_next):
            b.setEnabled(enabled)

    def update_image_display(self):
        item = self.sorter.get_current_item()
        if item is None:
            return
        path = Path(item['path'])
        if path.exists() and path.is_file():
            pix = QPixmap(str(path))
            if pix.isNull():
                # może format nieobsługiwany
                self.image_label.setText('Picture can not be load')
            else:
                # skaluj do rozmiaru label
                lbl_w = max(10, self.image_label.width())
                lbl_h = max(10, self.image_label.height())
                scaled = pix.scaled(lbl_w, lbl_h, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.image_label.setPixmap(scaled)
        else:
            # plik nie istnieje — wyczyść pixmap i napisz info
            self.image_label.setPixmap(QPixmap())
            self.image_label.setText(f'File not found:\n{item["path"]}')

    def update_status_label(self):
        item = self.sorter.get_current_item()
        if item is None:
            self.status_label.setText('')
            return
        status = item.get('status', 0)
        status_text = {
            0: 'Do zweryfikowania',
            1: 'Zweryfikowane',
            2: 'Zweryfikowane i przeniesione',
            3: 'Usunięte (przeniesione)'
        }.get(status, f'status: {status}')
        idx_text = f'[{self.sorter.current_index + 1}/{len(self.sorter.items)}] '
        self.status_label.setText(idx_text + status_text)

    def move_and_next(self, target_dir: Path, new_status: int):
        idx = self.sorter.current_index
        if idx is None:
            return
        self.sorter.move_file_and_update(idx, target_dir, new_status)
        # przejdź do następnej
        if idx < len(self.sorter.items) - 1:
            self.sorter.current_index = idx + 1
        self.update_ui()

    def on_prev(self):
        self.sorter.go_to_prev()
        self.update_ui()

    def on_leave(self):
        idx = self.sorter.current_index
        if idx is None:
            return
        self.sorter.set_status(idx, 1)
        # przejdź do następnej pozycji
        if idx < len(self.sorter.items) - 1:
            self.sorter.current_index = idx + 1
        self.update_ui()

    def on_defer1(self):
        self.move_and_next(self.sorter.defer1_dir, 2)

    def on_defer2(self):
        self.move_and_next(self.sorter.defer2_dir, 2)

    def on_defer3(self):
        self.move_and_next(self.sorter.defer3_dir, 2)

    def on_delete(self):
        # przenieś do katalogu usuniętych i ustaw status 3
        self.move_and_next(self.sorter.deleted_dir, 3)

    def on_next(self):
        self.sorter.go_to_next()
        self.update_ui()