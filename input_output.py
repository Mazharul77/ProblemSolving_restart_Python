'''

 Problem: ..............................Basic Input Output Operations:..................................
 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

def int_input():
    try:
        a = int(input("Now enter your choice corresponding input : "))
        return a
    except ValueError:
        print("Please Enter Valid integer Input only")


def flt_input():
    try:
        b = float(input("Now enter your choice corresponding input : "))
        return b
    except ValueError:
        print("Please Enter Valid integer Float type only")


def str_input():
    try:
        c = input("Now enter your choice corresponding input : ")
        return c

    except ValueError:
        print("Please Enter Valid integer String type only")


def default():
    return "Please Enter Valid Input"


switcher = {

        1: int_input,
        2: flt_input,
        3: str_input
    }


def take_give(choose):

    return switcher.get(choose, default)()


if __name__ == "__main__":
    print("enter 1 for integer input")
    print("enter 2 for double/float datatype input")
    print("enter 3 for string input")

    choose = int(input("Choose your option to take any type of input:"))
    print(take_give(choose))


'''
Input 1 :
1
12123
Outpput: 12123

Input 2 :
2
12123
Outpput: 12123.0

Input 3 :
3
hello world
Outpput: hello world
 
'''

