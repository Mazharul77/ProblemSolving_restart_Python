'''

 Problem: ..............................Write a python program to enter radius of a circle
                                        and find its diameter (baas) = 2*r,
                                         circumference (poridhi) = 2*math.pi*r
                                          and area = math.pi*r*r..................................
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

#from math import pi      or
import math

radius = float(input("Enter The Radius of the Circle:"))
diameter = 2*radius
circumference = 2*math.pi*radius
area = math.pi*radius*radius

print("The circle's diameter is: %.2f unit, circumference is: %.2f unit ,area is: %.2f sq. Unit " % (diameter, circumference, area))


