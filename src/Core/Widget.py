from PyQt5.QtWidgets import QWidget, QApplication

class OWidget(QWidget):

    def center(self):
        app = QApplication.instance()
        if app is None:
            raise RuntimeError("QApplication must exist before calling center().")

        screen = app.primaryScreen()
        screen_geo = screen.availableGeometry()

        frame = self.frameGeometry()
        frame.moveCenter(screen_geo.center())
        self.move(frame.topLeft())