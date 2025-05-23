# -*- coding: utf-8 -*-
"""22-47783-2_week01 .ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_MUJhvrG3kbtOSjSDV_RPlcpIFLEO9EY

# About this notebook
<p style="text-align: justify"> Here, you will learn the basic coding and data structures including numbers, strings, list, dictionaries and more. Some codes already done for demonstration. Some other codes, you will do as excercises.</p>

## Submission
<p style="text-align: justify">After completing the practice codes and exercises, download the notebook (.pynb file) and submit the notebook  to MS Teams inbox in the class period</p>
<p> 1.<b> You must submit your own code</b>. If similarity found negative marking will be given.</p>
<p> 2. Modify the file name writing your ID at the beigining of the file name.</p>
<p> 3. Other file format will not be accepted.</p>

# **INSTRUCTION**

# Number
"""

# basic numeric operations
34 - 30

# classic division returns a float
42/5

# floor division discards the fractional part
32 // 7



# assigin value to variable for later use
a = 1299 / 28
print(a)

# use the variable a for further operations
b = a*9
print(b)

a=2 ** 6
a

"""<b>Exercise 1:</b> Assign values to some variables and perform different operations. Also print the results."""

# code here
a=19
b=7

print(f'Addition= {a+b}')
print(f'Subtraction= {a-b}')
print(f'Division= {a/b}')
print("Multiplication= ",a*b)



"""# Import Module
<p style="text-align: justify"> Python code in one module gains access to the code in another module by the process of importing it. The import statement is the most common way of invoking the import machinery.</p>

<p style="text-align: justify">Python’s standard library is very extensive, offering a wide range of facilities. The library contains built-in modules (written in C) that provide access to system functionality such as file I/O that would otherwise be inaccessible to Python programmers, as well as modules written in Python that provide standardized solutions for many problems that occur in everyday programming. Some of these modules are explicitly designed to encourage and enhance the portability of Python programs by abstracting away platform-specifics into platform-neutral APIs.</p>

<b> Example:</b> Python has a built-in module that you can use for mathematical tasks. The math module has a set of methods and constants. The detail documentation can be found [here](https://docs.python.org/3/library/math.html).
"""

# importing the math module
import math
# accessing the constant π from math
print(math.tau)
print(math.pi)
print(math.fabs(-5))
print(math.ceil(5.8))
print(math.floor(9.45))
math.factorial(4)

# using the method sqrt from math
import math
math.sqrt(64)
#math.factorial(5)

"""<b>Remember:</b> A cell always outputs the value of last variable. If you want to show other values use print. See the below cell for an example."""

print(1+2)
print(a*4)
print(a/b)

"""<b>Exercise 2:</b> Import a module of your choice and show some operations.<br>
See all python module list [here](https://docs.python.org/3/py-modindex.html).
"""

# code here
# using the Time module
import time
current=time.time(0)
print("Current time since the epoch =",current)
print("current Time=  ",time.ctime(current))

#code
import random
print(random.randint(9,12))
list1 = [1, 2, 3, 4, 5]
print(random.sample(list1,3))

"""# Object types
The basic object types are Numbers, Strings, Lists, Dictionaries, Tuples, Files and Other types (Sets, types, None, Booleans etc.)
"""

a=10.5

# Checking the type of an object
print(type(a))
print(type(b))

c = 123
print(type(c))

d = '123'
print(type(d))

c = 45.5
print(type(c))

a = 7
d = 99+a
print(type(d))

"""# String"""

# assign value to a variable. The value can be qouted using '' or ""
s = 'Bangladesh'

# index
s[3]

# negative index
s = 'asdf'
s[-2]

"""When to use ' ' or " " ?

string operations with * and +
"""

'asif ' * 4

name='Tanzil '
name * 5

'asif ' + 'rahman'

'Kazi '+ name

# slicing
name = 'Ashraf Uddin'
print(name[4:8])
print(name[4:])
print(name[:4])
print(name[-3:])
print(name[1:8:2])
print(name[-1: :-1])

"""Some examples of string methods"""

name = 'Afsar Mahmud sayed'
sub = 'sa'
name.count(sub)

print(name.split())

print(name.split()[1])

name.islower()

mystring = 'I am right\nHe is fine\nThis it okay'
mystring.splitlines()

mystring = 'I am right\nHe is fine\nThis it okay'
mystring.split(' ')

separator = '??'
mystrings = ['Himel', 'Liton', 'Hasan', 'Fahim']
separator.join(mystrings)

#help(mystring.count)

len(name)

# check which functions you can use with variable 'name'
dir(name)

help(name.split)

"""<b>Exercise 3:</b> Demonstrate some string operations. Also, show uses of some string methods."""

# Code here

a='My name is '
b='Kazi Tanzizul '
c='Haque '
name=b+c
print("Welcome ",name)
print(a*2,b*3,c*5)
print(name[2:8])
print(name[1:])
print(name[:7])
print(name[-2:])
print(name[1:9:3])
print(name[-1: :-2])
x=a+'\n'+b+c
x.split()
x.splitlines()
name.islower()

"""# List
<p style="text-align: justify">Python knows a number of compound data types, used to group together other values. The most versatile is the list, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.</p>
"""

squares = [1, 4, 9, 16, 25]
squares

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.insert(0,10)
print(data)

"""Like strings (and all other built-in sequence types), lists can be indexed and sliced:"""

data[-3][1]

data[-1]

data[0:4]

data[1]

data[2][4]

len(data)

data

"""Some list methods"""

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.append(100)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.insert(2,100)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.remove(21)
print(data)

data = [21, 'Manager', ['Manager', 89000] ,4.50, 'Dhaka']
data.pop(3)
print(data)

dir(data)

#help(data.insert)

"""Lists also support operations like concatenation"""

squares + data

"""<b> Exercise 4:</b> Implement stack using list
<p><b>Hints:</b> The list methods make it very easy to use a list as a stack, where the last element added is the first element retrieved (“last-in, first-out”). To add an item to the top of the stack, use append(). To retrieve an item from the top of the stack, use pop() without an explicit index</p>

<b> Exercise 5:</b> Implement queue using list
<p><b>Hints:</b> It is also possible to use a list as a queue, where the first element added is the first element retrieved (“first-in, first-out”)</p>
"""

#code here
k=[1,2,3,4,5,['Tanzil',11],100]
k.append(100)
print(k)
k.append(['b',1])
print(k)
k.pop()
print(k)
k.pop()
print(k)
k.pop()
print(k)
k.pop(2)
print(k)

#code here
k=[1,2,3,4,5,['Tanzil',11],100]
k.append(15)
print(k)
k.append(['b',1])
print(k)
k.pop(0)
print(k)
k.pop(0)
print(k)
k.pop(0)
print(k)
k.pop(0)
print(k)

"""# Dictionary
<p style="text-align: justify">Dictionaries are sometimes found in other languages as “associative memories” or “associative arrays”. Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys, which can be any immutable type; strings and numbers can always be keys.</p>

<p style="text-align: justify">It is best to think of a dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary). A pair of braces creates an empty dictionary: {}. Placing a comma-separated list of key:value pairs within the braces adds initial key:value pairs to the dictionary; this is also the way dictionaries are written on output.</p>
"""

tel = {'jack': 4098, 'sape': 4139}

list(tel.keys())[1]

tel['guido'] = 4127
tel

person = {'Age':21,'Name':['niaz','rahman'], 'Salary':56000, 'Rating':4.50}

person['Rating']

len(person)

person.keys()

#person.has_key('Name')
'Name' in person.keys()

'niaz' in person['Name']

#dir(person)

"""<b> Exercise 6:</b> Define a dictionary to store the details of persons. Also, print some data from the dictionary.
 <p><b>Hint:</b> You may require nesting dictionary, lists, string inside the dictionary.</p>
"""

# Code here
person_Information = {'Age':22,'Name':['Kazi','Tanzizul'], 'Id':47783, 'Cgpa':4.93}
print(person_Information)
print(person_Information['Name'][1])
print(person_Information['Id'])
print(person_Information['Cgpa'])

print(list(person_Information.keys())[0])

dict_keys = person_Information.keys()
print(dict_keys)
print(person_Information.values())

print('Kazi' in person_Information['Name'])
print('Tanzil' in person_Information['Name'])
print('Cgpa' in person_Information.keys())

"""# Tuples and Sets
<b>Exercise 7: (Optional)</b> Use the content from [here](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) to follow some examples on tuple and set.
"""

# code from here