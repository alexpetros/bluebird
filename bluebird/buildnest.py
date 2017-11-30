#!/usr/local/bin/python3
import os, sys
import pandas as pd
import numpy as np

# TEMP add current package to sys 
sys.path.append(os.getcwd())


from bluebird import profiles

def main(argv):
    # validate args
    if len(argv) != 2:
        print('Usage: %s [FBDATA_DIR]' % argv[0])
        sys.exit(3)
    
    importpath = argv[1]

    # get full message history and create .bluebirdstore 
    profile = profiles.getProfile(importpath)
    storedir = createStoreDir(importpath)

    # export data
    conversations_path = os.path.join(storedir, 'conversations.csv')
    messages_path = os.path.join(storedir, 'messages.csv')
    profile.conversations.to_csv(conversations_path)
    profile.messages.to_csv(messages_path)


def createStoreDir(path):
    """
    check if bluebird store directory already exists in directory

    return path of new directory '/path/.bluebirdstore/'
    """
    storedir = os.path.join(path, '.bluebirdstore')

    if not os.path.exists(storedir):
        os.makedirs(storedir)
        return storedir
    else:
        extext = "Error: " + storedir + " already exists"
        raise Exception(extext)

# run script 
if __name__ == '__main__':
    main(sys.argv)
