
def write_config_file(train_config, name_new_config, name_new_mp3):
    f = open(f'{name_new_config}', 'tw', encoding='utf-8')
    train_config['[General]'][0] = f"AudioFilename: {name_new_mp3}"
    key = train_config.keys()
    for i in key:
        f.write(i +'\n')
        for j in train_config[i]:
            f.write(j + '\n')
    f.close()
    print(f"Created new train config file: (Train [train].osu)")
