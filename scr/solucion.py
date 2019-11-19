#-*-coding-8-*-

def parte_1():
    meses={}
    pais={}
    archivo=open("datos_vuelos.csv","r+")
    all_lines=archivo.readlines()
    all_lines.pop(0)

    for x in all_lines:
        datos=x.split(",")
        mat=datos[0][0:2]
        mes=datos[2][3:5]
        if mes not in meses:
            meses[mes]=1
        else:
            meses[mes]+=1
            
        if mes not in pais:
            pais[mes]={}
            
        if mat not in pais [mes]:
            pais[mes][mat]=1
        else:
            pais[mes][mat]+=1
        print(mes,mat)
        
        if mes =="01":
            mes="Enero"
        if mes =="02":
            mes="Febrero"
        if mes =="03":
            mes="Marzo"
        if mes =="04":
            mes="Abril"
        if mes =="05":
            mes="Mayo"
        if mes =="06":
            mes="Junio"
        if mes =="07":
            mes="julio"
        if mes =="08":
            mes="Agosto"
        if mes =="09":
            mes="Septiembre"
        if mes =="10":
            mes="Octubre"
        if mes =="11":
            mes="Noviembre"
        if mes =="12":
            mes="Diciembre"
        if mat=="A6":
            mat="Emiratos Árabes"
        if mat=="XA":
            mat="México"
        if mat=="JA":
            mat="Japón"
        if mat=="PK":
            mat="Indonesia"
        if mat=="A7":
            mat="Qatar"
        if mat=="HS":
            mat="Tailandia"
        if mat=="9V":
            mat="Singlapur"
        if mat=="EN":
            mat="España"
        if mat=="D9":
            mat="Alemania"
        if mat=="PP":
            mat="Brasil"
        if mat=="CF":
            mat="Canada"
            
    archivo.close()
    return meses,pais,mes,mat

def parte_2():
    meses,pais=parte_1()
    archivo=open("Resultados.csv","w+")
    archivo.write("Mes,Pais,Porcentaje\n")
    for mes in pais.keys():
        for mat in pais[mes].keys:
            porcentaje=((pais[mes][mat]/meses[mes])*100)
            if porcentaje>= 20:
                porcentaje_final=porcentaje
            else:
                pass
            
            archivo.write(mes)
            archivo.write(",")
            archivo.write(mat)
            archivo.write(",")
            archivo.write(str(porcentaje_final[mes][mat]))
            archivo.write("\n")

    archivo.close
    
parte_2()
