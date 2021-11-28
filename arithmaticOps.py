'''

 Problem: ..............................Basic Arithmatic Operations:..................................
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''


def addition(n1, n2):
    try:
        ans = n1 + n2
        return "The summation of %f and %f = %f" % (n1, n2, ans)
    except ValueError:
        print("Please Enter Valid Input only")


def subtraction(n1, n2):
    try:
        ans = n1 - n2
        return "The subtractio of %f - %f = %f" % (n1, n2, ans)
    except ValueError:
        print("Please Enter Valid Input only")


def multiplication(n1, n2):
    try:
        ans = n1 * n2
        return "The multiplication of %f and %f = %f" % (n1, n2, ans)
    except ValueError:
        print("Please Enter Valid Input only")


def division(n1, n2):
    try:
        ans = n1 / n2
        return "The divisio:  %f / %f = %f" % (n1, n2, ans)
    except ValueError:
        print("Please Enter Valid Input only")


def modulas_(n1, n2):
    try:
        ans = n1 % n2
        return "The modulas_:  %f and %f = %f" % (n1, n2, ans)
    except ValueError:
        print("Please Enter Valid Input only")


def default():
    return "Please Enter Valid Input"


switcher = {

        1: addition,
        2: subtraction,
        3: multiplication,
        4: division,
        5: modulas_
    }


def take_give(choose, n1, n2):

    return switcher.get(choose, default)(n1, n2)


if __name__ == "__main__":
    print("enter 1 for Addition(+):")
    print("enter 2 for Subtraction(-):")
    print("enter 3 for Multiplication(*):")
    print("enter 4 for Division(/):")
    print("enter 5 for Remainder/Modulas(%):")

    try:
        choose = int(input("Choose your option to take any type of input:"))
        n1 = float(input("\n Enter the 1st Number:"))
        n2 = float(input(" Enter the 2nd Number:"))

    except NameError:
        print("\nPlease Enter Input Correctly:")

    except ValueError:
        print("\nPlease Enter Input Correctly:")


    print(take_give(choose, n1, n2))
