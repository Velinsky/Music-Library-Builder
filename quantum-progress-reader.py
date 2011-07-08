__author__ = 'Martin'

from functions import *
from config import *
from mutagen.mp3 import MP3

import mutagen.mp3
import os

# constant definitions
ID3_PLAYERPRO_RATING_TAG = "POPM:PlayerPro Android"

files = os.listdir(MUSIC_QUANTUM_DIR)
files_to_delete = []


# deleting files with rating 1* (51 out of 255)
for file in files:
    tag_infos = MP3(MUSIC_QUANTUM_DIR + "\\" + file)

    if ID3_PLAYERPRO_RATING_TAG in tag_infos:
        if tag_infos[ID3_PLAYERPRO_RATING_TAG].rating == 51:
            files_to_delete.append(file)

print "Found " + str(len(files_to_delete)) + " files with 1* rating"

var = raw_input("Delete them? (y/n)")


if var == "y":
    for file in files_to_delete:
        file_to_delete = MUSIC_QUANTUM_DIR + "\\" + file
        os.unlink(file_to_delete)

    print "Deleted the files"
