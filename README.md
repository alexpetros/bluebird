# Vox Data 

A lightweight platform for exporting and analyzing message history as data. 

Currently supports Facebook messanger. Teddy claims he can do iMesssage. We shall see. 

## Setup and Usage
To install dependencies, run: 

`pip install -r requirements.txt`

To run a script that automatically generates a .csv, run: 

`./bluebird/main.py [CHAT_FILEPATH.html] [DEST _FILEPATH.csv]`

To load chat history as a Pandas DataFrame run: 

```python
from bluebird import parser

f = open(CHAT_FILEPATH.html)
data = parsers.getChat(f.read())
```

The only HTML files cuurently supported are messenger files extracted from Facebook's data download. Better, more flexible user interface to come.

## What does it do?

* Extracts each message and associates it with relevant metadata
* Generates list of chat participants, including client 
* Exports data in "clean" format to `.csv` file, where each row represents one message sent 

## What will it do?
* Build conversations by name from just pointing to data folder 
* Cross-conversation analysis 
* Classify conversations for more rigorious analysis
* Output pre-defined analyses and graphs 
* Support more chat platforms
* Better user interface (as in, a Gov prof should be able to use it)

## Contributing 
See the TODO.md file in this directory and let people know what you're working on. 

To run current testing suite (from root directory):

`python -m pytest` 

