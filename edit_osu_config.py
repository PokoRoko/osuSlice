from osuSlice.osu_format import osu_file_format_v14


# Функция считывает файл конфига и возвращает его словарь
def read_train_config(file_adress):
    file = open(file_adress, 'r', encoding='utf-8')
    config = osu_file_format_v14
    config_name = config.keys()
    key_for_key = 'osu_file_ver'

    for line in file:
        line = line.rstrip()
        if line in config_name:
            key_for_key = line
        else:
            x = config[key_for_key] + [line]
            config[key_for_key] = x
    file.close()
    return config


# Функция для определения начала среза
def begin_slice_point(dict_train_config):
    d = dict_train_config['[HitObjects]']
    search_min = 60000000
    for i in d:
        i = i.split(',')
        if int(i[2]) < search_min:
            search_min = int(i[2])
    print (f"Define begin slice point: {search_min}")
    return int(search_min)


# Функция для определения конца среза
def end_slice_point(dict_train_config):
    d = dict_train_config['[HitObjects]']
    search_max = 0
    for i in d:
        i = i.split(',')
        if int(i[2]) > search_max:
            search_max = int(i[2])
    print(f"Define end slice point: {search_max}")
    return int(search_max)


# Нужно определить интервал между вставками и привязаться к срезам [TimingPoints] и [HitObjects]
# Ну а тут самая жуть, так как требуется учесть кучу параметров, а потом еще и записать всё в файл.
def edit_new_TimingPoints(train_config,
                          begin_slice_point,
                          and_slice_point,
                          num_repeats):

    """
    !!!
    В этой функции некоректно отлажен счетчик повторов
    !!!
    """
    len_segment = and_slice_point - begin_slice_point
    new_TimingPoints = train_config['[TimingPoints]']

    len_old = len(train_config['[TimingPoints]'])  # Определяем длину списка для количества повторений
    count_repeats = 0  # Считает количество повторов и умнажает их в цикле
    #  Вырезает все параметры до момента с которого должны начаться повторы
    max_delete = []
    for i in new_TimingPoints:
        if i != '':
            j = i.split(',')
            if int(j[0]) >= and_slice_point:
                max_delete += [i]
    for i in max_delete:
        new_TimingPoints.remove(i)

    # Конфигурируем и создаем новые тайминговые точки
    for i in new_TimingPoints:
        if i != '':  # Лютый костыль изза которого появляются новые значения(некритично)
            i = i.split(',')  # Переводим строку в список
            if int(i[0]) > begin_slice_point:  # Отсечка по вырезаемомму отрезку
                i[0] = str(int(i[0]) + len_segment)  # Добавлям длину участка
                str_i = ','.join(i)  # Собираем обратно в строку
                new_TimingPoints.append(str_i)  # Добавляем строку с новым временем в конфиг
                count_repeats += 1  # Добвляем счетчик
        if count_repeats == num_repeats*len_old:
            break
    return new_TimingPoints


def edit_new_HitObjects(train_config,
                        begin_slice_point,
                        and_slice_point,
                        num_repeats):
    """
    !!!
    Обратить внимание на этот участок т.к добавляем абсолютно ровную длину отрезка, первая и последняя точка сходятся!
    Имеет смысл именно в этом месте закладывать дополнительный участок для переходал
    !!!
    """

    len_segment = and_slice_point - begin_slice_point
    new_HitObjects = train_config['[HitObjects]']

    len_old = len(train_config['[HitObjects]'])
    count_repeats = 0  # Считает количество повторов и умнажает их в цикле
    for i in new_HitObjects:
        i = i.split(',')  # Переводим строку в список
        # Добавлям к точке обьекта время переноса равное длине участка
        i[2] = str(int(i[2]) + len_segment)
        # !!! проверка типа обьекта на дополнительный параметр времени
        if int(i[3]) == 12:
            # Добавлям к точке обьекта время переноса равное длине участка
            i[5] = str(int(i[5]) + len_segment)
        str_i = ','.join(i)  # Собираем обратно в строку
        new_HitObjects.append(str_i)  # Добавляем строку с новым временем в конфиг
        count_repeats += 1  # Добвляем счетчик
        if count_repeats == num_repeats*len_old:
            break
    return new_HitObjects
