from random import *


name = input("Enter your Name: ")
mix = randrange(1,100)//10
number = len(name)*3*int(mix)



print("Hello {}, your lucky number is {}".format(name, number))
print(mix)
mix = 0
