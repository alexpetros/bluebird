## Core Functionality 
These are projects on the core platform, which expand the gathering and cleaning operations to enable deeper analysis.

### Data structure
New paradigm:

* Messages Table: [message, sender, timestamp, wordcount, convo_id]
* Conversations Table: [convo\_id, convo\_name, first\_message\_timestamp, last\_message\_timestamp, num\_messages]
* People: [name, friend date]


### Script Interface
Eventually this could be used to bundle bluebird into a larger platform that uses these commands to execute it. 
 
 Currently: `bluebird/buildnest.py [FBDATA_DIR]`

* Add `...[NAME_GLOB]` to build all coversations with x person 
  * so if I did `buildnest ../fb-data spencer`, it would build all the conversations with a "spencer" 
  * forgive name mispellings and/or add autcomplete?
  * potentially more idiomatic to build as a wrapper over pandas than a script function
* API integration

### Analysis
Making it easier to extract insight from the data generated

* Develop new tables (users over group and single chats, conversations as observable unit of analysis)
* Pre-defined seaborn visualizations

## Product Management

### Setup and installation
* Implement Python dependency management best practices - needs a better setup.py for sure 
* Should be much easier to install
* Makefile?

### Testing
* Script unit tests!