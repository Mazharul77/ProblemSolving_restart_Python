'''

 Problem:
...... Write a python program to enter any number and calculate its square root = math.sqrt(n) .........
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''
from math import sqrt
num = float(input("Enter any real Number to Calculate Square Root:"))
Root_num = sqrt(num)
print("The Square Root of the %.2f : %.2f" % (num, Root_num))
