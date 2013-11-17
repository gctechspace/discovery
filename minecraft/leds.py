from pyfirmata import Arduino, util
import time

board = Arduino('/dev/ttyACM0')

def rgb_cycle():
	board.digital[9].write(1)
	time.sleep(1)
	board.digital[9].write(0)
	board.digital[10].write(1)
	time.sleep(1)
	board.digital[10].write(0)
	board.digital[11].write(1)
	time.sleep(1)
	board.digital[11].write(0)

rgb_cycle()
