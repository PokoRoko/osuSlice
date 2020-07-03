# MAIN osuSlice
from edit_osu_config import (read_train_config, begin_slice_point, end_slice_point,
                                      edit_new_TimingPoints, edit_new_HitObjects)
from write_configurator import write_config_file
from edit_mp3 import edit_train_mp3
from pydub import AudioSegment
from search_train_files import address_list

# Settings
# Имя нового mp3 на выходе
name_new_mp3 = "mytrain.mp3"  #def="mytrain.mp3"
# Количество повторов
num_repeats = 15
# Время разрыва между повторами
break_time = 7000


# Работа программы
# Попеременно проходит все папки и обрабатывает программу на них
for address in address_list:

    address_folder = address[0]  # Путь к папке
    address_config = address[1]  # Полный путь к файлу конфикурации
    address_mp3 = address[2]     # Полный путь к mp3
    print(f'Folder processing: \{address_folder}')
    # Путь к исходному файлу с настроками
    train_config = read_train_config(address_config)
    # Путь к исходному файлу mp3
    original_mp3 = AudioSegment.from_mp3(address_mp3)
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
    edit_train_mp3(original_mp3, begin, end, num_repeats, break_time, address_folder, name_new_mp3)
    print("Successful processing")




