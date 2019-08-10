# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 15:16:58 2018

@author: admin
"""
#method in class (function in class)

import math
class Vector2D:   
#    method
    def __init__(self, x,y):
#        x and y will be pass in self.x and self.y
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    
    def __imul__(self, other):
        self.x *=  other.x
        self.y *=  other.y
        return self
    
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    
    def __floordiv__(self, other):
        return Vector2D(self.x // other.x, self.y // other.y)
    
    def getLength(self):
        return math.sqrt(self.x**2 +self.y**2)
    
    def normalizae(self):
        length = self.getLength()
        if length != 0:
            return Vector2D(self.x / length, self.y / length)
        else:
            return Vector2D(self)

    def getAngle(self):
        return math.degrees(math.atan2(self.y, self.x))
    
    def __str__(self):
        return "X: " + str(self.x ) + ",Y: " + str(self.y)

def Main():
    vec = Vector2D(2, 4)
    vec2 = Vector2D(3, 3)
#    print("X: "+str(vec.x) + ",Y: " + str(vec.y))
    print(vec)
    print(vec2)
    
    vec = vec + vec2
    print(vec)
    
    vec += vec2
    print(vec)
    
    print(vec.normalizae())
    print(vec.getAngle())
    
if __name__ =='__main__':
    Main()
    
    