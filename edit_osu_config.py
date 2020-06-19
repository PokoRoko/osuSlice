from osuSlice.osu_format import osu_file_format_v14

# Функция считывает файл конфига и возвращает его словарь
def read_train_config(file_adress):
    file = open(file_adress, 'r')
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
    return config


# Функция для определения начала среза
def begin_slice_point(dict_train_config):
    d = dict_train_config['[HitObjects]']
    search_min = 60000000
    for i in d:
        i = i.split(',')
        if int(i[2]) < search_min:
            search_min = int(i[2])
    return search_min


# Функция для определения конца среза
def and_slice_point(dict_train_config):
    d = dict_train_config['[HitObjects]']
    search_max = 0
    for i in d:
        i = i.split(',')
        if int(i[2]) > search_max:
            search_max = int(i[2])
    return search_max


print(begin_slice_point(read_train_config('obrazec_v14.osu')))
print(and_slice_point(read_train_config('obrazec_v14.osu')))


'''
# Функция для определения конца среза
def and_slice_point(dict_train_config):
'''