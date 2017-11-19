# Vox Data 

A lightweight platform for exporting and analyzing message history as data. 

Currently supports Facebook messanger. Teddy claims he can do iMesssage. We shall see. 

## Setup and Usage
To install dependencies, run: `pip3 install -r requirements`

To get .csv, run: `main.py [CHAT_FILEPATH.html] [DEST _FILEPATH.csv]`

To load as dataframe within python interpreter, run: 
```python
from voxdata import parser
f = open(CHAT_FILEPATH.html)
data = parser(f.read())
```

The only HTML files cuurently supported are messenger files extracted from Facebook's data download. Better, more flexible user interface to come.

## What does it do?

* Extracts each message and associates it with relevant metadata
* Exports data in "clean" format to `.csv` file, where each row represents one message sent 

## What will it do?
* Build convos by name from just pointing to data folder 
* Classify conversations for more rigorious analysis
* Output pre-defined analyses and graphs 
* Support more chat platforms
* Better user interface (as in, a Gov prof should be able to use it)


