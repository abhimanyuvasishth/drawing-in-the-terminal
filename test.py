from time import sleep
from sys import stdout
import random
import noise
from blessings import Terminal

term = Terminal()
width = term.width
height = term.height

print(width)
noise_step = 0

def map(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

while True:
	my_line = ""
	noise_value = noise.pnoise1(noise_step,1)
	mapped_value = int(map(noise.pnoise1(noise_step,1), -1,1,0,width))
	mapped_value_width = int(map(noise.pnoise1(noise_step,1), -1,1,2,10))

	# for x in range(0,mapped_value):
	for x in range(0,width):
		# my_line += "o"

		if x > mapped_value-mapped_value_width and x < mapped_value+mapped_value_width:
			my_line += ' '
		else:
			my_line += ' '

	print(term.on_color(random.randint(0,10)) + my_line + '\n')
	noise_step += 0.01
	stdout.flush()
	sleep(0.01)