'''

 Problem:
  ..............................Write a python program to enter
                                length in centimeter
                                and convert it into meter = c/100 and kilometer = c/100000 or m/1000.
   ..................................

 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

length = float(input("Enter the length in centimeter to convert it into meter and Kilometer:"))
meter = length/100
kilometer = meter/1000
print("The converted %.2f centimeter is: %.2f meter" % (length, meter))
print("The converted %.2f centimeter is: %.2f kilometer" % (length, kilometer))
