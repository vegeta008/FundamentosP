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
