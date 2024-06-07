def menu():
    print('''            
            1-Listar los alumnos por orden ascendente de apellido, si se repite, ordenar por nombre. Mostrar legajo, nombre, apellido y edad
            2-Obtener el promedio de notas para cada estudiante
            3-Listar legajo, nombre, apellido y edad de los estudiantes que cursan el programa de “Ingenieria en Informatica”
            4-Listar los datos del/los usuario/s más joven/es
            5-Informar el alumno con mayor pomedio de notas. Mostrar nombre y apellido
            6-Listar nombre y apellido de los alumnos que forman el grupo “Club de Informática” con sus respectivos promedios
            7-Listar legajo, nombre, apellido y programas que cursan los alumnos más jóvenes
            8-Salir.''')
    opcion = int(input("opcion: "))
    return opcion

def listar_alumnos_ascendente(estudiantes:list):
    #ordeno por apellido y si son el mismo ordeno por el nombre de forma ascendente
    for i in range(len(estudiantes)-1):
        for j in range(i+1, len(estudiantes)):
            if estudiantes[i]["apellido"] > estudiantes[j]["apellido"] or(estudiantes[i]["apellido"] == estudiantes[j]["apellido"] and estudiantes[i]["nombre"] > estudiantes[j]["nombre"]):
            
                auxiliar_apellido = estudiantes[i]
                estudiantes[i]= estudiantes[j]
                estudiantes[j] = auxiliar_apellido
            

    for estudiante in estudiantes:
        print(f"Legajo: {estudiante['legajo']} \tNombre: {estudiante['nombre']} \tApellido: {estudiante['apellido']} \tEdad: {estudiante['edad']}")


def promediar_notas(estudiantes:list)-> float:
    #obtener el promedio de las notas
    acumulador_notas = 0 
    contador_notas = 0
    for e_estudiantes in estudiantes:
        for nota in e_estudiantes["notas"]:
            acumulador_notas += nota
            contador_notas += 1 
    
    promedio = acumulador_notas / contador_notas
    return promedio

def listar_estudiantes_inge_informatica(estudiantes: list):
    for e_estudiante in estudiantes:
        if e_estudiante["programa"]["nombre"] == "Ingenieria en Informatica":
            print(f"Legajo: {e_estudiante['legajo']} \tNombre: {e_estudiante['nombre']} \tApellido: {e_estudiante['apellido']} \tEdad: {e_estudiante['edad']}")   

def listar_edad_joven(estudiantes:list):
    for i in range(len(estudiantes)-1):
        for j in range(i+1,len(estudiantes)):
            if estudiantes[i]["edad"] > estudiantes[j]["edad"]:
                aux_edad = estudiantes[i]
                estudiantes[i] = estudiantes[j]
                estudiantes[j] = aux_edad
                
    for estudiante in estudiantes:
        print(f"Edad: {estudiante['edad']}")  

def listar_edad_joven(estudiantes:list):
    edad_minima = estudiantes[0]['edad']
    
    
    for estudiante in estudiantes:
        if estudiante['edad'] < edad_minima:
            edad_minima = estudiante['edad']
            
    
    estudiantes_jovenes = []
    for estudiante in estudiantes:
        if estudiante['edad'] == edad_minima:
            estudiantes_jovenes.append(estudiante)
            
   
    for estudiante in estudiantes_jovenes:
        print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Edad: {estudiante['edad']}")


def mayor_promedio_notas(estudiantes:list):
    
    promedio_mayor = 0
    mejor_estudiante = None
       
    for e_estudiante in estudiantes:
        contador = 0
        acumulador = 0
        for e_nota in e_estudiante['notas']:         
            acumulador += e_nota
            contador += 1
            
        promedio = acumulador / contador
        
        if promedio > promedio_mayor:
            promedio_mayor = promedio
            mejor_estudiante = e_estudiante
    print(f"El estudiante con mayor promedio es {mejor_estudiante['nombre']} {mejor_estudiante['apellido']} con un promedio de {promedio_mayor:.2f}")

def listar_por_grupo_con_promedio(estudiantes:list):
  
    for e_estudiantes in estudiantes:
        if "grupos" in e_estudiantes:
            for grupo in e_estudiantes["grupos"]:
                if grupo["nombre"] == "Club de Informatica":
                    contador = 0
                    acumulador = 0
                    for e_nota in e_estudiantes['notas']:
                        acumulador += e_nota
                        contador += 1
                        
                    promedio = acumulador / contador
                                       
                    print(f"Nombre: {e_estudiantes['nombre']} \tapellido: {e_estudiantes['apellido']} \tpromedio: {promedio}")

def listar_edad_joven_con_programa(estudiantes:list):
    edad_minima = estudiantes[0]['edad']
    
    
    for estudiante in estudiantes:
        if estudiante['edad'] < edad_minima:
            edad_minima = estudiante['edad']
            
    
    estudiantes_jovenes = []
    for estudiante in estudiantes:
        if estudiante['edad'] == edad_minima:
            estudiantes_jovenes.append(estudiante)
            
   
    for estudiante in estudiantes_jovenes:
        print(f"Legajo: {estudiante['legajo']}, Nombre: {estudiante['nombre']}, Apellido: {estudiante['apellido']}, Programa: {estudiante['programa']}")
