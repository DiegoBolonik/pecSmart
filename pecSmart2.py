import json
import requests

# ----------------- Requesição dos dados da API -------------------------
response = requests.get('http://18.231.62.128:8400/sensors_logs', headers={ 'Authorization': 'Token b2925f3bba618a5f770ad67d6a1d5bd68e7f2d8f' })

#------------------ sensores SmartFeed que estão tortos ------------------
objeto = response.json()

valores = []
valores2 = []
index = 0
busca = 'IMU angle of'

# ------------------ busca pelos dispositivos, e ângulos -----------------
for i in objeto['results']:
  data2 = i['message']
  if busca in data2:
    elem = data2
    elem2 = i['owner']
    valores.append(data2)
    valores2.append(elem2)
    index = index +1

print("Dispositivos/Owner: ", valores2)
print("Valores diferentes de 0: ", valores)
print("Total de valores: ", index)

#print (objeto.values()) 
#print(objeto['results'])
