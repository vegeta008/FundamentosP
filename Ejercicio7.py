# -*- coding: utf-8 -*-
"""
@author: aorozco@dragonjar.org
"""

"NUMEROS"
def suma(x, y):
    return x + y
     
def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division (x, y):
    return x / y

print("CALCULADORA：")
print("1.SUMA")
print("2.RESTA")
print("3.MULTIPLICACION")
print("4.DIVICION")

choice = input("ELIJA LA OPCION (1/2/3/4):")

num1 = int(input("NUMERO: "))
num2 = int(input("NUMERO: "))

if choice == '1':
   print(num1,"+",num2,"=", suma(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", resta(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiplicacion(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", division(num1,num2))
else:
   print("ERROR")