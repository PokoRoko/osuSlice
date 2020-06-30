

# Функция создает и сохраняет файл с зацикленным фрагментом
def edit_train_mp3(original_mp3,  # Оригинальный файл mp3 для обработки
                   begin_slice_segment,  # Начало вырезаемого сегмента в тысячных секунды
                   end_slice_segment,  # Конец вырезаемого сегмента в тысячных секунды
                   num_repeats,  # Количество повторов
                   break_time,  # Интервал между повторами
                   address_folder,  # Адресс папки для записи
                   name_new_mp3  # Имя нового mp3
                   ):
    song = original_mp3

    # Определяем вырезаемый сегмент и присваиваем переменной
    slice_segment = song[begin_slice_segment:end_slice_segment]
    fade_slice_segment = slice_segment.fade_in(int(break_time/2)).fade_out(int(break_time/2))
    """
    Так как необходимо сохранить первую часть песни до среза, для того чтобы сохранились настройки карты
    необходимо определить с какого места мы будем запускать повтор вырезанного сегмента.
    """
    begin_song = song[:end_slice_segment]  # Начало трека до момента с которого будет начинаться повтор
    training_song = begin_song + (fade_slice_segment * num_repeats)  # Создаем тренировочную песню

    training_song.export(f'{address_folder+"//"+name_new_mp3}', format="mp3")  # Сохраняем результат в файл

    print(f"Created new mp3 file: ({name_new_mp3})")

