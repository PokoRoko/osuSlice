from pydub import AudioSegment


def edit_train_mp3(address_mp3,
                   time_first_slice,
                   time_last_slice,
                   num_repeats,
                   break_time,
                   address_folder,
                   name_new_mp3
                   ):
    """
    Функция создает зацикленный тренировочный mp3 файл
    :param address_mp3: Путь к файлу
    :param time_first_slice: Время начала зацикливания
    :param time_last_slice: Время окончания зацикливания
    :param num_repeats: Количество повторов
    :param break_time: Общее время для переходов затухания и набора громкости
    :param address_folder: Папка в которой лежит файл
    :param name_new_mp3: Имя для нового mp3 файла
    """

    song = AudioSegment.from_mp3(address_mp3)
    slice_segment = song[time_first_slice:time_last_slice]  # Определяем вырезаемый сегмент и присваиваем переменной
    fade_slice_segment = slice_segment.fade_in(int(break_time/2)).fade_out(int(break_time/2))
    begin_song = song[:time_last_slice]  # Начало трека до момента с которого будет начинаться повтор
    training_song = begin_song + (fade_slice_segment * num_repeats)  # Создаем тренировочный трек
    training_song.export(f'{address_folder+"//"+name_new_mp3}', format="mp3")  # Сохраняем результат в файл


