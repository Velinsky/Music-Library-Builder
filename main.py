from os import *
from functions import *

import sys

# constants definitions
MUSIC_INBOX_DIR = 'F:\Music\inbox'
MUSIC_QUANTUM_DIR = 'C:\Projects\Music quantum'
MUSIC_OUTBOX_DIR = 'F:\Music\outbox'

# application initialization

print style().h1() + ' === Otaguj si svoji hudbu === '


# make sure all necessary directories exists
ensure_dirs = [MUSIC_OUTBOX_DIR, MUSIC_OUTBOX_DIR]

for single_dir in ensure_dirs:
    if not os.path.isdir(single_dir):
        ensure_dir(single_dir)
        print style().info() + 'slozka ' + single_dir + ' neexistuje, vytvarim'




