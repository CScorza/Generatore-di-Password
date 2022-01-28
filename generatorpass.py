# File name: generatorpass.py
# Author: Scorza 
# Date created: 08/01/2022
# Python Version: 3.9


import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerbers = "0123456789"
symbols = "*?[]!-#@%$&/\=£°<>"

all = lower + upper + numerbers + symbols 

length = 16

password = "".join(random.sample(all, length))

print (password)
