This is some basic python to follow the minecraft log file and trigger something to happen on an Arduino (running firmata).

The log file entry in created via a command block issuing something like 

	tellraw @p { text:"Arduino LED Triggered" } 

There might be other ways to write to log (with the txt only showing once) but this was simplest I could find without using mods.

To run do something like this (don't have to use virtualenv but I like this way as you don't have to have root access)

	virtualenv ENV
	source ENV/bin/activate
	pip install -r requirements.txt 
	python follow.py



