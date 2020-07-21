import random, os, re
import shutil
from pathlib import Path


p = Path('LibriSpeech/dev-clean/')

source = 'LibriSpeech/dev-clean'
destination = 'selected_LS/'

#filenames = random.sample(os.listdir(source), 1)

#print(filenames)

print(os.listdir(source))

ext_list = [".txt"]

def removeNonPDFDirectories(dpath):
    '''Visit 'dpath', removing any subdirectory not containing any PDF
       file. Return True if 'dpath' is removed.
    '''
    import os
    if os.path.isdir(dpath):
        print('Entering', dpath)
        entries = [os.path.join(dpath, entry) for entry in os.listdir(dpath)]
        subdirs = filter(os.path.isdir, entries)
        print('    Subdirectories:', subdirs)
        if all(map(removeNonPDFDirectories, subdirs)):
            print('    All subdirectories were removed.')
            files = filter(os.path.isfile, entries)
            pdf_files = [f for f in files if f.endswith('.txt')]
            print('    PDF files:', pdf_files)
            if not pdf_files:
                try:
                    for f in files:
                        os.unlink(f)
                        print('    Removed file', f)
                    os.rmdir(dpath)
                    print('    Removed directory', dpath)
                except OSError as e:
                    # An error occurred: assume directory is not empty.
                    print('    ERROR:', e)
                    print('    Keeping directory', dpath)
                    return False
                # Directory was removed: report to caller.
                return True
        # Directory must be kept: report to caller.
        print('    Keeping directory', dpath)
        return False
    else:
        return False


print(removeNonPDFDirectories(source))


filenames = random.sample(list(p.glob('**/**/*.flac')), 50)

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




#filenames = random.sample([name for name in os.listdir(source) if not name.startswith('.')], 50)

#for name in filenames:
#	shutil.move(source+name, destination)
