#JGore
#Hayden N. Walters
import BinSearchTree
import Queue

campers = BinSearchTree.BinarySearchTree

#
def timer():
    pass

def age():
    pass

#help
def h():
    print('r: Reads in a text file with commands.\nw: Writes a text file with enrolled campers in pre-order listing.\nq: Exits or quits a command.\ne: Enrolls a new camper. Requires name, age, and gender.')

def q():
    quit()

def r():
    txtfile = input('Enter the name of the text file you wish to read in:\n')
    with open(txtfile, "r") as ins:
        array = []
        for line in ins:
            array.append(line)

def w():
    pass
#e name age gender
def e(args, campers):
    args.split()
    name = args[0]
    age = int(args[1])
    if args[2] == 'm' or args[2] == 'f':
        gender = args[2]
        campers.insert(name, [name, age, gender]) 

def d(name, campers):
    campers.remove(name)
    print(name + ' is no longer enrolled.')

def l(args):
    pass

def g(args):
    pass

def p(args):
    pass

def arrival(args):
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
           'h': lambda: h(),\
           'd': lambda: d(args, campers),\
           'r': lambda: r(),\
           'w': lambda: w(),\
           'e': lambda: e(args, campers),\
           'l': lambda: l(args),\
           'g': lambda: g(args),\
           'p': lambda: p(args),\
           'arrival': lambda: arrival(args),\
           't': lambda: t(args),\
           'c': lambda: c()}
    
    comdict[cmd]()
           
