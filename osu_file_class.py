
def read_train_config(file_address):
    """
    Функция для считывания файлов конфигурации OSU в словарь,
    где значения это список параметров.
    :param file_address: Полный путь к файлу
    :return: Словарь с параметрами по ключу
    """
    file = open(file_address, 'r', encoding='utf-8')
    config = OsuFileClass()
    # Создаем словарь с основными конфигурациями
    config.update({
                'OsuFileVersion': [],
                '[General]': [],
                '[Editor]': [],
                '[Metadata]': [],
                '[Difficulty]': [],
                '[Events]': [],
                '[TimingPoints]': [],
                '[Colours]': [],
                '[HitObjects]': []
               })

    # TODO разбивку конфигурационного файла можно расширить до чтения по одному параметру

    config_name = config.keys()
    key_for_key = 'OsuFileVersion'

    for line in file:
        line = line.rstrip()
        if line == '':  # Отсекаем пустые строкик
            pass
        elif line in config_name:   # Запись по последнему ключу
            key_for_key = line
        else:
            x = config[key_for_key] + [line]
            config[key_for_key] = x
    file.close()
    return config


class OsuFileClass(dict):

    def read_time_first_hit_object(self):
        """
        Определяет время первого игрового обьекта
        (время начала среза для зацикливания)
        :return: Числовое значение в миллисекундах
        """
        d = self['[HitObjects]']
        search_min = 6000000
        for i in d:
            i = i.split(',')
            if int(i[2]) < search_min:
                search_min = int(i[2])
        return int(search_min)

    def read_time_last_hit_object(self):
        """
        Определяет время последнего игрового обьекта
        (время окончания среза для зацикливания)
        :return: Числовое значение в миллисекундах
        """
        d = self['[HitObjects]']
        search_max = 0
        for i in d:
            i = i.split(',')
            if int(i[2]) > search_max:
                search_max = int(i[2])
        return int(search_max)

    def generate_new_hit_object(self,
                                time_first_slice,
                                time_last_slice,
                                num_repeats
                                ):
        """
        Функция генерирует повторы и возвращает в виде словаря параметры для [HitObjects]
        :param time_first_slice: Время начала среза в миллисекундах
        :param time_last_slice: Время окончания среза в миллисекундах
        :param num_repeats: Количетво повторов
        :return: Словарь [HitObjects] с повторением значений
        """
        len_segment = time_last_slice - time_first_slice
        new_hit_objects = self['[HitObjects]']
        len_old = len(self['[HitObjects]'])
        count_repeats = 0  # Считает количество повторов и умнажает их в цикле
        for i in new_hit_objects:
            i = i.split(',')  # Переводим строку в список
            i[2] = str(int(i[2]) + len_segment)  # Добавлям к точке обьекта время переноса равное длине участка
            if int(i[3]) == 12:  # Проверка типа обьекта на дополнительный параметр времени
                i[5] = str(int(i[5]) + len_segment)  # Добавлям к точке обьекта время переноса равное длине участка
            str_i = ','.join(i)  # Собираем обратно в строку
            new_hit_objects.append(str_i)  # Добавляем строку с новым временем в конфиг
            count_repeats += 1  # Добвляем счетчик
            if count_repeats == num_repeats*len_old:
                break
        return new_hit_objects

    def generate_new_timing_points(self,
                                   time_first_slice,
                                   time_last_slice,
                                   num_repeats):
        """
        Функция генерирует повторы и возвращает в виде словаря параметры для [TimingPoints]
        :param time_first_slice: Время начала среза в миллисекундах
        :param time_last_slice: Время окончания среза в миллисекундах
        :param num_repeats: Количетво повторов
        :return: Словарь [TimingPoints] с повторением значений
        """
        # TODO Переписать алгоритм генерации новых [TimingPoints]
        len_segment = time_last_slice - time_first_slice
        new_timingpoints = self['[TimingPoints]']
        len_old = len(self['[TimingPoints]'])  # Определяем длину списка для количества повторений
        count_repeats = 0  # Считает количество повторов и умнажает их в цикле
        max_delete = []  # Вырезает все параметры до момента с которого должны начаться повторы
        for i in new_timingpoints:
            if i != '':
                j = i.split(',')
                if int(j[0]) >= time_last_slice:
                    max_delete += [i]
        for i in max_delete:
            new_timingpoints.remove(i)

        for i in new_timingpoints:  # Конфигурируем и создаем новые тайминговые точки
            if i != '':  # Лютый костыль изза которого появляются новые значения(некритично)
                i = i.split(',')  # Переводим строку в список
                if int(i[0]) > time_first_slice:  # Отсечка по вырезаемомму отрезку
                    i[0] = str(int(i[0]) + len_segment)  # Добавлям длину участка
                    str_i = ','.join(i)  # Собираем обратно в строку
                    new_timingpoints.append(str_i)  # Добавляем строку с новым временем в конфиг
                    count_repeats += 1  # Добвляем счетчик
            if count_repeats == num_repeats*(len_old-len(max_delete)):
                break
        return new_timingpoints

    def write_train_file(self, address_folder, name_new_mp3):
        """
        Функция записывает и сохраняет новый конфигурационный тренировочный файл
        с необходимыми для чтения параметрами
        :param address_folder: Адрес куда сохраняем файл
        :param name_new_mp3: Имя нового mp3 для записи в конфигурацию
        :return:
        """
        address_save = f'{address_folder+"//"+self["[General]"][0][15:(len(self["[General]"][0])-4)]}[generated_train].osu'
        f = open(address_save, 'tw', encoding='utf-8')
        self['[General]'][0] = f"AudioFilename: {name_new_mp3}"
        self['[Metadata]'][5] = f"Version:generated_train"
        key = self.keys()
        for i in key:
            f.write(i + '\n')
            for j in self[i]:
                f.write(j + '\n')
        f.close()
