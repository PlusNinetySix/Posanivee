#JGore
#Hayden N. Walters
import BinSearchTree
import Queue

def age():
    pass

def h():
    print('r: Reads in a text file with commands.\nw: Writes a text file with enrolled campers in pre-order listing.\nq: Exits or quits a command.\ne: Enrolls a new camper. Requires name, age, and gender.')

def q():
    quit

def r():
    pass

def w():
    pass

def e(name, age, gender):
    pass

def d(name):
    drop = input("Input the name of the camper you wish to drop.")

def l(name):
    pass

def g():
    pass

def p(order):
    pass

def arrival(time, number, name):
    pass

def t(time):
    pass

def c():
    pass

while True:
    command = input('Input a command. Type "h" for help.\n')
    cmd = command[0]
    args = command[2:]

    comdict = {'age': lambda: age(),\
           'q': lambda: q(),\
           'h': lambda: h()}
    
    comdict[cmd]()
           
