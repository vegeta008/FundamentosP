# -*- coding: utf-8 -*-
"""

@author: aorozco@dragonjar.org
"""

var_ingresarestatura = int(input("tu estatura :"))
var_ingresarpeso = int(input("Cual es tu peso :"))

masa_corporal = var_ingresarpeso / var_ingresarestatura**2

print("Tu masa corporal es de :", masa_corporal )