# Datatypes in python

# standard datatypes: integers, floating, string, boolean
# advanced datatypes: lists, tuples, dictionaries, sets

# Variable naming conventions
# camelCase
# snake_case
# pascalcase
# 
# Shouldn't start with a number
# Shouldn't have spaces between words
# Can start with _ but not with any other character such as "-:{}"etc 
# Choose a meaningful name for your varaible (recommended) 

# Comments in python
# Single line comments
# Inline comments
# Block comments

# This is my integer : Single line comment
my_int = 10 # Value 10 is stored in my_int container : Inline comment
print(my_int)

# Block comments
'''
Comments in python
Single line comments
Inline comments
Block comments
'''

"""
Comments in python
Single line comments
Inline comments
Block comments
"""
#print(my_Bool)
my_float = 10.1234
my_bool = True # False
print(my_bool)

my_str = "sample's string"
print(my_str)

my_sample_str = 'sample\'s string'
print(my_sample_str)

my_sentence = """
Comments in python
Single line comments
Inline comments
Block comments
"""
print(my_sentence)

# bool my_bool = True (Not needed in python)
# During runtime, python decides the datatype of the variable and allocates the necessary memory

# Python is case sensitive
# E.g. my_int and My_int are 2 different variables
# False and false are 2 different things in python

# Operators
# +, -, *, /

first_num = 10
second_num = 20

add = first_num + second_num
sub = first_num - second_num
multi = first_num * second_num
div = first_num / second_num # Returns a floating point as a result

print(add, sub, multi, div, sep="\n", end="***")
print(add, sub, multi, div)

# Division
print(type(div))

# // -> integer division
quotient = second_num // first_num
print(quotient, type(quotient))

# % -> modulo operator
reminder = second_num % first_num
print(reminder, type(reminder))