# -*- coding: utf-8 -*-
"""
@author: aorozco@dragonjar.org
"""

var_empleados = int(input("numero de empleados" ))
var_horas = int(input("tiempo de entrega:"))


var_adicionarempleados = var_empleados*var_horas
var_masempleados = var_adicionarempleados-var_empleados

if var_masempleados >=1:
    print("Se necesitan :", var_masempleados , "Personas para realizar la actividad en una hora")
    
else:
    print("No es necesario mas empleados")