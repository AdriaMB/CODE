print("Hello World")

name = "Juan is" \
" my name"

print(name)

if name == "Juan":
    print("You are Juan")
elif name == "Eric":
    print("Macaquen suppen")
else:
    print(":3")

fruits =  ["apple", "macaquen", "suppen"]
for fruit in fruits:
    print(fruit)

counter = 0
while counter < 5:
    print(counter)
    counter += 1

    if counter == 3:
        break

for i in range(10):
    if i % 2 == 0:
        continue ## Jumps to the next iteration
    print(i)

fruits = ["apple", "banana", "orange"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1])
print(fruits[-2])
print(fruits[-3])

fruits.append("pear")
print(fruits)

fruits.insert(1, "macaquen")
print(fruits)

fruits.insert(8, "macaquen") ## works like an append
print(fruits)

fruits.remove("banana")
print(fruits)

remove_fruit = fruits.pop(2)
print(fruits)
print(remove_fruit)

fruits.sort()
print(fruits)

fruits.reverse()
print(fruits)


numbers = [1,2,3,4,5]
squares = [ x ** 2 for x in numbers if x % 2 == 0]; print(squares)

point = (3, 4)
print(point[0])
print(point[1])

my_tuple = (2,3,4,4,2,2)
print(my_tuple.index(2, 4))

print(len(my_tuple))

print(my_tuple.count(2))

## DICTIONARIES
person = {"Eric":19, "Irene":17, "Adrià":19}

print(person["Eric"])
print(person["Irene"])

print(person.keys())
print(person.values())
print(person.items())

profession = {"profession" : "Engineer"}
person.update(profession)
print(person)

## SETS
set1 = {1,2,3}
set2 = {3,4,1}

union = set1 | set2
print(union)

intersection = set1 & set2
print(intersection)

difference = set1 - set2
print(difference)       # Values of set1 not found in set2

symmetric_difference = set1 ^ set2
print(symmetric_difference)     # Values that are unique to both sets

fruits = {"Banana", "Apple", "Orange"}
vegetables = set(["cabbages", "broccoli", "carrot"])

fruits.add("pear")
print(fruits)

fruits.add("pear") # THIS SECOND TIME, pear "IS NOT ADDED". THERE ARE NOT 2 PEARS
print(fruits)

fruits.add("Pear") # THIS THIRD TIME, Pear "IS ADDED". CASE SENSITIVE!!!
print(fruits)

fruits.remove("Banana") # CASE SENSITIVE
print(fruits)

fruits.discard("Banana") # Same as remove, but does not raise exceptions

fruits.clear()
print(fruits)
#
# Lists are useful for ordered and MUTABLE collections

# tuples for ordered and IMMUTABLE collections

# dictionaries for storing KEY-VALUE PAIRS 

# sets for unordered collections of UNIQUE elements.
# 

number = 7
if number % 2 == 0:
    number = "Even"
else: 
    number = "Odd"

## FUNCTIONS
def greetings(name):
    print("Hello, " + name)

greetings("World")

def sum(a, b):
    return a + b

result = sum(1, 2)
print(result)

text = sum("Hello", " World")
print(text)

square = lambda x: x**2
print(square(5))

substract = lambda  : 3-1 # Lambda func. do not need an x always
print(substract())

def rectangle_area(base, height):
    """
    Calculates the area of the rectangle

    Arguments:
        float base : the base of the rectangle
        float height : the height of the rectangle
    
    Returns: 
        float : the area of the rectangle
    """
    return base * height

def variable_sum (*numbers):
    """
    Python allow us to define functions that accept a variable number of arguments

    """
    total = 0
    for n in numbers:
        total += n
    return total

print(variable_sum(1,2))
print(variable_sum(1,2,3,4,5,5))

# EXCEPTIONS 
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Error; Division by zero")
except ValueError:
    print("Invalid value")
finally:
    print("Im in the end")

condition = True

def function():
    if condition:
        raise Exception("Error description")

try:
    function()
except Exception as e:
    print(f"Error: {str(e)}")


"""

#INPUT AND OUTPUTS
name = input("Introduce your name: ")
age = input("Introduce your age: ")

age = int(age) # DATA CONVERSION. IMPORTANT

print("Hello, " + name)
if age < 18:
    print("You are still a kid")
elif age == 18:
    print("Congrats, you are now an adult")
else:
    print("You are quite old")

print("This string, " + name)
print(f" is the same as this string, {name}")

"""

# READING FILES

with open("Data.txt", "r") as file:
        content = file.read()
        print(content)

try: 
    file = open("data.txt", "w")
    file.write("Hello, world")
    file.close()
except Exception as e:
    print(f"Error: {str(e)}")

try:
    file = open("data.txt", "r")
    content = file.read()
    print(content)
    file.close()

except Exception as e:
    print(f"Error: {str(e)}")

with open("data.txt", "r") as file:
        content = file.read()
        print(content)



##IMPORTS
import math ## PUEDES PONER EL IMPORT EN CUALQUIER PARTE DEL CODIGO. caos
from random import random
import datetime

random_number = random()
print(random_number)
print(datetime.datetime.now())

##CUSTOMIZED IMPORTS
import CustomModules
CustomModules.greet("Juan")
print(CustomModules.calculate(1,1))

import utilities
name = utilities.get_user_name()
print(name)
