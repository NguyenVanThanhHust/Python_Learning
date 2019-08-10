# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 19:00:29 2018

@author: admin
"""
# =============================================================================
# 
# to learn how to use argparse
# argument parsing for python program 
# =============================================================================
# This function is to take a number and return its finbonatci

import argparse

def fib(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a

def Main():
	parser = argparse.ArgumentParser()

	group = parser.add_mutually_exclusive_group()
	group.add_argument("-v", "--verbose", action = "store_true")
	group.add_argument("-q", "--quite", action = "store_true")
	parser.add_argument("num", help = "The finbonatci number you you wish to calculate", type = int)
	# -o for shortcut of --output
	parser.add_argument("-o", "--output", help = "Output result to a file ", \
		action = "store_true")
	args = parser.parse_args()

	result = fib(args.num)
	print("The " + str(args.num)+"th fib number is " + str(result))

	# if args.output:
	# 	f = open("finbonatci.txt", "a")
	# 	f.write(str(result) + '\n')

	if args.verbose:
		print("The " + str(args.num) + "th fib number is " + str(result))
	elif args.quite:
		print(result)
	else:
		print("Fib " + str(result))

if __name__ == '__main__':
	Main()

# how to use
# open command in folder containing this file 
# command : python Advanced_Lecture2_argparge.py -h
# above cmd is to show option
# below cmd is to show calculate
# command : python Advanced_Lecture2_argparge.py 10
