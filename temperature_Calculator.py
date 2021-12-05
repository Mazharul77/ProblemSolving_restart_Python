'''

 Problem:
  .............................Write a python program to enter temperature in Celsius and convert it into Fahrenheit = (c*1.8)+32.
   ..................................

 Name: Mazharul Islam Bhuiyan
 Email:mazharul15-1425@diu.edu.bd

'''

def celcToFarenh(celcius):
    farenh = (celcius*1.8) + 32
    return farenh


def FarenhTocelc(farenheit):
    cel = (farenheit-32)/1.8
    return cel


if __name__ == "__main__":
    print("Press 1. To Convert Celcius to Farenheit: \nPress 2. To Convert Farenheit to Celcius:")
    press = int(input("Enter Your Choice:"))
    if press == 1:
        celcius = float(input("Enter Temperature in Celcius:"))
        print(celcToFarenh(celcius))

    else:
        farenheit = float(input("Enter Temperature in farenheit:"))
        print(FarenhTocelc(farenheit))
