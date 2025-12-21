"""
Example config.json:
{
  "main_dir": "/main/photo/search/directory",
  "deleted_dir": "/directory/to/store/deleted/files",
  "defer1_dir": "/first/custom/move/directory",
  "defer1_label": "First Custom Action Button Label",
  "defer2_dir": "/second/custom/move/directory",
  "defer2_label": "Second Custom Action Button Label"
}
"""

import sys
import os
import json
from pathlib import Path
from typing import List

from PyQt5.QtWidgets import QApplication, QMessageBox

from src import Sortopus, MainWindow, Config

CONFIG_FILENAME = "config.json"

def main():
    app = QApplication(sys.argv)

    base_path = Path(os.getcwd())
    config_path = base_path / CONFIG_FILENAME
    try:
        config = Config.Config().load_config(config_path)
    except Exception as e:
        QMessageBox.critical(None, 'Błąd', f'Cannot read config.json:\n{e}')
        return

    try:
        sorter = Sortopus.Sortopus(config)
    except Exception as e:
        QMessageBox.critical(None, 'Błąd', f'Exception occured during initialization:\n{e}')
        return

    window = MainWindow.MainWindow(sorter)
    window.resize(1000, 700)
    window.show()
    window.center()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
