#print((lambda num: "sueldo correcto" if num * 1.1 == 110 else "sueldo incorrecto")(100))

'''def incre_10_porciento(num:int)->int:
resultado = num * 1.1
return resultado
print(incre_10_porciento(100))'''

print((lambda num: (num * 1.1) if num > 0 else "error")(100)) 
