# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 18:40:10 2018

@author: admin
"""

# =============================================================================
# This is to learn how to use template 
# =============================================================================
# =============================================================================
# from string import Template
# def Main():
#     cart = []
#     cart.append(dict(item = "Coke", price = 8 , qty = 2))
#     cart.append(dict(item = "Cake", price = 12, qty = 1))
#     cart.append(dict(item = "Fist", price = 32, qty = 4))
#     
#     t = Template("$qty x $item = $price ")
#     total = 0
#     print("Cart :")
#     for data in cart :
#         print(t.substitute(data))
#         total += data["price"]
#         
#     print("Total: " + str(total ))
#     
# if __name__ == '__main__':
#     Main()
# =============================================================================

# =============================================================================
# to learn how to create class of template
# =============================================================================

from string import Template

class MyTemplate(Template):
    delimiter = '#'

def Main():
    cart = []
    cart.append(dict(item = "Coke", price = 8 , qty = 2))
    cart.append(dict(item = "Cake", price = 12, qty = 1))
    cart.append(dict(item = "Fist", price = 32, qty = 4))  

    t = MyTemplate("#qty x #item = #price ")
    total = 0
    print("Cart :")
    for data in cart :
        print(t.substitute(data))
        total += data["price"]
         
    print("Total: " + str(total ))
   
if __name__ == '__main__':
    Main()