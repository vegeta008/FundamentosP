

a = int(input("Ingrese un primer valor a: "))
b = int(input("Ingrese un segundo valor b: "))
c = int(input("Ingrese un tercer valor c: "))

valor_1 = (-b + (b*b - 4*a*c) ** (1/2)) / (2*a)
valor_2 = (-b - (b*b - 4*a*c) ** (1/2)) / (2*a)


print("El primer valor es: ", valor_1)
print("El segundo valor es: ", valor_2)