'''

 Problem:
 #.......Simple Interest:

 P = Principal amount
 N or T = Term of loan, in years?
 R = Annual interest rate

 Write a python program to enter P, T, R and calculate Simple Interest = P*N*R
'''

print("........Simple Interest Calculation:..........")

P = float(input("Enter The Principle AMount Of The Loan: "))
N = float(input("Enter Term of loan, in years: "))
N= N/100
R = float(input("Enter Annual interest rate: "))

simpleInterest = P*N*R
print("\n\t Calculated Simple Interest Is:%.2f\n" % simpleInterest)
