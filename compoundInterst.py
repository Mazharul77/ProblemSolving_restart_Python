'''

 Problem:
 #.......Compound Interest = P×(1+R)^N-P
where:
P = Principal amount
N or T = Number of years interest is applied?
R = Annual interest rate

Write a python program to enter P, T, R and calculate Compound Interest = P(1+R)^N-P.

'''

from math import pow
print("........Simple Interest Calculation:..........")

P = float(input("Enter The Principle AMount Of The Loan: "))
N = float(input("Enter Term of loan, in years: "))
R = float(input("Enter Annual interest rate: "))
R = R/100

compound_Interest = P*pow((1+R), N) - P
print("\n\t Calculated Compound Interest Is: %.2f\n" % compound_Interest)

