#!/usr/bin/python3
"""
built-in or user-defined class, is an instance of the 'type' metaclass.
so every class is of the class or data type "type".
"""
class myClass:
    pass

# in tthe reload() method in file_storage, I used the ouput from this to know
# what should be accepted from eval() after it evaluates the name str as an expression

print(type(myClass)) # prints <class type>  -> means tthat it's of type data-type or class

print(type(5))  # prints <class 'int'>  -> means that it's of int data-type or class