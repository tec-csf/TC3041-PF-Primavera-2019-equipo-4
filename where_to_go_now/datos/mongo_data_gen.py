import json
import random
import  data_arrs as data

nom_archivo="mongo_data.txt"

f = open(nom_archivo, "w")

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



l=len(data.tipo_atraccion)

print('serialization')
x=0
f.write("[\n")
for r in range(5):
    for i in range (len(estados)):
        for j in range (len(ciudades[i])):
            myDictObj = {
                "nombre":data.nombres_lugar[random.randint(0, len(data.nombres_lugar)-1)],
                "direccion":data.calles[random.randint(0, len(data.calles)-1)],
                "estado":estados[i],
                "ciudad":ciudades[i][j],
                "tipo":data.tipo_atraccion[random.randint(0, len(data.tipo_atraccion)-1)],
                "soleado":random.randint(0,1),
                "nublado":random.randint(0,1),
                "chubasco":random.randint(0,1),
                "tormenta":random.randint(0,1),
                "path_imagen":"path",
                "nivel de precios":random.randint(0,5)
            }
            ##convert object to json
            serialized = json.dumps(myDictObj, sort_keys=True, indent=3)
            #print(serialized)
            f.write(serialized+",\n")
            x+=1

f.write("]")
print(x)
## now we are gonna convert json to object
#deserialization=json.loads(serialized)
#print(deserialization)