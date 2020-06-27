# MAIN osuSlice
from osuSlice.edit_osu_config import (read_train_config, begin_slice_point, end_slice_point,
                                      edit_new_TimingPoints, edit_new_HitObjects)
from osuSlice.write_configurator import write_config_file
from osuSlice.edit_mp3 import edit_train_mp3
from pydub import AudioSegment


# Settings

# Путь к исходному файлу с настроками
train_config = read_train_config('obrazec_v14.osu')
# Путь к исходному файлу mp3
original_mp3 = AudioSegment.from_mp3("audio.mp3")
# Имя нового файла на выходе
name_new_mp3 = "myTrain.mp3"
# Количество повторов
num_repeats = 3


# Работа программы

# Определяет начало отрезка в мс
begin = begin_slice_point(train_config)
# Определяет конец отрезка в в мс
end = end_slice_point(train_config)
# Создаем новое наполнение для HitObjects
train_config['[HitObjects]'] = edit_new_HitObjects(train_config, begin, end, num_repeats)
# Создаем новое наполнение для TimingPoints
train_config['[TimingPoints]'] = edit_new_TimingPoints(train_config, begin, end, num_repeats)
# Записывает в новый конфиг
write_config_file(train_config,name_new_mp3)
# Сохраннение нового файла mp3
edit_train_mp3(original_mp3, begin, end, num_repeats, name_new_mp3)






