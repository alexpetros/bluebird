import os, glob
import pandas as pd

from bluebird import parsers

# PLACEHOLDER: eventually this should distinguish between chat platforms
def getProfile(path):
    return FBProfile(path)


class FBProfile:
    """data object for an entire facebook profile"""

    def __init__(self, path):
        """load tables-building wrapper on file"""
        self.chatlist = glob.glob(os.path.join(path, 'messages', '*.html'))

        # build JSON lists 
        convoList = []
        messageList = []
        self.buildChats(convoList, messageList)

        # save lists into dataframs
        self.conversations = pd.DataFrame(convoList)
        self.messages = pd.DataFrame(messageList)
        

    def buildChats(self, conversations, messages):
        """build conversations and messages tables"""
        id_count = 1000

        for file in self.chatlist:
            text = open(file).read()
            chat = parsers.getChat(text, convo_id=id_count)
            
            # ignores chats with only Facebook's annoying "auto" message
            if chat.data['sender'].count() != 1:
                # create new JSON conversation row
                convo = {
                    'uid': id_count,
                    'name': "chat with " + ", ".join(chat.users),
                    'num_messages': chat.data['sender'].count(),
                    'first_message_timestamp': pd.to_datetime(chat.data[:1].timestamp.item()),
                    'last_message_timestamp': pd.to_datetime(chat.data[-1:].timestamp.item())
                }

                # append to lists
                conversations.append(convo)
                messages.extend(chat.messages)

                id_count += 10
