import leds
import tailer
for line in tailer.follow(open('/home/dalts/.minecraft/logs/latest.log')):
    if "Arduino LED Triggered" in line:
	print "Sending message to Arduino"
        leds.rgb_cycle() 
