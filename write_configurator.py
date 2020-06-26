from osuSlice.edit_osu_config import result

def write_config_file(train_config):
    f = open('Train [train]', 'tw', encoding='utf-8')
    key = train_config.keys()
    for i in key:
        f.write(i +'\n')
        for j in train_config[i]:
            f.write(j + '\n')
    f.close()
write_config_file(result)