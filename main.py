# MAIN osuSlice
from osuSlice.edit_osu_config import (read_train_config, begin_slice_point, end_slice_point,
                                      edit_new_TimingPoints, edit_new_HitObjects)
from osuSlice.write_configurator import write_config_file
from osuSlice.edit_mp3 import edit_train_mp3
from pydub import AudioSegment


# Settings

# Путь к исходному файлу с настроками
train_config = read_train_config('train.osu')
# Путь к исходному файлу mp3
original_mp3 = AudioSegment.from_mp3("audio.mp3")
# Имя нового файла на выходе
name_new_config = "new train config.osu"
# Имя нового mp3 на выходе
name_new_mp3 = "mytrain.mp3"
# Количество повторов
num_repeats = 20
# Время разрыва между повторами
break_time = 6000


# Работа программы

# Определяет начало отрезка в мс
begin = begin_slice_point(train_config) + int(break_time/2)
# Определяет конец отрезка в в мс
end = end_slice_point(train_config) + int(break_time/2)
# Создаем новое наполнение для HitObjects
train_config['[HitObjects]'] = edit_new_HitObjects(train_config, begin, end, num_repeats)
# Создаем новое наполнение для TimingPoints
train_config['[TimingPoints]'] = edit_new_TimingPoints(train_config, begin, end, num_repeats)
# Записывает в новый конфиг
write_config_file(train_config, name_new_config,name_new_mp3)
# Сохраннение нового файла mp3
edit_train_mp3(original_mp3, begin, end, num_repeats, break_time, name_new_mp3)






