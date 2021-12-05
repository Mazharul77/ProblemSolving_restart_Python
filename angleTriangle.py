'''

 Problem:
...... Write a python program to enter two angles of a triangle and find the third angle ..........
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

tri_angle1 = float(input("Enter 1st angle of the Triangle:"))
tri_angle2 = float(input("Enter 2nd angle of the Triangle:"))

tri_angle3 = (180-(tri_angle1 + tri_angle2))
print("The third angle of the Triangle: %.2f" % tri_angle3)
