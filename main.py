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
        self.step = 0

    def ui_print(self,text):
        self.ui.logText.append(text)
        self.ui.logText.repaint()

    def progress_plus(self, proc):
        self.step = self.step + proc
        self.ui.progressBar.setValue(self.step)

    # Описываем функцию по кнопке
    def start_slice(self):
        self.step = 0
        difficulty = self.ui.nameDifficulty.text()  # Считываем сложность с интерфейса
        num_repeats = self.ui.numRepeat.value()  # Считываем количество повторов с интерфейса
        break_time = self.ui.interval.value()  # Считываем время интервала с интерфейса
        tpf = 0  # Total processed folders


        # Работа программы
        # Попеременно проходит все папки и обрабатывает программу на них
        address_list = find_old_mp3(find_train_file(('Songs'), difficulty))
        for address in address_list:

            address_folder = address[0]  # Путь к папке
            address_config = address[1]  # Полный путь к файлу конфикурации
            address_mp3 = address[2]     # Полный путь к mp3

            self.ui_print(f'{tpf+1}/{len(address_list)}\nFolder processing: .\{address_folder}')
            self.progress_plus(int(100/len(address_list)))
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
            self.ui_print(f"Creates new train configuration file: {name_new_mp3}[generated].osu")
            write_config_file(train_config, address_folder, name_new_mp3)
            # Сохраннение нового файла mp3
            self.ui_print(f"Creates new mp3 file: {name_new_mp3}")
            edit_train_mp3(address_mp3, begin, end, num_repeats, break_time, address_folder, name_new_mp3)
            self.ui_print(f"Folder processing finished: {address_folder}\n______________________")
            tpf += 1


        if tpf == 0:
            self.ui_print(f'Train files difficulty:{difficulty} not found.')
        else:
            self.ui_print(f'Total processed folders: {tpf}\nDone!')

# TO_DO
# Сделать проверку на обработанные папки чтобы не обрабатывать заново

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())