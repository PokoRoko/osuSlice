# MAIN osuSlice
# Для создания .exe можно использовать (pyinstaller --onefile --noconsole main.py )
# Для обновления файла интерфейса (pyuic5 interface.ui -o interface.py)

import sys
from PyQt5 import QtWidgets
from gi_operation import OsuSlice


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    osu_slice = OsuSlice()
    osu_slice.show()
    sys.exit(app.exec_())
