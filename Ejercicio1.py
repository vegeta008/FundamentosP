#1.Calcular el valor a pagar de una compra realizada, cuyo monto neto es ingresado por el usuario. Considere que el valor del IVA 
#(Impuesto al Valor Agregado- puede variar en cada país), y un descuento del 5% para todas las compras.
# -*- coding: utf-8 -*-
"""
@author: aorozco@dragonjar.org
"""


Valor_Compra = int(input("Ingrese Valor:"))

descuento = Valor_Compra * 0.05 
IVA = Valor_Compra * 0.19

print ("Valor Total Con IVA: ", Valor_Compra + IVA)
print ("Descuento: ", descuento )
print ("Valor a Pagar :", Valor_Compra - descuento + IVA)
