from random import randint
import math

def isRightAngle(a, b, c):
         if (str(a).isdigit() == False) | (str(b).isdigit() == False) | (str(c).isdigit() == False):
             return "Podano bledne wartosci"
         else:
             a = float(a)
             b = float(b)
             c = float(c)
             if (a<=0)|(b<=0)|(c<=0):
                 return "Podano bledne wartosci"
             elif (a > b) & (a > c):
                 check = b**2 + c**2
                 if a**2 == check:
                     return "Trojkat jest prostokatny"
                 else:
                     return "Trojkat nie jest prostokatny"
             elif (b > a) & (b > c):
                 check = a**2 + c**2
                 if b**2 == check:
                     return "Trojkat jest prostokatny"
                 else:
                     return "Trojkat nie jest prostokatny"
             else :
                 check = b ** 2 + a ** 2
                 if c ** 2 == check:
                     return "Trojkat jest prostokatny"
                 else:
                     return "Trojkat nie jest prostokatny"



a = input("Podaj dlugosc pierwszego boku trojkata: \n")
b = input("Podaj dlugosc drugiego boku trojkata: \n")
c = input("Podaj dlugosc trzeciego boku trojkata\n")
print(isRightAngle(a, b, c))