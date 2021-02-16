#   8.Calcular la fuerza que se debe aplicar a un cuerpo para moverlo en una mesa horizontal,  
#   sabiendo que tiene una masa m (kg) y un coeficiente de rozamiento estático  Us.




PesoNewton = int(input("Peso del artculo" ))
rosamientoestatico = float(input("rosamieno estatico de :"))
fuerzahorizontal = int(input("cual es la fuerza horizonotal :"))

masa = PesoNewton
grabedad = 10
peso = masa * grabedad
fuerzaderozamiento = rosamientoestatico * peso 

if fuerzaderozamiento >= fuerzahorizontal:
    print("el peso es de  :", peso , "en newton del articulo")
    print("la fuerza de rozamiento estatico para la fuerza aplicada es de  :", fuerzaderozamiento ,)
    print("felicidades con  :", fuerzahorizontal , "newton vas a poder mover")
    
else:
    print("Lo siento no lo puedes mover XD")
