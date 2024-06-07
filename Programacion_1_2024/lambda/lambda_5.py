#print((lambda num: "descuento #correcto" if num * 0.90 == 90 else "no hay descuento")(100))

'''def descuento_del_10(num:int)->int:
resultado = num * 0.90
return resultado
#print(descuento_del_10(100))'''

print((lambda num: (num * 0.90) if num != 0 else "no se le puede sacar un porcentaje")(100))