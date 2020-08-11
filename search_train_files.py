import os


def find_train_file(dir_for_search, difficalty):
    """
    Функция производит поиск по всем подпапкам и возвращает вложенные списки
    с путём и именем ко всем файлам *[НАЗВАНИЕ СЛОЖНОСТИ].osu
    :param dir_for_search: Папка для поиска
    :param difficalty: Название сложности
    :return: Вложеный список, где первый элемент списка адресс, второй полный путь к файлу
    """
    res = []
    for root, dirs, files in os.walk(dir_for_search):
        for file in files:
            if file.endswith(f"[{difficalty}].osu"):
                res += [[os.path.join(root), os.path.join(root, file)]]
    return res


def find_old_mp3(dir_for_search):
    """
    Функция возвращает полный путь к исходному mp3 файлу, на основании записи в исходном конфиг файле osu
    :param dir_for_search: пака в которой лежит конфигуратор
    :return: Полный путь к исходному файлу mp3
    """
    res = []
    for i in dir_for_search:
        file = open(i[1], 'r', encoding='utf-8')
        for line in file:
            line = line.rstrip()
            if line[0:15] == 'AudioFilename: ':
                mp3_name = line[15:len(line)]
                mp3_address = str(i[0])+'\\'+str(mp3_name)
                res += [i+[mp3_address]]
                break
    return res



