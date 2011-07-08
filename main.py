from os import *
from functions import *
from config import *

import re
import sys



# number of songs to move to quantum folder, if it is empty
QUANTUM_SIZE = 100

# application initialization

# print style().h1() + ' === Otaguj si svoji hudbu === ' + style().normal()


# make sure all necessary directories exists
ensure_dirs = [MUSIC_OUTBOX_DIR, MUSIC_QUANTUM_DIR]

for single_dir in ensure_dirs:
    if not os.path.exists(single_dir):
        ensure_dir(single_dir)
        print style().info() + 'slozka ' + single_dir + ' neexistuje, vytvarim' + style().normal()

# check whether any files are in quantum dir
if not os.listdir(MUSIC_QUANTUM_DIR):
    print
    print style().h2() + 'QUANTUM je prazdne, naplnim ho tudiz soubory' + style().normal()

    # list all files in inbox
    quantum_files = []
    for root, dirs, files in os.walk(MUSIC_INBOX_DIR):
        for file in files:
            if re.search(".mp3|.wma", file):
                quantum_files.append(root + "\\" + file)

    # take quantum from inbox
    quantum_files = quantum_files[:QUANTUM_SIZE]
    print 'Beru z inboxu ' + str(len(quantum_files)) + ' souboru'

    for quantum_file in quantum_files:
        os.rename(quantum_file, MUSIC_QUANTUM_DIR + "\\" + os.path.basename(quantum_file))
        sys.stdout.write('.')

    print style().normal()
    print style().normal() + 'Soubory presunuty z inboxu do kvanta'
else:
    print style().normal() + 'V kvantu jsou soubory (' + str(len(os.listdir(MUSIC_QUANTUM_DIR))) + '), nedelam tudiz nic'




