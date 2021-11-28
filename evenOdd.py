digit =  int(input("How many numbers want to take?:"))
print("Now Enter the numbers: ")
for i in range(digit):
    n = int(input())

    if n%2 == 0:
        print(n, " is even number.")

    else:
        print(n, "is an odd number")
