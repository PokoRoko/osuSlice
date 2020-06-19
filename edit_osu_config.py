from osuSlise.osu_format import osu_file_format_v14

file = open('obrazec_v14.osu', 'r')

config = osu_file_format_v14
config_name = config.keys()
key_for_key = '1'

for line in file:
    line = line.rstrip()
    for i in config_name:
        if line == i:
            key_for_key = i
        if line != i:

# config = file.read().splitlines()
# for i in range(len(config)):
#     if config[i] == '[TimingPoints]':
#     elif config[i]


'''
# Функция считывает файл конфига и возвращает его словарь
def read_train_config(file_train_config):

# Функция для определения начала среза
def begin_slice_point(dict_train_config):

# Функция для определения конца среза
def and_slice_point(dict_train_config):
'''