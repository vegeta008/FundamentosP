#   4.Realice un programa que obtenga la calificación que debe obtenerse en un 
#   examen supletorio, si se conoce que el promedio incluido el supletorio para aprobar debe 
#   ser mínimo de 3.5 . El usuario debe ingresar las calificaciones en números enteros del primer y segundo bimestre.

# -*- coding: utf-8 -*-
"""4

@author: aorozco@dragonjar.org
"""

var_primersemestre = int(input("  calificaciones del primer semestre :"))
var_segundosemestre = int(input("  calificaciones del segundo semestre :"))

promedio = (var_primersemestre + var_segundosemestre)/2

if promedio <= 3.5:
    print("Debes repetir el semestre")
else:
    print("Felicidades, Haz aprobado el semestre")
