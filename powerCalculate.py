'''

 Problem:
  .............................Write a python program to find power of any number x ^ y = math.pow(x,y)................................
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

from math import pow
# num__ = float(input("\nEnter any Number:"))
# power__ = float(input("Enter power of the Number:"))
#
# calculatedPower_number = pow(num__, power__)
# print(calculatedPower_number)

#or
print("........Finding power any number:........")

num = float(input("Enter any Number:"))
power = float(input("Enter power of the Number:"))

calculatedPower = num**power
print("The Calculated Power: %.2f" % calculatedPower)




