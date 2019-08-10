# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 17:50:09 2018

@author: admin
"""

# =============================================================================
# class Reverse:
#     
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     
#     def __iter__(self):
#         return self
#     
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index -1
#         return self.data[self.index]
#     
# def Main():
#     rev = Reverse('some_string')
#     for char in rev:
#         print(char)
#         
# if __name__ == '__main__':
#     Main()
# 
# =============================================================================


def Reverse(data):
    for index in range(len(data) - 1, -1, -1 ):
        yield data[index]

def Main():
    rev = Reverse('sting')
    for char in rev:
        print(char)
    data = 'string'
    print(list(data[i] for i in range (len(data) -1, -1, -1)))

if __name__ == '__main__':
    Main()
        
