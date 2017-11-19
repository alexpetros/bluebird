#!/usr/local/bin/python3
import pandas as pd
import numpy as np
import sys

from voxdata import parser

# validate args
if len(sys.argv) != 3:
    print('Usage: [%s] [CHAT.html] [DEST FILEPATH]' % sys.argv[0])
    sys.exit(3)

# get message history as a DataFrame
importPath = sys.argv[1]
exportPath = sys.argv[2]
f = open(importPath)
data = parser.getMessageData(f.read())
data = data.reindex(index=data.index[::-1])


# write it to a csv
data.to_csv(exportPath)
