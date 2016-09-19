# builtin packages
from sys import stdout
import os
from time import sleep
import random

#additional packages > install using pip install <NAMEOFPACKAGE>
import noise
from blessings import Terminal

interval = 0.001

term = Terminal()
width = term.width
height = term.height
unit = 5

cols = []
os.system("clear")

for x in range(0,int(width/unit)):
	cols.append(x*unit)

def random_move_drawing():
    while True:
        with term.location(cols[random.randint(0,len(cols)-1)], random.randint(0, height-2)):
            print(term.green+str(random.randint(0,9)))
            term.location()

try:
    random_move_drawing()
except KeyboardInterrupt:
    print("bye!")
