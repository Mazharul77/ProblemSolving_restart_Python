'''

 Problem:
  .............................Write a python program to convert days into years = d/365, weeks = d/7 and days = d%d_m.
   ..................................

 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''
days = int(input("Enter Days to convert in Years, Weeks, Days:"))
year = days // 365
rem_years = days % 365

weeks = rem_years//7
final_rem_days = rem_years % 7

print("The Days Converted into %d Years, %d Weeks, %d days: " % (year, weeks, final_rem_days))


