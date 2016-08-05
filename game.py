import global_vars
from characters import *
import functions
import random
from lol import *

global_vars.enemies.append(trol('grog', 1))
name = raw_input('What is thy name brave warrior? ')
char.name = name
print('Greetings %s, a trol is attacking our village please help us.') % char.name

functions.combat()



