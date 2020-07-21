import random, os, re
import shutil
from pathlib import Path

p = Path('source/')

source = 'source/'
destination = 'selected_LRW/'

filenames = random.sample(list(p.glob('**/**/*.wav')), 50)


for name in filenames:
    print(str(name))
    source = name.parents[0]
    print(str(source))
    transcript = ''
    flag = 0
    for file in os.listdir(source):
        if file.endswith(".txt"):
            transcript = file
            flag = 1
    if flag == 0:
        print("DF:SKF:KDF:SKJD")
    print(transcript)

    shutil.copy(str(name), str(destination))
    shutil.copy(str(source) + '/' + transcript, str(destination))
