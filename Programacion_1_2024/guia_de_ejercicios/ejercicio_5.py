'''Una agencia de viajes debe sacar las tarifas de los viajes , se cobra $15.000
por cada estadía como base, se pide el ingreso de una estación del
año(Invierno/Verano/Otoño/Primavera) y localidad(Bariloche/Cataratas/Mar del
Plata/Córdoba) para vacacionar para poder calcular el precio final:
-en Invierno: Bariloche tiene un aumento del 20% Cataratas y Córdoba tiene un
descuento del 10% Mar del Plata tiene un descuento del 20%
-en Verano: Bariloche tiene un descuento del 20% Cataratas y Córdoba tiene
un aumento del 10% Mar del Plata tiene un aumento del 20%
-en Otoño y Primavera: Bariloche tiene un aumento del 10% Cataratas tiene un
aumento del 10% Mar del Plata tiene un aumento del 10% y Córdoba tiene el
precio sin descuento.
Validar el ingreso de datos'''

precio_base = 15000
precio_final = 0

estacion = input("Ingrese una estacion del año 'Invierno/Verano/Otoño/Primavera': ")
while estacion != "Invierno" and estacion != "Verano" and estacion != "Otoño" and estacion != "Primavera":
    print("Error, ingrese de nuevo la estación")
    estacion = input("Ingrese una estacion del año 'Invierno/Verano/Otoño/Primavera': ")

localidad = input("Ingrese una localidad 'Bariloche/Cataratas/Mar del Plata/Córdoba': ")
while localidad != "Bariloche" and localidad != "Cataratas" and localidad != "Mar del Plata" and localidad != "Córdoba":
    print("Error, ingrese de nuevo la localidad")
    localidad = input("Ingrese una localidad 'Bariloche/Cataratas/Mar del Plata/Córdoba': ")


match estacion:
    case "Invierno":
        match localidad:
            case "Bariloche":
                precio_final = precio_base * 1.20 #aumento del 20%
            case "Cataratas" | "Córdoba":
                precio_final = precio_base * 0.90 #descuento del 10%
            case "Mar del Plata":
                precio_final = precio_base * 0.80

    case "Verano":
        match localidad:
            case "Bariloche":
                precio_final = precio_base * 0.80
            case "Cataratas" | "Córdoba":
                precio_final = precio_base * 1.10
            case "Mar del Plata":
                precio_final = precio_base * 1.20
    
    case "Otoño" | "Primavera":
        match localidad:
            case "Bariloche" | "Cataratas" | "Mar del Plata":
                precio_final = precio_base * 1.10
            case _:
                precio_final = precio_base

print(f"El precio final de {localidad} en la temporada de {estacion} es de: {precio_final}")

