# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 16:48:32 2018

@author: admin
"""
#inheritance, from subclass to call to base class

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def talk(self):
        raise NotImplementedError("Subclass must implement method")
        
        
class Cat(Pet):
    def __init__(self, name, age):
#        this is to call base class Pet, the pass the name and age to this class
        super().__init__(name, age)
    
    def talk(self):
        return "Meoww"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def talk(self):
        return "wooff"
        
        
def Main():
# =============================================================================
#     thePet = Pet("cat", 1)
#     milk = Cat("milk", 3)
#     print(str(isinstance(milk, Cat)))
#     print(str(isinstance(milk, Pet)))
#     print(str(isinstance(thePet, Cat)))
#     print(str(isinstance(thePet, Pet)))
#     
#     print(milk.name)
# =============================================================================
    pets =[Cat("milk", 3), Dog("jack", 2), Cat("cafe", 3), Pet("thePet", 3)]
    for pet in pets:
        print("Name: " + pet.name + ",age: " + str(pet.age) + ", say: " + pet.talk())
if __name__ == '__main__':
    Main()