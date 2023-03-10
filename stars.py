import math
import decimal

def print_rating(star,a,b,c):
    if (star == 0):
        print(c, c, c, c, c)
    elif (star == 0.5):
        print(a, c, c, c, c)
    elif(star == 1):
        print(b, c,c,c,c)
    elif (star == 1.5):
        print(b, a, c, c, c)
    elif(star == 2):
        print(b,b,c,c,c)
    elif (star == 2.5):
        print(b, b, a, c, c)
    elif(star == 3):
        print(b,b,b,c,c)
    elif (star == 3.5):
        print(b, b, b, a, c)
    elif(star == 4):
        print(b,b,b,b,c)
    elif (star == 4.5):
        print(b, b, b, b, a)
    elif(star == 5):
        print(b,b,b,b,b)
    else:
        print("not a valid number for rating")
    


if __name__ == '__main__':
    a = "half"
    b = "full"
    c = "empty"
    num= input()
    num = float(num)
    if (num != 1.5 and num != 2.5 and num != 3.5 and num != 4.5 and num != 0.5):
        star = round(num)
        print_rating(star,a,b,c)
    else:
        print_rating(num,a,b,c)