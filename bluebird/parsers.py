from bs4 import BeautifulSoup
import pandas as pd

 
# PLACEHOLDER: eventually this should distinguish b/w chat plaftorms
def getChat(text, convo_id=None):
    return FBChat(text, convo_id)


class FBChat:
    """chat object for a Facebook conversation"""
    HEADER_STRING= len("Conversation with ")
    STYLE_STRING= '/* Copyright 2004-present Facebook. All Rights Reserved. */'

    def __init__(self, text, convo_id):
        """ load parsing wrapper """
        self.soup = BeautifulSoup(text, 'html.parser')

        if not self.isFBChatFile():
            raise Exception('Not a Facebook chat file')

        self.client = ''
        self.users = self.getUsers()
        # temp loading dialogue
        print("saving chat with " + ", ".join(self.users))
        self.messages = self.getMessages(convo_id)

        self.data = pd.DataFrame(self.messages)

    def getUsers(self):
        """get names of people in the conversation"""
        title = self.soup.find('title').text[self.HEADER_STRING:]
        names = title.split(", ")
        return names    

    def getMessages(self, convo_id):
        """
        given text in HTML format, return dataframe

        relies on self.getUsers() having been already called
        so that it can check for the missing user (the sender)
        """
     
        thread = self.soup.find('div', attrs={'class': 'thread'})
        items = thread.contents
        foundSelf = False

        # get each header and subsequent paragraph
        messages = []
        for i in range(1, len(items), 2):
            div = items[i]
            name = div.find('span', attrs={'class': 'user'}).text
            timestamp = pd.to_datetime(div.find('span', attrs={'class': 'meta'}).text[:-4])
            text = items[i+1].text

            # JSON is easy for pandas to parse 
            message = {
                'sender': name,
                'timestamp': timestamp,
                'message': text,
                'wordcount': len(text),
                'convo_id': convo_id
            }

            # run a quick test to see if the user is in the senders yet
            # practical chat limits prevent this from being too time-intensive
            if not foundSelf and name not in self.users:
                self.client = name
                foundSelf = True

            messages.append(message)
        
        return messages


    def isFBChatFile(self):
        """checks header string to see if it matches expected style"""
        return self.soup.style.string[:59] == self.STYLE_STRING
