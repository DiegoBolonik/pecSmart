
import json
import requests

# ----------------- Requesição dos dados da API -------------------------
response = requests.get('http://18.231.62.128:8400/sensors/', headers={ 'Authorization': 'Token b2925f3bba618a5f770ad67d6a1d5bd68e7f2d8f' })

valores = []
repetidos = []
index = 0

#------------------ Busca pelos valores 'mac' repetidos ------------------
objeto = response.json()
for i in objeto['results']:
  if i['mac'] != 0:
    data = i['mac']
    if data not in valores:
      valores.append(data)
      index = index +1
    else:
      repetidos.add(data)
      index = index +1
      
print("Valores: ", valores)
print("Repetidos: ", repetidos)
print("Total de valores MAC: ", index)
    

#print(objeto.keys())
