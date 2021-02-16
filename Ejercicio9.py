#   9.Leer la temperatura en grados Celsius y convertirla a grados Kelvin y a grados Farenheit

grados = int(input('Ingrese la temperatura en grados Celsius: '))
Kelvin = 273 + grados
fahrenheit = 9.0/5.0 * grados +32
print("grados kelvin  :", Kelvin )
print("Grados Fahrenheit  :", fahrenheit )
