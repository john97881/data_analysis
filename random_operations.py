# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:56:10 2023

@author: User
"""

# This is a "guide" code that will help you become more acquianted with python

# we import the libraries of choice random and matplotlib
# remember to install the libraries using pip install in the console
# "as" works as a shorthand for libraries with big names

import matplotlib.pyplot as plt
import random

# We will define a function named coinflip , This sunction flips casts a six sided die
# we then count all evens in the list and replace all odds with the value six

def coinflip(N): #Name of the function and inputs eithin brackets
    i=0 # any numeric value can be set only by assigning the value using =
    # a string requires the " or the ' symbols
    
    list = [None] * N         #populate list, length n with n entries "None" 
    # this is how we create an empty list of size N
    # We can also create an empty list an use append, however it is slower 
    #for big calculations
    
    while i<N: # an alternetive to for - loops , here we must set the step size manually
    # first we set the rabdon process (from the random library)
        a = random.randrange(0, 6, 1)
        i=i+1 #manual counter
        if a%2==1 : # if the modulo of the die is 1 (odd)
            list.append(6)
        else:
            list.append(a)
        list = list[-N:] # What does this do? food for thought
    return(list)        
  
    # How can I do this using a for - loop ?

cf=coinflip(1400)

# Creating histogram
fig, ax = plt.subplots(figsize =(10, 7))
ax.hist(cf, bins = [ 0, 1, 2, 3, 4, 5, 6 ])
# Show plot
plt.show()


# General information\
    
# a for loop needs an enumerator and a range
# for i in range(10) does 10 steps, from 0 to 9
# for x in x, means for every element of list x in list x

x1=[11, 21, 31, 41]
for x1 in x1:
    print("Hello",x1)
    
#Except for lists, there also exist dictionaries and tuples
# tuples use the () instead of []
# a list of tuples

vectorspace = [(1,2), (3,4),(5,6),(7,8)]

#using print with strings and variables
# use + only for strings otherwise ,
print("The number" +" is " , vectorspace[3][1] , " from the last place of vectorspace")

# A dictionary uses {}

listofspaces={}
listofspaces[0] = {"Space1 ": vectorspace}
listofspaces[1] = {"Space2 ": vectorspace*2}

print(listofspaces)
print(listofspaces[0])