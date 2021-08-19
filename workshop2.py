# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:08:13 2021

@author: laura
"""

pressure=[0.27,0.456,0.33333,0.7,1.4] # lists can have different types of data in them (ie, str,int,float, etc.)
print('pressure:', pressure) # prints the entire list
print(len(pressure)) # list has a length of 5
pressure[1] # subsetting the second value (because starts at 0)

pressure.append(0.54333333) # will add this new value on to the end of the list
pressure.append([0.43,2.7,0.665]) # can append a list to an existing list
print(pressure)

pressure1=[0.27,0.456,0.33333,0.7,1.4]
pressure1.extend([0.43,2.7,0.665]) # extend the list (rather than adding a list within a list)
print(pressure1)

del pressure1[0] # should delete the first element of the list
print(pressure1)

empty = [] # creates an empty list
empty = [1,"rrrrr",1.2345] # can't change strings in lists (immutable)

del empty[1]
print(empty)

## For loops
"I like cats"
"I like dogs"
"I like gold fish"
"I like Jacob"

subjects=["cats","dogs","gold fish","Jacob"]
for i in subjects:
    print("I really like", i)  # this is the iterator
# can't comment on the first line of a for loop, but can add comments on the other lines. 

for number in [2,3,4]:
    print('the value of number * x=',number*2)

primes = [2,3,5]
for p in primes:
    squared=p ** 2
    cubed=p**3
    print("original:",p,"squared:",squared,"cubed:",cubed)
    
squared = []
primes = [2,3,5]
for p in primes:
    sqr=p**2
    squared.append(sqr)
print(squared)

for i in range(0,4,1):
    print("the value of i in this loop is:",i) # python ranges finish on the number before the one listed, ie, at 3. 
    
for i in range(0,len(primes),1):
    print("the value of i in this loop is:",i)

for i in range(0,len(primes),1):
    print("the value of i in this loop is:",primes[i])

















