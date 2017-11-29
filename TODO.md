## Core Functionality 
These are projects on the core platform, which expand the gathering and cleaning operations to enable deeper analysis.

New paradigm:

* Messages Table: [message, sender, timestamp, wordcount, convo_id]
* Conversations Table: [convo\_id, convo\_name, first\_message\_timestamp, last\_message\_timestamp, num\_messages]
* People: [name, friend date]


## Interface
These are projects on expanding the platform's ease of use, starting with cmd interface and eventually a gui?

* Given FB folder, allow users to navigate and build individual conversations
* Default data build and indexing - where does it go?
* Encapsulate the neccesity of indexing into main functionality 
  - i.e. generate fucntion vs explore function

## Analysis
Making it easier to extract insight from the data generated 

* Develop new tables (users over group and single chats, conversations as observable unit of analysis)
* Pre-defined seaborn visualizations

## Product Management
Going the distance

* Clearner dependency management
* Makefile?