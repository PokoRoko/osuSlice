# MAIN osuSlice











'''
from pydub import AudioSegment
print("Hello World")

song = AudioSegment.from_mp3("audio.mp3")
# Количество повторов
num_repeats = 4
# Размер одной секунды


# Начало вырезаемого сегмента в тысячных секунды
begin_slice_segment = 10000
# Конец вырезаемого сегмента в тысячных секунды
end_slice_segment = 14000
# Определяем вырезаемый сегмент и присваиваем переменной
slice_segment = song[begin_slice_segment:end_slice_segment]

"""
Так как необходимо сохранить первую часть песни до среза, для того чтобы сохранились настройки карты
необходимо определить с какого места мы будем запускать повтор вырезанного сегмента.
"""
# Начало трека до момента с которого будет начинаться повтор
begin_song = song[:end_slice_segment]

#Создаем тренировочную песню
training_song = begin_song + (slice_segment * num_repeats)

# Сохраняем результат в файл
training_song.export("training_song.mp3", format="mp3")


# Save the results with tags (metadata)
# awesome.export("mashup.mp3", format="mp3", tags={'artist': 'Various artists', 'album': 'Best of 2011', 'comments': 'This album is awesome!'})
'''


