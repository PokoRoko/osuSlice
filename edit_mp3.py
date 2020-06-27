
# Функция создает и сохраняет файл с зацикленным фрагментом
def edit_train_mp3(original_mp3,  # Оригинальный файл mp3 для обработки
                   begin_slice_segment,  # Начало вырезаемого сегмента в тысячных секунды
                   end_slice_segment,  # Конец вырезаемого сегмента в тысячных секунды
                   num_repeats,  # Количество повторов
                   name_new_mp3
                   ):
    song = original_mp3

    # Определяем вырезаемый сегмент и присваиваем переменной
    slice_segment = song[begin_slice_segment:end_slice_segment]

    """
    Так как необходимо сохранить первую часть песни до среза, для того чтобы сохранились настройки карты
    необходимо определить с какого места мы будем запускать повтор вырезанного сегмента.
    """
    begin_song = song[:end_slice_segment]  # Начало трека до момента с которого будет начинаться повтор
    training_song = begin_song + (slice_segment * num_repeats)  # Создаем тренировочную песню

    training_song.export(name_new_mp3, format="mp3")  # Сохраняем результат в файл
    print(f"Created new mp3 file: ({name_new_mp3})")
