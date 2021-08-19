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

# If statements
mass=4.02
mass=[4.02,2.0,3.0,3.1]
if mass > 3.0:
    print(mass, 'is large')
else:
    print(mass, 'is not large')
    
if mass <= 3.0 and mass > 10.0:
    print(mass, 'is ridiculously large')
else:
    print(mass, 'is not large')

# If, elif (else if) and else statements:
if mass > 3.0 and mass <= 10.0:
    print(mass,'is large')
elif mass > 10.0:
    print(mass,'is ridiculously large')
else:
    print(mass, 'is not large')
    
masses = [2.4,7.4,1.1,52.3] # containing a conditional statement inside a for loop
for i in masses:
    if i > 3.0 and i <= 10.0:
        print(i,'is large')
    elif i > 10.0:
        print(i,'is ridiculously large')
    else:
        print(i, 'is not large')

# could replace the 'and' with 'or' to allow either conditional statement to be true.

masses=[2.4,7.4,1.1,52.3]
velocity=[53.6,100.4,7.2,10000.5]
if masses[1] > 3.0 and masses[2] <= 10.0 or velocity == 54:
    print('all good')

# glob library - deal with multiple files at once
import glob
import pandas as pd
for filename in glob.glob('C:/Users/laura/Documents/20210818 Python workshop/data/*.csv'):
    contents=pd.read_csv(filename)
    print(filename,len(contents))

contents = [] # create an empty list first
for filename in glob.glob('C:/Users/laura/Documents/20210818 Python workshop/data/*.csv'):
    cont=pd.read_csv(filename)
    contents=cont.append(contents)
    #print(filename,len(contents))

contents = [] # create an empty list first
for filename in glob.glob('C:/Users/laura/Documents/20210818 Python workshop/data/*.csv'):
    contents[filename]=pd.read_csv(filename)

cont.shape # gives dimensions of a data frame
cont.shape[1] # gives number of columns
cont.shape[0] # gives numer of rows

# create our own functions
def print_greeting():
    print("hello!!!")

print_greeting()

# create a function that does something useful
def print_date(year,month,day):
    joined=str(year)+'-'+str(month)+'-'+str(day)
    print(joined)
    return(joined)

Date = print_date(2021,"August",19)
Date

def average(values):
    if len(values) == 0:
        print("You must provide some values")
        return None # None is a special type in python
    return sum(values)/len(values)

av = average([2,5,3])
av = average([])
print(av)

def report(pressure):
    print('pressure is',pressure) # this prints on the fly, but won't add this to a variable
    return(pressure) # this will add this value to a variable if the function call is assigned to a variable
print('calling', report(22.5))

















































