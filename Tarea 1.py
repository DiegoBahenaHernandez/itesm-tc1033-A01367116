#-*-coding-8-*-
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
print(pais)
print(meses)

for mes in pais:
    for mat in pais[mes]:
        porcentaje=pais[mes][mat]/meses[mes] 
        print(mes, mat, porcentaje)
