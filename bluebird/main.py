#!/usr/local/bin/python3
import pandas as pd
import numpy as np
import sys

import parsers

# validate args
if len(sys.argv) != 3:
    print('Usage: %s [CHAT.html] [DEST FILEPATH]' % sys.argv[0])
    sys.exit(3)
importPath = sys.argv[1]
exportPath = sys.argv[2]

# get message history as a DataFrame
f = open(importPath)
chat = parsers.getChat(f.read())
data = chat.data.reindex(index=chat.data.index[::-1])
users = chat.users

# write it to a csv
data.to_csv(exportPath)
