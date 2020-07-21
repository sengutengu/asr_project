import random, os, re
import shutil

def listdir_nohidden(path):
    for f in os.listdir(path):
        if not f.startswith('.'):
            yield f

source = 'musan/noise/sound-bible/'
destination = 'selected_noise/'


filenames = random.sample([name for name in os.listdir(source) if not name.startswith('.')], 50)

for name in filenames:
	shutil.move(source+name, destination)
