#! /usr/bin/python
#  ECE 2524 Homework 5 Problem 1 Ben Kaija

f = open('/etc/passwd')
lines = f.readlines()
for x in lines:
	y = x.split(':')
	print y[2]+'\t'+y[0] 
