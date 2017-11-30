import os, glob
import parsers


path = './'
chatlist = glob.glob(os.path.join(path, '*.html'))
messages = []

for files in chatlist:
