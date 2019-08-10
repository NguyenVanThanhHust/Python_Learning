# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#this is to learn python intermediate series
#class 1
#create a class
#introduce to class
#class is just a hand packets with data and method (function)
class MyClass:
#    first and second attribute
    number = 0
    name = "no_name"

def Main():
#    new variables
    me = MyClass()
    me.name = "draps"
    me.number =1234
    
    friend = MyClass()
    friend.number = 3
    friend.name = "Steve"
    
    print("name " + me.name + " " + str(me.number) )
    
if __name__ == '__main__':
    Main()