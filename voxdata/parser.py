from bs4 import BeautifulSoup
import pandas as pd 

def getMessageData(chat):
    """given text in HTML format, return dataframe"""

    # get soup objects 
    soup = BeautifulSoup(chat, 'html.parser')
    thread = soup.find('div', attrs={'class': 'thread'})
    items = thread.contents

    # get each header and subsequent paragraph
    messages = []
    for i in range(1, len(items), 2):
        div = items[i]
        name = div.find('span', attrs={'class': 'user'}).text
        timestamp = pd.to_datetime(div.find('span', attrs={'class': 'meta'}).text)
        text = items[i+1].text

        # put into JSON dict 
        message = {
            'sender': name,
            'timestamp': timestamp,
            'message': text,
            'wordcount': len(text) 
        }
        # append dict to list of messages 
        messages.append(message)
    
    return pd.DataFrame(messages)