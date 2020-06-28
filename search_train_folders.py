import glob
all_mp3 = glob.glob('./*/*/*.mp3')
for i in all_mp3:
    print(i)
