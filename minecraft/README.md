This is some basic python to follow the minecraft log file and trigger something to happen on an Arduino (running firmata).

The log file entry is created via a command block using a command something like 

	tellraw @p { text:"Arduino LED Triggered" } 

There might be other ways to write to log (with the txt only showing once) but this was simplest I could find without using mods.

To run, do something like this (don't have to use virtualenv but I like this way as you don't have to have root access)

	virtualenv ENV
	source ENV/bin/activate
	pip install -r requirements.txt 
	python follow.py

Tested on Linux - but everything is pure python so you should be able to run on windows and mac (just change the path to the minecraft log file in follow script).

The leds.py currently just switches the RGB led on my leostick - you can make your Arduino do whatever you like. If you don't like firmata then you could also write your own program on the Arduino and communicate via the python serial library.

