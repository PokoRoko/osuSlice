from interface import *
from PyQt5 import QtWidgets
from osu_file_class import *
from edit_mp3 import edit_train_mp3
from search_train_files import find_old_mp3, find_train_file

name_new_mp3 = "mytrain.mp3"


class OsuSlice(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.buttonStartSlice.clicked.connect(self.start_slice)  # Вешаем на кнопку функцию start_slice
        self.step = 0

    def ui_print(self, text):
        self.ui.logText.append(text)
        self.ui.logText.repaint()

    def progress_plus(self, proc):
        self.step = self.step + proc
        self.ui.progressBar.setValue(self.step)

    # Путь к исходному файлу с конфигурацией
    def start_slice(self):
        self.step = 0
        difficulty = self.ui.nameDifficulty.text()  # Считываем сложность с интерфейса
        num_repeats = self.ui.numRepeat.value()  # Считываем количество повторов с интерфейса
        break_time = self.ui.interval.value()  # Считываем время интервала с интерфейса
        tpf = 0  # Total processed folders

        # Работа программы
        address_list = find_old_mp3(find_train_file(('Songs'), difficulty))
        for address in address_list:

            address_folder = address[0]  # Путь к папке
            address_config = address[1]  # Полный путь к файлу конфикурации
            address_mp3 = address[2]     # Полный путь к mp3

            self.ui_print(f'{tpf+1}/{len(address_list)}\nFolder processing: .\{address_folder}')
            self.progress_plus(int(100/len(address_list)))

            osu_cfg = read_train_config(address_config)  # Путь к исходному файлу с конфигурацией
            begin = osu_cfg.read_time_first_hit_object() - int(break_time/2)  # Определяет интервал для набора громкости
            end = osu_cfg.read_time_last_hit_object() + int(break_time/2)  # Определяет интервал для затухания громкости

            new_timing_points = osu_cfg.generate_new_timing_points(begin, end, num_repeats)
            osu_cfg['[HitObjects]'] = new_timing_points  # Новое наполнение для HitObjects
            new_timing_points = osu_cfg.generate_new_timing_points(begin, end, num_repeats)
            osu_cfg['[TimingPoints]'] = new_timing_points  # Новое наполнение для TimingPoints

            self.ui_print(f"Creates new train configuration file: {name_new_mp3}[generated].osu")
            osu_cfg.write_train_file(address_folder, name_new_mp3)  # Создается новый файл osu

            self.ui_print(f"Creates new mp3 file: {name_new_mp3}")
            edit_train_mp3(address_mp3, begin, end, num_repeats, break_time, address_folder, name_new_mp3)

            self.ui_print(f"Folder processing finished: {address_folder}\n______________________")
            tpf += 1

        if tpf == 0:
            self.ui_print(f'Config files difficulty:"{difficulty}" not found.')
        else:
            self.ui_print(f'Total processed folders: {tpf}\nDone!')
