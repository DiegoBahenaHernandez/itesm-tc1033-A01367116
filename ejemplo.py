#-*-coding-8-*-
archivo=open("datos_vuelos.csv","r+")
all_lines=archivo.readlines()
for x in all_lines:
    datos=x.split(",")
    matri=datos[0][0:2]
    mes=datos[2][3:5]
    print(matri,mes)
    
