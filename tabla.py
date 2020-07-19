dic = {'generar_archivo': {'Nombre': 'generar_archivo.archivos.py', 'Parametros': 'lista ruta',
                           'Lineas': 6, 'Invocaciones': 0, 'return': 0, 'if': 1, 'elif':3, 'for': 0, 'while': 0, 'break': 0, 'exit': 0,
                           'Coment': 0, 'Ayuda': 'Si', 'Autor': 'Nicolas'}, 'grabar_archivo': {'Nombre': 'grabar_archivo.archivos.py',
                                                                                      'Parametros': 'archivo leyenda', 'Lineas': 2, 'Invocaciones': 0, 'return': 0, 'if': 0, 'elif': 0, 'for': 0, 'while': 0, 'break': 0, 'exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}, 'leer_linea': {'Nombre': 'leer_linea.archivos.py', 'Parametros': 'archivo', 'Lineas': 7, 'Invocaciones': 0, 'return': 0, 'if': 0, 'elif': 0, 'for': 0, 'while': 0, 'break': 0, 'exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}, 'leer_linea_string': {'Nombre': 'leer_linea_string.archivos.py', 'Parametros': 'archivo', 'Lineas': 2, 'Invocaciones': 0, 'return': 0, 'if': 0, 'elif':0, 'for': 0, 'while': 0, 'break': 0, 'exit': 0, 'Coment': 0, 'Ayuda': '', 'Autor': ''}}

################################################################################################################################################
def imprimir_panel(dic):
    """[Autor: Lucia]"""
    """[Ayuda: Crea la una tabla]"""
    Tabla = """\
+-----------------------------------------------------------------------------------------------------------------------------------------------+
|        FUNCION                Parametros   Líneas   Invocaciones   Returns   If/elif    for   while   Break   Exit   Coment  Ayuda    Autor   |
------------------------------------------------------------------------------------------------------------------------------------------------|
{}
+-----------------------------------------------------------------------------------------------------------------------------------------------+\
"""
    Tabla = (Tabla.format('\n'.join('|{0:30}\t{1:5}\t{2:8}\t{3:5}\t{4:9}\t{5:4}\t{6:4}\t{7:3}\t{8:3}\t{9:3}\t{10:3}\t{11:1}\t{12:8}|'.format(dic[funcion]["Nombre"], dic[funcion]["Parametros"].count(" "), dic[funcion]["Lineas"],
                                            dic[funcion]["Invocaciones"], dic[funcion]["return"],
                                                                                 dic[funcion]["if"] + dic[funcion]["elif"], dic[funcion]["for"], dic[funcion]["while"], dic[funcion]["break"], dic[funcion]["exit"], dic[funcion]["Coment"],
                                                                                                                      dic[funcion]["Ayuda"], dic[funcion]["Autor"])
     for funcion in dic)))
    print (Tabla)

def tabla_consultas(archivo):
    from generales import leer_archivo
    """[Autor : Juan Godoy]"""
    """[Ayuda : Funcion que acumula nombres de funciones para luego dibujarlas en una tabla]"""
    contador=0
    nueva_lista=[]
    linea=leer_archivo(archivo)
    print("{}".format("\tFunciones:\n".expandtabs(1)))
    while linea!=[""] or nueva_lista!=[""]:
        if contador!=5:
            nueva_lista.append(linea[0])
            contador+=1
        else:
            espaciador1=25-len(nueva_lista[0])
            espaciador2=25-len(nueva_lista[1])
            espaciador3=25-len(nueva_lista[2])
            espaciador4=25-len(nueva_lista[3])
            espaciador5=25-len(nueva_lista[4])
            print(" |{0}{5}|{1}{6}|{2}{7}|{3}{8}|{4}{9}|".format(nueva_lista[0], nueva_lista[1], nueva_lista[2], nueva_lista[3],nueva_lista[4],
                                                                 "\t".expandtabs(espaciador1),"\t".expandtabs(espaciador2),"\t".expandtabs(espaciador3),"\t".expandtabs(espaciador4), "\t".expandtabs(espaciador5)))
            nueva_lista=[]
            contador=0
            nueva_lista.append(linea[0])
        linea=leer_archivo(archivo)
    return

def imprimir_informacion_desarrollador(dicc_desarrolladores,total_lineas):
    total_desarrollador = 0
    with open("participacion.txt","w") as informe:
        total_funciones = 0
        linea = '-'*50
        print('\n\tInforme de Desarrollo por Autor\n')
        print(linea)
        informe.write('\n\tInforme de Desarrollo por Autor\n'+'\n')
        informe.write(linea)
        for autor,funciones in dicc_desarrolladores.items():
            acum_lineas = 0
            cant_funciones_desarrollador = 0
            print('\nAutor:  {}\n'.format(autor))
            informe.write('\nAutor:  {}\n'.format(autor))
            print('\tFunción\t\tLineas')
            informe.write('\tFunción\t\tLineas'+'\n')
            informe.write(linea+'\n')
            lista_funciones = sorted(funciones, key= lambda funcion:funcion[1])
            total_funciones += len(lista_funciones)
            for data in lista_funciones:
                cant_funciones_desarrollador += 1
                acum_lineas += data[1]
                print("\t{}\t{}".format(data[0],data[1]))
                informe.write("{}\t\t{}".format(data[0],data[1])+'\n')
                porcentaje=(acum_lineas*100)//total_lineas
            print("\t{} Funciones-lineas\t{}\t{}%".format(cant_funciones_desarrollador,acum_lineas,porcentaje))
            informe.write("\t{}Funciones-Lineas\t{}\t{}%".format(cant_funciones_desarrollador,acum_lineas,porcentaje))
        print('\nTotal Funciones {} - Lineas {}'.format(total_funciones,total_lineas))
        informe.write('\n\nTotal Funciones {} - Lineas {}'.format(total_funciones,total_lineas)+'\n')
        
