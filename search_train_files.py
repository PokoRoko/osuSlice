import os

# Функция производит поиск по всем подпапкам и возвращает вложенные списки с путём и именем ко всем файлам *[train].osu
# Где первый элемент списка это адресс, а второй полный адрес к файлу
def find_train_file(dir_for_search):
    res = []
    for root, dirs, files in os.walk(dir_for_search):
        for file in files:
            if file.endswith("[train].osu"):
                res += [[os.path.join(root), os.path.join(root, file)]]
    return res

# Принимает список с адресами папок и конфиг файлов, считывает конфиг и подцепляет оттуда путь оригинального mp3 файла
def find_old_mp3(dir_for_search):
    res = []
    for i in dir_for_search:
        file = open(i[1], 'r', encoding='utf-8')
        for line in file:
            line = line.rstrip()
            if line[0:15] == 'AudioFilename: ':
                mp3_name = line[15:len(line)]
                mp3_adress = str(i[0])+'\\'+str(mp3_name)
                res += [i+[mp3_adress]]
                break

    return res

adress_list = find_old_mp3(find_train_file('Songs'))
print(adress_list)
