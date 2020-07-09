
def write_config_file(train_config, address_folder, name_new_mp3):
    f = open(f'{address_folder+"//"+train_config["[General]"][0][15:(len(train_config["[General]"][0])-4)]}[generated_train].osu', 'tw', encoding='utf-8')
    train_config['[General]'][0] = f"AudioFilename: {name_new_mp3}"
    train_config['[Metadata]'][5] = f"Version:generated_train"
    key = train_config.keys()
    for i in key:
        f.write(i +'\n')
        for j in train_config[i]:
            f.write(j + '\n')
    f.close()

