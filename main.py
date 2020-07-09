# MAIN osuSlice
# Для создания .exe можно использовать (pyinstaller --onefile)
# Для обновления файла интерфейса (pyuic5 interface.ui -o interface.py)

import sys
from interface import *
from PyQt5 import QtWidgets
from edit_osu_config import (read_train_config, begin_slice_point, end_slice_point,
                                      edit_new_TimingPoints, edit_new_HitObjects)
from write_configurator import write_config_file
from edit_mp3 import edit_train_mp3
from search_train_files import find_old_mp3,find_train_file

name_new_mp3 = "mytrain.mp3"
class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Вешаем на кнопку функцию start_slice
        self.ui.buttonStartSlice.clicked.connect(self.start_slice)

    # Описываем функцию
    def start_slice(self):
        # В переменную stroki с помощья .toPlainText получаем текст из nameDifficulty
        difficulty = self.ui.nameDifficulty.text()
        num_repeats = self.ui.numRepeat.value()
        break_time = self.ui.interval.value()
        tpf = 0  # Total processed folders
        # Работа программы
        # Попеременно проходит все папки и обрабатывает программу на них
        address_list = find_old_mp3(find_train_file(('Songs'), difficulty))
        for address in address_list:
            address_folder = address[0]  # Путь к папке
            address_config = address[1]  # Полный путь к файлу конфикурации
            address_mp3 = address[2]     # Полный путь к mp3
            print(f'{tpf+1}/{len(address_list)}')
            print(f'Folder processing: .\{address_folder}')
            # Путь к исходному файлу с конфигурацией
            train_config = read_train_config(address_config)
            # Определяет начало отрезка в мс и отнимает половину интервала для набора звука
            begin = begin_slice_point(train_config) - int(break_time/2)
            # Определяет конец отрезка в в мс и прибавляет половину интервала для затухания
            end = end_slice_point(train_config) + int(break_time/2)
            # Создаем новое наполнение для HitObjects
            train_config['[HitObjects]'] = edit_new_HitObjects(train_config, begin, end, num_repeats)
            # Создаем новое наполнение для TimingPoints
            train_config['[TimingPoints]'] = edit_new_TimingPoints(train_config, begin, end, num_repeats)
            # Записывает в новый конфиг
            write_config_file(train_config, address_folder, name_new_mp3)
            # Сохраннение нового файла mp3
            edit_train_mp3(address_mp3, begin, end, num_repeats, break_time, address_folder, name_new_mp3)
            print(f"Folder processing finished: {address_folder}")
            print('______________________________________________')
            tpf += 1


        if tpf == 0:
            print(f'Train files difficulty:{difficulty} not found.')
        else:
            print(f'Total processed folders: {tpf}')

# TO_DO
# Сделать проверку на обработанные папки чтобы не обрабатывать заново

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())