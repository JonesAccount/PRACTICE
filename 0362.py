from random import *

words = (" гей", " не гей")

jabka = lambda name, true: name + choice(true)

print(jabka("Жаба", words))