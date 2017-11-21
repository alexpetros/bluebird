from bs4 import BeautifulSoup
import pandas as pd

 
# PLACEHOLDER: eventually this should distinguish b/w chat plaftorms
def getChat(chat):
    return FBchat(chat)


class FBchat:
    """chat object for a Facebook conversation"""
    HEADER_CONSTANT = len("Conversation with ")

    def __init__(self, chat):
        """ load parsing wrapper """
        self.soup = BeautifulSoup(chat, 'html.parser')
        self.client = ''
        self.users = self.getUsers()
        self.data = self.getMessageData()

    def getMessageData(self):
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
            timestamp = pd.to_datetime(div.find('span', attrs={'class': 'meta'}).text)
            text = items[i+1].text

            # put into JSON for pandas use 
            message = {
                'sender': name,
                'timestamp': timestamp,
                'message': text,
                'wordcount': len(text) 
            }

            # run a quick test to see if the user is in the senders yet
            # practical chat limits prevent this from being too time-intensive
            if not foundSelf and name not in self.users:
                self.client = name
                foundSelf = True

            # append dict to list of messages 
            messages.append(message)
        
        return pd.DataFrame(messages)

    def getUsers(self):
        """get names of people in the conversation"""
        title = self.soup.find('title').text[self.HEADER_CONSTANT:]
        names = title.split(", ")
        return names
