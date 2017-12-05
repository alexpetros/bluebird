# Bluebird  

A lightweight platform for exporting and analyzing message history as data. 

Currently supports Facebook messanger. iMessage pending. 

### What does it do?

* Builds full profile of your chat history in three discrete tables (okay right now it's two)
* Extracts each message and associates it with relevant metadata
* Generates list of chat participants, including client 
* Exports data in "clean" format to `.csv` file, where each row represents one message sent 

### What will it do?
* Cross-conversation analysis 
* Classify conversations for more rigorious analysis
* Output pre-defined analyses and graphs 
* Support more chat platforms
* Better user interface (as in, a Gov prof should be able to use it)

## Usage 

### Installation
1. Requires Python 3. In most cases the default installation binds the shell to `python3` and `pip3`, but if your default `python` doesn't point to 2.7x for some reason, then adjust the console commands accordingly. Yes, I will add better Python dependency management practices soon. 

2. Download your data dump from Facebook. You can learn about that process [here](https://www.facebook.com/help/131112897028467 "Facebook Help Center"). It's not hard, just submit a request and the data is ready to download in a few minutes.

3. Download and extract the folder somewhere.

4. Clone the repo. I'm not finished packaging it yet, so for now just work out of the repo's root directory and you're fine.

5. Install dependencies with: `pip3 install -r requirements.txt`


### Script (build tables for external analysis)
From root directory, run: `bluebird/buildnest.py [FBDATA_DIR]`

The script builds a `.bluebirdstore` directory in the facebook data folder. Currently it holds a `conversations.csv` file, and `messages.csv` file.

The two .csv files correspond to tables that you can import into visulazation or analysis software of your choice. Messages contains your entire message history - and each message has a conversation id that corresponds to a unique entry in the conversations table, for joining. 

### Module (build tables for python analysis)
To build aggregate history profile run:

```python
from bluebird import profiles

profile = profiles.getProfile(FBDATA_FILEPATH)
convo = profile.conversations
messasges = profile.messages
```

To load a single chat as a Pandas DataFrame run: 

```python
from bluebird import parsers

f = open(CHAT_FILEPATH)
data = parsers.getChat(f.read())
```

The only HTML files cuurently supported are messenger files extracted from Facebook's data download. 


## Contributing 
See the TODO.md file in this directory and let people know what you're working on. 

To run current testing suite (from root directory):

`python3 -m pytest` 

