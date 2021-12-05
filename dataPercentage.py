'''

 Problem:
...... Write a python program
        to enter marks of five subjects
         and calculate total,
          average = total/5 and
           percentage = (obtained_mark/total_5subj_full_marks)*100
.......
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''


print("\n..........Enter all Marks/numbers to calculate Average & Percentage of the marks/numbers................")
obtained_marks = 0
print("How many numbers you want to Enter?:")
size = int(input())
totalMarks = (size*100)
print("Now Enter the %d numbers: " % size)

for numbers in range(size):
    marks = float(input())
    obtained_marks += marks

average = obtained_marks/size
percentage = (obtained_marks/totalMarks)*100

print("Total Obtained Marks: %.2f\n" % obtained_marks)
print("The Average of the Obtained Marks: %.2f\n" % average)
print("The Percentage of the Obtained Marks of Total: %.2f%% \n" % percentage)
