import random

nom_archivo="pfprueba.txt"
nom_base="pfprueba"

f = open(nom_archivo, "w")


f.write("# DDL\n\nCREATE DATABASE "+ nom_base +"\n\n# DML\n\n# CONTEXT-DATABASE: "+ nom_base +"\n\n")

measurements=["Temperatura","Clima"]
tags=["Estado", "Ciudad"]
estados=["Aguascalientes", "BajaCalifornia", "BajaCaliforniaSur", "Campeche", "Chiapas",
         "Chihuahua", "Coahuila", "Colima", "Durango", "CDMX", "Guanajuato", "Guerrero", "Hidalgo",
         "Jalisco", "EdoMexico", "Michoacan", "Morelos", "Nayarit", "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro", "QuintanaRoo",
         "SanLuisPotosi", "Sinaloa", "Sonora", "Tabasco", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas"]
ciudades=[["Aguascalientes"], ["Ensenada", "Mexicali", "Tijuana"], ["LaPaz"], ["Campeche"], ["Comitan", "SanCristobaldelasCasas", "Tapachula", "Tuxtla"],
          ["CasasGrandes", "Chihuahua", "CiudadDelicias", "HidalgodelParral", "Juarez", "NuevoCasasGrandes"], ["CiudadAcuña", "Monclova", "Muzquiz", "PiedrasNegras", "Saltillo", "Torreon"],
          ["Colima", "Manzanillo", "Tecoman"], ["Durango"], ["CDMX"], ["Acambaro", "Celaya", "Guanajuato", "Irapuato", "Leon", "Salamanca", "SanMigueldeAllende"],
          ["Acapulco", "Chilpancingo", "Iguala"], ["Pachuca", "Tulancingo"], ["Arandas", "Guadalajara", "Ocotlan", "PuertoVallarta", "Tlaquepaque", "Zapopan"],
          ["Nezahualcoyotl", "Tlalnepantla", "Toluca"], ["Apatzingan", "Ciudad Hidalgo", "Morelia", "Zitacuaro"], ["Cuernavaca", "Tepoztlan"], ["Tepic"],
          ["Monterrey"], ["Juchitan", "Oaxaca"], ["Cholula", "Matamoros", "Puebla"], ["Queretaro"], ["Cancun", "Chetumal"], ["Matehuala", "San Luis Potosi"], ["Culiacan", "Mazatlan"],
          ["CiudadObregon", "Hermosillo", "Nogales", "SanLuis", ], ["Villahermosa"], ["Tlaxcala"], ["Coatzacoalcos", "Orizaba", "Xalapa"], ["Merida"], ["Zacatecas"]]

temp_min=10
temp_max=30
sens_min=0
sens_max=35
hum_min=10
hum_max=80
clima=["Soleado", "Nublado", "Chubasco", "Tormenta"]
UV_min=1
UV_max=15
visibilidad_min=2
visibilidad_max=10
viento_min=1
viento_max=35

#Serie Temperatura
t = 1546300800

while (t<1577833200):
    for i in range(len(estados)):
        for j in range (len(ciudades[i])):
            f.write(measurements[0] +
                ",estado=" + estados[i] +
                ",ciudad=" + ciudades[i][j] +
                " temperatura=" + str(random.randint(temp_min, temp_max)) +
                ",sensacion=" + str(random.randint(sens_min, sens_max)) +
                ",viento=" + str(random.randint(viento_min, viento_max)) +
                " " + str(t) + "\n")

    t = t + 3600

t = 1546300800
while (t<1577833200):
    for i in range(len(estados)):
        for j in range (len(ciudades[i])):
            f.write(measurements[1] +
                ",estado=" + estados[i] +
                ",ciudad=" + ciudades[i][j] +
                " clima=" + '"' + str(clima[random.randint(0, len(clima))-1]) + '"' +
                ",humedad=" + str(random.randint(hum_min, hum_max)) +
                ",UV=" + str(random.randint(UV_min, UV_max)) +
                ",visibilidad=" + str(random.randint(viento_min, visibilidad_max)) +
                " " + str(t) + "\n")
    t = t + 3600


f.close()

